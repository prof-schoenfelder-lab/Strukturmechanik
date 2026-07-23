"""MkDocs-Hook: baut die Praktikums-Übersichten automatisch.

Auf einer Praktikums-Startseite (z.B. P2_.../index.md) genügt der Marker
`<!-- uebersicht -->`. Beim Build wird er durch Karten ersetzt, die aus den
Inhaltsseiten desselben Praktikums-Ordners entstehen. Eine Seite erscheint als
Karte, sobald sie im Frontmatter ein Feld `sektion:` hat:

    ---
    title: Lager
    sektion: Lagerungen
    kurz: Fest-, Los- und weitere Lagerungen richtig anbringen
    thumb: images/Lager.png    # optional, sonst erstes Bild der Seite
    typ: uebung                # optional (Badge: inhalt|beispiel|uebung)
    order: 20                  # optional (Reihenfolge; steuert auch Sektions-Reihenfolge)
    ---

Ungetaggte Seiten (z.B. Schritte eines Beispiels) erscheinen NICHT — einfach
kein `sektion:` setzen. Die Navigation bleibt wie gehabt von Hand gepflegt.
"""
import os
import re
from mkdocs.utils import meta as mkmeta

MARKER = re.compile(r'<!--\s*uebersicht\s*-->', re.I)
_H1 = re.compile(r'^#\s+(.+?)\s*$', re.M)
_IMG_HTML = re.compile(r'<img[^>]+src="([^"]+)"')
_IMG_MD = re.compile(r'!\[[^\]]*\]\(\s*([^)\s]+)')
TYP_LABEL = {"inhalt": "Inhalt", "beispiel": "Beispiel", "uebung": "Übung"}


def _first_h1(body):
    m = _H1.search(body)
    return m.group(1).strip() if m else None


def _first_image(body):
    m = _IMG_HTML.search(body) or _IMG_MD.search(body)
    return m.group(1) if m else None


def _esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def on_page_markdown(markdown, page, config, files, **kwargs):
    if not MARKER.search(markdown):
        return markdown
    idx_dir = os.path.dirname(page.file.src_path)
    prefix = (idx_dir + "/") if idx_dir else ""

    units = []
    for f in files.documentation_pages():
        sp = f.src_path.replace(os.sep, "/")
        if sp == page.file.src_path.replace(os.sep, "/"):
            continue
        if prefix and not sp.startswith(prefix):
            continue
        try:
            with open(f.abs_src_path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError:
            continue
        body, fm = mkmeta.get_data(text)
        if "sektion" not in fm:
            continue
        title = fm.get("title") or _first_h1(body) or f.name
        try:
            order = float(fm.get("order", 1e6))
        except (TypeError, ValueError):
            order = 1e6
        thumb = fm.get("thumb") or _first_image(body)
        thumb_rel = None
        if thumb:
            unit_dir = os.path.dirname(sp)
            full = os.path.normpath(os.path.join(unit_dir, thumb)).replace(os.sep, "/")
            thumb_rel = os.path.relpath(full, idx_dir or ".").replace(os.sep, "/")
        units.append({
            "sektion": str(fm["sektion"]),
            "title": str(title),
            "kurz": str(fm.get("kurz", "")),
            "typ": str(fm.get("typ", "")).lower(),
            "order": order,
            "thumb": thumb_rel,
            "href": f.url_relative_to(page.file),
        })

    units.sort(key=lambda u: (u["order"], u["title"]))
    sektionen, by = [], {}
    for u in units:
        by.setdefault(u["sektion"], [])
        if u["sektion"] not in sektionen:
            sektionen.append(u["sektion"])
        by[u["sektion"]].append(u)

    out = []
    for s in sektionen:
        out.append("## " + s + "\n")
        out.append('<div class="prakt-cards">')
        for u in by[s]:
            out.append('  <a class="prakt-card" href="%s">' % u["href"])
            if u["thumb"]:
                out.append('    <img class="prakt-cimg no-lightbox" src="%s" alt="">' % u["thumb"])
            out.append('    <span class="prakt-cbody">')
            if u["typ"] in TYP_LABEL:
                out.append('      <span class="prakt-ctyp prakt-ctyp--%s">%s</span>'
                           % (u["typ"], TYP_LABEL[u["typ"]]))
            out.append('      <span class="prakt-ctitle">%s</span>' % _esc(u["title"]))
            if u["kurz"]:
                out.append('      <span class="prakt-cdesc">%s</span>' % _esc(u["kurz"]))
            out.append("    </span>")
            out.append("  </a>")
        out.append("</div>\n")

    return MARKER.sub("\n".join(out), markdown)
