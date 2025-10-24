---
hide:
    - toc
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

### Spannungen

Welche Lagerung führt zur ähnlichen Spannung wie die Variante mit dem Schraubkopf?

Hinweis: Wenn sie die Körperauswahl verwenden und den Inbus der jeweiligen Randbedingung auswählen bevor Sie die Spannung einfügen, können Sie auch nur die Spannung des jeweiligen Bauteils anzeigen.

<div class="multiple-choice-question" data-correct="C,D" data-points="5" data-attempts="3">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="q1a" name="q1">
      <label for="q1a">Fixed Support</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="q1b" name="q1">
      <label for="q1b">Remote Displacement (rigid)</label>
    </div>
    <div class="mc-option" data-value="C">
      <input type="checkbox" id="q1c" name="q1">
      <label for="q1c">Remote Displacement (deformable)</label>
    </div>
    <div class="mc-option" data-value="D">
      <input type="checkbox" id="q1d" name="q1">
      <label for="q1d">Elastic Support</label>
    </div>
  </div>
</div>
