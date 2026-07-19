---
hide:
 - toc
---

# Zweiseitig gelagerter Balken mit Flächenlast

Wir rechnen nun das eben betrachtete Beispiel:

<figure style="text-align:center;">
  <img src="../images/Uebung01.excalidraw.png" alt="Uebung 1" width="400" class="no-lightbox">
</figure>

## Gegeben

### Material

Stahl

- Elastizitätsmodul: \(E = 210\,\mathrm{GPa}\)
- Querkontraktionszahl: \(\nu = 0{,}3\)

### Geometrie

Balken mit rechteckigem Querschnitt

- Länge \(L = 1000\,\mathrm{mm}\)
- Breite \(b = 30\,\mathrm{mm}\)
- Höhe \(h = 30\,\mathrm{mm}\)

### Vernetzung

- Netzgröße global: \(15\,\mathrm{mm}\)

### Randbedingungen

**Lagerung:**

- entsprechend Skizze

**Belastung:**

- Gleichmäßig verteilte Belastung mit einer resultierenden Kraft  
  \(F = 1000\,\mathrm{N}\) über die gesamte Balkenlänge  
  (entspricht einer Streckenlast \(q_0 = 1\,\mathrm{N/mm}\)).

!!! danger "Wird die Kraftangriffsfläche geteilt, muss die Kraft auch durch die Anzahl der Symmetrie geteilt werden"

    Die Kraft würde sich im Vollmodell auf die gesamte betroffene Fläche verteilen.  
    Durch die Verwendung von Symmetrie wird jedoch nur ein Teil dieser Fläche im Modell abgebildet.  
    Daher muss im reduzierten Modell auch der **Kraftwert** entsprechend angepasst werden.

    Beispiel: Bei zwei Symmetrieebenen (Viertelmodell) wirkt im Modell nur noch  
    \(F_\text{Modell} = F_\text{voll} / 4 = 250\,\mathrm{N}\).

## Aufgabenstellung

!!! abstract "Alle möglichen Symmetrien ausnutzen und die unten gefragten Spannungen und Verschiebungen berechnen."

### Symmetrie

Welche Symmetrieebenen sind im Bauteil möglich?  Das Koordinatensystem liegt genau im Schwerpunkt des Bauteils.

Daran denken:

Um eine Symmetrie zu verwenden, müssen bei der Spiegelung um diese Symmetrieebene folgende Komponenten identisch zum Vollmodell bleiben:

- Geometrie  
- Lasten  
- Lagerung  

<figure style="text-align:center;">
  <img src="../images/SymmetrieBsp_FrageSymmetrie.excalidraw.png" alt="Frage Symmetrieebenen" width="600" class="no-lightbox">
</figure>

<div class="multiple-choice-question" data-correct="B,C" data-points="5" data-attempts="2">
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

## Hinweise


??? tip "<code>HINWEIS</code> – Geometrie (klicken zum aufklappen)"

    --8<-- "P4_Abstraktionen/01_Symmetrie/Umsetzung.md:Geometrie"

??? tip "<code>HINWEIS</code> – Symmetrie (klicken zum aufklappen)"

    --8<-- "P4_Abstraktionen/01_Symmetrie/Umsetzung.md:Symmetrie"

??? success "<code>LÖSUNG</code> – Detailfenstereinstellungen für die Symmetrieebenen (klicken zum aufklappen)"

    <figure style="text-align:center;">
    <img src="../images/Symmetrie_xz.png" alt="Symmetrieebene xz" width="600" class="no-lightbox">
    </figure>

    <figure style="text-align:center;">
    <img src="../images/Symmetrie_yz.png" alt="Symmetrieebene yz" width="600" class="no-lightbox">
    </figure>

??? tip "<code>HINWEIS</code> – Darstellung als Vollmodell (klicken zum aufklappen)"

    --8<-- "P4_Abstraktionen/01_Symmetrie/Umsetzung.md:Darstellung"


!!! danger "Wird die Kraftangriffsfläche geteilt, muss die Kraft auch durch die Anzahl der Symmetrie geteilt werden"

    Die Kraft würde sich im Vollmodell auf die gesamte Fläche aufteilen. Hier wird durch die Symmetrie jedoch nur ein Teil dieser Fläche verwendet, und daher muss der Kraftwert entsprechend reduziert werden. 

    Wenn die Belastung bereits flächennormiert wäre (also z. B. ein Druck in MPa), wäre dies nicht notwendig.

## Gesucht

Die folgenden Größen berechnen:

### Die maximale Durchbiegung im Bauteil \(u_\text{max}\) in mm

<div class="numeric-question" data-answer="0.921" data-tolerance="0.05" data-points="5" data-attempts="5"  data-hints="Kraft durch 4 geteilt? Material auf 210 GPa gestellt und Netzgröße 15 mm? Symmetrieeinstellungen richtig übernommen?">
</div>

### Die maximale von-Mises-Vergleichsspannung im Bauteil \(\sigma_\text{von Mises}\) in MPa

<div class="numeric-question" data-answer="27.784" data-tolerance="0.25" data-points="5" data-attempts="5"  data-hints="Kraft durch 4 geteilt? Material auf 210 GPa gestellt und Netzgröße 15 mm? Symmetrieeinstellungen richtig übernommen?">
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<figure style="text-align:center;">
  <img src="../images/Uebung01_umax.png" alt="maximale Durchbiegung" width="900">
  <figcaption>Maximale Durchbiegung</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="../images/Uebung01_sigmamax.png" alt="maximale Vergleichsspannung" width="900">
  <figcaption>Maximale Vergleichsspannung</figcaption>
</figure>

</div>
