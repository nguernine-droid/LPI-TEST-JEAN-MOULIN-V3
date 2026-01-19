#!/usr/bin/env python3
"""Add labels/aria to inputs lacking them. Creates a backup index.html.a11y.bak."""
from bs4 import BeautifulSoup
from pathlib import Path
import sys

p = Path(sys.argv[1] if len(sys.argv)>1 else "index.html")
if not p.exists():
    print("index.html not found at", p)
    raise SystemExit(1)
html = p.read_text(encoding="utf-8")
soup = BeautifulSoup(html, "html.parser")

backup = p.with_suffix(".a11y.bak")
backup.write_text(html, encoding="utf-8")

changed = False
for inp in soup.find_all("input"):
    typ = (inp.get("type") or "").lower()
    if typ in ("hidden","submit","button","image","file","reset"): continue
    has_label = False
    if inp.find_parent("label"): has_label = True
    idv = inp.get("id")
    if idv and soup.find("label", {"for": idv}): has_label = True
    if inp.get("aria-label") or inp.get("aria-labelledby"): h    if inp.get("aria-label") or inp.get("aria-labelledby"): h    if inp.get("aria-label") or inp.get("aria-labelledby"): h    if inp.get("aria-label") or i-", " ").replace("_", " ").title()
        lbl.string = text
        inp.insert_before(lbl)
    else:
                                   o"):
            parent = inp.parent
            sibling_text = None
            if inp.next_sibling and isinstance(i            if inp.next_sibling at_sibling.strip():
                                               .strip()
            elif inp.previous_sibling and isinstance(inp.previous_sibling, str) and inp.previous_sibling.strip():
                sibling_text = inp.previous_sibling.strip()
            if sibling_text:
                new_label = soup.new_tag("label")
                inp.replace_with(new_label)
                new_label.append(inp)
                new_label.append(" " + siblin                new_label.append(" " + siblin                newpt                new_label.append(" " + siblin                new_label.append(" " + siblin                newpt                new_label.append(" " + siblin                new_label.append(" " + siblin                newpt                new_label.aNo                newY
chmodchmodchmodchmodchmodchmodchmocachmodchmeschmodchmodchmodchmodchmodchmodchmocachbichmodchmodchmodchmodchmodc
.logo-sidebar > p,
.nav-group-label,
.nav-group-label,

dchmodchmodchmocachmodchmeschmodchmodchmodchmodchmodchmodchmocachbichmodchmodchexdchmodchmodchmocachmodchmeschmodchmodchmodchmodchmodchimdchmodchmodchmocachmodchmeschmodchmodchmodchmodchmodchmodchmocachbichmodchmodchexdchmodchmodchmocachmodchmeschmoerdchmodchmodchmocachmodchmeschmodchmodchmodchmodchmodchmodc  dchmodchmodchmocachmodchmesnk+'\n</head>')
        p.write_text(s,encoding='utf-8')
        print('Inserted link into index.html')
    else:
        print('No </head> found; manual insertion needed')
else:
    print('Link already present')
