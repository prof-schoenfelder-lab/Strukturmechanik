"""MkDocs-Hook: entfernt Antworten aus dem ausgelieferten HTML.

Beim Build werden aus allen Fragen (.numeric-question / .multiple-choice-question)
die Attribute data-answer, data-tolerance und data-correct entfernt und
stattdessen eine stabile data-qid vergeben. Die Antworten landen gesammelt in
answers.json im Projektroot (NICHT im site-Output!) — diese Datei gehört auf
das Backend (siehe backend/DEPLOY.md).

Die qid entspricht dem bisherigen Client-Schema, damit vorhandene
localStorage-Einträge gültig bleiben: <site-pfad>/<seite>:q<i> bzw. :mc<i>.

Numerische Fragen können typische Fehlwerte mit Ursache tragen:
data-diagnose="7,747: Text | 0,35: Text". Auch diese landen nur in answers.json;
das Backend nennt die Ursache, wenn eine Eingabe zu einem Fehlwert passt.

Modell-Detektiv: <div class="detektiv-fall" data-fall="name"> lädt den Fall aus
content/detektiv/name.json. Strukturbaum und Details kommen als JSON in die
Seite, Fehlerzeile, Begründungen und Auflösung nur in answers.json (qid :det<i>).
"""

import json
import os
import re
from urllib.parse import urlsplit

_answers = {}

_TAG_RE = re.compile(
    r'<div\b[^>]*class="[^"]*\b(numeric-question|multiple-choice-question|detektiv-fall)\b[^"]*"[^>]*>'
)
_SUFFIX = {"numeric-question": ":q", "multiple-choice-question": ":mc", "detektiv-fall": ":det"}
_ATTR_RE = re.compile(r'\s*data-(answer|tolerance|correct|diagnose)="([^"]*)"')


def _attr(tag, name, default=""):
    m = re.search(r'data-' + name + r'="([^"]*)"', tag)
    return m.group(1) if m else default


def _diagnose(raw, qid):
    """'7,747: Text | 0,35: Text' -> [{"value": 7.747, "hint": "Text"}, ...]"""
    out = []
    for part in raw.split("|"):
        val, sep, hint = part.partition(":")
        try:
            if not sep:
                raise ValueError
            out.append({"value": float(val.strip().replace(",", ".")), "hint": hint.strip()})
        except ValueError:
            if part.strip():
                print(f"answers_hook: data-diagnose in {qid} nicht lesbar: {part.strip()!r}")
    return out


def _detektiv(root, name):
    """Fall laden und teilen: (öffentlicher Teil für die Seite, Lösungsteil für answers.json)."""
    with open(os.path.join(root, "content", "detektiv", name + ".json"), encoding="utf-8") as f:
        fall = json.load(f)
    explain = {}
    for knoten in fall["baum"]:
        for zeile in knoten["details"]:
            if "grund" in zeile:
                explain[zeile["id"]] = zeile.pop("grund")
    loesung = {"correct": [fall.pop("fehler")], "explain": explain,
               "aufloesung": fall.pop("aufloesung")}
    return fall, loesung


def on_page_content(html, page, config, files):
    prefix = urlsplit(config["site_url"]).path.rstrip("/")
    page_path = (prefix + "/" + page.url).rstrip("/")
    counters = {cls: 0 for cls in _SUFFIX}

    def replace(m):
        tag, cls = m.group(0), m.group(1)
        idx = counters[cls]
        counters[cls] += 1
        qid = page_path + _SUFFIX[cls] + str(idx)

        entry = {
            "points": float(_attr(tag, "points", "1") or 1),
            "attempts": int(_attr(tag, "attempts", "5") or 5),
        }
        if cls == "detektiv-fall":
            root = os.path.dirname(config["config_file_path"])
            fall, loesung = _detektiv(root, _attr(tag, "fall"))
            entry.update(loesung)
            _answers[qid] = entry
            daten = json.dumps(fall, ensure_ascii=False).replace("</", "<\\/")
            return (tag[:-1] + ' data-qid="' + qid + '">'
                    + '<script type="application/json" class="detektiv-daten">' + daten + '</script>')
        if cls == "numeric-question":
            try:
                entry["answer"] = float(_attr(tag, "answer").replace(",", "."))
            except ValueError:
                return tag  # kein/kaputtes data-answer: Frage unverändert lassen
            entry["tolerance"] = float(_attr(tag, "tolerance", "0").replace(",", ".") or 0)
            diagnose = _diagnose(_attr(tag, "diagnose"), qid)
            if diagnose:
                entry["diagnose"] = diagnose
        else:
            correct = [s.strip() for s in _attr(tag, "correct").split(",") if s.strip()]
            if not correct:
                return tag
            entry["correct"] = correct
        _answers[qid] = entry

        stripped = _ATTR_RE.sub("", tag)
        return stripped[:-1] + ' data-qid="' + qid + '">'

    return _TAG_RE.sub(replace, html)


def on_post_build(config):
    out = os.path.join(os.path.dirname(config["config_file_path"]), "answers.json")
    with open(out, "w") as f:
        json.dump(_answers, f, indent=1, ensure_ascii=False, sort_keys=True)
    print(f"answers_hook: {len(_answers)} Fragen -> {out} (aufs Backend kopieren!)")
