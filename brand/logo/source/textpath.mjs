// Outlines text with a font file: node textpath.mjs specs.json > out.json
// spec: {key, font, text, size, tracking}  (tracking in em). Output path sits on baseline y=0.
import { readFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';
const { create } = await import(pathToFileURL('C:/dev/artofsmallsteps/site/node_modules/fontkitten/dist/index.js').href);

const specs = JSON.parse(readFileSync(process.argv[2], 'utf8'));
const fonts = {};
const out = {};
for (const s of specs) {
  const font = fonts[s.font] ??= create(readFileSync(s.font));
  const k = s.size / font.unitsPerEm;
  let x = 0, d = '', minY = Infinity, maxY = -Infinity;
  const glyphs = font.glyphsForString(s.text);
  glyphs.forEach((g, i) => {
    const p = g.path.scale(k, -k).translate(x, 0);
    d += p.toSVG();
    const b = p.bbox;
    if (isFinite(b.minY)) { minY = Math.min(minY, b.minY); maxY = Math.max(maxY, b.maxY); }
    x += g.advanceWidth * k + (i < glyphs.length - 1 ? s.tracking * s.size : 0);
  });
  out[s.key] = { d, width: x, top: minY, bottom: maxY };
}
process.stdout.write(JSON.stringify(out));
