#!/usr/bin/env python3
"""Auto-insert accessible labels for inputs/selects/textareas.

Usage: python3 scripts/fix_inputs_clean.py path/to/index.html

Creates a backup at path + '.bak.fixlabels' before editing.
"""
import sys
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except Exception:
    print('BeautifulSoup not found. Install with: pip3 install beautifulsoup4')
    raise


def ensure_id(el, prefix='auto-input', counter=[1]):
    if el.has_attr('id') and el['id'].strip():
        return el['id']
    candidate = f"{prefix}-{counter[0]}"
    counter[0] += 1
    el['id'] = candidate
    return candidate


def add_label_before(soup, el, text):
    label = soup.new_tag('label')
    label['for'] = el['id']
    label.string = text
    el.insert_before(label)


def wrap_with_label(soup, el, text):
    label = soup.new_tag('label')
    if el.has_attr('id'):
        label['for'] = el['id']
    el.replace_with(label)
    label.append(el)
    label.append(' ' + text)


def derive_label_text(el):
    for attr in ('placeholder', 'title', 'aria-label', 'name'):
        if el.has_attr(attr) and el[attr].strip():
            return el[attr].strip()
    ns = el.next_sibling
    if ns and isinstance(ns, str) and ns.strip():
        return ns.strip()[:60]
    ps = el.previous_sibling
    if ps and isinstance(ps, str) and ps.strip():
        return ps.strip()[:60]
    return 'Champ de formulaire'


def process(soup):
    changed = False
    for inp in soup.find_all('input'):
        if inp.find_parent('label'):
            continue
        if inp.has_attr('aria-label') or inp.has_attr('aria-labelledby'):
            continue
        typ = (inp.get('type') or '').lower()
        if typ in ('hidden', 'submit', 'button', 'image', 'file', 'reset'):
            continue
        lbl = derive_label_text(inp)
        ensure_id(inp)
        if typ in ('checkbox', 'radio'):
            wrap_with_label(soup, inp, lbl)
        else:
            add_label_before(soup, inp, lbl)
        changed = True

    for ta in soup.find_all('textarea'):
        if ta.find_parent('label') or ta.has_attr('aria-label'):
            continue
        lbl = derive_label_text(ta)
        ensure_id(ta)
        add_label_before(soup, ta, lbl)
        changed = True

    for sel in soup.find_all('select'):
        if sel.find_parent('label') or sel.has_attr('aria-label'):
            continue
        lbl = derive_label_text(sel)
        ensure_id(sel)
        add_label_before(soup, sel, lbl)
        changed = True

    return changed


def main():
    if len(sys.argv) < 2:
        print('Usage: fix_inputs_clean.py path/to/file.html')
        return 2
    path = Path(sys.argv[1])
    if not path.exists():
        print('File not found:', path)
        return 2
    backup = path.with_suffix(path.suffix + '.bak.fixlabels')
    backup.write_bytes(path.read_bytes())
    html = path.read_text(encoding='utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    changed = process(soup)
    if changed:
        path.write_text(str(soup), encoding='utf-8')
        print('Labels added/updated. Backup at', backup)
        return 0
    else:
        print('No changes needed')
        return 0


if __name__ == '__main__':
    raise SystemExit(main())
