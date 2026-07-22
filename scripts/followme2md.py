#!/usr/bin/env python3
"""FollowMe-Export -> Kurzanleitung im Kurs-Muster.

Aufnahme wie gewohnt mit FollowMe (Auto-Screenshots bei jedem Klick,
Hinweise dazu tippen), Export-Ordner nach docs/assets/tutorials/<Name>/
legen und dann:

    python3 scripts/followme2md.py docs/assets/tutorials/Festlager_anbringen

Das Skript druckt einen fertigen Kurzanleitungs-Block (??? tip mit
nummerierten Schritten + Bildern) auf stdout — zum Einfügen in eine
Inhaltsseite. Mit --title lässt sich der Titel überschreiben, mit
--img-prefix der relative Bildpfad von der Zielseite aus.

Menüpfade werden automatisch auf die Chip-Konvention gebracht:
aus  `Display` > `Show` > `All Coordinate Systems`
wird `Display → Show → All Coordinate Systems`  (eine Pfad-Angabe,
die modern-ui.js in Menüpfad-Chips mit Icons verwandelt).
"""
import argparse
import json
import re
import sys
from pathlib import Path


def merge_menu_paths(text):
    """`A` > `B` > `C`  ->  `A → B → C` (eine Chip-Kette)."""
    pattern = re.compile(r'`([^`]+)`\s*>\s*`([^`]+)`')
    while True:
        merged = pattern.sub(
            lambda m: '`%s → %s`' % (m.group(1).strip(), m.group(2).strip()),
            text)
        if merged == text:
            break
        text = merged
    # `Rechtsklick` auf `X → Y` -> `Rechtsklick X → Y` (verbundene Klick-Pille)
    text = re.sub(r'`(Rechtsklick|Doppelklick|Linksklick)`\s*(?:auf\s*)?`',
                  lambda m: '`%s ' % m.group(1), text)
    return text


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('folder', help='Export-Ordner mit imported.json und img/')
    ap.add_argument('--title', help='Titel der Kurzanleitung (Standard: guide.title)')
    ap.add_argument('--img-prefix',
                    help='Bildpfad-Präfix relativ zur Zielseite '
                         '(Standard: aus dem Ordnerpfad unter docs/ abgeleitet, '
                         'von einer Seite eine Ebene unter docs/ aus gesehen)')
    args = ap.parse_args()

    folder = Path(args.folder)
    data = json.loads((folder / 'imported.json').read_text(encoding='utf-8'))
    title = args.title or data['guide'].get('title') or folder.name

    if args.img_prefix:
        prefix = args.img_prefix.rstrip('/')
    else:
        # docs/assets/tutorials/X -> ../assets/tutorials/X (eine Ebene tief)
        parts = folder.resolve().parts
        try:
            i = parts.index('docs')
            prefix = '../' + '/'.join(parts[i + 1:])
        except ValueError:
            prefix = str(folder)

    steps = sorted(data['steps'], key=lambda s: s.get('index', 0))
    out = ['??? tip "Kurzanleitung: %s"' % title, '']
    n = 0
    for step in steps:
        text = merge_menu_paths((step.get('title') or '').strip())
        desc = (step.get('description') or '').strip()
        img = step.get('screenshotFilename')
        if not text and not img:
            continue
        n += 1
        out.append('    %d. %s' % (n, text or 'Schritt %d' % n))
        if desc:
            out.append('')
            out.append('        %s' % desc)
        if img and (folder / 'img' / img).exists():
            out.append('')
            out.append('        ![](%s/img/%s)' % (prefix, img))
        out.append('')
    sys.stdout.write('\n'.join(out).rstrip() + '\n')


if __name__ == '__main__':
    main()
