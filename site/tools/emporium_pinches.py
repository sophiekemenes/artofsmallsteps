"""Build site/src/data/emporium-pinches.json from emporium/copy/01-missions-en.md.

Run from the repo root (or anywhere): python site/tools/emporium_pinches.py
Re-run whenever the missions file changes, then commit the JSON.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "emporium" / "copy" / "01-missions-en.md"
OUT = ROOT / "site" / "src" / "data" / "emporium-pinches.json"

flavour = None
pinches = []
cur = None
for line in SRC.read_text(encoding="utf-8").splitlines():
    m = re.match(r"^## (.+?) · ", line)
    if m:
        flavour = m.group(1).strip()
        continue
    m = re.match(r"^\*\*No\. (\d+) · (.+?)\*\*", line)
    if m and flavour:
        cur = {"no": m.group(1), "flavour": flavour, "title": m.group(2).strip(), "text": ""}
        pinches.append(cur)
        continue
    if cur is not None:
        if line.strip() == "" or line.startswith("#") or line.startswith("---"):
            if cur["text"]:
                cur = None
            continue
        cur["text"] = (cur["text"] + " " + line.strip()).strip()

assert len(pinches) == 57, f"expected 57 pinches, got {len(pinches)}"
assert all(p["text"] for p in pinches), "empty pinch text"
assert "—" not in json.dumps(pinches, ensure_ascii=False), "em dash found"
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(pinches, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"{len(pinches)} pinches -> {OUT}")
