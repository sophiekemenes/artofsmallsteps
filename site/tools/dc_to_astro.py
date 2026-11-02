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

# Exit-intent popup (Sophie, 2026-11-02): page behaviour rather than canvas content, so it lives here.
# Offers the free first stage to someone leaving before they reached the bottle signup.
# Desktop: pointer leaves through the top of the window. Phones: a fast scroll back up.
# At most once per visit, never after the #bearings section was seen or a form was sent.
# Add ?popup to the URL to see it straight away.
popup = """
    <dialog id="exit-popup" aria-labelledby="exit-popup-h">
      <button type="button" class="exit-close" aria-label="Close" data-close>&times;</button>
      <img src="/images/wayfinder/message-in-bottle.webp" alt="" class="exit-img" />
      <p class="hand" style="margin:0;font-size:24px;color:#8A5129">Before you drift off…</p>
      <h2 id="exit-popup-h" class="display" style="margin:4px 0 0;font-size:clamp(30px,4vw,40px);line-height:1.1">Take a message in a bottle with you.</h2>
      <p style="margin:14px 0 0;font-size:17px;line-height:1.65;color:#3E4852">A five-minute game for your imagination, and the first stage of the Wayfinder Method. Free. Leave your email and I'll send you the bottle. The rest of this page will still be here whenever you want it. (Or never. I'll survive.)</p>
      <form id="exit-form" style="margin-top:20px;display:flex;flex-wrap:wrap;gap:10px">
        <label style="flex:1 1 220px;display:flex;flex-direction:column;gap:6px;font-size:14px;font-weight:600;color:#142230">Your email
          <input type="email" required placeholder="you@example.com" style="font:inherit;font-weight:400;font-size:17px;padding:13px 16px;border:1.5px solid #142230;border-radius:999px;background:#FFF9F0;color:#142230;min-height:48px;box-sizing:border-box" />
        </label>
        <button type="submit" class="btn" style="align-self:flex-end;background:#142230;color:#FBF1E3;border:0;padding:0 26px;border-radius:999px;font:inherit;font-weight:600;font-size:17px;min-height:48px;cursor:pointer">Send me the bottle</button>
      </form>
      <p style="margin:12px 0 0;font-size:13px;color:#4A5560">You can unsubscribe with one click, any time.</p>
      <button type="button" data-close style="margin-top:10px;background:none;border:0;padding:8px 0;min-height:44px;font:inherit;font-size:15px;color:#4A5560;text-decoration:underline;cursor:pointer">No thanks, I'll keep looking around</button>
    </dialog>

    <script is:inline>
      (function () {
        var dlg = document.getElementById('exit-popup');
        if (!dlg || !dlg.showModal) return;
        var KEY = 'rechart-exit-popup';
        var done = false, start = Date.now();
        try { if (sessionStorage.getItem(KEY)) done = true; } catch (e) {}
        var bearings = document.getElementById('bearings');
        function reachedBearings() {
          return bearings && bearings.getBoundingClientRect().top < window.innerHeight * 0.7;
        }
        function open() {
          if (done || reachedBearings()) { if (reachedBearings()) done = true; return; }
          done = true;
          try { sessionStorage.setItem(KEY, '1'); } catch (e) {}
          dlg.showModal();
        }
        function stop() { done = true; }
        // someone who has seen the bottle signup, or sent a form, never gets the popup
        document.addEventListener('submit', function (e) { if (e.target.id !== 'exit-form') stop(); }, true);
        // desktop: the pointer leaves through the top edge (towards the tabs or the address bar)
        document.addEventListener('mouseout', function (e) {
          if (!e.relatedTarget && e.clientY <= 0 && Date.now() - start > 8000) open();
        });
        // phones: a quick scroll back up after reading a while
        var lastY = window.scrollY, lastT = Date.now();
        window.addEventListener('scroll', function () {
          var y = window.scrollY, t = Date.now();
          if (reachedBearings()) stop();
          if (matchMedia('(pointer: coarse)').matches && t - start > 20000 && y > 600 && lastY - y > 250 && t - lastT < 400) open();
          if (t - lastT > 150) { lastY = y; lastT = t; }
        }, { passive: true });
        dlg.querySelectorAll('[data-close]').forEach(function (b) { b.addEventListener('click', function () { dlg.close(); }); });
        dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
        // the signup is not connected yet: thank instead of sending
        document.getElementById('exit-form').addEventListener('submit', function (e) {
          e.preventDefault();
          this.outerHTML = '<p style="margin:20px 0 0;font-size:17px;color:#1C4F6B">Thank you! (Preview: the email signup is not connected yet.)</p>';
        });
        if (/[?&]popup\\b/.test(location.search)) setTimeout(open, 600);
      })();
    </script>"""

popup_style = """
#exit-popup{max-width:520px;width:calc(100% - 32px);box-sizing:border-box;border:0;border-radius:6px;padding:30px 30px 18px;background:#FFF8EE;color:#142230;box-shadow:0 30px 70px rgba(5,14,24,.35);font-family:'Lora',Georgia,serif}
#exit-popup::backdrop{background:rgba(20,34,48,.45)}
#exit-popup .exit-img{display:block;width:180px;height:auto;margin:-6px auto 10px;-webkit-mask-image:radial-gradient(ellipse 70% 70% at 50% 50%,#000 55%,transparent 100%);mask-image:radial-gradient(ellipse 70% 70% at 50% 50%,#000 55%,transparent 100%)}
#exit-popup .exit-close{position:absolute;top:8px;right:8px;width:44px;height:44px;border:0;background:none;font-size:30px;line-height:1;color:#4A5560;cursor:pointer}
#exit-popup .exit-close:focus-visible,#exit-popup [data-close]:focus-visible{outline:3px solid #1C4F6B;outline-offset:2px}
"""
style += popup_style

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
{popup}

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
