"""Convert the Find Your Bearings canvas artboard (Bearings.dc.html) into a static Astro page.

This is the page the "message in a bottle" email leads to: the game video,
then the answer key, folded until the reader says they've played.

Usage (from the repo root):
  1. Read project/Bearings.dc.html from the "RECHART landing wireframe" Design canvas
     (https://claude.ai/artifact/7n3ErbDfdTQzFUBYGi9zvD) to a local file.
  2. python -I site/tools/bearings_to_astro.py <Bearings.dc.html> site/src/pages/wayfinder-method/find-your-bearings.astro
  3. cd site && npm run build, then commit and push (the branch deploys to production on Vercel).
Images reuse the sales page's files in site/public/images/wayfinder/.
"""
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
html = open(src, encoding="utf-8").read()

start = html.index('<div class="page"')
end = html.index("</x-dc>")
body = html[start:end].rstrip()

blobs = {
    "09db5105a3965a175a26a01a5bcd03e9": "sextant",
    "0356ad3b0acb558cc8c074944d28c9e6": "compass-copper-route",
    "53a58f4924a1160f74e21a74e755ad2d": "map-quill-hand",
    "b3a9ee51047fd0ede4f631ce0c153458": "anchor-rope-waves",
}
for blob, name in blobs.items():
    body = body.replace(f"/_blob/{blob}", f"/images/wayfinder/{name}.webp")

# links between artboards -> real URLs
body = body.replace('href="Main.dc.html" style="display:flex;justify-content:center', 'href="/wayfinder-method/#journey" style="display:flex;justify-content:center')
body = body.replace('<a href="Main.dc.html" style="display:inline-flex', '<a href="/wayfinder-method/#method" style="display:inline-flex')
body = body.replace('href="Main.dc.html"', 'href="/wayfinder-method/"')
body = body.replace('<a href="#key">', '<a href="/wayfinder-method/#legal">')

# the key stays folded until "I've played" is pressed
body = re.sub(r'<sc-if value="\{\{folded\}\}" hint-placeholder-val="\{\{ \w+ \}\}">', '<div data-key="folded">', body)
body = re.sub(r'<sc-if value="\{\{open\}\}" hint-placeholder-val="\{\{ \w+ \}\}">', '<div data-key="open" hidden>', body)
body = body.replace("</sc-if>", "</div>")
body = body.replace('onClick="{{unfold}}"', "data-unfold")

leftover = re.findall(r"\{\{.*?\}\}|<sc-|\{|\}", body)
if leftover:
    sys.exit(f"unconverted template syntax left: {leftover[:5]}")

style = html[html.index("<style>") + len("<style>"):html.index("</style>")]
style += "[data-key][hidden]{display:none}\n"

page = f"""---
// Find Your Bearings: stage 0 of RECHART, the page the "message in a bottle" email leads to.
// Generated from the "Bearings" artboard of the Design canvas "RECHART landing wireframe"
// by site/tools/bearings_to_astro.py; the canvas is the design source of truth.
// noindex: reached from the email only, and the English video is not recorded yet.
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="robots" content="noindex, nofollow" />
    <meta name="description" content="Find Your Bearings: a five-minute game for your imagination, and the key to what your pictures might mean." />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <title>Find Your Bearings · RECHART · Art of Small Steps</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Lora:ital,wght@0,400;0,600;1,400&family=Shadows+Into+Light+Two&display=swap" />
    <style is:global>
{style}    </style>
  </head>
  <body>
{body}

    <script is:inline>
      // "I've played, unfold the key": swap the folded note for the key and bring it into view.
      (function () {{
        var btn = document.querySelector('[data-unfold]');
        btn.addEventListener('click', function () {{
          document.querySelector('[data-key="folded"]').hidden = true;
          var key = document.querySelector('[data-key="open"]');
          key.hidden = false;
          key.setAttribute('tabindex', '-1');
          key.focus({{ preventScroll: true }});
          document.getElementById('key').scrollIntoView({{ behavior: 'smooth', block: 'start' }});
        }});
      }})();
    </script>
  </body>
</html>
"""
open(dst, "w", encoding="utf-8", newline="\n").write(page)
print("ok", len(page))
