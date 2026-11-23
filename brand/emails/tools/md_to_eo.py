"""Turn an approved email .md (brand/emails/...) into the HTML for ONE EmailOctopus "Code" block.

Usage: python md_to_eo.py <email.md> <header-image-url> [out.html]

Reads the body between the 2nd and 3rd '---' lines (or to the end / a '## Header' section).
Rules:
- a paragraph that is only **[Text](url)** or [Text](url) becomes the copper button
- '## Heading' becomes a dusty-blue h2
- '- item' lines become a list
- 'With love,' + 'Sophie' become the signature, a 'P.S.' paragraph gets the small grey style
- **bold**, *italic* and inline [text](url) links are converted
Style = the FYB bottle welcome v2 (navy Georgia 17px on white, copper button).
"""
import html
import re
import sys

BODY = "font-family:Georgia,'Times New Roman',serif;font-size:17px;line-height:1.6;color:#142230;"
H2 = "margin:4px 0 12px;font-family:Georgia,'Times New Roman',serif;font-size:21px;font-weight:normal;color:#1C4F6B;"
LINK = "color:#1C4F6B;text-decoration:underline;"


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f'<a href="{m.group(2)}" style="{LINK}">{m.group(1)}</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    return t.replace("→", "&rarr;").replace("’", "'")


def button(text, url):
    text = html.escape(text, quote=False).replace("→", "&rarr;")
    return ('<table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center" style="margin:6px auto 24px;">'
            f'<tr><td align="center" bgcolor="#B87345" style="border-radius:28px;"><a href="{url}" style="display:inline-block;'
            'padding:15px 34px;font-family:Arial,Helvetica,sans-serif;font-size:16px;font-weight:bold;color:#FFFFFF;'
            f'text-decoration:none;border-radius:28px;">{text}</a></td></tr></table>')


def body_of(md):
    lines = md.splitlines()
    seps = [i for i, l in enumerate(lines) if l.strip() == "---"]
    start = seps[1] + 1
    end = seps[2] if len(seps) > 2 else len(lines)
    return "\n".join(lines[start:end]).strip()


def convert(md, header_url):
    blocks = re.split(r"\n\s*\n", body_of(md))
    out = []
    for b in blocks:
        b = b.strip()
        if not b:
            continue
        m = re.fullmatch(r"\*{0,2}\[([^\]]+)\]\(([^)]+)\)\*{0,2}", b)
        if m:
            out.append(button(m.group(1), m.group(2)))
        elif b.startswith("## "):
            out.append(f'<h2 style="{H2}">{inline(b[3:])}</h2>')
        elif all(l.startswith("- ") for l in b.splitlines()):
            items = b.splitlines()
            lis = "".join(f'<li style="margin:0 0 8px;">{inline(l[2:])}</li>' for l in items)
            out.append(f'<ul style="margin:0 0 24px;padding-left:22px;">{lis}</ul>')
        elif b.startswith("With love,"):
            name = b.splitlines()[1] if "\n" in b else "Sophie"
            out.append('<p style="margin:0 0 4px;">With love,</p>' f'<p style="margin:0 0 26px;">{inline(name)}</p>')
        elif b.startswith("P.S.") or b.startswith("P.P.S."):
            out.append(f'<p style="margin:0 0 20px;font-size:15px;color:#3a4a58;">{inline(b).replace(chr(10), "<br>")}</p>')
        else:
            out.append(f'<p style="margin:0 0 18px;">{inline(b).replace(chr(10), "<br>")}</p>')
    return ('<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border-collapse:collapse;">'
            f'<tr><td style="padding:0;"><img src="{header_url}" width="100%" alt="" style="display:block;width:100%;height:auto;border:0;"></td></tr>'
            f'<tr><td style="padding:32px 36px 14px;{BODY}">' + "".join(out) + "</td></tr></table>")


if __name__ == "__main__":
    src, url = sys.argv[1], sys.argv[2]
    res = convert(open(src, encoding="utf-8").read(), url)
    dst = sys.argv[3] if len(sys.argv) > 3 else src[:-3] + ".html"
    open(dst, "w", encoding="utf-8", newline="\n").write(res + "\n")
    print(dst, len(res))
