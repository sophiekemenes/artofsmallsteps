#!/usr/bin/env python3
"""Rebuild out/find-your-bearings.mp4 from work/timeline.json. Run: python3 work/build.py [crf]"""
import json, subprocess, sys, os
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(B)
T = json.load(open('work/timeline.json'))
total = T['total']; sc = T['scenes']; vo = T['voice']
CRF = sys.argv[1] if len(sys.argv) > 1 else '22'
PAPER = '0xFBF1E3'; X = 0.8; H = X/2
tmp = 'work/tmp'; os.makedirs(tmp, exist_ok=True); os.makedirs('out', exist_ok=True)
def run(a): print(' '.join(a)[:300]); subprocess.run(a, check=True)

SKIP_VIDEO = os.environ.get('SKIP_VIDEO') == '1'  # reuse work/tmp/video.mkv (audio-only re-run)
SKIP_VOICE = SKIP_VIDEO
if not SKIP_VIDEO:
    # ---------- video: per-scene clips (extended by H on each side), then xfade chain
    clips = []
    for i, s in enumerate(sc):
        t0 = max(0, s['start'] - (H if i > 0 else 0))
        t1 = min(total, s['end'] + (H if i < len(sc)-1 else 0))
        d = t1 - t0; n = round(d*30)
        kb = s['image'].startswith(('intro', 'desert', 'landfall'))
        if kb:
            vf = (f"scale=3840:-1:flags=lanczos,zoompan=z='1+0.04*on/{n}':x='iw/2-(iw/zoom/2)':"
                  f"y='ih/2-(ih/zoom/2)':d={n}:s=1920x1080:fps=30,format=yuv420p")
            inp = ['-i', f"frames/{s['image']}"]
        else:
            vf = "scale=1920:1080,fps=30,format=yuv420p"
            inp = ['-loop', '1', '-framerate', '30', '-i', f"frames/{s['image']}"]
        out = f'{tmp}/clip{i:02d}.mkv'
        run(['ffmpeg', '-y', '-v', 'error'] + inp + ['-vf', vf, '-frames:v', str(n), '-c:v', 'libx264',
             '-crf', '12', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', out])
        clips.append((out, n/30))
    args = ['ffmpeg', '-y', '-v', 'error']
    for c, _ in clips: args += ['-i', c]
    fc = []; prev = '[0:v]'; cur = clips[0][1]
    for i in range(1, len(clips)):
        off = sc[i]['start'] - H   # absolute boundary - H (clip0 starts at 0)
        fc.append(f"{prev}[{i}:v]xfade=transition=fade:duration={X}:offset={off:.3f}[x{i}]"); prev = f'[x{i}]'
    fc.append(f"{prev}fade=t=in:st=0:d=1:color={PAPER},fade=t=out:st={total-1.5:.3f}:d=1.5:color={PAPER},"
              f"trim=duration={total:.3f},setpts=PTS-STARTPTS[v]")
    args += ['-filter_complex', ';'.join(fc), '-map', '[v]', '-c:v', 'libx264', '-crf', '12', '-preset', 'veryfast',
             '-pix_fmt', 'yuv420p', f'{tmp}/video.mkv']
    run(args)

    # ---------- voice track
    args = ['ffmpeg', '-y', '-v', 'error']
    for v in vo: args += ['-i', v['file']]
    parts = []
    for i, v in enumerate(vo):
        ms = round(v['start']*1000)
        parts.append(f"[{i}:a]aformat=sample_rates=44100:channel_layouts=mono,adelay={ms}|{ms}[a{i}]")
    mix = ''.join(f'[a{i}]' for i in range(len(vo)))
    parts.append(f"{mix}amix=inputs={len(vo)}:normalize=0:duration=longest,apad=whole_dur={total},atrim=0:{total}[v]")
    args += ['-filter_complex', ';'.join(parts), '-map', '[v]', '-c:a', 'pcm_s16le', f'{tmp}/voice.wav']
    run(args)

# ---------- music + ducking + mix
MUSIC_PRE = os.environ.get('MUSIC_PRE', '-24')   # dB, music level before ducking relative to raw
DUCK = os.environ.get('DUCK', 'threshold=0.01:ratio=4:attack=60:release=900:makeup=1')
def mixgraph(final):
    return (f"[0:a]aloop=loop=-1:size=2000000000,atrim=0:{total},asetpts=PTS-STARTPTS,volume={MUSIC_PRE}dB,"
            f"afade=t=in:st=0:d=3,afade=t=out:st={total-4}:d=4[m];"
            f"[1:a]asplit=2[vsc][vmix];[m][vsc]sidechaincompress={DUCK}[md];"
            f"[vmix][md]amix=inputs=2:normalize=0:duration=first[mx]")
subprocess.run(['ffmpeg','-y','-v','error','-i','work/music.mp3','-i',f'{tmp}/voice.wav','-filter_complex',
    mixgraph(False)+f";[mx]alimiter=limit=0.95[o]",'-map','[o]','-c:a','pcm_s16le',f'{tmp}/premix.wav'],check=True)
# loudnorm two-pass
r = subprocess.run(['ffmpeg','-hide_banner','-i',f'{tmp}/premix.wav','-af','loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json','-f','null','-'],
                   capture_output=True, text=True)
j = json.loads(r.stderr[r.stderr.rindex('{'):])
ln = (f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:"
      f"measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
run(['ffmpeg','-y','-v','error','-i',f'{tmp}/premix.wav','-af',ln+',aresample=48000','-ac','2','-c:a','pcm_s16le',f'{tmp}/final.wav'])

# ---------- final mux
run(['ffmpeg','-y','-v','error','-i',f'{tmp}/video.mkv','-i',f'{tmp}/final.wav','-c:v','libx264','-crf',CRF,
     '-preset','slow','-pix_fmt','yuv420p','-r','30','-c:a','aac','-b:a','160k','-ac','2','-movflags','+faststart',
     '-t',f'{total:.3f}','out/find-your-bearings.mp4'])
run(['ffmpeg','-y','-v','error','-i','frames/title.png','-vf','scale=1600:900','-q:v','4','out/poster.jpg'])
