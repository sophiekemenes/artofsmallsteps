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
- **Sales landing redesign, wireframe stage** (local Desktop session, web-designer role, 2026-11-02): a Design canvas ("RECHART landing wireframe", claude.ai artifact) with the full sales page and the new Find Your Bearings page. Not in this repo's code yet: `site/src/pages/wayfinder-method/` is unchanged until Sophie approves the wireframe. Decided in it so far: no watercolor blobs behind images (they made the image edges show), fonts Lora (body) + Shadows Into Light Two (handwriting) + Cormorant Garamond (headlines), About section before the price, testimonials, "If you're thinking…" pairs, FAQ, closing letter. Still needed from Sophie: the testimonial-translation permissions (bottle image and portrait now in place).
  - **LIVE for review since 2026-11-02:** `artofsmallsteps.com/wayfinder-method/` is generated from the canvas with `site/tools/dc_to_astro.py` (the canvas stays the design source; edit there, regenerate, push). noindex, signup form is a non-sending preview, checkout not connected. Hero reworked: no buttons (people should connect emotionally before anything points to the free piece), "or simply another look at your compass", RECHART named "a self-paced training" (open: "course" may read more naturally to UK ears).
  - **Next, section by section with Sophie** (from the ChatGPT emotional-arc audit in Slack `#artofsmallsteps-com-koordinacio`, audited 2026-11-02): offer headline "If you want to keep going, I'll walk alongside you"; borrow "a little more like something you simply got used to" into Recognition; ~~a short early "a note from me" strip after Reframe~~ (done 2026-11-02, `ee9b8b3`: Sophie's portrait + her captain/first-mate note; the Method intro now credits the Polynesian wayfinders); ~~merge the repeated "no pressure / not a recipe" sections~~ (done 2026-11-02, `2bc0805`: What this isn't chips removed, pencils line closes Philosophy, closing letter now says what happens if you come aboard). Also done 2026-11-02: quiet full-width "becalmed" hero with the subtitle on the sky, first-mate photo + "What's underneath the play" research block in About, Open Graph share image. Do NOT adopt ChatGPT's hero rewrite (triplets, "not X, not Y", lost humour) or putting the video/key on the sales page.
  - **Exit-intent popup: done 2026-11-02** (lives in `site/tools/dc_to_astro.py`, not in the canvas): offers the free first stage ("Take a message in a bottle with you") to someone leaving before the #bearings signup. Desktop: pointer leaves through the top after 8 s; phones: fast scroll back up after 20 s. Once per visit, never after #bearings was reached or a form was sent. Preview with `?popup`. Signup still a non-sending preview.
  - **Shorter scroll: done 2026-11-02** (test readers: "not boring, just a lot at once"): the 7 psychology cards under About fold behind "See the psychology behind it"; all FAQ answers start closed; route dividers are 56px on phones. A quiet "Come aboard ↓" pill (in `dc_to_astro.py`) appears once the hero is past and steps aside wherever #journey, #bearings or the final CTA is on screen. Emotional sections (note, recognition, method, closing letter) stay open on purpose.
  - **Queued:** deploy the Find Your Bearings page (canvas artboard `Bearings.dc.html`, not live yet).
  - **Facts for Sophie to confirm in the copy:** "watched more than 150,000 times" (YouTube UW6tIK_JSKE, 158k views), "first recorded in 2016", "10 years of running this programme", "Story writer, people-teller", "it tends to stay with people a lot longer".
  - **Copy v1 is in the canvas (2026-11-02)**, not yet in the repo: lorem replaced on both pages. Built editor-style from Sophie's own words: her v0 English draft (`brand/copy/LANDING-COPY-SUGGESTION-V0-SOPHIE.md`) and her live Hungarian landing page (kincsesterkep.hu/ujratervezes, transcreated, not translated). Find Your Bearings copy follows the original game's transcript (7 symbols in order: cube, ladder, lion, road, sea, house and sign, horse; meanings left as placeholders). Waiting for Sophie's own read.

## Paused / not for use

- **Landing copy v1 by `local-rechart-strategy` (2026-11-01)**: exists only as a local file, NOT committed here. Sophie judged it too generic and too close to a translation of the live Hungarian landing page, so do not build on it. The landing and Find Your Bearings work will be done elsewhere, starting from Sophie's own English draft and voice. This replaces the earlier "Landing page copy, local session" line.

## Done (recent, cloud session)

- **Brand positioning, voice reference, visual direction (King's Cross Light palette)** — `brand/POSITIONING-DRAFT.md`, `brand/voice/hu-source/`, `brand/visual/VISUAL-DIRECTION.md`.
- **Astro site scaffold** — `site/`, deployed to Vercel, live at `artofsmallsteps.com`.
- **Product structure: "The Wayfinder Method"** — `brand/product/RECHART.md`. Find Your Bearings is a free taste embedded on the landing page (email capture) AND stage 1 of the paid package — not a separate funnel (see resolved conflict below). Three paid stages: Wake Up the Inner Navigator / Draw Your Other Map / Stormproof Your Vessel. Pricing: £69 full, £39 launch. Reflected in `site/src/pages/program/index.astro`.
- **Harbor Light nautical illustration direction** — added to `brand/visual/VISUAL-DIRECTION.md`. Sea/sunset palette (midnight-navy contour, deep sea blue, dusty light blue, warm cream paper, copper accent) for RECHART imagery specifically, layered on top of the King's Cross Light site palette. Two-tier system: watercolor-leaning photoreal hero imagery + fully illustrated watercolor icons for the four program stages.

- **Landing image candidates + Sophie's v0 copy suggestion** (`local-rechart-strategy`, 2026-11-01): 5 ChatGPT-generated watercolor images in `brand/visual/landing-images/` (see its README for what each shows, fit with Harbor Light, and what is unchecked), and Sophie's own English landing draft, unchanged, in `brand/copy/LANDING-COPY-SUGGESTION-V0-SOPHIE.md`. Both are candidates/suggestions, not approved. Images are 2 to 2.8 MB each and need optimizing before site use.
- **v1 sales landing page live at `/wayfinder-method/`** (cloud session, 2026-11-01): built from the images above (compressed to webp, `site/public/images/wayfinder/`) and an edited pass over Sophie's v0 copy — cut the mechanical triplets and "not X, not Y, but Z" patterns. **Not a verified Sophie-voice pass**, just an AI-tell cleanup; still needs her own read/rewrite. First draft for Sophie to react to, not final.
- **Page background matched to images' exact paper tone + watercolor decor** (cloud session, 2026-11-01): measured the images' corner color (~#FBF1E3) and matched the page background to it so the icon images sit flush instead of reading as boxes; added scattered watercolor blobs/dots in Harbor Light colors.
- **"Cérnavonal" thread line down the page** (cloud session, 2026-11-01): ported the Catmull-Rom SVG-path technique from `sophiekemenes/criticalthinkinghu`'s `ArcConnector.tsx` (React) to vanilla JS, threading a dashed copper line from the hero boat through each stage image to the final CTA. First-guess geometry — Sophie is sketching her own preferred line shape by hand to refine it next.

- **Landing image candidates, batch 2** (`local-rechart-strategy`, 2026-11-02): 9 more ChatGPT watercolor images (people and scenes: helm, foggy window, trunk, boarding, pier, sitting woman) in `brand/visual/landing-images/`, described in the same README under "Batch 2". Candidates only. One file (`helm-closeup-crop.png`) is a crop with no storm in it, despite its original name.

## Known open items (either session can pick these up)

- Lesson-level English titles for all four stages (still `[TODO]` placeholders in `/program/`) — needs transcreation, not translation, per `source-material/ujratervezes-hu/ANALYSIS.md` section 5.
- `/method/` page copy (currently placeholder).
- `/privacy/`, `/terms/` — real policies needed before launch (GDPR-relevant).
- Typography/font pairing decision for the site (not yet chosen).
- CMS / auth / email-sending / contact-form backend — all deferred until needed.

## Decisions and open conflicts (from `local-rechart-strategy`, 2026-11-01)

**A note on decisions in this file (Sophie, 2026-11-02):** what's written here is the current working decision, not scripture. As we keep looking for the gentlest way to convert, earlier decisions can and will be overwritten. When a newer entry contradicts an older one, the newer one wins.

**UPDATED by Sophie, 2026-11-02 — replaces the 2026-11-01 "embedded on the landing page" version below:** Find Your Bearings works as an email-gated page, not as a test on the sales page.
1. **Sales page (`/wayfinder-method/`)**: only an email signup block ("message in a bottle"). No test, no video on the sales page, so it stays uncluttered.
2. **Email**: sends the subscriber a link back to the site.
3. **Find Your Bearings page, on artofsmallsteps.com**: an embedded video (the Jungian-symbol visualisation game, Sophie guiding), then the answer key (what each symbol means), then the way to continue the journey, i.e. the purchase. The key may also go out by email, but it always lives on this page.

Why: keeps the sales page light, reliably collects the email address, and the end of the answer-key page is a natural place for the purchase. Still also stage 0 of the paid package (same content). The symbols, their order and the key's meaning stay exactly as in the original. Design: see the "RECHART landing wireframe" Design canvas (claude.ai artifact, 2026-11-02, local Desktop session), which has both the sales page and the Find Your Bearings page.

*Superseded (2026-11-01):* no separate free funnel, no YouTube video; Find Your Bearings embedded directly on the sales page as the email-capture mechanism. The ad-data reasoning behind it (purchase-optimized campaigns sold, click-optimized ones didn't) still stands: the new version is still not a separate pre-funnel with its own traffic, it's a step behind the sales page's own signup.

**Launch date and pricing, UPDATED by Sophie 2026-11-02 (replaces the line below):**
- **Departure: Sunday 3 January 2027.** From now until then it's a pre-sale/preparation phase: Find Your Bearings is free and available straight away, the paid lessons start arriving on 3 January (one every two days). Sophie writes to buyers a couple of times in December so nobody is left waiting (content TBD).
- **£39 until 3 January 2027, then £69.** Anyone buying after 3 January starts right away, at their own pace, at £69.
- **Refund: statutory rights**, including the 14-day right to cancel under UK consumer law. Final wording to match the Merchant of Record's terms.
- **No sales counter** on the page.
- **No "crew" / cohort framing.** A life reset is an inner, personal process. "We" on the page means Sophie and the reader, never a group of buyers starting together.
- The landing page is being built to also serve the Merchant of Record review: clear product and delivery description, price and statutory-rights line at checkout, legal footer (business name/address placeholders, Terms, Refund policy, Privacy, Cookies, Contact, "processed by [Merchant of Record]").

*Superseded:* **Pricing, final:** £69 full price, £39 at launch/ad-period (introductory). Find Your Bearings is included, not sold separately. Guarantee/refund: still undecided.

**"100+ people over ten years"**: confirmed true by Sophie, cleared for the English page. Individual names are lost, so testimonials stay anonymized.

Other things the cloud session should know (all from Sophie, local session):
- Product line: **RECHART · The Wayfinder Method**, page planned at `artofsmallsteps.com/wayfinder-method`. "Wake up" naming stays (matches the repo's "Wake Up the Inner Navigator").
- Delivery as decided locally: 15 lessons by email, one every 2 days (about 4 weeks), the full 126-page workbook PDF at the end, audio versions promised (audio does not exist yet).
- Launch prerequisites list (Merchant of Record, legal pages, email/DNS, Meta pixel + purchase event with value) and a go-live audit checklist exist in Sophie's local files (`LAUNCH-ELOFELTETELEK.md`), not in this repo — being worked on locally with Sophie directly, cloud session is not picking this up. `/privacy/` and `/terms/` here are on that list.
- The cube/ladder/lion/road/beach test is live in Hungarian as a free answer-key page (`kincsesterkep.hu/megoldokulcs-kocka/`) fed by a YouTube video; in the paid course it is Lesson 1, with the key in the appendix. (Not the model for the English version per the resolution above — no separate free page/video for now.)
