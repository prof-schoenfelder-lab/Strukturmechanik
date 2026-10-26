---
hide:
    - toc
sektion: Lagerungen
title: Übung 4
order: 180
kurz: Vergleich verschiedener Lagerungsbedingungen am Beispiel des Inbus
thumb: images/Uebung-06.png
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

### Archivdatei mit Material, Geometrie, Netz und Belastung

[:material-paperclip: Uebung-06.wbpz](assets/Uebung-06.wbpz)

Wie das Archiv importiert wird, steht in [Übung 1](../01_Geometrie_anpassen/Uebung-1.md#archiv-importieren).

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

Hinweis: Wird die Körperauswahl verwendet und der Inbus der jeweiligen Randbedingung ausgewählt bevor die Spannung eingefügt wird, lässt sich auch nur die Spannung des jeweiligen Bauteils anzeigen.

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


<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<iframe title="maximale Spannungen (MPa)" aria-label="Balken" id="datawrapper-chart-ZVQD6" src="https://datawrapper.dwcdn.net/ZVQD6/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="185" data-external="1"></iframe><script type="text/javascript">window.addEventListener("message",function(a){if(void 0!==a.data["datawrapper-height"]){var e=document.querySelectorAll("iframe");for(var t in a.data["datawrapper-height"])for(var r,i=0;r=e[i];i++)if(r.contentWindow===a.source){var d=a.data["datawrapper-height"][t]+"px";r.style.height=d}}});</script>

<iframe title="maximale Spannungen (MPa)" aria-label="Bar Chart" id="datawrapper-chart-pQGBH" src="https://datawrapper.dwcdn.net/pQGBH/3/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="185" data-external="1"></iframe><script type="text/javascript">window.addEventListener("message",function(a){if(void 0!==a.data["datawrapper-height"]){var e=document.querySelectorAll("iframe");for(var t in a.data["datawrapper-height"])for(var r,i=0;r=e[i];i++)if(r.contentWindow===a.source){var d=a.data["datawrapper-height"][t]+"px";r.style.height=d}}});</script>

<h3>Warum liegen zwei Lagerungen nah am Schraubkopf?</h3>
<p>Im echten Schraubkopf gibt die Auflagefläche ein wenig nach: Der Inbus kann sich dort verformen, die Last verteilt sich über die ganze Fläche.</p>
<ul>
<li><code>Fixed Support</code>: Jeder Knoten der Fläche steht fest, die Fläche kann sich gar nicht verformen. Das ist steifer als in Wirklichkeit, und am Rand der Einspannung entsteht eine Singularität: Die Spannung dort hängt vom Netz ab, nicht von der Lagerung.</li>
<li><code>Remote Displacement (rigid)</code>: Die Fläche darf sich nur als Ganzes bewegen, bleibt aber starr. Für die Fläche wirkt das fast wie eine feste Einspannung, mit derselben Spannungsspitze am Rand.</li>
<li><code>Remote Displacement (deformable)</code>: Gesperrt ist nur die Bewegung des Bezugspunkts, die Fläche selbst darf sich verformen. So verteilt sich die Last wie im Schraubkopf.</li>
<li><code>Elastic Support</code>: Die Fläche liegt auf Federn mit der Bettungssteifigkeit k und gibt nach wie im Schraubkopf. Wie nah das Ergebnis an der Wirklichkeit liegt, hängt von k ab. Prüffrage: Woher kommt der Wert für k, und wie stark ändert sich das Ergebnis, wenn k doppelt oder halb so groß ist?</li>
</ul>

</div>

