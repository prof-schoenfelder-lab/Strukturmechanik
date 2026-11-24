---
icon: material/clipboard-check-outline
hide:
  - toc
sektion: Ergebnisse prüfen und darstellen
title: Ergebnisse prüfen
order: 210
kurz: Fünf Schritte nach jeder Rechnung, von der Verformung bis zur Bewertung
thumb: images/Verformung_Massstab.png
---

# :material-clipboard-check-outline: Ergebnisse prüfen

Ein Farbbild ist noch kein Ergebnis. Nach jeder Rechnung steht dieselbe Reihenfolge an, von grob nach fein: erst ob sich das Modell so bewegt wie erwartet, zuletzt die Spannung an der Stelle, die zählt.

<div class="steps" markdown="1" data-kategorie="Auswertung" data-titel="Ergebnisse prüfen in fünf Schritten">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Verformung</p>
    <p>Passt die Größenordnung? Bewegt sich das Bauteil in die erwartete Richtung, bleiben die Lager dort, wo sie sein sollen?</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Kräfte</p>
    <p>Die Lagerkräfte müssen zusammen so groß sein wie die aufgebrachten Lasten.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Spannung</p>
    <p>Für jede Spannungsspitze gibt es einen Grund: eine Kerbe, eine Last, ein Lager. Wenn sich kein Grund findet, dann stimmt etwas am Modell nicht.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Netz</p>
    <p>Ändert sich die Spannung an der Stelle, die zählt, mit feinerem Netz noch? Das Vorgehen steht in <a href="../../../P3_Vernetzung/01_Grundlagen/Sensitivitaetsanalyse/">Praktikum 3</a>.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Bewertung</p>
    <p>Die Spannung mit der Streckgrenze des Werkstoffs vergleichen.</p>
  </div>

</div>

## Verformung: Ausgangsgeometrie und Maßstab

<figure style="text-align:center;">
  <img src="../images/Verformung_Massstab.png" alt="Kragarm aus Praktikum 4, oben im wahren Maßstab, unten 15-fach überhöht, jeweils mit der Ausgangsgeometrie als gestrichelte Linie" width="900">
  <figcaption>Kragarm aus Praktikum 4: dieselbe Verformung im wahren Maßstab und 15-fach überhöht</figcaption>
</figure>

- Mechanical zeigt die Verformung meist überhöht, damit man sie sieht. Die Form stimmt dann, die Größe täuscht.
- Wenn die Verformung im Bild riesig aussieht, dann zuerst den Maßstab ansehen, bevor Sie am Modell suchen.

<div class="steps" markdown="1" data-kategorie="Auswertung" data-titel="Verformung mit Ausgangsgeometrie und Maßstab ansehen">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Ausgangsgeometrie einblenden</p>
    <p>Ergebnis auswählen, dann <code>Reiter Result → Edges → Show Undeformed Wireframe</code>. Die unverformte Geometrie erscheint als Drahtgitter. <code>Show Undeformed Model</code> zeigt sie durchscheinend.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Maßstab wählen</p>
    <p>Im <code>Reiter Result</code> steht in derselben Gruppe die Auswahl für den Maßstab: <code>1.0 (True Scale)</code> zeigt die wahre Größe, <code>Auto Scale</code> eine Überhöhung, die Mechanical selbst wählt. Ein eigener Faktor lässt sich direkt eintippen.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Animation ansehen</p>
    <p>Mit dem Abspielknopf im Fenster <code>Graph</code> läuft die Verformung als Film. Eine falsche Bewegung fällt dabei schneller auf als im Standbild.</p>
  </div>

</div>

<!-- ENTWURF: Bildschirmfoto des Reiters Result mit Maßstab und Edges aus 2025 R2 ergänzen; Lage der Auswahl im Pool prüfen. -->

## Kräfte: Lagerkräfte gegen Lasten

<div class="steps" markdown="1" data-kategorie="Auswertung" data-titel="Lagerkraft ablesen (Force Reaction)">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Lagerkraft einfügen</p>
    <p><code>Rechtsklick Strukturbaum Solution → Insert → Probe → Force Reaction</code></p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Lager wählen</p>
    <p><code>Detailfenster → Boundary Condition</code>: das Lager auswählen, zum Beispiel <code>Fixed Support</code></p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Auswerten</p>
    <p><code>Rechtsklick Strukturbaum Solution → Evaluate All Results</code>. Im Detailfenster stehen die Komponenten der Lagerkraft.</p>
  </div>

</div>

Wenn die Summe der Lagerkräfte nicht zu den Lasten passt, dann fehlt eine Last, sie hat die falsche Richtung oder die falsche Einheit.

## Bewertung: Spannung gegen Streckgrenze

Bis zur Streckgrenze verformt sich ein Metall elastisch, darüber bleibend: Es fließt. Das Material in unseren Modellen kennt kein Fließen und rechnet auch oberhalb der Streckgrenze weiter, als wäre es elastisch.

$$
S = \frac{R_e}{\sigma_v}
$$

- $S$: Sicherheit gegen Fließen, ohne Einheit
- $R_e$: Streckgrenze des Werkstoffs in MPa (bei Aluminium die Dehngrenze $R_{p0{,}2}$)
- $\sigma_v$: größte Vergleichsspannung (von Mises) in MPa

- Wenn die Vergleichsspannung über der Streckgrenze liegt, dann gilt die lineare Rechnung an dieser Stelle nicht mehr.
- Wenn die Stelle eine Singularität ist, dann sagt der Wert dort nichts aus. Bewertet wird die größte Spannung, für die es einen physikalischen Grund gibt.
