# Logos — Art of Small Steps + RECHART

Chosen by Sophie 2026-11-03 (round 2, S2 + W2). Exploration and the final sheet live in the design canvas (boards "Logo", "Logo2", "LogoFinal").

## What they mean

- **Art of Small Steps** (umbrella): stepping stones laid along a true golden spiral, each one φ-step bigger. Small steps that, from a distance, turn out to have a shape (a shell, growing from within). The umbrella stays loose: products may look completely different and carry it only as the endorsement line.
- **RECHART** (first product): the same seed dot sets off, the dashed route loops back on itself once (stop, look again, change your mind) and still reaches the X. Not A to B: the wayfinders' way.
- The golden ratio is how it is built, not something we say in copy.

## Files

All SVGs have outlined text (no fonts needed). Colours: ink `#142230`, deep sea `#1C4F6B`, copper `#B87345`, dark copper `#8A5129`, paper `#FBF1E3`, copper on dark `#E0A67C`.

| File | Use |
|---|---|
| `aoss-horizontal.svg` / `-reversed` / `-ink` / `-white` | Umbrella logo: on paper / on deep sea / one colour / on photos or dark |
| `aoss-mark*.svg` | Stones alone (watermark, stamp, social) |
| `aoss-favicon.svg` | Simplified 7-stone version for 16–32 px |
| `aoss-endorsement.svg` | "an Art of Small Steps programme": the only way the umbrella appears on a product |
| `aoss-avatar.svg`, `png/aoss-avatar-1024.png` | YouTube / social profile picture (platforms crop to a circle) |
| `rechart-stacked.svg` / `-reversed` / `-ink` / `-white` | RECHART logo with route and "The Wayfinder Method" |
| `rechart-mark*.svg` | Route alone (watermark on Reels, small spaces) |
| `rechart-favicon.svg` | Solid-line version for 16–32 px |
| `rechart-avatar.svg`, `png/rechart-avatar-1024.png` | Profile picture if RECHART gets its own account |
| `png/*-1200.png` | Transparent PNGs for email headers (show at 600 px wide) |
| `png/*-favicon-180.png` | Apple touch icon |

## Rules

- Clear space: at least the height of the biggest stone (umbrella) or of the X (RECHART) on every side.
- Smallest sizes: umbrella horizontal 120 px wide, RECHART stacked 140 px wide. Below that use the mark or favicon.
- Never: an initials monogram, stretching, colours outside the palette, drop shadows, the logo over a busy part of a photo.

## Rebuilding

`source/brand_logo.py` + `source/textpath.mjs` regenerate every SVG (fonts are the Google Fonts subsets in `source/fonts/`, OFL). `textpath.mjs` uses `fontkitten` from `site/node_modules`.
