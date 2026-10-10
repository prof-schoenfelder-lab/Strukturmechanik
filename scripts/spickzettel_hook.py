"""MkDocs-Hook: sammelt die Bausteine für „Mein Spickzettel“ (Spickzettel.md, assets/js/spickzettel.js).

Kernaussagen: Schrittkästen mit data-spickzettel="ja" (z. B. in den Zusammenfassungen), je Schritt
Überschrift (kurz) und Text darunter (ausführlich). Fehlersuche: die Punkte der Fehler-Checkliste.
Jeder Baustein bekommt im Kurs eine id (kern-…, check-…), damit der Spickzettel dorthin verlinkt.
Ergebnis: assets/spickzettel.json im Site-Ordner, Links relativ zur Site-Wurzel.
"""
import json
import os
import re
from html import unescape

_BLOCK = re.compile(r'<div class="steps"[^>]*data-spickzettel="ja"[^>]*>')
_DIV = re.compile(r'<div\b|</div>')
_SCHRITT = re.compile(r'<div class="step">\s*<p class="step-title"[^>]*>(.*?)</p>(.*?)</div>', re.S)
_ABSATZ = re.compile(r'<p>(.*?)</p>', re.S)
_PUNKT = re.compile(r'<li class="task-list-item"><input type="checkbox"[^>]*>\s*(.*?)</li>', re.S)
CHECKLISTE = "00_FAQ/Fehler_checkliste/"

_kern, _check = [], []


def _text(html):
    return " ".join(unescape(re.sub(r"<[^>]+>", "", html)).split())


def _id(praefix, text):
    slug = re.sub(r"[^a-z0-9]+", "-", _text(text).lower().translate(str.maketrans("äöüß", "aous")))
    return praefix + "-" + slug.strip("-")[:60]


def on_pre_build(config, **kwargs):
    _kern.clear()  # mkdocs serve baut mehrfach
    _check.clear()


def on_page_content(html, page, config, files, **kwargs):
    if page.url == CHECKLISTE:
        def punkt(m):
            pid = _id("check", m.group(1))
            _check.append({"id": pid, "html": m.group(1).strip(), "url": page.url + "#" + pid})
            return m.group(0).replace('<li class="task-list-item"', '<li class="task-list-item" id="%s"' % pid, 1)
        return _PUNKT.sub(punkt, html)
    m = _BLOCK.search(html)
    if not m:
        return html
    tiefe, ende = 0, len(html)
    for t in _DIV.finditer(html, m.start()):
        tiefe += 1 if t.group(0) == "<div" else -1
        if tiefe == 0:
            ende = t.end()
            break
    p = re.match(r"P(\d+)_", page.url)
    praktikum = "P" + p.group(1) if p else ""

    def schritt(s):
        kid = _id("kern-" + praktikum.lower(), s.group(1))
        _kern.append({"id": kid, "praktikum": praktikum, "kurz": _text(s.group(1)),
                      "lang": " ".join(_text(a) for a in _ABSATZ.findall(s.group(2))),
                      "url": page.url + "#" + kid, "seite": page.title})
        return s.group(0).replace('<div class="step">', '<div class="step" id="%s">' % kid, 1)
    return html[:m.start()] + _SCHRITT.sub(schritt, html[m.start():ende]) + html[ende:]


def on_post_build(config, **kwargs):
    ziel = os.path.join(config["site_dir"], "assets", "spickzettel.json")
    os.makedirs(os.path.dirname(ziel), exist_ok=True)
    with open(ziel, "w", encoding="utf-8") as f:
        json.dump({"kernaussagen": _kern, "checkliste": _check}, f, ensure_ascii=False, indent=1)
