"""Convert the RECHART landing canvas artboard (Main.dc.html) into a static Astro page.

Usage (from the repo root):
  1. Read project/Main.dc.html from the "RECHART landing wireframe" Design canvas
     (https://claude.ai/artifact/7n3ErbDfdTQzFUBYGi9zvD) to a local file.
  2. python -I site/tools/dc_to_astro.py <Main.dc.html> site/src/pages/wayfinder-method/index.astro
  3. cd site && npm run build, then commit and push (the branch deploys to production on Vercel).
New canvas images: add the /_blob/<id> -> file name pair to `blobs` and the .webp to
site/public/images/wayfinder/.
"""
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
html = open(src, encoding="utf-8").read()

start = html.index('<div class="page"')
end = html.index("</x-dc>")
body = html[start:end].rstrip()

blobs = {
    "f191a2db0f29c302f2b599314948e40d": "hero-sailboat-sunset-banner",
    "6b107dc03f1b7d738c91f2795a12f366": "woman-sitting-thinking-bun",
    "edc176d6caaf0cf5741787cb7d0219de": "man-wiping-foggy-window",
    "09db5105a3965a175a26a01a5bcd03e9": "sextant",
    "0356ad3b0acb558cc8c074944d28c9e6": "compass-copper-route",
    "53a58f4924a1160f74e21a74e755ad2d": "map-quill-hand",
    "b3a9ee51047fd0ede4f631ce0c153458": "anchor-rope-waves",
    "8d777366d45c395955640029d2d89a44": "helm-woman-wind-portrait",
    "a8580c855686d99502e73f36559e08b4": "travel-trunk-map-boots",
    "661ebeb1da495d7f034384fdec5c3e46": "boarding-sailboat-from-pier",
    "91d3547b37fdf198b746c26d52611f12": "man-bow-facing-wind",
    "2e3230be8c54bef262815563918a3efd": "sophie-portrait-compass",
    "790857a0c9c439ea7523e99c74e79577": "message-in-bottle",
    "47bc6627a7444bf5f9d72920868ed497": "sophie-first-mate-oar",
    "6b8ab26509e8a54dde92d46ea8f7d97f": "hero-becalmed-sailboat",
}
for blob, name in blobs.items():
    body = body.replace(f"/_blob/{blob}", f"/images/wayfinder/{name}.webp")

body = body.replace('<div class="page" style="--body: {{bodyStack}}; --hand: {{handStack}}">', '<div class="page">')
body = body.replace("--log-order: {{logOrder}};", "--log-order: 1;")
body = body.replace("{{activeLabel}}", '<span id="log-label">Stage 0 · free taste</span>')

def card(m):
    n = m.group(1)
    return f'data-stage="{n}" aria-pressed="{"true" if n == "0" else "false"}"'
body = re.sub(r'onClick="\{\{pick(\d)\}\}" aria-pressed="\{\{a\d\}\}"', card, body)

# sc-if on one line (the "You are here" badges inside the buttons) -> span; multi-line blocks -> div
def inline_if(m):
    n, inner = m.group(1), m.group(2)
    return f'<span data-show="{n}"{"" if n == "0" else " hidden"}>{inner}</span>'
body = re.sub(r'<sc-if value="\{\{a(\d)\}\}" hint-placeholder-val="\{\{ \w+ \}\}">(.*?)</sc-if>', inline_if, body)
def block_if(m):
    n = m.group(1)
    return f'<div data-show="{n}"{"" if n == "0" else " hidden"}>'
body = re.sub(r'<sc-if value="\{\{a(\d)\}\}" hint-placeholder-val="\{\{ \w+ \}\}">', block_if, body)
body = body.replace("</sc-if>", "</div>")

body = body.replace('<form style=', '<form data-preview-form style=')

leftover = re.findall(r"\{\{.*?\}\}|<sc-|\{|\}", body)
if leftover:
    sys.exit(f"unconverted template syntax left: {leftover[:5]}")

style = html[html.index("<style>") + len("<style>"):html.index("</style>")]
style = style.replace("var(--body,'Source Sans 3',system-ui,sans-serif)", "'Lora',Georgia,serif")
style = style.replace("var(--hand,'Caveat',cursive)", "'Shadows Into Light Two',cursive")
style += "[data-show][hidden]{display:none}\n"

page = f"""---
// RECHART / The Wayfinder Method sales landing page.
// Generated from the approved Design canvas "RECHART landing wireframe"
// (claude.ai artifact, 2026-11-02) by site/tools/dc_to_astro.py: the
// canvas is the design source of truth while copy is still being reviewed.
// Standalone document on purpose: no site nav on the sales page (Sophie,
// 2026-11-02), so it does not use Layout.astro. noindex until launch:
// the page still carries [placeholders] (legal details, checkout, signup).
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="robots" content="noindex, nofollow" />
    <meta name="description" content="RECHART · The Wayfinder Method. Maybe you don't need a new life. Maybe you need a new direction." />
    <link rel="canonical" href="https://artofsmallsteps.com/wayfinder-method/" />
    <!-- share preview (Facebook, LinkedIn, WhatsApp, X); image made from site/tools/og-rechart.html -->
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="Art of Small Steps" />
    <meta property="og:url" content="https://artofsmallsteps.com/wayfinder-method/" />
    <meta property="og:title" content="Becalmed? RECHART · The Wayfinder Method" />
    <meta property="og:description" content="Maybe you don't need a new life. Maybe you need a new direction. A self-paced training to pause, find your bearings and work out what comes next. We set sail on 3 January 2027." />
    <meta property="og:image" content="https://artofsmallsteps.com/images/wayfinder/og-rechart.jpg" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta property="og:image:alt" content="Becalmed? A small sailboat alone on a mirror-calm watercolor sea" />
    <meta name="twitter:card" content="summary_large_image" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <title>RECHART · The Wayfinder Method · Art of Small Steps</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Lora:ital,wght@0,400;0,600;1,400&family=Shadows+Into+Light+Two&display=swap" />
    <style is:global>
{style}    </style>
  </head>
  <body>
{body}

    <script is:inline>
      // Stage cards: move the "You are here" seal, swap the ship's log page,
      // and on phones (CSS order) drop the log page right under the tapped card.
      (function () {{
        var labels = ['Stage 0 · free taste', 'Stage 1 · lessons 1–6', 'Stage 2 · lessons 7–12', 'Stage 3 · lessons 13–15'];
        var cards = document.querySelectorAll('[data-stage]');
        var panel = document.querySelector('.log-panel');
        var label = document.getElementById('log-label');
        cards.forEach(function (card) {{
          card.addEventListener('click', function () {{
            var n = card.getAttribute('data-stage');
            cards.forEach(function (c) {{ c.setAttribute('aria-pressed', String(c === card)); }});
            document.querySelectorAll('[data-show]').forEach(function (el) {{
              el.hidden = el.getAttribute('data-show') !== n;
            }});
            label.textContent = labels[n];
            panel.style.setProperty('--log-order', String(n * 2 + 1));
          }});
        }});
        // Email signup is not connected yet: keep the preview from reloading.
        var form = document.querySelector('[data-preview-form]');
        form.addEventListener('submit', function (e) {{
          e.preventDefault();
          form.insertAdjacentHTML('afterend', '<p style="margin:12px 0 0;font-size:15px;color:#1C4F6B">Thank you! (Preview: the email signup is not connected yet.)</p>');
        }}, {{ once: true }});
      }})();
    </script>
  </body>
</html>
"""
open(dst, "w", encoding="utf-8", newline="\n").write(page)
print("ok", len(page))
