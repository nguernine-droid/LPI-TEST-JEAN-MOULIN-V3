#!/usr/bin/env python3
"""
Fix common accessibility issues in index.html:
- Add rel="noopener noreferrer" to <a target="_blank"> when missing
- Add aria-label, role="button" and tabindex="0" to elements with onclick="switchSection('id')"
Creates backups before writing.
"""
import re
from pathlib import Path
p = Path('index.html')
if not p.exists():
    print('ERROR: index.html not found in current directory')
    raise SystemExit(1)
text = p.read_text(encoding='utf-8')
orig = text

# 1) Add rel to target="_blank" if missing
# This matches <a ... target="_blank" ...>
def add_rel(m):
    tag = m.group(0)
    if re.search(r"\brel\s*=", tag, re.I):
        return tag
    # insert before the closing > of the start tag
    return tag[:-1] + ' rel="noopener noreferrer">'
text = re.sub(r'<a\b[^>]*\btarget=(?:"|\')_blank(?:"|\')[^>]*>', add_rel, text, flags=re.I|re.S)

# 2) Add aria-label/role/tabindex to elements with onclick="switchSection('id')"
def add_attrs_to_onclick(m):
    full = m.group(0)
    tag = m.group('tag')
    attrs = m.group('attrs') or ''
    id = m.group('id')
    additions = []
    if not re.search(r"\baria-(label|labelledby)\s*=", attrs, re.I):
        additions.append(f'aria-label="Ouvrir la section {id}"')
    if not re.search(r"\brole\s*=", attrs, re.I):
        additions.append('role="button"')
    if not re.search(r"\btabindex\s*=", attrs, re.I):
        additions.append('tabindex="0"')
    if additions:
        # insert additions before the closing >
        return full[:-1] + ' ' + ' '.join(additions) + '>'
    return full

text = re.sub(r'<(?P<tag>[a-zA-Z0-9]+)(?P<attrs>[^>]*)onclick=\"switchSection\((?:\'|\")(?P<id>[^\'\"]+)(?:\'|\")\)\"(?P<after>[^>]*)>', add_attrs_to_onclick, text, flags=re.I|re.S)

if text == orig:
    print('No changes needed')
else:
    bak = Path('index.html.a11y.bak')
    bak.write_text(orig, encoding='utf-8')
    p.write_text(text, encoding='utf-8')
    print('Patched index.html; backup saved to', str(bak))

# Summary counts
print('\nSummary counts:')
print('target="_blank" count ->', len(re.findall(r'target=\"_blank\"', text)))
print('rel noopener occurrences ->', len(re.findall(r'rel=\"noopener noreferrer\"', text)))
print('onclick switchSection occurrences ->', len(re.findall(r'onclick=\"switchSection', text)))
print('aria-label additions ->', len(re.findall(r'aria-label=\"Ouvrir la section', text)))
