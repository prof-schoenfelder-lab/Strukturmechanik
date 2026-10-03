"""MkDocs-Hook: sammelt die Schrittkästen der Kursseiten als Listen-Anleitungen.

Jeder Block <div class="steps"> wird auf der Seite „Anleitungen“ (tutorials.md,
assets/js/tutorials.js) eine Listen-Anleitung neben den Klick-Anleitungen. Titel ist
die Überschrift über dem Block, bei allgemeinen Überschriften wie „Hinweise“ mit dem
Seitentitel. Gleiche Blöcke auf mehreren Seiten erscheinen einmal, mit allen
Fundstellen. Im Kurs bekommt jeder Block eine id (anleitung-1, -2, …), damit der
Link zur Fundstelle direkt dorthin springt. Ergebnis: assets/anleitungen.json im
Site-Ordner, Bild- und Linkpfade relativ zur Site-Wurzel.
"""
import hashlib
import json
import os
import re
from html import unescape
from urllib.parse import urljoin

_BLOCK = re.compile(r'<div class="steps"')
_DIV = re.compile(r'<div\b|</div>')
_KOPF = re.compile(r"<h([1-4])[^>]*>(.*?)</h\1>", re.S)
_SCHRITT = re.compile(r'class="step-title"[^>]*>(.*?)</p>', re.S)
_PFAD = re.compile(r'\b(src|href)="([^"]+)"')
ALLGEMEIN = {"Hinweise", "Gegeben", "Geometrie", "Umsetzung", "Lösung"}
# Seiten, deren Schrittkästen Inhalte zusammenfassen statt Handgriffe zu zeigen
OHNE = ("P1_Einfuehrung/Zusammenfassung/", "P1_Einfuehrung/01_Grundlagen/Grundprinzipien-FEM/", "styleguide/")

_bloecke = []


def _text(html):
    return " ".join(unescape(re.sub(r"<[^>]+>", "", re.sub(r'<a class="headerlink".*?</a>', "", html))).split())


def _kategorie(url):
    teil = url.split("/")[0]
    m = re.match(r"P(\d+)_", teil)
    return "Praktikum " + m.group(1) if m else ("FAQ" if teil == "00_FAQ" else teil.replace("_", " "))


def _von_wurzel(seite, ziel):
    """Pfad relativ zur Seite -> relativ zur Site-Wurzel; Adressen, Anker und Wurzelpfade bleiben."""
    if re.match(r"^(?:[a-z]+:|//|/|#)", ziel):
        return ziel
    return urljoin("/" + seite, ziel).lstrip("/")


def on_pre_build(config, **kwargs):
    _bloecke.clear()  # mkdocs serve baut mehrfach


def on_page_content(html, page, config, files, **kwargs):
    if page.url.startswith(OHNE):
        return html
    teile, pos, n = [], 0, 0
    for m in _BLOCK.finditer(html):
        tiefe, ende = 0, None
        for t in _DIV.finditer(html, m.start()):
            tiefe += 1 if t.group(0) == "<div" else -1
            if tiefe == 0:
                ende = t.end()
                break
        if ende is None:
            break
        block = html[m.start():ende]
        schritte = [_text(s) for s in _SCHRITT.findall(block)]
        if not schritte:
            continue
        n += 1
        anker = "anleitung-%d" % n
        kopf = [_text(k.group(2)) for k in _KOPF.finditer(html, 0, m.start())]
        titel = kopf[-1] if kopf else page.title
        allgemein = titel in ALLGEMEIN
        inhalt = _PFAD.sub(lambda p: '%s="%s"' % (p.group(1), _von_wurzel(page.url, p.group(2))), block)
        _bloecke.append({
            "titel": "%s (%s)" % (titel, page.title) if allgemein else titel, "allgemein": allgemein,
            "kategorie": _kategorie(page.url), "seite": page.title, "schritte": schritte,
            "html": inhalt,
            "fundstelle": {"titel": "%s, %s" % (_kategorie(page.url), page.title), "url": page.url + "#" + anker},
        })
        teile += [html[pos:m.start()], block.replace('<div class="steps"', '<div class="steps" id="%s"' % anker, 1)]
        pos = ende
    return "".join(teile) + html[pos:]


def on_post_build(config, **kwargs):
    gleich = {}
    for b in _bloecke:
        key = hashlib.sha1(b["html"].encode("utf-8")).hexdigest()[:10]
        if key not in gleich:
            gleich[key] = dict(b, id=key, fundstellen=[])
        a = gleich[key]
        a["fundstellen"].append(b["fundstelle"])
        if a["allgemein"] and not b["allgemein"]:  # aussagekräftige Überschrift bevorzugen
            a.update(titel=b["titel"], allgemein=False)
    # Block unter „Hinweise“ o. ä. mit denselben Schritten wie ein benannter Block (meist leicht
    # abgewandelt kopiert): nur als weitere Fundstelle des benannten
    benannt = {}
    for a in gleich.values():
        if not a["allgemein"]:
            benannt.setdefault(tuple(a["schritte"]), a)
    liste = []
    for a in gleich.values():
        ziel = benannt.get(tuple(a["schritte"])) if a["allgemein"] else None
        if ziel is not None:
            ziel["fundstellen"] += a["fundstellen"]
        else:
            liste.append(a)
    liste.sort(key=lambda a: (not a["kategorie"].startswith("Praktikum"), a["kategorie"]))
    for a in liste:
        del a["allgemein"], a["fundstelle"]
    ziel = os.path.join(config["site_dir"], "assets", "anleitungen.json")
    os.makedirs(os.path.dirname(ziel), exist_ok=True)
    with open(ziel, "w", encoding="utf-8") as f:
        json.dump({"anleitungen": liste}, f, ensure_ascii=False, separators=(",", ":"))
