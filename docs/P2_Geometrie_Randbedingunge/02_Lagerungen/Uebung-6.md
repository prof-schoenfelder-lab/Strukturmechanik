---
hide:
---

# Vergleich verschiedener Lagerungsbedingungen am Beispiel des Inbus

Wir benutzen nun den Inbusschlüssel aus dem ersten Praktikum um folgende Lagerungen miteinander zu vergleichen:

- a) Referenz mit `Schraubkopf`
- b) `Fixed Support`
- c&d) `Remote Displacement` (starr und verformbar)
- e) `Elastic Support`

Als Referenz was am nächsten an der Wirklichkeit dran ist ist ein Schraubkopf modelliert. 

<figure style="text-align:center;">
  <img src="../images/Uebung-06.png" alt="Inbus" width="700" class="no-lightbox">
</figure>

## Gegeben

### Material

Stahl

- Elastizitätsmodul $E=210 \mathrm{GPa}$
- Querkontraktionszahl $\nu=0,3$

### Vernetzung

- Netzgröße global: 1 mm

### Geometrie

[:material-paperclip: Uebung-06.wpbz](../assets/Uebung-06.wpbz)

### Randbedingungen

Lagerung im Bereich des Kopfes:

- a) Verbund mit Schraubenkopf (Ende Schraubenkopf mit `Fixed Support` gelagert) 
- b) feste Einspannung mit `Fixed Support` 
- c) feste Einspannung mit `Remote Displacement alle Freiheitsgrade gesperrt (rigid)` 
- d) feste Einspannung mit `Remote Displacement alle Freiheitsgrade gesperrt (deformable)` 
- e) elastische Bettung mit `Elastic Support` mit $k=20000\,N/mm^3$ + `Frictionless Support` auf der Stirnseite

Belastung:

- Am Langen Ende 30 mm senkrecht auf die Fläche (negative y-Richtung) mit einer Kraft von 200 N

## Gesucht

### Die maximale Durchbiegung $u_{\max }$ in mm

<div class="numeric-question" data-answer="2.06" data-tolerance="0.2" data-points="5" data-attempts="5"  data-hints="Material zugeordnet?">
</div>

<!---
Fixed Support: 1,9867 mm
RemoteDisp (Fläche): 2,1309 mm
-->

### Die maximale Spannung in von-Mises Spannung 

<div class="numeric-question" data-answer="353.11" data-tolerance="3" data-points="5" data-attempts="5"  data-hints="Haben Sie die von-Mises Spannung ausgewertet? Fixierte Lagerung mit Remote Displacement?">
</div>

<!---
Fixed Support: 353,11 MPa
RemoteDisp+ (Fläche): 353,11 MPa
-->