# cat-wisdom (English cat microsite, prepared for artofsmallsteps.com)

Prepared 2026-11-17 by `local-rechart-strategy` at Sophie's request. **Copy, not a move:** the English version stays live on kincsesterkep.hu (`/en/working-cats/` and the three sub pages). Nothing here is wired into `site/` yet; building it into the Astro site belongs to `local-landing-design`.

## What is here

| Path | What it is |
|---|---|
| `pages/index.html` | Main page ("Working cats"). Becomes `/cat-wisdom/` |
| `pages/toto-tells-you.html` | Totó's verdict generator. `/cat-wisdom/toto-tells-you/` |
| `pages/rozi-wisdom.html` | Rozi's wisdom. `/cat-wisdom/rozi-wisdom/` |
| `pages/kormi-helps-decide.html` | Kormi decides. `/cat-wisdom/kormi-helps-decide/` |
| `assets/images/` | 35 images (posters, nav cards, share cards, cat photos, hero), all downloaded from the live pages |
| `assets/fonts/` | 10 Nunito woff2 files (latin + latin-ext), taken from the live pages |

Each page is an HTML **fragment** (style + markup + script, no `<html>`/`<head>`), exactly the content the WordPress page has, wrapped in `#tvm-page` / `.tmm-wrap`. Wrap it in a bare layout (no site header/footer, the pages bring their own nav), set a `<title>` and meta tags, and serve the assets from `/cat-wisdom/assets/`.

## What was already changed in the fragments

- All inline base64 images and fonts were moved out into `assets/` (the main page was 1.8 MB of HTML before, now about 49 KB).
- Image URLs now point to `/cat-wisdom/assets/images/...` (also inside the share-card canvas script of the Totó page, same origin so the canvas stays untainted).
- Links between the four English pages now point to the `/cat-wisdom/...` routes above.

## What is deliberately NOT changed (decisions needed or for landing-design)

1. **Newsletter form.** The WordPress form (FluentForm 24, Kincsestérkep's FluentCRM) is gone; each page has a comment `NEWSLETTER-FORM` where it was, with its CSS left in place (`.fluentform_wrapper_24` rules). Sophie's decision: connect it to EmailOctopus later (one embed per page is an EmailOctopus rule). Until then hide the `#hirlevel` section.
2. **Donate / subscribe buttons** keep the current Kincsestérkep Stripe links (Sophie's decision): donate `https://donate.stripe.com/aFaaEX56W1Am4XH0WIfnO07?locale=en`, monthly 9.99 EUR `https://buy.stripe.com/4gM3cvfLA3Iuai134QfnO08?locale=en`, plus `paypal.me/sophiekemenes`. These are not under the merchant-of-record setup; flagged for Sophie.
3. **Kincsestérkép branding on the pages.** Header logo link and "About" link go to `https://kincsesterkep.hu/` and `/#bemutatkozas`; the footer contact is `sophie@kincsesterkep.hu`. Left as is; decide how the cat site should sit under the Art of Small Steps brand.
4. **"Magyarul" links** go to the live Hungarian pages (`kincsesterkep.hu/macskabolcsessegek/`, `/toto-megmondja/`, `/rozi-bolcsessegek/`, `/kormisegiteldonteni/`). Fine for a copy.
5. **Share card link label** `bit.ly/iaskedacatwhatswrongwithme` (Totó page, `CARD_LINK_LABEL`) and the friend-link `?v=N` logic still point at the kincsesterkep.hu pages. Decide whether the shared link should lead to the new site.
6. **Duplicate content for Google.** The same English pages live on kincsesterkep.hu, so on the new site either add a canonical to the original or set noindex, and add hreflang as needed. No canonical or meta tags are in the fragments.
7. **Not included:** page `<title>`, meta description and Open Graph tags (the share image `assets/images/en-share-all-cats.jpg` is the Open Graph image used live), the GA4 event code is inside the page scripts (generate_verdict, share_verdict, copy_verdict_link, friend_link_open) and will report to whichever GA4 property the site has.

## Source

Fetched from the live WordPress pages 974/975/976/977 on 2026-11-17 (read only). The original build history is in Sophie's local `Kincsesterkep\Macskak\` folder and the memory notes `kincsesterkep-macskabolcsessegek-angol-verzio`.
