---
icon: material/play-box-outline
hide:
  - toc
sektion: Schrauben
title: Geführtes Beispiel
order: 120
kurz: Vorgespannte Schraube M10 zwischen zwei Platten
thumb: images/Schraube-Aufgabe.excalidraw.png
typ: beispiel
---

# :material-play-box-outline: Geführtes Beispiel: vorgespannte Schraube

Zwei Stahlplatten werden mit einer Schraube M10 verspannt und danach auseinandergezogen. Sie klicken das Beispiel Schritt für Schritt nach und vergleichen die Schraubenkraft mit dem [Verspannungsschaubild](Schraube.md#warum-die-schraube-so-wenig-abbekommt).

<figure style="text-align:center;">
  <img src="../images/Schraube-Aufgabe.excalidraw.png" alt="Schnitt durch zwei Platten von je 15 mm mit einer Schraube M10, die untere Platte ist an den Seitenflächen eingespannt, an der oberen Platte ziehen 10 kN nach oben" width="700" class="no-lightbox">
</figure>

!!! bug "ENTWURF: Modell, Archiv und Kontrollwerte fehlen"
    - Das Modell ist in ANSYS noch nicht gebaut und nicht gerechnet. Die Klickwege stammen aus der ANSYS-Hilfe 2025 R2.
    - Alle Kontrollwerte („Wert folgt“) und die Rechenzeit kommen aus dem Pool.

## Gegeben

### Archiv mit Geometrie, Material, Netz und Lagerung

[:material-paperclip: Beispiel-Schraube.wbpz](assets/Beispiel-Schraube.wbpz)

### Geometrie

- Zwei Platten, je 60 mm × 60 mm × 15 mm, Bohrung 11 mm
- Schraube M10 als Volumenkörper ohne Gewinde: Schaft 10 mm, Kopf und Mutter als Zylinder mit 16 mm Durchmesser
- Schraube und Mutter sind ein Körper, die Schraubenachse ist die y-Achse

### Material

Stahl (`Structural Steel`) für alle Körper

### Randbedingungen

- Lagerung: Die untere Platte ist an ihren vier Seitenflächen fest eingespannt (`Fixed Support`). Die obere Platte ist an ihren Seitenflächen seitlich geführt (`Displacement` mit x = 0 und z = 0, y frei).
- Vorspannkraft: 29,6 kN
- Betriebskraft: 10 kN nach oben an den vier Seitenflächen der oberen Platte
- Reibungszahl: 0,12

## Schritt für Schritt

### 1. Kontakte einstellen

Nach dem Import sind alle Kontakte Verbund. Mit Verbund zwischen den Platten trägt die Schraube fast nichts, weil die verklebte Fuge die Last selbst überträgt.

<div class="steps" markdown="1" data-kategorie="Verbindungen" data-titel="Kontakte für eine vorgespannte Schraube einstellen">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Trennfuge zwischen den Platten: Reibung</p>
    <p><code>Strukturbaum → Connections → Contacts</code>, den Kontakt zwischen den Platten auswählen, <code>Detailfenster → Type: Frictional</code>, <code>Friction Coefficient: 0,12</code></p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Kopfauflage: Reibung</p>
    <p>Den Kontakt zwischen Schraubenkopf und oberer Platte genauso einstellen.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Mutter: Verbund lassen</p>
    <p>Zwischen Mutter und unterer Platte bewegt sich in diesem Lastfall nichts. Der Verbund hält die Schraube an ihrem Platz, damit sie in der Rechnung nicht wegrutschen kann.</p>
  </div>

</div>

### 2. Zwei Lastschritte anlegen

<div class="steps" markdown="1" data-kategorie="Belastung" data-titel="Zwei Lastschritte anlegen">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Zahl der Lastschritte auf 2 stellen</p>
    <p><code>Strukturbaum → Analysis Settings</code>, dann <code>Detailfenster → Step Controls → Number Of Steps: 2</code></p>
  </div>

</div>

- Schritt 1: nur vorspannen
- Schritt 2: Vorspannung sperren und die Betriebskraft aufbringen

### 3. Schraube vorspannen

<div class="steps" markdown="1" data-kategorie="Belastung" data-titel="Schraube vorspannen (Bolt Pretension)">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Bolt Pretension einfügen</p>
    <p>Die Mantelfläche des Schafts auswählen, dann <code>Rechtsklick Strukturbaum Static Structural → Insert → Bolt Pretension</code></p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Schritt 1: Vorspannkraft</p>
    <p><code>Detailfenster → Define By: Load</code>, <code>Preload: 29600 N</code></p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Schritt 2: sperren</p>
    <p>Im Fenster <code>Tabular Data</code> in der Zeile für Schritt 2 unter <code>Define By</code> den Eintrag <code>Lock</code> wählen.</p>
  </div>

</div>

<!-- ENTWURF: Im Pool prüfen, ob Mechanical Schritt 2 von selbst auf Lock stellt und wo genau Define By je Schritt gewählt wird. -->

!!! info "Warum sperren?"
    - `Load` hält die Schraubenkraft auf dem eingetragenen Wert fest.
    - `Lock` friert die Dehnung der Schraube ein. Erst dann kann die Schraubenkraft unter der Betriebskraft steigen.

### 4. Betriebskraft aufbringen

<div class="steps" markdown="1" data-kategorie="Belastung" data-titel="Kraft erst im zweiten Lastschritt aufbringen">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Kraft einfügen</p>
    <p>Die vier Seitenflächen der oberen Platte auswählen, dann <code>Rechtsklick Strukturbaum Static Structural → Insert → Force</code>, <code>Detailfenster → Define By: Components</code></p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Kraft je Lastschritt eintragen</p>
    <p>Im Fenster <code>Tabular Data</code> für die y-Komponente: Schritt 1 = 0 N, Schritt 2 = 10000 N</p>
  </div>

</div>

### 5. Lösen

`Solve`. Die Rechnung ist wegen der Reibkontakte nichtlinear und dauert länger als die bisherigen Übungen.

<!-- ENTWURF: Rechenzeit auf einem Pool-PC eintragen. -->

### 6. Auswerten

<div class="steps" markdown="1" data-kategorie="Auswertung" data-titel="Schraubenkraft und Kontaktdruck auswerten">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Schraubenkraft</p>
    <p><code>Rechtsklick Strukturbaum Solution → Insert → Probe → Bolt Pretension</code>. <code>Working Load</code> zeigt in Schritt 2 die Kraft in der Schraube. In Schritt 1 steht dort 0, das ist kein Fehler.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Druck in der Trennfuge</p>
    <p><code>Rechtsklick Strukturbaum Solution → Insert → Contact Tool</code>, darin <code>Pressure</code>. Unter <code>Detailfenster → Display Time</code> zwischen Schritt 1 und Schritt 2 wechseln.</p>
  </div>

</div>

!!! check "Kontrolle"
    | Größe | nach Schritt 1 | nach Schritt 2 |
    |---|---|---|
    | Schraubenkraft | 29,6 kN (eingetragen) | Wert folgt |
    | Zusatzkraft aus 10 kN Betriebskraft | | Wert folgt |
    | größter Druck in der Trennfuge | Wert folgt | Wert folgt |

    Aus dem Verspannungsschaubild: Die Schraube bekommt höchstens rund 1,7 kN der 10 kN ab.

## Verständnis

### Wie viel der Betriebskraft kommt in der vorgespannten Schraube an?

<div class="multiple-choice-question" data-correct="C" data-points="5" data-attempts="2" data-hints="Vergleichen Sie Working Load in Schritt 2 mit der Vorspannkraft.">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="p5s1_a" name="p5s1">
      <label for="p5s1_a">Die ganze Betriebskraft</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="p5s1_b" name="p5s1">
      <label for="p5s1_b">Etwa die Hälfte</label>
    </div>
    <div class="mc-option" data-value="C">
      <input type="checkbox" id="p5s1_c" name="p5s1">
      <label for="p5s1_c">Nur ein kleiner Teil, der Rest entlastet die Platten</label>
    </div>
  </div>
</div>

### Was passiert, wenn in Schritt 2 `Load` statt `Lock` steht?

<div class="multiple-choice-question" data-correct="B" data-points="5" data-attempts="2" data-hints="Load hält die Kraft in der Schraube fest, Lock die Dehnung.">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="p5s2_a" name="p5s2">
      <label for="p5s2_a">Die Vorspannung geht verloren</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="p5s2_b" name="p5s2">
      <label for="p5s2_b">Die Schraubenkraft bleibt bei 29,6 kN, die Zusatzkraft aus dem Betrieb erscheint nicht</label>
    </div>
    <div class="mc-option" data-value="C">
      <input type="checkbox" id="p5s2_c" name="p5s2">
      <label for="p5s2_c">Die Rechnung bricht ab</label>
    </div>
  </div>
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images" markdown="1">

🎯 <strong>Lösung</strong>

**Drei typische Fehler und woran man sie erkennt**

| Fehler | Was man sieht |
|---|---|
| Verbund zwischen den Platten gelassen | Die Schraubenkraft ändert sich unter der Betriebskraft fast nicht, die Fuge bleibt überall zu |
| in Schritt 2 `Load` statt `Lock` | Die Schraubenkraft bleibt genau bei 29,6 kN |
| Vorspannung und Betriebskraft im selben Lastschritt | Die Schraubenkraft passt nicht zum Verspannungsschaubild |

<!-- ENTWURF: Bilder aus dem Pool ergänzen (Druck in der Trennfuge nach Schritt 1 und nach Schritt 2). -->

</div>
