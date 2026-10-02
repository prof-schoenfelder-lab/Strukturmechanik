# Mechanical-Dump: liest das offene Mechanical-Modell vollstaendig aus.
#
# Laeuft IN Mechanical (IronPython, ANSYS 2024 R2), entweder
#   a) per Workbench-Journal (extrahiere.wbjn setzt die A2A_*-Variablen davor) oder
#   b) von Hand in der Scripting-Konsole von Mechanical (dann gelten die Standardwerte unten).
#
# Ergebnis im Ausgabeordner:
#   modell.json          Baum mit allen Objekten und Eigenschaften, Koerper, Meldungen
#   <Analyse>.dat        APDL-Solverinput je Analyse (WriteInputFile)
#   bilder/*.png         Geometrie, Netz, jede Randbedingung, jedes Ergebnis
#   log.txt              Ablauf und abgefangene Fehler
#
# Datei bewusst nur ASCII: sie wird als Text per SendCommand an Mechanical uebergeben.

import os
import re
import json
import traceback
import System

try:
    unicode
except NameError:       # CPython (PyMechanical) statt IronPython
    unicode = str
    long = int

# ---------------------------------------------------------------- Einstellungen
try:
    A2A_AUSGABE
except NameError:
    A2A_AUSGABE = os.path.join(os.path.expanduser("~"), "Desktop", "extrakt")
try:
    A2A_LOESEN
except NameError:
    A2A_LOESEN = True       # Analysen loesen, falls keine Ergebnisse vorliegen
try:
    A2A_BILDER
except NameError:
    A2A_BILDER = True       # Bilder exportieren
try:
    A2A_KENNUNG
except NameError:
    A2A_KENNUNG = ""        # z. B. Archivname + System, nur zur Beschriftung

BILD_BREITE = 1600
BILD_HOEHE = 1000
MAX_LISTE = 2000            # laengere Listen werden gekuerzt
MAX_GEO_BESCHREIBUNG = 50   # so viele Geometrie-IDs je Auswahl werden beschrieben

# Eigenschaften, die nur Rauschen oder Rekursion erzeugen
AUSLASSEN = set([
    "Children", "Parent", "InternalObject", "Properties", "VisibleProperties",
    "PropertyNames", "Comments", "Figures", "Images", "Author",
])

# Pfade (Laufwerk, UNC, Benutzerordner) werden nicht ins JSON uebernommen
PFAD = re.compile(r"[A-Za-z]:[\\/]|\\\\|/Users/|/home/")

model = ExtAPI.DataModel.Project.Model
geodata = ExtAPI.DataModel.GeoData
try:
    tree = Tree
except NameError:
    tree = ExtAPI.DataModel.Tree
try:
    graphics = Graphics
except NameError:
    graphics = ExtAPI.Graphics

if not os.path.isdir(A2A_AUSGABE):
    os.makedirs(A2A_AUSGABE)
_log = open(os.path.join(A2A_AUSGABE, "log.txt"), "a")
fehler = []


def text(e):
    """Fehlertext ohne Kodierungsfalle (deutsche .NET-Meldungen)."""
    try:
        t = e.Message
    except Exception:
        t = str(e)
    try:
        return t.encode("ascii", "replace")
    except Exception:
        return repr(t)


def log(msg):
    try:
        _log.write(msg.encode("ascii", "replace") + "\n")
    except Exception:
        _log.write(repr(msg) + "\n")
    _log.flush()


def merke_fehler(wo, e):
    eintrag = {"wo": wo, "fehler": text(e)}
    fehler.append(eintrag)
    log("FEHLER %s: %s" % (wo, eintrag["fehler"]))


def sauber(s):
    if s is None:
        return None
    s = unicode(s)
    if PFAD.search(s):
        return "<pfad entfernt>"
    return s


def dateiname(s):
    s = unicode(s)
    for a, b in ((u"\u00e4", "ae"), (u"\u00f6", "oe"), (u"\u00fc", "ue"), (u"\u00c4", "Ae"),
                 (u"\u00d6", "Oe"), (u"\u00dc", "Ue"), (u"\u00df", "ss")):
        s = s.replace(a, b)
    s = re.sub(r"[^A-Za-z0-9_-]+", "_", s).strip("_")
    return s[:60] or "objekt"


# ---------------------------------------------------------------- Werte umwandeln
def ist_objekt(v):
    return hasattr(v, "ObjectId") and hasattr(v, "DataModelObjectCategory")


def objekt_ref(v):
    return {"objekt": sauber(v.Name), "kategorie": str(v.DataModelObjectCategory), "id": v.ObjectId}


def geo_beschreibung(i):
    """Lage und Groesse einer Geometrie-ID, damit Flaechen ohne ID benennbar sind."""
    try:
        e = geodata.GeoEntityById(i)
    except Exception:
        return None
    if e is None:
        return None
    d = {"id": i}
    for attr in ("Type", "Area", "Length", "Volume", "Centroid", "X", "Y", "Z",
                 "SurfaceType", "CurveType"):
        try:
            d[attr] = konv(getattr(e, attr), 1)
        except Exception:
            pass
    try:
        d["Normal"] = konv(e.NormalAtParam(0.5, 0.5), 1)
    except Exception:
        pass
    try:
        b = e.Bodies[0] if hasattr(e, "Bodies") else e.Body
        d["Koerper"] = sauber(model.Geometry.GetBody(b).Name)
    except Exception:
        pass
    return d


def konv(v, tiefe=0):
    """.NET-/Mechanical-Wert -> JSON-faehiger Wert. Unbekanntes wird None."""
    if v is None:
        return None
    if isinstance(v, bool):
        return v
    if isinstance(v, (int, long, float)):
        return v
    if isinstance(v, (str, unicode)):
        return sauber(v)
    if isinstance(v, System.Enum):
        return str(v)
    if isinstance(v, System.DateTime):
        return None
    if isinstance(v, (System.Single, System.Double, System.Decimal)):
        return float(v)
    if isinstance(v, (System.Int16, System.Int32, System.Int64, System.UInt32, System.UInt64)):
        return long(v)
    # Quantity (Wert mit Einheit)
    if hasattr(v, "Value") and hasattr(v, "Unit"):
        try:
            return {"wert": float(v.Value), "einheit": sauber(v.Unit)}
        except Exception:
            pass
    # Feld (Lastgroesse, ggf. tabellarisch ueber der Zeit)
    if hasattr(v, "Output") and hasattr(v, "Inputs"):
        d = {}
        try:
            d["werte"] = konv(v.Output.DiscreteValues, tiefe + 1)
        except Exception:
            pass
        try:
            d["eingaben"] = [konv(inp.DiscreteValues, tiefe + 1) for inp in v.Inputs]
        except Exception:
            pass
        return d
    if ist_objekt(v):
        return objekt_ref(v)
    # Auswahl (Geometrie-, Knoten-, Elementauswahl)
    if hasattr(v, "Ids") and hasattr(v, "SelectionType"):
        ids = list(v.Ids)
        d = {"auswahl": str(v.SelectionType), "anzahl": len(ids), "ids": ids[:MAX_LISTE]}
        if str(v.SelectionType) == "GeometryEntities":
            d["geometrie"] = [geo_beschreibung(i) for i in ids[:MAX_GEO_BESCHREIBUNG]]
        return d
    if tiefe < 3 and isinstance(v, System.Collections.IEnumerable):
        aus = []
        for k, x in enumerate(v):
            if k >= MAX_LISTE:
                aus.append("<gekuerzt>")
                break
            aus.append(konv(x, tiefe + 1))
        return aus
    return None


# ---------------------------------------------------------------- Baum
def eigenschaften(obj, wo):
    d = {}
    for p in obj.GetType().GetProperties():
        name = p.Name
        if name in AUSLASSEN or p.GetIndexParameters().Length > 0:
            continue
        try:
            w = konv(p.GetValue(obj, None))
        except Exception as e:
            merke_fehler("%s.%s" % (wo, name), e)
            continue
        if w is not None:
            d[name] = w
    return d


def details(obj):
    """Detailfenster so, wie es in der Oberflaeche steht (Beschriftung + Text)."""
    aus = []
    try:
        props = list(obj.VisibleProperties)
    except Exception:
        return aus
    for p in props:
        eintrag = {"name": p.Name}
        try:
            eintrag["beschriftung"] = p.Caption
        except Exception:
            pass
        try:
            eintrag["text"] = sauber(p.StringValue)
        except Exception:
            try:
                eintrag["text"] = sauber(str(p.InternalValue))
            except Exception:
                pass
        aus.append(eintrag)
    return aus


def knoten(obj, pfad):
    wo = "%s/%s" % (pfad, obj.Name)
    d = {
        "name": sauber(obj.Name),
        "kategorie": str(obj.DataModelObjectCategory),
        "id": obj.ObjectId,
    }
    try:
        d["eigenschaften"] = eigenschaften(obj, wo)
    except Exception as e:
        merke_fehler(wo, e)
    d["details"] = details(obj)
    kinder = []
    try:
        for c in obj.Children:
            kinder.append(knoten(c, wo))
    except Exception as e:
        merke_fehler(wo + "/Children", e)
    if kinder:
        d["kinder"] = kinder
    return d


# ---------------------------------------------------------------- Koerper
def koerper():
    aus = []
    for asm in geodata.Assemblies:
        for part in asm.Parts:
            for gb in part.Bodies:
                d = {}
                try:
                    d["name"] = sauber(model.Geometry.GetBody(gb).Name)
                except Exception:
                    pass
                try:
                    xs = [v.X for v in gb.Vertices]
                    ys = [v.Y for v in gb.Vertices]
                    zs = [v.Z for v in gb.Vertices]
                    d["bbox_min"] = [min(xs), min(ys), min(zs)]
                    d["bbox_max"] = [max(xs), max(ys), max(zs)]
                except Exception as e:
                    merke_fehler("koerper/bbox", e)
                for attr in ("Volume", "Area", "Centroid"):
                    try:
                        d[attr] = konv(getattr(gb, attr), 1)
                    except Exception:
                        pass
                for attr in ("Faces", "Edges", "Vertices"):
                    try:
                        d["anzahl_" + attr.lower()] = len(list(getattr(gb, attr)))
                    except Exception:
                        pass
                aus.append(d)
    return aus


def ist_2d(kp):
    try:
        return len(kp) > 0 and all(abs(k["bbox_max"][2] - k["bbox_min"][2]) < 1e-12 for k in kp)
    except Exception:
        return False


# ---------------------------------------------------------------- Bilder
_bild_settings = None


def bild(obj, name, ansicht):
    global _bild_settings
    ordner = os.path.join(A2A_AUSGABE, "bilder")
    datei = os.path.join(ordner, name + ".png")
    try:
        if _bild_settings is None:
            s = Ansys.Mechanical.Graphics.GraphicsImageExportSettings()
            s.Resolution = GraphicsResolutionType.EnhancedResolution
            s.Background = GraphicsBackgroundType.White
            s.CurrentGraphicsDisplay = False
            s.Width = BILD_BREITE
            s.Height = BILD_HOEHE
            _bild_settings = s
        if not os.path.isdir(ordner):
            os.makedirs(ordner)
        tree.Activate([obj])
        graphics.Camera.SetSpecificViewOrientation(ansicht)
        graphics.Camera.SetFit()
        graphics.ExportImage(datei, GraphicsImageExportFormat.PNG, _bild_settings)
        return "bilder/" + name + ".png"
    except Exception as e:
        merke_fehler("bild " + name, e)
        return None


# ---------------------------------------------------------------- Ablauf
def analysen_vorbereiten():
    aus = []
    for k, a in enumerate(model.Analyses):
        d = {"nr": k + 1, "name": sauber(a.Name), "id": a.ObjectId}
        try:
            d["system"] = sauber(a.SystemCaption)
        except Exception:
            pass
        try:
            d["status_vorher"] = str(a.Solution.Status)
        except Exception as e:
            merke_fehler("status " + a.Name, e)
        if A2A_LOESEN and d.get("status_vorher") != "Done":
            log("loese %s" % a.Name)
            try:
                a.Solve(True)
            except Exception as e:
                merke_fehler("solve " + a.Name, e)
        if A2A_LOESEN:
            try:
                a.Solution.EvaluateAllResults()
            except Exception as e:
                merke_fehler("evaluate " + a.Name, e)
        try:
            d["status_nachher"] = str(a.Solution.Status)
        except Exception:
            pass
        datei = "%02d_%s.dat" % (k + 1, dateiname(a.Name))
        try:
            a.WriteInputFile(os.path.join(A2A_AUSGABE, datei))
            d["input_datei"] = datei
        except Exception as e:
            merke_fehler("WriteInputFile " + a.Name, e)
        aus.append(d)
    return aus


def meldungen():
    aus = []
    try:
        for m in ExtAPI.Application.Messages:
            aus.append({"art": str(m.Severity), "text": sauber(m.DisplayString)})
    except Exception as e:
        merke_fehler("meldungen", e)
    return aus


def bilder_exportieren(analysen, zwei_d):
    ansicht = ViewOrientationType.Front if zwei_d else ViewOrientationType.Iso
    liste = []

    def neu(obj, name):
        p = bild(obj, name, ansicht)
        if p:
            liste.append({"objekt": sauber(obj.Name), "id": obj.ObjectId, "datei": p})

    neu(model.Geometry, "00_geometrie")
    try:
        if model.Mesh.Nodes == 0:
            model.Mesh.GenerateMesh()
    except Exception as e:
        merke_fehler("GenerateMesh", e)
    neu(model.Mesh, "01_netz")
    for k, a in enumerate(model.Analyses):
        for j, c in enumerate(a.Children):
            kat = str(c.DataModelObjectCategory)
            if kat in ("AnalysisSettings", "Solution", "InitialConditions"):
                continue
            neu(c, "a%d_rb%02d_%s" % (k + 1, j + 1, dateiname(c.Name)))
        try:
            for j, r in enumerate(a.Solution.Children):
                if str(r.DataModelObjectCategory) == "SolutionInformation":
                    continue
                neu(r, "a%d_erg%02d_%s" % (k + 1, j + 1, dateiname(r.Name)))
        except Exception as e:
            merke_fehler("bilder ergebnisse", e)
    return liste


def schreibe(daten):
    with open(os.path.join(A2A_AUSGABE, "modell.json"), "w") as f:
        json.dump(daten, f, indent=1)


def main():
    log("=== start %s" % A2A_KENNUNG)
    daten = {"format": 1, "kennung": sauber(A2A_KENNUNG)}
    try:
        daten["einheitensystem"] = str(ExtAPI.Application.ActiveUnitSystem)
    except Exception:
        pass
    try:
        daten["geo_einheit"] = str(geodata.Unit)
    except Exception:
        pass
    daten["analysen"] = analysen_vorbereiten()
    kp = koerper()
    daten["koerper"] = kp
    daten["zwei_d"] = ist_2d(kp)
    daten["baum"] = knoten(model, "")
    daten["meldungen"] = meldungen()
    daten["fehler"] = fehler
    schreibe(daten)                 # erst ohne Bilder, falls der Export abstuerzt
    if A2A_BILDER:
        daten["bilder"] = bilder_exportieren(daten["analysen"], daten["zwei_d"])
        schreibe(daten)
    log("=== fertig, %d abgefangene Fehler" % len(fehler))


try:
    main()
except Exception as e:
    log("ABBRUCH: " + text(e))
    log(traceback.format_exc())
finally:
    _log.close()
