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

[:material-paperclip: Inbus.scdoc](../assets/Inbus.scdoc)

<div class="steps" markdown="1">

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

<div class="tutorial-embed"
   data-tutorial="/assets/tutorials/Flaechen_erzeugen_Split_Ebene"
   style="width:600px">
</div>

### Randbedingungen

Lagerung:

- feste Einspannung im Bereich des Kopfes (10 mm)

Belastung:

- Am Langen Ende 30 mm senkrecht auf die Fläche (negative y-Richtung) mit einer Kraft von 200 N

## Hinweise

<div class="steps" markdown="1">

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
    <p>Zur Erstellung der Geometrieflächen beachten Sie das Klick-Tutorial weiter oben</p> 
    <p>In Mechanical: Um dann in mehrere Flächen für eine Randbedingung auszuwählen halten Sie `STRG` gedrückt</p> 
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Alternative fixierte Lagerung</p>
    <p>Verwenden Sie in diesem Fall zum Ersatz der fixierten Lagerung nur `Remote Displacement` mit allen Freiheitsgraden auf Null gesetzt.</p> 
  </div>

</div>

## Gesucht

### Die maximale Durchbiegung $u_{\max }$ in mm

<div class="numeric-question" data-answer="2.06" data-tolerance="0.2" data-points="5" data-attempts="5"  data-hints="Material zugeordnet?">
</div>

<!---
Fixed Support: 1,9867 mm
RemoteDisp (Fläche): 2,1309 mm
-->

### Die maximale Spannung in von-Mises Spannung 

<div class="numeric-question" data-answer="353.11" data-tolerance="0.5" data-points="5" data-attempts="5"  data-hints="Haben Sie die von-Mises Spannung ausgewertet? Fixierte Lagerung mit Remote Displacement?">
</div>

<!---
Fixed Support: 353,11 MPa
RemoteDisp+ (Fläche): 353,11 MPa
-->