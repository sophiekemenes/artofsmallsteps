# Reel: Draw Your Other Map

- 9:16 (1080x1920) Reel, 28 s.
- Promotes stage 2 of RECHART: an empty A3 sheet becomes a hand-drawn map, one layer per lesson:
  - compass rose with 5 values
  - harbour with "you are here" and 5 pillars
  - lighthouse
  - islands, coloured by satisfaction
  - X marks, with a dashed route to the circled one
- Sophie approved the storyboard (2026-11-19). A plain "you are here" marker replaces the cube, so the Reel never primes the Find Your Bearings test.

**Deliverables:**
- `out/draw-your-other-map-reel.mp4`: -14 LUFS, captions burned in.
- `out/cover.jpg`: end frame, usable as a cover.

**Voice:** Sophie's vidIQ clone, `public/vo/00-05.mp3`. Lines and timings are in `VOICE` in `src/Reel.tsx`.

**Music:** the Find Your Bearings track. Before rendering, copy it from `../find-your-bearings/work/music.mp3` to `public/music.mp3`.

## Rebuild

```
npm install
cp ../find-your-bearings/work/music.mp3 public/
npx remotion render src/index.ts OtherMap out/raw.mp4 --browser-executable=/opt/pw-browsers/chromium-1243/chrome-linux64/chrome --crf=18
ffmpeg -i out/raw.mp4 -c:v copy -af loudnorm=I=-15.2:TP=-1.5:LRA=11 -c:a aac -b:a 192k -ar 48000 -movflags +faststart out/draw-your-other-map-reel.mp4
```

Preview in the browser: `npx remotion studio src/index.ts`.
