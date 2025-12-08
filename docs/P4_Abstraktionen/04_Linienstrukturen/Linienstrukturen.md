---
icon: material/chart-timeline-variant
hide:
  - toc
---

# Linienstrukturen mit `BEAM`- (Balken-)Elementen

Die nächste Abstraktion ist eine **1D-Abstraktion** im dreidimensionalen Raum.  Sie wird für Linienstrukturen mit (annähernd) konstantem Querschnitt verwendet. Dabei wird die reale 3D-Struktur durch eine Linie mit einem zugeordneten Querschnitt beschrieben.

<figure style="text-align:left;">
    <img src="../images/Linienstrukur.excalidraw.png" alt="Linienstruktur" width="600" class="no-lightbox">
</figure>

In der CAD-Geometrie werden dafür **Linien** verwendet, die anschließend mit sogenannten `BEAM`- (Balken-)Elementen vernetzt und mit einem Profil (Querschnitt) versehen werden. `BEAM`-Elemente besitzen u. a. folgende Eigenschaften:

- Zusätzlich zu den Verschiebungsfreiheitsgraden haben sie **Rotationsfreiheitsgrade**.
- Der Querschnitt wird als **starr** angenommen, d. h. er kann sich im Vergleich zum 3D-Körper nicht lokal verformen. (Die Linie kann sich also verformen, aber der Querschnitt eben nicht)

`BEAM`-Elemente sind hinsichtlich Rechenzeit sehr effizient, haben aber den Nachteil, dass sie lokale Effekte (z. B. Schweißnähte, Kerben, lokale Querschnittsaufdickungen) nicht abbilden können.
