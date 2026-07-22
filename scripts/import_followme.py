#!/usr/bin/env python3
"""FollowMe-Exporte -> Tutorial-Datenbank unter docs/tutorials/.

Liest die vorhandenen docs/assets/tutorials/<Name>/imported.json (+ img/)
und erzeugt je Tutorial einen Ordner docs/tutorials/<slug>/ mit
tutorial.json + kopierten Bildern sowie ein Register docs/tutorials/index.json.

Aufruf:  python3 scripts/import_followme.py
"""
import json
import re
import shutil
from pathlib import Path

SRC = Path("docs/assets/tutorials")
DST = Path("docs/tutorials")

# Name -> (Titel, Kategorie, Software, Tags)
META = {
    "Analyse_hinzufuegen":           ("Neue Analyse anlegen",     "Setup",      "Workbench",  ["Static Structural", "Projekt"]),
    "Geometrie_Erstellen":           ("Geometrie erstellen",      "Geometrie",  "SpaceClaim", ["SpaceClaim", "Skizze"]),
    "Material_hinzufuegen":          ("Material hinzufügen",      "Material",   "Workbench",  ["Engineering Data"]),
    "Material_zuordnen":             ("Material zuordnen",        "Material",   "Mechanical", ["Assignment"]),
    "Flaechen_erzeugen_Split_Ebene": ("Flächen teilen (Split)",  "Geometrie",  "SpaceClaim", ["Split", "Fläche"]),
    "Festlager_anbringen":           ("Festlager anbringen",      "Lagerung",   "Mechanical", ["Fixed Support"]),
    "Loslager_anbringen":            ("Loslager anbringen",       "Lagerung",   "Mechanical", ["Displacement", "Support"]),
    "Flaechenlast_anbringen":        ("Flächenlast anbringen",    "Belastung",  "Mechanical", ["Pressure", "Force"]),
    "Vernetzung":                    ("Vernetzung",               "Vernetzung", "Mechanical", ["Mesh", "Sizing"]),
}


def slugify(name):
    s = name.lower()
    s = (s.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss"))
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def normalize(text):
    """Menüpfade auf Chip-Konvention bringen (wie followme2md)."""
    text = (text or "").strip()
    pat = re.compile(r"`([^`]+)`\s*>\s*`([^`]+)`")
    while True:
        merged = pat.sub(lambda m: "`%s → %s`" % (m.group(1).strip(), m.group(2).strip()), text)
        if merged == text:
            break
        text = merged
    text = re.sub(r"`(Rechtsklick|Doppelklick|Linksklick)`\s*(?:auf\s*)?`",
                  lambda m: "`%s " % m.group(1), text)
    return text


def main():
    DST.mkdir(parents=True, exist_ok=True)
    register = []
    for name, (title, cat, software, tags) in META.items():
        src = SRC / name
        jf = src / "imported.json"
        if not jf.exists():
            print("übersprungen (fehlt):", name)
            continue
        data = json.loads(jf.read_text(encoding="utf-8"))
        slug = slugify(name)
        out = DST / slug
        out.mkdir(parents=True, exist_ok=True)
        steps = []
        thumb = None
        for i, st in enumerate(sorted(data["steps"], key=lambda s: s.get("index", 0))):
            caption = normalize(st.get("title", ""))
            desc = (st.get("description") or "").strip()
            media = []
            img = st.get("screenshotFilename")
            if img and (src / "img" / img).exists():
                target = "step-%d.png" % i
                shutil.copyfile(src / "img" / img, out / target)
                media.append(target)
                if thumb is None:
                    thumb = target
            step = {"caption": caption, "media": media}
            if desc:
                step["note"] = desc
            steps.append(step)
        tutorial = {
            "slug": slug, "title": title, "category": cat,
            "software": software, "tags": tags, "steps": steps,
        }
        (out / "tutorial.json").write_text(
            json.dumps(tutorial, ensure_ascii=False, indent=2), encoding="utf-8")
        register.append({
            "slug": slug, "title": title, "category": cat,
            "software": software, "tags": tags,
            "steps": len(steps), "thumb": thumb,
        })
        print("ok", slug, "-", len(steps), "Schritte")

    # Register nach Kategorie, dann Titel sortieren
    order = ["Setup", "Geometrie", "Material", "Vernetzung", "Lagerung", "Belastung", "Postprocessing"]
    register.sort(key=lambda t: (order.index(t["category"]) if t["category"] in order else 99, t["title"]))
    (DST / "index.json").write_text(
        json.dumps({"tutorials": register}, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Register:", len(register), "Tutorials ->", DST / "index.json")


if __name__ == "__main__":
    main()
