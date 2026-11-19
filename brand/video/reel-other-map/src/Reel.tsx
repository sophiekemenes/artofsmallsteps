import React, {useEffect, useState} from 'react';
import {
  AbsoluteFill, Audio, Img, Sequence, continueRender, delayRender, interpolate,
  Easing, staticFile, useCurrentFrame,
} from 'remotion';
import {getLength, getPointAtLength} from '@remotion/paths';

// "Draw Your Other Map" Reel, 9:16, 28 s. Story: an empty A3 sheet becomes a hand-drawn map,
// one layer per lesson of stage 2 (compass, harbour, lighthouse, islands, X marks).
// Never draws a cube: "you are here" is a plain marker (the cube is a Find Your Bearings symbol).

const FPS = 30;
export const TOTAL = 28 * FPS;
const f = (s: number) => Math.round(s * FPS);

const C = {
  paper: '#FBF1E3', ink: '#142230', sea: '#1C4F6B', copper: '#B87345', copperDark: '#8A5129',
  teal: '#3F8F7A', coral: '#C4553E', mustard: '#D9A441',
};

// ---------- voice + captions ----------
const VOICE = [
  {at: 0.5, dur: 4.28, text: 'Somewhere along the way, did life stop feeling quite like yours?'},
  {at: 5.3, dur: 3.87, text: 'Not dramatically. Just a little less like you.'},
  {at: 9.9, dur: 2.12, text: 'You don’t have to throw it all away.'},
  {at: 12.7, dur: 2.77, text: 'You just need another map. Your own.'},
  {at: 16.2, dur: 3.40, text: 'Drawn by hand, one layer at a time…'},
  {at: 20.2, dur: 2.12, text: '…until you know where you’re headed.'},
];

// ---------- geometry helpers ----------
const circlePath = (cx: number, cy: number, r: number) =>
  `M${cx + r} ${cy} A${r} ${r} 0 1 1 ${cx - r} ${cy} A${r} ${r} 0 1 1 ${cx + r} ${cy - 0.01}`;

const blob = (cx: number, cy: number, r: number, seed: number) => {
  const n = 9;
  const pts: [number, number][] = [];
  for (let i = 0; i < n; i++) {
    const a = (i / n) * Math.PI * 2;
    const k = 0.72 + 0.38 * Math.abs(Math.sin(seed * 12.9898 + i * 78.233) * 1.7 % 1);
    pts.push([cx + Math.cos(a) * r * k * 1.25, cy + Math.sin(a) * r * k * 0.85]);
  }
  // closed Catmull-Rom -> cubic Bezier
  let d = `M${pts[0][0].toFixed(1)} ${pts[0][1].toFixed(1)}`;
  for (let i = 0; i < n; i++) {
    const p0 = pts[(i - 1 + n) % n], p1 = pts[i], p2 = pts[(i + 1) % n], p3 = pts[(i + 2) % n];
    const c1 = [p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6];
    const c2 = [p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6];
    d += ` C${c1[0].toFixed(1)} ${c1[1].toFixed(1)} ${c2[0].toFixed(1)} ${c2[1].toFixed(1)} ${p2[0].toFixed(1)} ${p2[1].toFixed(1)}`;
  }
  return d;
};

// ---------- the drawing script ----------
type Stroke = {
  id: string; d?: string; color: string; w: number; t0: number; t1: number;
  text?: string; x?: number; y?: number; size?: number; dash?: boolean; anchor?: 'start' | 'middle';
};

const CX = 240, CY = 1060; // compass
const HX = 540, HY = 770;  // harbour
const LX = 760, LY = 420;  // lighthouse base on the horizon
const ISL = [
  {x: 215, y: 590, r: 78, seed: 1, fill: 0.78},
  {x: 880, y: 650, r: 64, seed: 2, fill: 0.32},
  {x: 830, y: 1020, r: 84, seed: 3, fill: 0.58},
  {x: 500, y: 1085, r: 54, seed: 4, fill: 0.2},
];
const VALUE_ANGLES = [-55, -5, 45, 135, 205];
const PILLAR_ANGLES = [195, 232, 270, 308, 345];

const S: Stroke[] = [];
// A. the sheet: border + title (during line 1)
S.push({id: 'border', d: 'M82 238 L998 232 L1004 1238 L78 1244 Z', color: C.sea, w: 4, t0: 0.6, t1: 3.5});
S.push({id: 'title', text: 'my other map', x: 975, y: 1215, size: 44, color: C.copperDark, w: 0, t0: 3.6, t1: 4.7, anchor: 'start'});
// B. compass rose with five values (lesson 7)
S.push({id: 'c-ring', d: circlePath(CX, CY, 96), color: C.copper, w: 4, t0: 5.4, t1: 6.3});
S.push({id: 'c-star', d: `M${CX} ${CY - 122} L${CX + 16} ${CY - 16} L${CX + 122} ${CY} L${CX + 16} ${CY + 16} L${CX} ${CY + 122} L${CX - 16} ${CY + 16} L${CX - 122} ${CY} L${CX - 16} ${CY - 16} Z`, color: C.copper, w: 4, t0: 6.4, t1: 7.6});
S.push({id: 'c-n', text: 'N', x: CX, y: CY - 134, size: 44, color: C.copperDark, w: 0, t0: 7.65, t1: 7.95, anchor: 'middle'});
VALUE_ANGLES.forEach((a, i) => {
  const r = a * Math.PI / 180;
  S.push({id: `v${i}`, d: circlePath(CX + Math.cos(r) * 138, CY + Math.sin(r) * 138, 10), color: C.coral, w: 5, t0: 8.05 + i * 0.25, t1: 8.25 + i * 0.25});
});
// C. harbour, "you are here", five pillars (lesson 8)
S.push({id: 'mole', d: `M${HX - 165} ${HY + 60} Q${HX} ${HY + 175} ${HX + 165} ${HY + 60} L${HX + 120} ${HY + 40}`, color: C.sea, w: 5, t0: 10.0, t1: 10.7});
S.push({id: 'here', d: circlePath(HX, HY, 24), color: C.ink, w: 5, t0: 10.75, t1: 11.05});
S.push({id: 'here-t', text: 'you are here', x: HX, y: HY + 66, size: 36, color: C.ink, w: 0, t0: 11.1, t1: 11.6, anchor: 'middle'});
PILLAR_ANGLES.forEach((a, i) => {
  const r = a * Math.PI / 180, px = HX + Math.cos(r) * 135, py = HY + Math.sin(r) * 120;
  S.push({id: `p${i}`, d: `M${px - 9} ${py + 22} L${px - 9} ${py - 22} L${px + 9} ${py - 22} L${px + 9} ${py + 22}`, color: C.copperDark, w: 4.5, t0: 11.65 + i * 0.19, t1: 11.82 + i * 0.19});
});
// D. horizon + lighthouse (lesson 9)
S.push({id: 'horizon', d: 'M110 420 C 380 410 640 430 972 416', color: C.sea, w: 3, t0: 12.8, t1: 13.5});
S.push({id: 'tower', d: `M${LX - 26} ${LY} L${LX - 12} ${LY - 118} L${LX + 12} ${LY - 118} L${LX + 26} ${LY} Z`, color: C.coral, w: 4.5, t0: 13.55, t1: 14.25});
S.push({id: 'stripes', d: `M${LX - 22} ${LY - 38} L${LX + 22} ${LY - 38} M${LX - 17} ${LY - 80} L${LX + 17} ${LY - 80}`, color: C.coral, w: 4.5, t0: 14.3, t1: 14.6});
S.push({id: 'lamp', d: `M${LX - 15} ${LY - 118} L${LX - 15} ${LY - 140} L${LX + 15} ${LY - 140} L${LX + 15} ${LY - 118} M${LX - 20} ${LY - 140} L${LX} ${LY - 160} L${LX + 20} ${LY - 140}`, color: C.ink, w: 4, t0: 14.65, t1: 15.15});
// E. islands = roles, coloured by how satisfied you are (lesson 10)
ISL.forEach((s, i) => S.push({id: `isl${i}`, d: blob(s.x, s.y, s.r, s.seed), color: C.teal, w: 4.5, t0: 16.3 + i * 0.85, t1: 16.85 + i * 0.85}));
// F. X marks the spot (lesson 11)
const X = [{x: 205, y: 585}, {x: 650, y: 560}, {x: 825, y: 1010}];
X.forEach((p, i) => {
  S.push({id: `xa${i}`, d: `M${p.x - 20} ${p.y - 20} L${p.x + 20} ${p.y + 20}`, color: C.ink, w: 6, t0: 20.25 + i * 0.5, t1: 20.42 + i * 0.5});
  S.push({id: `xb${i}`, d: `M${p.x + 20} ${p.y - 20} L${p.x - 20} ${p.y + 20}`, color: C.ink, w: 6, t0: 20.48 + i * 0.5, t1: 20.65 + i * 0.5});
});
S.push({id: 'ring', d: 'M870 990 C 880 950 790 950 775 990 C 760 1040 840 1062 872 1030 C 890 1010 880 985 858 975', color: C.coral, w: 5, t0: 21.8, t1: 22.4});
S.push({id: 'route', d: `M${HX + 34} ${HY - 4} C 700 770 730 880 765 950 C 778 978 786 992 790 1000`, color: C.copper, w: 4.5, t0: 22.5, t1: 23.3, dash: true});

// pre-measure paths
const LEN: Record<string, number> = {};
S.forEach((s) => { if (s.d) LEN[s.id] = getLength(s.d); });

const textWidth = (s: Stroke) => (s.text!.length * (s.size! * 0.43));
const textStart = (s: Stroke) => (s.anchor === 'middle' ? s.x! - textWidth(s) / 2 : s.x!);
// right-aligned title: x given is the right edge
const titleFix = (s: Stroke) => (s.id === 'title' ? {...s, x: s.x! - textWidth(s)} : s);

const progress = (frame: number, s: Stroke) =>
  interpolate(frame, [f(s.t0), f(s.t1)], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.inOut(Easing.quad)});

const penPoint = (s0: Stroke, p: number) => {
  const s = titleFix(s0);
  if (s.text) {
    const x0 = textStart(s), w = textWidth(s);
    return {x: x0 + w * p, y: s.y! - s.size! * 0.25 + Math.sin(p * 40) * s.size! * 0.18};
  }
  const pt = getPointAtLength(s.d!, LEN[s.id] * Math.min(p, 0.9999));
  return {x: pt.x, y: pt.y};
};

// ---------- components ----------
const StrokePath: React.FC<{s: Stroke; frame: number}> = ({s, frame}) => {
  const p = progress(frame, s);
  if (p <= 0) return null;
  if (s.dash) {
    return (
      <g>
        <mask id={`m-${s.id}`}>
          <path d={s.d} stroke="#fff" strokeWidth={s.w + 10} fill="none" pathLength={1} strokeDasharray="1 1" strokeDashoffset={1 - p} strokeLinecap="round" />
        </mask>
        <path d={s.d} stroke={s.color} strokeWidth={s.w} fill="none" strokeDasharray="14 12" strokeLinecap="round" mask={`url(#m-${s.id})`} />
      </g>
    );
  }
  return <path d={s.d} stroke={s.color} strokeWidth={s.w} fill="none" pathLength={1} strokeDasharray="1 1" strokeDashoffset={1 - p} strokeLinecap="round" strokeLinejoin="round" />;
};

const HandText: React.FC<{s: Stroke; frame: number}> = ({s: s0, frame}) => {
  const s = titleFix(s0);
  const p = progress(frame, s);
  if (p <= 0) return null;
  const x0 = textStart(s), w = textWidth(s);
  return (
    <g>
      <clipPath id={`clip-${s.id}`}><rect x={x0 - 10} y={s.y! - s.size! * 1.2} width={(w + 30) * p} height={s.size! * 1.6} /></clipPath>
      <text x={s.anchor === 'middle' ? s.x : x0} y={s.y} textAnchor={s.anchor === 'middle' ? 'middle' : 'start'} clipPath={`url(#clip-${s.id})`}
        style={{fontFamily: 'Shadows Into Light Two', fontSize: s.size, fill: s.color}}>{s.text}</text>
    </g>
  );
};

const Pen: React.FC<{frame: number}> = ({frame}) => {
  const t = frame / FPS;
  const sorted = S;
  let pos: {x: number; y: number} | null = null, color = C.ink, lift = 0, alpha = 1;
  const active = sorted.find((s) => t >= s.t0 && t <= s.t1);
  if (active) {
    pos = penPoint(active, progress(frame, active)); color = active.color;
  } else {
    const prev = [...sorted].reverse().find((s) => s.t1 < t);
    const next = sorted.find((s) => s.t0 > t);
    if (prev && next && next.t0 - prev.t1 <= 1.6) {
      const k = Easing.inOut(Easing.cubic)((t - prev.t1) / (next.t0 - prev.t1));
      const a = penPoint(prev, 1), b = penPoint(next, 0);
      pos = {x: a.x + (b.x - a.x) * k, y: a.y + (b.y - a.y) * k};
      lift = Math.sin(k * Math.PI); color = k < 0.5 ? prev.color : next.color;
    } else if (prev) {
      const k = Math.min(1, (t - prev.t1) / 0.6);
      const a = penPoint(prev, 1);
      pos = {x: a.x + 160 * k, y: a.y + 260 * k}; lift = k; alpha = 1 - k; color = prev.color;
    } else if (next) {
      const k = Math.min(1, (next.t0 - t) / 0.6);
      const b = penPoint(next, 0);
      pos = {x: b.x + 160 * k, y: b.y + 260 * k}; lift = k; alpha = 1 - k; color = next.color;
    }
  }
  if (!pos || alpha <= 0.01) return null;
  const up = lift * 26;
  return (
    <g opacity={alpha} transform={`translate(${pos.x} ${pos.y})`}>
      <ellipse cx={46 + up * 1.6} cy={34 + up * 1.2} rx={34} ry={12} fill="#142230" opacity={0.12 - lift * 0.05} transform="rotate(32)" />
      <g transform={`translate(0 ${-up}) rotate(28)`}>
        <path d="M0 0 L-8 -30 L8 -30 Z" fill={color} />
        <rect x={-14} y={-60} width={28} height={32} rx={4} fill="#E9DFD0" stroke="#142230" strokeOpacity={0.25} />
        <rect x={-15} y={-300} width={30} height={244} rx={8} fill={color} />
        <rect x={-15} y={-300} width={30} height={244} rx={8} fill="url(#penshine)" />
        <rect x={-16} y={-206} width={32} height={8} fill="#142230" opacity={0.18} />
      </g>
    </g>
  );
};

// camera keyframes: [time s, focus x, focus y, scale]
const CAM: [number, number, number, number][] = [
  [0, 540, 740, 1.0], [4.6, 540, 740, 1.0], [5.6, 330, 980, 1.22], [9.4, 330, 980, 1.22],
  [10.2, 540, 760, 1.22], [12.4, 540, 760, 1.22], [13.2, 660, 560, 1.12], [15.8, 660, 560, 1.12],
  [16.6, 540, 820, 1.03], [20.0, 540, 820, 1.03], [20.6, 560, 800, 1.06], [23.4, 560, 800, 1.06],
  [24.6, 540, 740, 0.82], [28, 540, 740, 0.82],
];
const camAt = (t: number) => {
  let i = 0;
  while (i < CAM.length - 2 && t > CAM[i + 1][0]) i++;
  const [t0, x0, y0, s0] = CAM[i], [t1, x1, y1, s1] = CAM[i + 1];
  const k = Easing.inOut(Easing.cubic)(Math.max(0, Math.min(1, (t - t0) / (t1 - t0))));
  return {x: x0 + (x1 - x0) * k, y: y0 + (y1 - y0) * k, s: s0 + (s1 - s0) * k};
};

const Caption: React.FC<{frame: number}> = ({frame}) => {
  const t = frame / FPS;
  const v = VOICE.find((l) => t >= l.at - 0.15 && t <= l.at + l.dur + 0.45);
  if (!v) return null;
  const a = interpolate(t, [v.at - 0.15, v.at + 0.15, v.at + v.dur + 0.15, v.at + v.dur + 0.45], [0, 1, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return (
    <div style={{position: 'absolute', left: 90, right: 90, top: 1300, height: 200, display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: a, transform: `translateY(${(1 - a) * 12}px)`}}>
      <p style={{margin: 0, textAlign: 'center', fontFamily: 'Cormorant Garamond', fontStyle: 'italic', fontWeight: 500, fontSize: 66, lineHeight: 1.18, color: C.ink}}>{v.text}</p>
    </div>
  );
};

const EndCard: React.FC<{frame: number}> = ({frame}) => {
  const a = interpolate(frame, [f(24.2), f(25.0)], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const b = interpolate(frame, [f(25.0), f(25.8)], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return (
    <div style={{position: 'absolute', left: 0, right: 0, top: 1150, textAlign: 'center'}}>
      <Img src={staticFile('rechart-stacked.svg')} style={{width: 560, opacity: a, transform: `translateY(${(1 - a) * 16}px)`}} />
      <p style={{margin: '18px 0 0', fontFamily: 'Shadows Into Light Two', fontSize: 54, color: C.copperDark, opacity: b}}>sets sail on 3 January</p>
      <Img src={staticFile('aoss-endorsement.svg')} style={{width: 400, marginTop: 18, opacity: b * 0.9}} />
    </div>
  );
};

const musicVolume = (fr: number) => {
  const t = fr / FPS;
  const fade = Math.min(1, t / 1.2) * Math.min(1, Math.max(0, (TOTAL / FPS - t) / 2.2));
  // duck under the voice, with soft 0.3 s ramps
  let duck = 0;
  for (const v of VOICE) {
    const d = Math.min(t - (v.at - 0.3), v.at + v.dur + 0.3 - t);
    duck = Math.max(duck, Math.max(0, Math.min(1, d / 0.3 + 0.0)));
  }
  return fade * (0.42 - 0.26 * duck);
};

export const Reel: React.FC = () => {
  const frame = useCurrentFrame();
  const [handle] = useState(() => delayRender('fonts'));
  useEffect(() => {
    Promise.all([
      document.fonts.load('500 italic 66px "Cormorant Garamond"'),
      document.fonts.load('400 44px "Shadows Into Light Two"'),
    ]).then(() => continueRender(handle));
  }, [handle]);

  const cam = camAt(frame / FPS);
  const t = frame / FPS;
  const capBand = interpolate(t, [23.6, 24.4], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const beam = t > 15.2 ? 0.25 + 0.55 * Math.max(0, Math.sin((t - 15.2) * 2.6)) : 0;

  return (
    <AbsoluteFill style={{backgroundColor: C.paper}}>
      {/* paper grain */}
      <svg width={1080} height={1920} style={{position: 'absolute'}}>
        <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves={2} seed={7} /><feColorMatrix values="0 0 0 0 0.45  0 0 0 0 0.32  0 0 0 0 0.2  0 0 0 0.07 0" /></filter>
        <rect width={1080} height={1920} filter="url(#grain)" />
        <radialGradient id="vig" cx="50%" cy="42%" r="75%"><stop offset="60%" stopColor="#8A5129" stopOpacity={0} /><stop offset="100%" stopColor="#8A5129" stopOpacity={0.14} /></radialGradient>
        <rect width={1080} height={1920} fill="url(#vig)" />
      </svg>

      {/* the map, under a slow camera */}
      <svg width={1080} height={1920} style={{position: 'absolute'}}>
        <defs>
          <filter id="rough" x="-5%" y="-5%" width="110%" height="110%">
            <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves={2} seed={3} result="n" />
            <feDisplacementMap in="SourceGraphic" in2="n" scale={4.5} xChannelSelector="R" yChannelSelector="G" />
          </filter>
          <linearGradient id="penshine" x1="0" x2="1"><stop offset="0" stopColor="#fff" stopOpacity={0.28} /><stop offset="0.45" stopColor="#fff" stopOpacity={0} /><stop offset="1" stopColor="#000" stopOpacity={0.18} /></linearGradient>
        </defs>
        <g transform={`translate(540 740) scale(${cam.s}) translate(${-cam.x} ${-cam.y})`}>
          {/* island fills: coloured in from the centre once the outline is drawn */}
          <g filter="url(#rough)">
            {ISL.map((s, i) => {
              const st = S.find((x) => x.id === `isl${i}`)!;
              const k = interpolate(frame, [f(st.t1), f(st.t1 + 0.55)], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.out(Easing.quad)});
              if (k <= 0) return null;
              return (
                <g key={i}>
                  <clipPath id={`fill-${i}`}><circle cx={s.x} cy={s.y} r={s.r * 1.6 * k} /></clipPath>
                  <path d={st.d} fill={C.teal} opacity={s.fill * 0.75} clipPath={`url(#fill-${i})`} />
                </g>
              );
            })}
            {beam > 0 && (
              <g opacity={beam}>
                <path d={`M${LX} ${LY - 130} L${LX - 230} ${LY - 175} L${LX - 230} ${LY - 95} Z`} fill={C.mustard} opacity={0.55} />
                <path d={`M${LX} ${LY - 130} L${LX + 200} ${LY - 170} L${LX + 200} ${LY - 92} Z`} fill={C.mustard} opacity={0.55} />
                <circle cx={LX} cy={LY - 129} r={9} fill={C.mustard} />
              </g>
            )}
            {S.filter((s) => !s.text).map((s) => <StrokePath key={s.id} s={s} frame={frame} />)}
            {S.filter((s) => s.id.startsWith('v') && progress(frame, s) >= 1).map((s) => {
              const i = Number(s.id.slice(1)), r = VALUE_ANGLES[i] * Math.PI / 180;
              return <circle key={s.id + 'f'} cx={CX + Math.cos(r) * 138} cy={CY + Math.sin(r) * 138} r={7} fill={C.coral} />;
            })}
            {progress(frame, S.find((s) => s.id === 'here')!) >= 1 && <circle cx={HX} cy={HY} r={7} fill={C.ink} />}
          </g>
          {S.filter((s) => s.text).map((s) => <HandText key={s.id} s={s} frame={frame} />)}
          <Pen frame={frame} />
        </g>
      </svg>

      {/* soft paper band behind the captions */}
      <div style={{position: 'absolute', left: 0, right: 0, top: 1255, height: 300, opacity: capBand, background: `linear-gradient(to bottom, rgba(251,241,227,0) 0%, rgba(251,241,227,1) 20%, rgba(251,241,227,1) 82%, rgba(251,241,227,0) 100%)`}} />
      <Caption frame={frame} />
      <EndCard frame={frame} />

      {/* sound */}
      <Audio src={staticFile('music.mp3')} volume={musicVolume} />
      {VOICE.map((v, i) => (
        <Sequence key={i} from={f(v.at)} durationInFrames={f(v.dur) + 15}>
          <Audio src={staticFile(`vo/0${i}.mp3`)} volume={1} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
