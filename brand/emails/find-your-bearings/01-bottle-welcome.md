# Find Your Bearings · The bottle email (welcome)

- **Status:** APPROVED by Sophie 2026-11-23 (header image still to be generated)
- **Where it lives:** EmailOctopus → Automations → "Find Your Bearings - welcome" → step "Welcome email". Trigger: Contact added. The automation is **PAUSED** right now, so new signups get nothing until it's switched back on.
- **Sent from:** Sophie | Art of Small Steps <hello@artofsmallsteps.com>
- **Merge tags:** none. The signup form only asks for an email address, so the greeting is "Hi there," (Sophie, 2026-11-23). Open question for later: add an optional First name field to the EmailOctopus form? Trade-off: a personal greeting versus one more field before the game starts.
- **Sophie's edits 2026-11-23:** subject option 3 chosen; "in person" added to the 200; **no Hungarian origin, no other language, no Kincsestérkép at all** (Sophie: UK readers, don't push "I'm not British" at them); the 150,000 views of the original video added (YouTube shows ~158k).
- **Placeholders:** `[HEADER-IMAGE]` (to be generated in ChatGPT), `[SOPHIE-PHOTO]` (ready: `brand/visual/email-assets/sophie-polaroid-email.jpg`)
- **Links:** button → `https://artofsmallsteps.com/wayfinder-method/find-your-bearings/` · RECHART → `https://artofsmallsteps.com/wayfinder-method/`

## What was weak in v1, and what changed

- **The opening** told people what they'd signed up for instead of handing it over. Now the first line is the gift, and the button comes straight after it.
- **There was no "how to play".** The game needs a quiet corner, a pen and your first impression, and the key shouldn't be read early. All of that is now in four short lines before anything else. This is also what makes the game work.
- **The "why"** (ten years, over 200 people, the pub bench, keys rather than a portrait) is kept, because it's your own and it's the strongest part. It now has its own heading, so it doesn't disappear into the middle of the email.
- **There was no person in it.** Now there's your photo and a few lines about who you are, with no origin story: self-development, change, hard bits, making things of use, and the 150,000 views of the game's original video.
- **The newsletter paragraph is kept almost word for word.** "Much." stays as the punchline.
- **A P.S. invites a reply.** It's warmer, and replies also help deliverability.
- **Removed:** the empty 3-column row under the button (the "Drag content blocks here" boxes) and the divider line.
- **FYB rule:** none of the seven symbols (cube, ladder, lion, road, sea, house, horse), and no scene from the game, appears in the email or in the header image. The text names none of them; "voyage" and "set sail" are RECHART's brand language, not the game's sea scene.

## Design (the "watered-down colours")

The current version is cream on cream: a cream page, a cream card, grey Arial text and a light copper button, so nothing has weight. Suggested settings, all from the brandbook tokens:

| Element | Now | Suggested |
|---|---|---|
| Page background | cream | cream `#F7F5F0` (keep) |
| Content card | cream | **white `#FFFFFF`**, so the letter sits on the paper like a page |
| Body text | grey, Arial ~15px | **navy `#142230`, Georgia, 17px**, line height 1.6 |
| Headings (2 small ones) | none | Georgia, 20px, dusty blue `#1C4F6B` |
| Button | light copper, white text | **copper `#B87345`, white bold text, 16px**, a bit narrower |
| Links | copper | dusty blue `#1C4F6B`, underlined |
| Top | small logo | logo, then the **2:1 header image**, full card width |
| Photo | none | **`brand/visual/email-assets/sophie-polaroid-email.jpg`** (Sophie's choice 2026-11-23: the landing-page watercolour portrait, as a taped polaroid on white, 551×699, 60 KB). Upload to EmailOctopus Images, show it **centred, 260px wide**, alt text "Sophie", at the top of the "Who's writing to you" section. JPG, not WebP, because Outlook can't show WebP. |

Also check: "Sent with EmailOctopus" still shows at the bottom of the footer, even though the account is on Pro. The branding switch is under Brand → Settings or the template's Settings tab.

---

**Subject:** The game I've been playing with people for ten years

**Preview text:** Free, and there's no way to do it wrong.

---

[HEADER-IMAGE]

Hi there,

You've opened the bottle. Here's what was inside:

**[BUTTON: Play Find Your Bearings →]**

It takes about six minutes, plus however long you want to spend writing.

Before you press play:

- **Find a quiet corner.** Kettle on, phone face down.
- **Keep a pen and paper close.** You'll pause the video and write down what you see.
- **Go with your very first picture.** Not the clever one, not the nice one. The first one.
- **Don't scroll down to the key until you've finished.** I know. I'd want to peek too.

## Why I keep coming back to this game

For about ten years now I've considered it the best psychological game around. I've played it in person with over 200 people, sometimes sitting on a pub bench, and the likeness between a person and what they came up with was often unbelievable.

One small warning, though: it won't tell you what you're like. It works from your own imagination, and what it hands you are **keys**. So if you're hoping for a neat portrait that says exactly who you are, you won't get one. What can happen instead is a big aha: the moment you realise you've been holding the key all along.

And there's no way to do it wrong. Whatever comes up is yours. That's the whole point.

## Who's writing to you

[SOPHIE-PHOTO]

I'm Sophie. I'm into self-development: growing, changing, and getting through the hard bits (my own included). All my life I've been trying to make things that are of real use to people. This game is one of them. Its original video has already been watched more than 150,000 times.

You're on my newsletter now too. I'll write to you now and then, though I honestly don't know yet what or when. My advice: don't unsubscribe right away (I do that too, sometimes). Wait a bit and see what I'm cooking up. I've got a few more playful things up my sleeve. But if you do unsubscribe, I promise I won't take it personally. Much.

If the game opens something up and you'd like to keep going: Find Your Bearings is the first stage of **RECHART: The Wayfinder Method**, a self-paced voyage in small, doable steps. We set sail on 3 January 2027. [Have a look at the route →]

With love,
Sophie

P.S. If something on your page surprises you, hit reply and tell me what. I'd love to hear it.

---

## Header image prompt (ChatGPT)

Use the STYLE block from `brand/visual/email-headers/HEADER-PROMPTS.md` and the same two reference images, then:

```
Scene: an old wooden chart table in soft morning light from a small window on the left. On it lies a small glass message bottle, its cork just pulled out and resting beside it, the rolled paper message half unrolled next to the bottle, blank. Nearby: a pencil, a small brass compass and a closed notebook. Faded chart paper under everything, with a few dashed route lines and no land shapes. Quiet, hopeful, a little secret, as if someone is about to begin. Bottle slightly right of centre, lots of soft cream space at the top.
```

Rules check: no text, no faces, and none of the seven Find Your Bearings symbols. **No sea, shore or water in the picture,** because the sea is one of the symbols. That's why this is a table and not a beach.
