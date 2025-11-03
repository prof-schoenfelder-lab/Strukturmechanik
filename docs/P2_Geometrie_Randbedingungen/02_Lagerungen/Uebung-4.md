---
hide:
 - toc
---

# Externe Lagerung am Fahrradrahmen

Im vierten Beispiel verwenden wir den vereinfachten Fahrradrahmen. Wer dies in dem vorherigen Teil nicht gemacht hat, kann auch die gegebene Geometrie verwenden. 

Es sollen zwei externe Lager laut folgender Abbildung und eine Kraft im Tretlager angebracht werden:

<figure style="text-align:center;">
  <img src="../images/Uebung-04.excalidraw.png" alt="Fahrradrahmen mit externen Lagern" width="550" class="no-lightbox">
</figure>

## Gegeben

### Material

Aluminiumlegierung 6061-T6

- Elastizitätsmodul $E=68{,}3 \mathrm{GPa}$
- Querkontraktionszahl $\nu=0{,}33$

### Geometrie

Selbstvereinfachte Rahmengeometrie oder diese fertig aufbereitete:

[:material-paperclip: TrekkingRahmen_vereinfacht.scdoc](assets/TrekkingRahmen_vereinfacht.scdoc)

### Vernetzung

- Netzgröße global: 10 mm

### Randbedingungen

Lagerung:

- <code>Remote Displacement</code> auf die Hinterradaufhängung (Kugelgelenk, alle Rotationen frei) (verformbare Geometrie)
    - horizontaler Abstand $dz=0\,\mathrm{mm}$
    - vertikaler Abstand $dy=-390\,\mathrm{mm}$
    - $\sum u_x=0$
    - $\sum u_y=0$
    - $\sum u_z=0$

!!! info inline 

    Damit das Koordinatensystem in der Mitte zwischen den zwei Ausfallenden liegt, müssen Sie die zwei Linien der Radien (nicht die Flächen) für den Ursprung des Koordinatensystems verwenden

<figure style="text-align:center;">
  <img src="../images/Uebung-04-Hinweis-KOS-hinten.png" alt="Koordinatensystem hinten" width="550" class="no-lightbox">
</figure>

- <code>Frictionless Support</code> auf den Innenseiten der Ausfallenden (weil sich sonst die Endpunkte des Rahmens hinten auseinanderschieben)
<figure style="text-align:center;">
  <img src="../images/Uebung-04-Hinweis-FrictionlessSupport-hinten.png" alt="Frictionless Support hinten" width="550" class="no-lightbox">
</figure>


- <code>Remote Displacement</code> auf die Innenseite des Steuerrohrs (zylindrisches Lager, eine Rotationen frei)  (verformbare Geometrie)
    - horizontaler Abstand $dz=-210\,\mathrm{mm}$
    - vertikaler Abstand $dy=-460\,\mathrm{mm}$
    - $\sum u_y=0$
    - $\sum u_z=0$
    - $\sum rot_y=0$
    - $\sum rot_z=0$

Belastung:

- Kraft $F=800\,\mathrm{N}$ vertikal nach unten auf die Innenseite des Tretlagers

## Gesucht

Berechnen Sie anschließend die folgenden Größen:

### Die maximale Verschiebung in z-Richtung (entgegen Fahrtrichtung) $u_{z}$ in mm

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Directional Deformation einfügen</p>
    <p>Im Strukturbaum: <code>Rechtsklick</code> auf <code>Solution</code> > <code>Insert</code> > <code>Deformation</code> > <code>Directional</code></p>
  </div>

 <div class="step">
    <p class="step-title" role="heading" aria-level="2">z-Achse auswählen</p>
    <p>Im Detailfenster: Unter <code>Orientation</code> die <code>z-Achse</code> auswählen</p>
  </div>

</div>


<div class="numeric-question" data-answer="0.39728" data-tolerance="0.05" data-points="5" data-attempts="5"  data-hints="Einheit auf mm gewechselt? Verschiebung in z-Richtung ausgewertet?">
</div>

### Die maximale Verschiebung des Rahmens in <code>negative</code> y-Richtung (Richtung Boden) $u_{y}$ in mm

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Directional Deformation einfügen</p>
    <p>Im Strukturbaum: <code>Rechtsklick</code> auf <code>Solution</code> > <code>Insert</code> > <code>Deformation</code> > <code>Directional</code></p>
  </div>

 <div class="step">
    <p class="step-title" role="heading" aria-level="2">y-Achse auswählen</p>
    <p>Im Detailfenster: Unter <code>Orientation</code> die <code>y-Achse</code> auswählen</p>
  </div>

</div>

<div class="numeric-question" data-answer="0.17581" data-tolerance="0.02" data-points="5" data-attempts="5"  data-hints="Wert in negative y-Richtung ist hier der kleinste Wert (im negativen), hier aber nur Betrag angeben!">
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<figure style="text-align:center;">
  <img src="../images/Uebung-04-Loesung-disp-z.png" alt="Lagerung Lösung" width="700">
  <figcaption>Verschiebung in z-Richtung</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="../images/Uebung-04-Loesung-disp-y.png" alt="Lagerung Lösung" width="700">
  <figcaption>Verschiebung in y-Richtung</figcaption>
</figure>

</div>

