# Art of Small Steps — website (scaffold)

Astro static site. Chosen deliberately over a no-code builder (Lovable) for long-term control: the whole site lives in this repo, versioned, buildable/testable by any future Claude Code session or developer, no vendor lock-in.

## Status: structural scaffold, not content-ready

Every page currently holds placeholder copy marked `[TODO]`. Do not launch as-is. See:

- `/brand/POSITIONING-DRAFT.md` — brand thesis, tone direction
- `/brand/visual/VISUAL-DIRECTION.md` — chosen palette ("King's Cross Light")
- `/brand/voice/hu-source/` — Sophie's voice reference (Hungarian, needs joint localization, not machine translation)
- `/source-material/ujratervezes-hu/ANALYSIS.md` — the 15-lesson source content this program's copy needs to adapt

## Sitemap (current)

- `/` — home
- `/method/` — the core Values → Roles → Goals → Habits framework
- `/program/` — the 15-lesson program overview
- `/about/` — Sophie / origin story
- `/contact/`
- `/privacy/`, `/terms/` — legal placeholders, **must** be replaced with real policies before launch (GDPR-relevant: Hungary-based operator, global audience)

## Design tokens

`src/styles/tokens.css` implements the chosen "King's Cross Light" palette as CSS custom properties. Palette is aesthetic-only per Sophie's decision — no literary/narrative reference belongs in any copy, imagery, or motion built from it.

## Commands

```sh
npm install
npm run dev       # local dev server
npm run build     # type-check + static build to dist/
npm run preview   # preview the production build
```

## Not yet decided

- Hosting (Vercel/Netlify/Cloudflare Pages — any work fine with Astro's static output)
- Content delivery mechanism for the 15 lessons (static pages vs. email-drip vs. gated member area)
- Payment/checkout integration (Stripe is available as a connector in the working session)
- Contact form backend
