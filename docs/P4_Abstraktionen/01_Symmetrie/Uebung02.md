---
hide:
 - toc
---

# Kragarm mit Einzelkraft

Die zweite Übung ist ebenfalls ein bekanntes Beispiel:

<figure style="text-align:center;">
  <img src="../images/Uebung02.excalidraw.png" alt="Kragarm mit Einzelkraft" width="400" class="no-lightbox">
</figure>

## Gegeben

### Material

Aluminium

- Elastizitätsmodul $E=70 \mathrm{GPa}$
- Querkontraktionszahl $\nu=0{,}34$

### Geometrie

Balken mit rechteckigem Querschnitt

- Länge $L=500 \mathrm{mm}$
- Breite $b=30 \mathrm{mm}$
- Höhe $h=60 \mathrm{mm}$

### Vernetzung

- Netzgröße global: 5 mm

### Randbedingungen

Lagerung:

- Feste Einspannung auf der Stirnseite links

Belastung:

- Kraft $F=3000 \mathrm{N}$ auf der oberen Kante der rechten Stirnseite

!!! danger "Wird die Kraftangriffsfläche geteilt, muss auch die Kraft geteilt werden"

    Im reduzierten Modell ist nur ein Teil der belasteten Fläche vorhanden, also darf auch nur der passende Teil der Kraft angreifen: im Halbmodell F/2, im Viertelmodell F/4. Drücke (in MPa) sind schon flächenbezogen und bleiben gleich.

## Aufgabenstellung

!!! abstract "Alle möglichen Symmetrien ausnutzen und die unten gefragte Verschiebung berechnen."

### Symmetrie

Welche Symmetrieebenen sind im Bauteil möglich?  Das Koordinatensystem liegt genau im Schwerpunkt des Bauteils.

Daran denken:

Um eine Symmetrie zu verwenden, müssen bei der Spiegelung um diese Symmetrieebene folgende Komponenten identisch zum Vollmodell bleiben:

- Geometrie  
- Lasten  
- Lagerung  

<figure style="text-align:center;">
  <img src="../images/Uebung02.excalidraw.png" alt="Frage Symmetrieebenen" width="600" class="no-lightbox">
</figure>

<div class="multiple-choice-question" data-correct="B" data-points="5" data-attempts="2">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="q1a" name="q1">
      <label for="q1a">x-y Ebene</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="q1b" name="q1">
      <label for="q1b">y-z Ebene</label>
    </div>
    <div class="mc-option" data-value="C">
      <input type="checkbox" id="q1c" name="q1">
      <label for="q1c">x-z Ebene</label>
    </div>
  </div>
</div>

## Gesucht

### Die maximale Durchbiegung $u_{\max }$ in mm

<div class="numeric-question" data-answer="3.3462" data-tolerance="0.1" data-points="5" data-attempts="5"  data-hints="Symmetrie in y-z Ebene? Kraft halbiert? Netzgröße 5 mm eingestellt?" data-diagnose="1.171: Dieser Wert entsteht mit dem Standardmaterial Structural Steel (E = 200 GPa) statt Aluminium (E = 70 GPa). Ist das vorgegebene Material angelegt und dem Körper zugeordnet?">
</div>

<div class="zwischenspiel" data-seite="/P4_Abstraktionen/01_Symmetrie/Uebung01,/P4_Abstraktionen/01_Symmetrie/Uebung02" data-voraussetzung="Übung 1 und 2" data-name="Balken mit Streckenlast (Übung 1)" data-teil="bau-2u6.______________________________.fB001lBt01.T05u66y">
<h2>Zwischenspiel: Knackpunkt</h2>
<p>Der Balken aus Übung 1: Festlager links, Loslager rechts, die Last gleichmäßig auf der ganzen Oberseite. Im Spiel ist er 300 mm lang und 60 mm hoch, eine 10 mm dicke Platte aus Stahl S235, belastet mit 25 kN. Nehmen Sie so viel Material weg wie möglich, ohne dass er versagt. Das Spiel rechnet übrigens selbst mit einer Abstraktion: 2D im ebenen Spannungszustand mit 10 mm Dicke, das ist das nächste Thema. Merken Sie sich Ihr Ergebnis: Am Ende des Praktikums kommt derselbe Balken als Halbmodell.</p>
</div>
