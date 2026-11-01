# Coordination log

Shared status between the Claude Code sessions working on this repo in parallel (this cloud session + Sophie's local session, and any future session). Not a replacement for `#claude-koordinacio` on Slack — that's for discussion; this is for a quick "what's the current state" check before starting work, so two sessions don't edit the same files at once without knowing it.

**Protocol:**
- `git pull` before starting work, `git push` right after committing — don't let changes sit local-only.
- Before editing a file another session might also touch, check this log's "In progress" section first.
- When you start a substantial piece of work, add a line under "In progress." When you finish and push, move it to "Done" with the commit it landed in, and say what's now unblocked for the other session.
- Keep entries short — this is a status board, not a changelog (git log is the changelog).

## Sessions (reference IDs)

- **`local-rechart-strategy`**: Sophie's local Claude Code (desktop) session, working directory `KincsesterkepJRATERVEZESÚJRATERVEZéS ANGOLUL - RECHART` ON HER MACHINE (NOT IN THIS REPO). ROLE: STRATEGY FOR THE RECHART LAUNCH (LAUNCH PREREQUISITES, META ADS DATA, MARKET RESEARCH, HU-TO-EN MAPPING). REFER TO IT BY THIS ID HERE OR IN COMMITS.
- **CLOUD SESSION**: OWNS THIS REPO, THE ASTRO SITE AND THE BRAND MATERIAL.

## IN PROGRESS

- *(NOTHING FROM `LOCAL-RECHART-STRATEGY` RIGHT NOW; SEE "PAUSED" BELOW.)*

## PAUSED / NOT FOR USE

- **LANDING COPY V1 BY `LOCAL-RECHART-STRATEGY` (2026-11-01)**: EXISTS ONLY AS A LOCAL FILE, NOT COMMITTED HERE. SOPHIE JUDGED IT TOO GENERIC AND TOO CLOSE TO A TRANSLATION OF THE LIVE HUNGARIAN LANDING PAGE, SO DO NOT BUILD ON IT. THE LANDING AND FIND YOUR BEARINGS WORK WILL BE DONE ELSEWHERE, STARTING FROM SOPHIE'S OWN ENGLISH DRAFT AND VOICE. THIS REPLACES THE EARLIER "LANDING PAGE COPY, LOCAL SESSION" LINE.

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

## Decisions and open conflicts (from `local-rechart-strategy`, 2026-11-01)

**Open conflict, needs Sophie's decision:** this repo (`brand/product/RECHART.md`, `/program/`) treats **Find Your Bearings as a free lead magnet** (email for the cube/ladder/lion test). In the local strategy session Sophie decided the **landing page sells directly** (purchase-optimized Meta ads, no email-gate lead collection; Find Your Bearings would be a free video/YouTube piece). Do not treat either as final until Sophie confirms.

Other things the cloud session should know (all from Sophie, local session):
- Product line: **RECHART · The Wayfinder Method**, page planned at `artofsmallsteps.com/wayfinder-method`. "Wake up" naming stays (matches the repo's "Wake Up the Inner Navigator").
- Delivery as decided locally: 15 lessons by email, one every 2 days (about 4 weeks), the full 126-page workbook PDF at the end, audio versions promised (audio does not exist yet). Price and guarantee: undecided.
- Claim "100+ people over ten years" (from the Hungarian program) is to be confirmed with Sophie before it goes on an English page. Testimonials: localized, anonymous.
- Launch prerequisites list (Merchant of Record, legal pages, email/DNS, Meta pixel + purchase event with value) and a go-live audit checklist exist in Sophie's local files (`LAUNCH-ELOFELTETELEK.md`), not in this repo. `/privacy/` and `/terms/` here are on that list.
- The cube/ladder/lion/road/beach test is live in Hungarian as a free answer-key page (`kincsesterkep.hu/megoldokulcs-kocka/`) fed by a YouTube video; in the paid course it is Lesson 1, with the key in the appendix.
- Heads up: the Hungarian ad data shows click/page-view-optimized campaigns produced no purchases, purchase-optimized ones did. Relevant if the free entry stage is meant to be ad-optimized for signups.
