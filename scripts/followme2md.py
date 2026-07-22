#!/usr/bin/env python3
"""FollowMe-Export -> Kurzanleitung im Kurs-Muster.

Aufnahme wie gewohnt mit FollowMe (Auto-Screenshots bei jedem Klick,
Hinweise dazu tippen). Zwei Export-Formate werden unterstützt:

1) App-Export (Ordner mit imported.json + img/):

    python3 scripts/followme2md.py docs/assets/tutorials/Festlager_anbringen

2) Markdown-Export (auch via FollowMe Remote): eine .md-Datei mit
   "### N. Titel"-Schritten und base64-eingebetteten Bildern, optional
   daneben ein Ordner mit step-N.png. Die Bilder werden nach
   docs/assets/tutorials/<Name>/img/ übernommen:

    python3 scripts/followme2md.py Inbox/Test.md --name Mein_Beispiel

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
import base64
import json
import re
import shutil
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


def parse_md_export(md_path, name):
    """FollowMe-Markdown-Export -> (guide-dict, Zielordner unter docs/).

    Liest "### N. Titel"-Schritte; Bilder kommen bevorzugt aus einem
    Geschwister-Ordner mit step-N.png, sonst aus den base64-Daten der
    Datei. Beides wird nach docs/assets/tutorials/<name>/img/ kopiert.
    """
    md_path = Path(md_path)
    dest = Path('docs/assets/tutorials') / name
    (dest / 'img').mkdir(parents=True, exist_ok=True)

    text = md_path.read_text(encoding='utf-8')
    m = re.search(r'^#\s+(.+)$', text, re.M)
    guide_title = m.group(1).strip() if m else name

    # Geschwister-Ordner mit fertigen PNGs (FollowMe legt ihn mit ab)
    img_src = None
    for sib in md_path.parent.iterdir():
        if sib.is_dir() and list(sib.glob('step-*.png')):
            img_src = sib
            break

    steps = []
    blocks = re.split(r'^###\s+', text, flags=re.M)[1:]
    for i, block in enumerate(blocks):
        first, _, rest = block.partition('\n')
        title = re.sub(r'^\d+\.\s*', '', first).strip()
        img_name = 'step-%d.png' % i
        target = dest / 'img' / img_name
        if img_src and (img_src / img_name).exists():
            shutil.copyfile(img_src / img_name, target)
        else:
            b64 = re.search(r'data:image/png;base64,([A-Za-z0-9+/=\s]+?)\)', block)
            if b64:
                target.write_bytes(base64.b64decode(b64.group(1)))
            else:
                img_name = None
        # Freitext zwischen Titel und Bild als Beschreibung übernehmen
        desc_lines = [l.strip() for l in rest.splitlines()
                      if l.strip() and not l.strip().startswith('![')]
        steps.append({'index': i, 'title': title,
                      'description': ' '.join(desc_lines),
                      'screenshotFilename': img_name})
    return {'guide': {'title': guide_title}, 'steps': steps}, dest


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('source',
                    help='Export-Ordner (imported.json + img/) oder '
                         'Markdown-Export-Datei (.md)')
    ap.add_argument('--name',
                    help='Zielname unter docs/assets/tutorials/ '
                         '(nur für Markdown-Exporte)')
    ap.add_argument('--title', help='Titel der Kurzanleitung (Standard: guide.title)')
    ap.add_argument('--img-prefix',
                    help='Bildpfad-Präfix relativ zur Zielseite '
                         '(Standard: aus dem Ordnerpfad unter docs/ abgeleitet, '
                         'von einer Seite eine Ebene unter docs/ aus gesehen)')
    args = ap.parse_args()

    src = Path(args.source)
    if src.is_file() and src.suffix == '.md':
        if not args.name:
            ap.error('Für Markdown-Exporte --name <Zielname> angeben')
        data, folder = parse_md_export(src, args.name)
    else:
        folder = src
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
