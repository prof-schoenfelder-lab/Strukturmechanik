# ANSYS-Extraktor

Liest Workbench-Archive (`.wbpz`) vollständig aus, ohne dass jemand klickt. Grundlage dafür,
aus einem fertigen Modell automatisch eine Übungsseite zu erzeugen.

Läuft nur auf einem Windows-Rechner mit **ANSYS 2025 R2** (2024 R2 geht weiterhin, der Starter nimmt die neueste installierte Version). Ältere Archive werden beim Öffnen auf die neue Version migriert, das betrifft nur die Arbeitskopie. Kein zusätzliches Python nötig, alles
läuft im ANSYS-eigenen IronPython.

## Dateien

| Datei | Zweck |
|---|---|
| `extrahiere.cmd` | Starter: ein Archiv oder ein ganzer Ordner |
| `extrahiere.wbjn` | Workbench-Journal: entpackt, öffnet jedes Modell in Mechanical |
| `mechanical_dump.py` | läuft in Mechanical: Baum, Körper, Lösung, Solverinput, Bilder |

## Aufruf

```bat
tools\ansys-extraktor\extrahiere.cmd docs\P3_Vernetzung\02_ANSYS_Umsetzung\assets\Uebung-01-Inbus.wbpz
```

Optionen vorher mit `set` setzen:

| Variable | Standard | Wirkung |
|---|---|---|
| `A2A_LOESEN` | `1` | `1` = jede Analyse ohne Ergebnisdatei lösen, `0` = nicht rechnen (Ausnahme siehe unten) |
| `A2A_BILDER` | `1` | `0` = keine Bilder |
| `A2A_INTERAKTIV` | `0` | `1` = Mechanical sichtbar öffnen (zur Fehlersuche) |
| `A2A_AUSGABE_ROOT` | `out\` | Zielordner |

## Ergebnis

`out/<Archivname>/<System>/` je Modell:

- `modell.json`: kompletter Strukturbaum (alle Eigenschaften per Reflection, dazu das Detailfenster
  als Text), Körper mit Bounding Box, Analysestatus vor und nach dem Lösen, Meldungen, abgefangene Fehler
  - `geo_einheit`: Einheit der GeoData-Werte (Bounding Box, Flächen, Kantenlängen), meist `m`
  - `materialdaten` an jedem Material: Werte aus Engineering Data, `Größe: [Einheit, [Werte]]`
  - `nicht_lesbar` an einem Objekt: Eigenschaften, die Mechanical im aktuellen Zustand nicht liefert
    (in der Oberfläche ausgeblendet), mit Grund; das sind keine Fehler
  - `input_vollstaendig`, `nachgeloest`, `zustand_nachher` je Analyse (z. B. `SolveFailed`)
- `NN_<Analyse>.dat`: APDL-Solverinput je Analyse
- `bilder/`: Geometrie, Netz, jede Randbedingung, jedes gelöste Ergebnis (PNG, 1600 × 1000, weißer
  Hintergrund). Ergebnisse, die nicht `Solved` sind, bekommen kein Bild: Die mechdb hält sonst
  Konturen eines älteren Modellstands.
- `log.txt`, `../journal_log.txt`: Ablauf

Pfade werden aus dem JSON entfernt (`<pfad entfernt>`), Zeitstempel nicht übernommen. Das JSON ist
reines ASCII, Umlaute stehen als `ä` usw. darin.

**Gekoppelte Analysen:** Hängt eine Analyse am Ergebnis einer anderen (z. B. Anfangstemperatur aus
Steady-State) und fehlt dessen Ergebnisdatei im Archiv, schreibt Mechanical einen unvollständigen
Solverinput ohne Lasten. Dann werden die vorgeschalteten Analysen auch bei `A2A_LOESEN=0` nachgelöst
(`nachgeloest` im JSON). Bei Klausuren ist das eine Sekundensache.

## Ohne Stapellauf testen

Archiv in Workbench öffnen, Mechanical öffnen, Scripting-Konsole, `mechanical_dump.py` laden und
ausführen. Ausgabe landet dann in `Desktop\extrakt\`.
