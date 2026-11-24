---
icon: material/palette-outline
hide:
  - toc
sektion: Ergebnisse prüfen und darstellen
title: Spannungen darstellen
order: 220
kurz: Farbskala einstellen, lokale Maxima finden, Modelle vergleichen
thumb: images/Legende_obere_Grenze.png
---

# :material-palette-outline: Spannungen darstellen

Mechanical spannt die Farbskala vom kleinsten bis zum größten Wert. Wenn eine einzelne Spitze viel höher liegt als der Rest, dann ist fast das ganze Bauteil blau, und man sieht nicht, wo es sonst noch hoch beansprucht ist.

## Obere Grenze der Farbskala setzen

<figure style="text-align:center;">
  <img src="../images/Legende_obere_Grenze.png" alt="Kragarm aus Praktikum 4 mit feinem Netz: oben reicht die Farbskala bis zur Spitze am Kraftangriffspunkt, das Bauteil ist fast ganz blau; unten ist der zweite Legendenwert auf 80 MPa gesetzt, die Biegespannung wird sichtbar" width="900">
  <figcaption>Kragarm aus Praktikum 4 mit feinerem Netz: oben die Skala bis zum Maximum, unten mit gesetzter Grenze</figcaption>
</figure>

<div class="steps" markdown="1" data-kategorie="Auswertung" data-titel="Obere Grenze der Farbskala setzen">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Zweiten Wert von oben setzen</p>
    <p>In der Legende den zweiten Wert von oben doppelklicken und die gewünschte Grenze eintippen. Das oberste Band bleibt rot und reicht von dieser Grenze bis zum Maximum, die Farben darunter verteilen sich neu.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Zurücksetzen</p>
    <p><code>Rechtsklick Legende → Reset All</code> stellt die Skala wieder her.</p>
  </div>

</div>

<!-- ENTWURF: Im Pool prüfen, ob sich auch der oberste Wert ändern lässt (laut Ansys-Forum nicht). Bildschirmfoto der Legende ergänzen. -->

- Wenn die Grenze gesetzt ist, dann heißt Rot nur noch: über der Grenze. Wie hoch die Spannung dort wirklich ist, steht am Maximum.
- Wenn nur ein Teil des Bauteils interessiert, dann das Ergebnis nur auf diese Flächen legen, wie bei der Schweißnaht in [Praktikum 3, Übung 5](../../P3_Vernetzung/02_ANSYS_Umsetzung/Uebung-5.md). Skala und Maximum gelten dann nur dort.

## Lokale Maxima finden

Das Etikett `Max` zeigt nur die höchste Stelle. Die nächsthöheren Stellen findet Mechanical selbst:

<div class="steps" markdown="1" data-kategorie="Auswertung" data-titel="Lokale Maxima anzeigen">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Lokale Maxima einblenden</p>
    <p>Ergebnis auswählen, dann <code>Rechtsklick Grafikfenster → Create Local Max Probes</code>. Mechanical setzt Etiketten <code>Max 1</code>, <code>Max 2</code> und so weiter, bis zu sechs. <code>Max 1</code> ist das größte Maximum.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Etiketten wieder löschen</p>
    <p>Im Fenster <code>Graphics Annotations</code> die Zeilen auswählen und <code>Entf</code> drücken.</p>
  </div>

</div>

Ein lokales Maximum ist ein Knoten, dessen Nachbarn alle kleinere Werte haben. Zu jedem lokalen Maximum gehört die Frage: Gibt es dafür einen physikalischen Grund, oder ist es eine Singularität?

## Gleiche Farbskala für zwei Modelle

Zwei Farbbilder lassen sich nur vergleichen, wenn dieselbe Farbe in beiden denselben Wert bedeutet.

<div class="steps" markdown="1" data-kategorie="Auswertung" data-titel="Farbskala für mehrere Ergebnisse speichern (Named Legend)">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Skala einstellen</p>
    <p>Beim ersten Ergebnis die Grenzen so setzen, dass sie für beide Modelle passen.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Skala speichern</p>
    <p><code>Rechtsklick Legende → Named Legends → New</code> und einen Namen vergeben.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Skala beim anderen Ergebnis wählen</p>
    <p><code>Rechtsklick Legende → Named Legends</code> und den Namen auswählen.</p>
  </div>

</div>

<!-- ENTWURF: Im Pool prüfen, wie sich Grenzen über das Maximum des ersten Modells hinaus setzen lassen (laut Ansys-Forum: Max, Min on Color Bar abwählen). -->
