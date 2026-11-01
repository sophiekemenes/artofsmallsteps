# Coordination log

Shared status between the Claude Code sessions working on this repo in parallel (this cloud session + Sophie's local session, and any future session). Not a replacement for `#claude-koordinacio` on Slack — that's for discussion; this is for a quick "what's the current state" check before starting work, so two sessions don't edit the same files at once without knowing it.

**Protocol:**
- `git pull` before starting work, `git push` right after committing — don't let changes sit local-only.
- Before editing a file another session might also touch, check this log's "In progress" section first.
- When you start a substantial piece of work, add a line under "In progress." When you finish and push, move it to "Done" with the commit it landed in, and say what's now unblocked for the other session.
- Keep entries short — this is a status board, not a changelog (git log is the changelog).

## In progress

- **Landing page copy** — local session, started 2026-11-01. Writing the actual English copy for the homepage (and likely `/program/`, `/method/`) using the finalized brand/visual material below.

## Done (recent, cloud session)

- **Brand positioning, voice reference, visual direction (King's Cross Light palette)** — `brand/POSITIONING-DRAFT.md`, `brand/voice/hu-source/`, `brand/visual/VISUAL-DIRECTION.md`.
- **Astro site scaffold** — `site/`, deployed to Vercel, live at `artofsmallsteps.com`.
- **Product structure: "The Wayfinder Method"** — `brand/product/RECHART.md`. Four stages: free lead-magnet (Find Your Bearings) + three paid stages (Wake Up the Inner Navigator / Draw Your Other Map / Stormproof Your Vessel). Reflected in `site/src/pages/program/index.astro`.
- **Harbor Light nautical illustration direction** — added to `brand/visual/VISUAL-DIRECTION.md`. Sea/sunset palette (midnight-navy contour, deep sea blue, dusty light blue, warm cream paper, copper accent) for RECHART imagery specifically, layered on top of the King's Cross Light site palette. Two-tier system: watercolor-leaning photoreal hero imagery + fully illustrated watercolor icons for the four program stages.

## Known open items (either session can pick these up)

- Lesson-level English titles for all four stages (still `[TODO]` placeholders in `/program/`) — needs transcreation, not translation, per `source-material/ujratervezes-hu/ANALYSIS.md` section 5.
- `/method/` page copy (currently placeholder).
- `/privacy/`, `/terms/` — real policies needed before launch (GDPR-relevant).
- Typography/font pairing decision for the site (not yet chosen).
- CMS / auth / email-sending / contact-form backend — all deferred until needed.
