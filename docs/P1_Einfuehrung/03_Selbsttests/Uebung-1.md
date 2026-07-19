---
hide:
---

# zweiseitig gelagerter Balken mit Einzelkraft

Zum Start ein einfaches Beispiel bei dem sich nur die Belastung von einer Linienlast zu einer Einzellast ausgetauscht wird.

<figure style="text-align:center;">
  <img src="../images/Uebung-01.png" alt="Zweiseitig gelagerter Balken mit Einzelkraft" width="400" class="no-lightbox">
</figure>

## Gegeben

### Material

Stahl

- Elastizitätsmodul $E=210 \mathrm{GPa}$
- Querkontraktionszahl $\nu=0{,}3$

### Geometrie

Balken mit rechteckigem Querschnitt

- Länge $L=1000 \mathrm{mm}$
- Breite $b=30 \mathrm{mm}$
- Höhe $h=30 \mathrm{mm}$

### Vernetzung

- Netzgröße global: 15 mm


### Randbedingungen

Lagerung:

- Loslager auf der linken Seite
- Festlager auf der rechten Seite

Belastung:

- Kraft $F=5000 \mathrm{N}$

## Hinweise

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Analyse duplizieren</p>
    <p>Im Workbench Projektmenü auf das Dreieck der bereits vorhandenen Analyse <code>klicken</code> und <code>Duplicate</code> auswählen</p>
    <figure style="text-align:center;">
    <img src="../images/Analyse_duplizieren.png" alt="Aufgabenstellung" width="300" class="no-lightbox">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Analyse umbenennen und Geometrie in SpaceClaim öffnen</p>
    <p>Analyse durch Doppelklick auf Namen ändern und mit <code>Rechtsklick</code> auf <code>Geometry</code> und <code>Edit Geometry in SpaceClaim...</code> auswählen</p>
    <figure style="text-align:center;">
    <img src="../images/Analyse_duplizieren2.png" alt="Aufgabenstellung" width="300" class="no-lightbox">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">In SpaceClaim: Split-Tool auswählen</p>
    <p>Auf den Reiter <code>Design</code> klicken und <code>Split</code> auswählen</p>
    <figure style="text-align:center;">
    <img src="../images/Kante_erzeugen1.png" alt="Split Tool" width="500" class="no-lightbox">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">In SpaceClaim: Fläche in der Mitte teilen</p>
    <p>Obere Fläche <code>anklicken</code> und Mauszeiger auf Kante <code>bewegen</code> (nicht klicken) und mit <code>TAB</code> zur Prozentanzeige wechseln. Anschließend <code>50</code> eingeben und mit <code>ENTER</code> bestätigen.</p>
    <figure style="text-align:center;">
    <img src="../images/Kante_erzeugen2.png" alt="Fläche halbieren" width="400" class="no-lightbox">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Im Projektmenü: Geometrie neu reinladen und Mechanical öffnen</p>
    <p><code>Rechtsklick</code> auf <code>Model</code> und anschließend auf <code>Update</code> und dann auf <code>Edit...</code> klicken.</p>
    <figure style="text-align:center;">
    <img src="../images/Geometrie_updaten.png" alt="Fläche halbieren" width="300" class="no-lightbox">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Im Mechanical: Alte Flächenlast löschen</p>
    <p>Im Strukturbaum: <code>Rechtsklick</code> auf <code>Force (alte Flächenlast)</code> und anschließend auf <code>Delete</code> klicken.</p>
  </div>

</div>

## Gesucht

### Die maximale Durchbiegung $u_{\max }$ in mm

<div class="numeric-question" data-answer="7.378" data-tolerance="0.1" data-points="5" data-attempts="5"  data-hints="Einheit auf mm gewechselt? Kraft auf -5000N in z-Richtung auf der Kante?">
</div>

### Die maximale Spannung in y-Richtung $\sigma_{y, \max }$ in MPa

<div class="numeric-question" data-answer="275.03" data-tolerance="0.5" data-points="5" data-attempts="5"  data-hints="Einheit auf mm gewechselt? Kraft auf -5000N in z-Richtung auf der Kante?">
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

### 🎯 Lösung

Hier sehen Sie die korrekte Lösung für diese Übung:

<figure style="text-align:center;">
  <img src="../images/Uebung-01_Loesung_Kraft.png" alt="Kraft auf Kante" width="700">
  <figcaption>Schritt 1: Kraft korrekt auf der Kante appliziert (-5000N in z-Richtung)</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="../images/Uebung-01_Loesung_Durchbiegung.png" alt="Durchbiegung Ergebnis" width="700">
  <figcaption>Schritt 2: Maximale Durchbiegung u_max = 7.378 mm (Total Deformation)</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="../images/Uebung-01_Loesung_Spannung.png" alt="Spannung Ergebnis" width="700">
  <figcaption>Schritt 3: Maximale Spannung in y-Richtung σ_y,max = 275.03 MPa (Normal Stress Y)</figcaption>
</figure>

**Wichtige Punkte:**
- Einheit auf mm umstellen (nicht vergessen!)
- Kraft muss auf der **Kante** appliziert werden (nicht auf der Fläche)
- Kraftrichtung: -5000N in **z-Richtung** (negativ!)
- Spannung in **y-Richtung** auswerten (Längsrichtung des Balkens)

</div>

