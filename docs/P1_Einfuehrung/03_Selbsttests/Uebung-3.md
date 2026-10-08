---
hide:
---

# Inbus Schlüssel

Nun zu realen Bauteilen die einen Mehrachsigen Spannungszustand hervorrufen. Beginnen wir mit einem Inbusschlüssel der mit einer Kraft belastet wird.

<figure style="text-align:center;">
  <img src="../images/Uebung-03.png" alt="Inbu" width="400" class="no-lightbox">
</figure>

## Gegeben

### Material

Stahl

- Elastizitätsmodul $E=210 \mathrm{GPa}$
- Querkontraktionszahl $\nu=0,3$

### Vernetzung

- Netzgröße global: 1 mm

### Geometrie

[:material-paperclip: Inbus.scdoc](assets/Inbus.scdoc)

<div class="steps" markdown="1" data-kategorie="Geometrie" data-titel="Geometrie einladen">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Geometrie einladen</p>
    <p>Im Projektmenü: <code>Rechtsklick</code> auf <code>Geometry</code> > <code>Import Geometry</code> > <code>Browse ..</code>  </p>
    <figure style="text-align:center;">
    <img src="../images/Geometrie_importieren.png" alt="von Mises Spannung einfügen" width="600" class="no-lightbox">
    </figure>
    <p>Geometriedatei auswählen</p>
  </div>

</div>

Die Geometrie beinhaltet noch nicht die Flächen an denen die Randbedingungen angebracht werden. Diese können in `SpaceClaim` so erstellt werden:

<tutorial slug="flaechen-erzeugen-split-ebene"></tutorial>

Die Fläche für die Kraft am langen Ende entsteht genauso: eine Ebene auf der Stirnfläche des langen Endes erzeugen, um `30` mm verschieben und die Flächen mit `Split` teilen.

### Randbedingungen

Lagerung:

- feste Einspannung im Bereich des Kopfes (10 mm), umgesetzt mit `Remote Displacement` (alle Verschiebungen und Rotationen 0) wie in Übung 2, damit an den Kanten keine Singularität entsteht

Belastung:

- Kraft $F_y=-200 \mathrm{N}$ auf den letzten 30 mm am langen Ende, senkrecht auf die Fläche

## Hinweise

<div class="steps" markdown="1" data-anleitung="nein">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">von-Mises Spannung einfügen</p>
    <p>Um Mehrachsige Spannungszustände bei duktilen Materialien verwenden wir die von-Mises Spannung. Diese kann wie folgt hinzugefügt werden</p>
    <p>im Strukturbaum: <code>Rechtsklick</code> auf <code>Solution</code> und anschließend auf <code>Insert</code> > <code>Stress</code> > <code>Equivalent (von-Mises)</code> klicken.</p>
    <figure style="text-align:center;">
    <img src="../images/vonMisesSpannung.png" alt="von Mises Spannung einfügen" width="600" class="no-lightbox">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Ort der maximalen Spannung anzeigen</p>
    <p>Um zu prüfen wo die maximale Spannung auftreten sind folgende Schritte notwendig:</p> 
    <p>Im Strukturbaum (unter Solution) von Mises Spannung auswählen</p> 
    <p>In der Menüleiste oben: Reiter<code>Result</code> auf <code>Maximum</code> klicken.</p>
    <figure style="text-align:center;">
    <img src="../images/Stress_Maximum.png" alt="Ort der Maximalen Spannung anzeigen" width="600" class="no-lightbox">
    <p>Im Grafikfenster erscheint ein Hinweis mit dem Maximum</p> 
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Kraft auf die Fläche anbringen</p>
    <p>Zur Erstellung der Geometrieflächen das Klick-Tutorial weiter oben beachten</p> 
    <p>In Mechanical: Um dann in mehrere Flächen für eine Randbedingung auszuwählen `STRG` gedrückt halten</p> 
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Alternative fixierte Lagerung</p>
    <p>In diesem Fall zum Ersatz der fixierten Lagerung nur `Remote Displacement` mit allen Freiheitsgraden auf Null gesetzt verwenden.</p> 
  </div>

</div>

## Gesucht

### Die maximale Durchbiegung $u_{\max }$ in mm

<div class="numeric-question" data-baum="p1-u3" data-answer="2.06" data-tolerance="0.2" data-points="5" data-attempts="5"  data-hints="Material zugeordnet? Netzgröße 1 mm eingestellt?">
</div>

<!---
Fixed Support: 1,9867 mm
RemoteDisp (Fläche): 2,1309 mm
-->

### Die maximale von-Mises-Spannung in MPa

<div class="numeric-question" data-baum="p1-u3" data-answer="353.11" data-tolerance="3" data-points="5" data-attempts="5"  data-hints="Wurde die von-Mises Spannung ausgewertet? Fixierte Lagerung mit Remote Displacement? Netzgröße 1 mm eingestellt?" data-diagnose="393.35 [lager]: Das Maximum liegt an der festen Einspannung, einer Singularität. Remote Displacement verwenden oder außerhalb der Einspannung auswerten. | 331.07 [netz.groesse]: Dieser Wert entsteht mit dem Standardnetz. Hier ist eine Netzgröße von 1 mm vorgegeben.">
</div>

<!---
Fixed Support: 353,11 MPa
RemoteDisp+ (Fläche): 353,11 MPa
-->