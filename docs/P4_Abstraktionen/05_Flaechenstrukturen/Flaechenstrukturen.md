---
icon: material/vector-square
hide:
  - toc
---

# Flächenstrukturen mit `SHELL`- (Schalen-)Elementen

Die nächste Abstraktion ist eine **2D-Abstraktion im dreidimensionalen Raum**.  
Sie wird für flächenförmige Strukturen mit (annähernd) konstanter Dicke verwendet. Dabei wird die reale 3D-Struktur durch eine Fläche mit zugeordneter Dicke beschrieben.

<figure style="text-align:left;">
    <img src="../images/SHELL.excalidraw.png" alt="SHELL" width="600" class="no-lightbox">
</figure>

In der CAD-Geometrie werden dafür **Flächen** verwendet, die anschließend mit sogenannten `SHELL`- (Schalen-)Elementen vernetzt und mit einer Dicke versehen werden.  
`SHELL`-Elemente besitzen u. a. folgende Eigenschaften:

- Zusätzlich zu den Verschiebungsfreiheitsgraden haben sie **Rotationsfreiheitsgrade**.
- Über die Dicke wird ein **Schalenansatz** verwendet: die Mittelfläche kann sich verformen und krümmen, die Dicke bleibt dabei idealisiert (keine lokale 3D-Querschnittsverzerrung wie bei Volumenelementen).

`SHELL`-Elemente sind hinsichtlich Rechenzeit sehr effizient, haben aber den Nachteil, dass sie stark lokale Effekte (z. B. Schweißnahtgeometrien, kleine Kerben) nur eingeschränkt oder gar nicht abbilden können.

Sie sind auch besonders effizient bei Bauteilen mit sehr geringer Dicke im Vergleich zur Fläche, die sonst aus Gründen der Elementqualität als Volumenkörper sehr fein vernetzt werden müssten.

## Abgrenzung zu 2D / plane stress

Diese Abstraktion wirkt auf den ersten Blick ähnlich zur bereits bekannten 2D-Abstraktion mit *plane stress*.  
Wichtiger Unterschied:

- `plane stress`-Modelle liegen in einer festen Ebene (x–y) und beschreiben einen **2D-Schnitt**.
- `SHELL`-Elemente können dagegen beliebig im 3D-Raum liegen, gekrümmt sein und auch komplexe Flächengeometrien (z. B. Schalen, Bleche mit Krümmung) abbilden.

SHELL-Modelle sind also 2D-Elemente, die im **vollen 3D-Raum** eingebettet sind, während *plane stress* eine reine 2D-Vereinfachung in einer Ebene ist.
