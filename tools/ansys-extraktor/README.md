# ANSYS-Extraktor

Liest Workbench-Archive (`.wbpz`) vollständig aus, ohne dass jemand klickt. Grundlage dafür,
aus einem fertigen Modell automatisch eine Übungsseite zu erzeugen.

Läuft nur auf einem Windows-Rechner mit **ANSYS 2024 R2**. Kein zusätzliches Python nötig, alles
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
| `A2A_LOESEN` | `1` | `0` = nicht rechnen |
| `A2A_BILDER` | `1` | `0` = keine Bilder |
| `A2A_INTERAKTIV` | `0` | `1` = Mechanical sichtbar öffnen (zur Fehlersuche) |
| `A2A_AUSGABE_ROOT` | `out\` | Zielordner |

## Ergebnis

`out/<Archivname>/<System>/` je Modell:

- `modell.json`: kompletter Strukturbaum (alle Eigenschaften per Reflection, dazu das Detailfenster
  als Text), Körper mit Bounding Box, Analysestatus vor und nach dem Lösen, Meldungen, abgefangene Fehler
- `NN_<Analyse>.dat`: APDL-Solverinput je Analyse
- `bilder/`: Geometrie, Netz, jede Randbedingung, jedes Ergebnis (PNG, 1600 × 1000, weißer Hintergrund)
- `log.txt`, `../journal_log.txt`: Ablauf

Pfade werden aus dem JSON entfernt (`<pfad entfernt>`), Zeitstempel nicht übernommen.

## Ohne Stapellauf testen

Archiv in Workbench öffnen, Mechanical öffnen, Scripting-Konsole, `mechanical_dump.py` laden und
ausführen. Ausgabe landet dann in `Desktop\extrakt\`.
