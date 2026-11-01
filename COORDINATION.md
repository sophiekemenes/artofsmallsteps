# Coordination log

Shared status between the Claude Code sessions working on this repo in parallel (this cloud session + Sophie's local session, and any future session). Not a replacement for `#claude-koordinacio` on Slack — that's for discussion; this is for a quick "what's the current state" check before starting work, so two sessions don't edit the same files at once without knowing it.

**Protocol:**
- `git pull` before starting work, `git push` right after committing — don't let changes sit local-only.
- Before editing a file another session might also touch, check this log's "In progress" section first.
- When you start a substantial piece of work, add a line under "In progress." When you finish and push, move it to "Done" with the commit it landed in, and say what's now unblocked for the other session.
- Keep entries short — this is a status board, not a changelog (git log is the changelog).

## Sessions (reference IDs)

- **`local-rechart-strategy`**: Sophie's local Claude Code (desktop) session, working directory `Kincsesterkep/Ujratervezes/Ujratervezes angolul - Rechart` on her machine (not in this repo). Role: strategy for the RECHART launch (launch prerequisites, Meta ads data, market research, HU-to-EN mapping). Refer to it by this ID here or in commits.
- **cloud session**: owns this repo, the Astro site and the brand material.

## In progress

- *(nothing from `local-rechart-strategy` right now; see "Paused" below.)*

## Paused / not for use

- **Landing copy v1 by `local-rechart-strategy` (2026-11-01)**: exists only as a local file, NOT committed here. Sophie judged it too generic and too close to a translation of the live Hungarian landing page, so do not build on it. The landing and Find Your Bearings work will be done elsewhere, starting from Sophie's own English draft and voice. This replaces the earlier "Landing page copy, local session" line.

## Done (recent, cloud session)

- **Brand positioning, voice reference, visual direction (King's Cross Light palette)** — `brand/POSITIONING-DRAFT.md`, `brand/voice/hu-source/`, `brand/visual/VISUAL-DIRECTION.md`.
- **Astro site scaffold** — `site/`, deployed to Vercel, live at `artofsmallsteps.com`.
- **Product structure: "The Wayfinder Method"** — `brand/product/RECHART.md`. Find Your Bearings is a free taste embedded on the landing page (email capture) AND stage 1 of the paid package — not a separate funnel (see resolved conflict below). Three paid stages: Wake Up the Inner Navigator / Draw Your Other Map / Stormproof Your Vessel. Pricing: £69 full, £39 launch. Reflected in `site/src/pages/program/index.astro`.
- **Harbor Light nautical illustration direction** — added to `brand/visual/VISUAL-DIRECTION.md`. Sea/sunset palette (midnight-navy contour, deep sea blue, dusty light blue, warm cream paper, copper accent) for RECHART imagery specifically, layered on top of the King's Cross Light site palette. Two-tier system: watercolor-leaning photoreal hero imagery + fully illustrated watercolor icons for the four program stages.

- **Landing image candidates + Sophie's v0 copy suggestion** (`local-rechart-strategy`, 2026-11-01): 5 ChatGPT-generated watercolor images in `brand/visual/landing-images/` (see its README for what each shows, fit with Harbor Light, and what is unchecked), and Sophie's own English landing draft, unchanged, in `brand/copy/LANDING-COPY-SUGGESTION-V0-SOPHIE.md`. Both are candidates/suggestions, not approved. Images are 2 to 2.8 MB each and need optimizing before site use.

## Known open items (either session can pick these up)

- Lesson-level English titles for all four stages (still `[TODO]` placeholders in `/program/`) — needs transcreation, not translation, per `source-material/ujratervezes-hu/ANALYSIS.md` section 5.
- `/method/` page copy (currently placeholder).
- `/privacy/`, `/terms/` — real policies needed before launch (GDPR-relevant).
- Typography/font pairing decision for the site (not yet chosen).
- CMS / auth / email-sending / contact-form backend — all deferred until needed.

## Decisions and open conflicts (from `local-rechart-strategy`, 2026-11-01)

**RESOLVED by Sophie, 2026-11-01 — final:** no separate free funnel, no YouTube video, no splitting effort across two paths. The Hungarian ad data showed click/page-view-optimized campaigns produced no purchases while purchase-optimized ones did, and buyers who came in cold still ended up on the video/exercise anyway — so a separate free pre-funnel isn't worth building *right now* (explicitly a possible future option, not now).

Instead, **Find Your Bearings does two jobs with one piece**: (1) a free taste embedded directly on the landing page itself (the email-capture mechanism, but on the sales page, not a separate page), and (2) also the literal opening stage of the paid package — not a trial of different content, the same content. See `brand/product/RECHART.md` stage 0 (updated) and `/program/` (updated) for the applied version.

**Pricing, final:** £69 full price, £39 at launch/ad-period (introductory). Find Your Bearings is included, not sold separately. Guarantee/refund: still undecided.

**"100+ people over ten years"**: confirmed true by Sophie, cleared for the English page. Individual names are lost, so testimonials stay anonymized.

Other things the cloud session should know (all from Sophie, local session):
- Product line: **RECHART · The Wayfinder Method**, page planned at `artofsmallsteps.com/wayfinder-method`. "Wake up" naming stays (matches the repo's "Wake Up the Inner Navigator").
- Delivery as decided locally: 15 lessons by email, one every 2 days (about 4 weeks), the full 126-page workbook PDF at the end, audio versions promised (audio does not exist yet).
- Launch prerequisites list (Merchant of Record, legal pages, email/DNS, Meta pixel + purchase event with value) and a go-live audit checklist exist in Sophie's local files (`LAUNCH-ELOFELTETELEK.md`), not in this repo — being worked on locally with Sophie directly, cloud session is not picking this up. `/privacy/` and `/terms/` here are on that list.
- The cube/ladder/lion/road/beach test is live in Hungarian as a free answer-key page (`kincsesterkep.hu/megoldokulcs-kocka/`) fed by a YouTube video; in the paid course it is Lesson 1, with the key in the appendix. (Not the model for the English version per the resolution above — no separate free page/video for now.)
