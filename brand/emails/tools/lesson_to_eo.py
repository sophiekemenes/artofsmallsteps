"""Turn the approved RECHART lesson .md files into ONE EmailOctopus "Code" block each.

Usage: python lesson_to_eo.py [headers.json]
  headers.json (optional) maps a lesson slug ("01", "06b", ...) to its EmailOctopus-hosted header image URL.
  Lessons without a URL get no header image (an HTML comment marks the spot).

Output: brand/emails/rechart-lessons/eo/<file>.html plus eo/_subjects.txt (subject + preview per lesson).

Builds on md_to_eo.py (same style) and adds what the lessons need:
- body = from the 2nd '---' to the LAST '---' (lesson 12 has a '---' divider inside the body)
- '> ' blockquotes become a cream box with a copper left border (opening scenes, the first mate's logbook)
- '1. item' lines become numbered lists
- {{Nickname}} becomes {{Nickname|default("Wayfinder")}}
- FYB links get ?from=rechart
- placeholders that aren't ready yet are hidden inside HTML comments, so readers never see a raw
  [PLACEHOLDER]: the audio line ([AUDIO-LINK]) sits ready-made in a comment at the top of the lesson,
  any other paragraph with an unfilled [PLACEHOLDER] is commented out with a TODO note
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from md_to_eo import BODY, H2, LINK, button, inline  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
LESSONS = os.path.join(HERE, "..", "rechart-lessons")
OUT = os.path.join(LESSONS, "eo")

# Filled placeholders (known, public URLs)
FILLED = {
    "[AMY-CUDDY-TED-LINK]": "[Watch Amy Cuddy's talk →](https://www.ted.com/talks/amy_cuddy_your_body_language_may_shape_who_you_are)",
}

QUOTE = ("margin:0 0 24px;padding:16px 20px;background:#F7F5F0;border-left:3px solid #B87345;"
         "font-size:16px;line-height:1.6;color:#2a3a48;")
HR = '<hr style="border:0;border-top:1px solid #E3DDD2;margin:28px 0;">'
PH = re.compile(r"\[[A-Z][A-Z0-9-]+\]")


def body_of(md):
    lines = md.splitlines()
    seps = [i for i, l in enumerate(lines) if l.strip() == "---"]
    return "\n".join(lines[seps[1] + 1:seps[-1]]).strip()


def meta(md, key):
    m = re.search(rf"^\*\*{key}:\*\*\s*(.+)$", md, re.M)
    return m.group(1).strip() if m else ""


def para(b, style="margin:0 0 18px;"):
    return f'<p style="{style}">{inline(b).replace(chr(10), "<br>")}</p>'


def render_block(b):
    m = re.fullmatch(r"\*{0,2}\[([^\]]+)\]\(([^)]+)\)\*{0,2}", b)
    if m:
        return button(m.group(1), m.group(2))
    if b.startswith("## "):
        return f'<h2 style="{H2}">{inline(b[3:])}</h2>'
    lines = b.splitlines()
    if all(l.startswith("- ") for l in lines):
        lis = "".join(f'<li style="margin:0 0 8px;">{inline(l[2:])}</li>' for l in lines)
        return f'<ul style="margin:0 0 24px;padding-left:22px;">{lis}</ul>'
    if all(re.match(r"\d+\. ", l) for l in lines):
        start = re.match(r"(\d+)\. ", lines[0]).group(1)
        lis = "".join(f'<li style="margin:0 0 6px;">{inline(re.sub(r"^\d+\. ", "", l))}</li>' for l in lines)
        return f'<ol start="{start}" style="margin:0 0 24px;padding-left:26px;">{lis}</ol>'
    if b.startswith("With love,"):
        name = lines[1] if len(lines) > 1 else "Sophie"
        return '<p style="margin:0 0 4px;">With love,</p>' f'<p style="margin:0 0 26px;">{inline(name)}</p>'
    if b.startswith("P.S.") or b.startswith("P.P.S."):
        return para(b, "margin:0 0 20px;font-size:15px;color:#3a4a58;")
    return para(b)


def convert(md, header_url, slug):
    body = body_of(md)
    for k, v in FILLED.items():
        body = body.replace(k, v)
    body = body.replace("{{Nickname}}", '{{Nickname|default("Wayfinder")}}')
    body = re.sub(r"(find-your-bearings/)(?!\?from=rechart)(?=[)\s])", r"\1?from=rechart", body)

    out, todos = [], []
    # group lines into blocks; a run of '>' lines is one quote block
    blocks = re.split(r"\n\s*\n", body)
    for b in blocks:
        b = b.strip()
        if not b:
            continue
        if b == "---":
            out.append(HR)
            continue
        if "[AUDIO-LINK]" in b:
            out.append(f"<!-- AUDIO LINK (lesson {slug}): when the recording exists, put its URL in place of AUDIO-URL "
                       "and delete the two comment markers around the next line. -->\n<!-- "
                       f'<p style="margin:0 0 22px;font-size:15px;"><em><a href="AUDIO-URL" style="{LINK}">'
                       "Listen to this lesson instead &rarr;</a></em></p> -->")
            continue
        if b.startswith(">"):
            inner = re.sub(r"^> ?", "", b, flags=re.M)
            parts = [p.strip() for p in re.split(r"\n\s*\n", inner) if p.strip()]
            html_parts = "".join(para(p, "margin:0 0 10px;") for p in parts)
            out.append(f'<div style="{QUOTE}">{html_parts}</div>')
            continue
        missing = PH.findall(b)
        if missing:
            todos.append(", ".join(missing))
            out.append(f"<!-- TODO (lesson {slug}): {', '.join(missing)} not ready yet. This paragraph is hidden until "
                       "the link exists: put the URL in, then delete the comment markers. -->\n<!-- "
                       + render_block(b).replace("--", "&#45;&#45;") + " -->")
            continue
        out.append(render_block(b))

    head = (f'<tr><td style="padding:0;"><img src="{header_url}" width="100%" alt="" '
            'style="display:block;width:100%;height:auto;border:0;"></td></tr>' if header_url
            else f"<!-- HEADER IMAGE (lesson {slug}): none yet -->")
    html_out = ('<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" '
                'style="background:#FFFFFF;border-collapse:collapse;">' + head +
                f'<tr><td style="padding:32px 36px 14px;{BODY}">' + "\n".join(out) + "</td></tr></table>")
    return html_out, todos


if __name__ == "__main__":
    headers = json.load(open(sys.argv[1], encoding="utf-8")) if len(sys.argv) > 1 else {}
    os.makedirs(OUT, exist_ok=True)
    summary = []
    for f in sorted(os.listdir(LESSONS)):
        m = re.match(r"(\d\db?)-.+\.md$", f)
        if not m:
            continue
        slug = m.group(1)
        md = open(os.path.join(LESSONS, f), encoding="utf-8").read()
        res, todos = convert(md, headers.get(slug, ""), slug)
        open(os.path.join(OUT, f[:-3] + ".html"), "w", encoding="utf-8", newline="\n").write(res + "\n")
        left = PH.findall(re.sub(r"<!--.*?-->", "", res, flags=re.S))
        summary.append(f"{slug}\t{meta(md, 'Subject')}\t{meta(md, 'Preview text')}\t"
                       f"header={'yes' if headers.get(slug) else 'NO'}\thidden={';'.join(todos) or '-'}\tvisible_ph={left or '-'}\tlen={len(res)}")
    open(os.path.join(OUT, "_subjects.txt"), "w", encoding="utf-8", newline="\n").write("\n".join(summary) + "\n")
    print("\n".join(summary))
