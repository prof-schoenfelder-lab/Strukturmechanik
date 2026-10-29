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

[:material-paperclip: Uebung-04.wbpz](assets/Uebung-04.wbpz)

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

### Verformung

Werten Sie bei jeder Variante die Gesamtverformung des Inbus aus (`Total Deformation`).

### Die maximale Gesamtverformung mit `Fixed Support` in mm

<div class="numeric-question" data-answer="1.9867" data-tolerance="0.03" data-points="5" data-attempts="5" data-hints="Fixed Support auf den Flächen am Kopf? Kraft 200 N in negative y-Richtung? Einheit mm?" data-diagnose="2.1307: Das ist der Wert mit Remote Displacement (deformable). Gefragt ist hier die Variante mit Fixed Support.">
</div>

### Die maximale Gesamtverformung mit `Remote Displacement` (deformable) in mm

<div class="numeric-question" data-answer="2.1307" data-tolerance="0.03" data-points="5" data-attempts="5" data-hints="Alle sechs Freiheitsgrade gesperrt? Behavior auf Deformable?" data-diagnose="1.9867: Dieser Wert entsteht mit Behavior Rigid oder mit Fixed Support. Steht Behavior auf Deformable?">
</div>

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


### Woher kommt der Unterschied in der Verformung?

Zeigen Sie bei `Fixed Support` und bei `Remote Displacement` (deformable) die Gesamtverformung nur an den Flächen der Lagerung an: Flächen auswählen, dann `Rechtsklick Strukturbaum Solution → Insert → Deformation → Total`.

<div class="multiple-choice-question" data-correct="A" data-points="5" data-attempts="2">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="q4u_a" name="q4u">
      <label for="q4u_a">Mit deformable verschiebt sich die Lagerfläche selbst ein wenig. Der Inbus verformt sich in beiden Fällen gleich und wird nur mitgenommen.</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="q4u_b" name="q4u">
      <label for="q4u_b">Mit deformable ist der Inbus selbst weicher.</label>
    </div>
    <div class="mc-option" data-value="C">
      <input type="checkbox" id="q4u_c" name="q4u">
      <label for="q4u_c">Mit deformable wirkt eine größere Kraft auf den Inbus.</label>
    </div>
  </div>
</div>

### Reicht hier ein `Fixed Support`?

Kreuzen Sie alle Aufgabenstellungen an, für die ein `Fixed Support` am Kopf ausreicht.

<div class="multiple-choice-question" data-correct="A" data-points="5" data-attempts="2">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="q4f_a" name="q4f">
      <label for="q4f_a">Ich will die Spannung im langen Schenkel wissen, weit weg vom Kopf.</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="q4f_b" name="q4f">
      <label for="q4f_b">Ich will die Verformung an der Last genau vorhersagen.</label>
    </div>
    <div class="mc-option" data-value="C">
      <input type="checkbox" id="q4f_c" name="q4f">
      <label for="q4f_c">Ich will die Spannung direkt am Kopf wissen.</label>
    </div>
  </div>
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<h3>Verformung und Spannung je Lagerung</h3>

<table>
<thead><tr><th>Lagerung</th><th>max. Gesamtverformung</th><th>gegenüber Schraubkopf</th><th>max. Vergleichsspannung</th><th>gegenüber Schraubkopf</th></tr></thead>
<tbody>
<tr><td>a) Schraubkopf (Referenz)</td><td>2,066 mm</td><td></td><td>353,7 MPa</td><td></td></tr>
<tr><td>b) <code>Fixed Support</code></td><td>1,987 mm</td><td>-4 %</td><td>405,2 MPa</td><td>+15 %</td></tr>
<tr><td>c) <code>Remote Displacement</code> (rigid)</td><td>1,987 mm</td><td>-4 %</td><td>405,2 MPa</td><td>+15 %</td></tr>
<tr><td>d) <code>Remote Displacement</code> (deformable)</td><td>2,131 mm</td><td>+3 %</td><td>353,0 MPa</td><td>-0,2 %</td></tr>
<tr><td>e) <code>Elastic Support</code></td><td>2,304 mm</td><td>+12 %</td><td>354,2 MPa</td><td>+0,1 %</td></tr>
</tbody>
</table>

<ul>
<li><code>Fixed Support</code> und <code>Remote Displacement</code> (rigid) mit allen Freiheitsgraden gesperrt sind dasselbe: Die Lagerfläche kann sich in beiden Fällen nicht bewegen.</li>
<li>Der Inbus selbst verformt sich in allen Varianten gleich, außer direkt an der Lagerung. Die Unterschiede kommen nur daher, wie stark die Lagerung nachgibt.</li>
<li>Der echte Schraubkopf gibt etwas nach: mehr als ein <code>Fixed Support</code>, weniger als <code>deformable</code> annimmt.</li>
<li>Der <code>Elastic Support</code> ist mit k = 20 000 N/mm³ hier weicher als der Schraubkopf. Mit einem größeren k läge er näher an der Referenz.</li>
<li>Bei der Spannung ist es anders: <code>deformable</code> und <code>Elastic Support</code> liegen weniger als 1 % neben dem Schraubkopf, <code>Fixed Support</code> und <code>rigid</code> 15 % darüber. Dort entsteht am Rand der Lagerung eine Singularität.</li>
<li>Ob eine Lagerung als Ersatz taugt, hängt also davon ab, was gefragt ist: Für die Spannung passen hier <code>deformable</code> und <code>Elastic Support</code>, für die Verformung keine der Varianten ganz genau. Ein <code>Fixed Support</code> reicht, wenn Spannungen weit weg von der Lagerung gefragt sind.</li>
</ul>

<h3>Warum liegen zwei Lagerungen nah am Schraubkopf?</h3>
<p>Im echten Schraubkopf gibt die Auflagefläche ein wenig nach: Der Inbus kann sich dort verformen, die Last verteilt sich über die ganze Fläche.</p>
<ul>
<li><code>Fixed Support</code>: Jeder Knoten der Fläche steht fest, die Fläche kann sich gar nicht verformen. Das ist steifer als in Wirklichkeit, und am Rand der Einspannung entsteht eine Singularität: Die Spannung dort hängt vom Netz ab, nicht von der Lagerung.</li>
<li><code>Remote Displacement (rigid)</code>: Die Fläche darf sich nur als Ganzes bewegen. Mit allen Freiheitsgraden gesperrt ist das genau eine feste Einspannung, mit derselben Spannungsspitze am Rand.</li>
<li><code>Remote Displacement (deformable)</code>: Gesperrt ist nur die Bewegung des Bezugspunkts, die Fläche selbst darf sich verformen. So verteilt sich die Last wie im Schraubkopf.</li>
<li><code>Elastic Support</code>: Die Fläche liegt auf Federn mit der Bettungssteifigkeit k und gibt nach wie im Schraubkopf. Wie nah das Ergebnis an der Wirklichkeit liegt, hängt von k ab.</li>
</ul>

</div>

<div class="zwischenspiel" data-seite="/P2_Geometrie_Randbedingungen/02_Lagerungen/Uebung-4,/P2_Geometrie_Randbedingungen/02_Lagerungen/Uebung-6" data-voraussetzung="Übung 3 und 4" data-name="Inbus (Übung 4)" data-teil="bau-2o9.8AAA8AAA8AAA8AAA8AAA________________.wB004.Tn8160k">
<h2>Zwischenspiel: Knackpunkt</h2>
<p>Der Inbus aus dieser Übung, vereinfacht als ebenes L: Der lange Schenkel ist 240 mm lang, der kurze 90 mm, beide sind 40 mm breit, eine 10 mm dicke Platte aus Stahl S235. Der kurze Schenkel ist unten eingespannt wie im Schraubkopf, am Ende des langen Schenkels drücken 2 kN nach unten. Nehmen Sie so viel Material weg wie möglich, ohne dass er versagt.</p>
</div>
