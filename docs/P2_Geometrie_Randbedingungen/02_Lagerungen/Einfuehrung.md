---
icon: material/information-variant-box
hide:
  - toc
sektion: Lagerungen
title: Einführung
order: 100
thumb: images/Starrkoerperbewegungen.png
---

# Einführung in Lagerungen

Lagerungen verhindern an definierten Orten der Geometrie eine Bewegungen in eine oder mehrere Richtung(en). Ziel ist es dabei immer möglichst die Lagerungen aus der Realität abzubilden und Starrkörperbewegungen zu verhindern.

<figure style="text-align:center;">
    <img src="../images/Starrkoerperbewegungen.png" alt="Beispiele von Starrkörperbewegungen" width="400">
</figure>


## Anbringen von Randbedingungen

<figure style="text-align:center;">
    <img src="../images/RB_add.gif" alt="Hinzufügen von Randbedingungen" width="700">
</figure>

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Geometrie auswählen</p>
    <p>Je nach Geometrie das jeweilige <code>Selektionstool anklicken</code> (Punkt/Kante/Fläche/Körper) und die <code>Geometrie selektrieren</code></p>
    <p>Mehrere Geometrien mit <code>STRG</code> gedrückt halten auswählen</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Randbedingungen hinzufügen</p>
    <p>Im Strukturbaum: <code>Rechtsklick</code> auf <code>Static Structural</code> > <code>Insert</code> und dann die jeweilige Randbedingung auswählen</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Randbedingungen Details bearbeiten</p>
    <p>Im Detailfenster: Details bearbeiten wie z.B. den Wert der Verschiebungen in die jeweilige Achse</p>
  </div>

</div>

## Geometrie austauschen

### Weg 1: über das Detailfenster neue ausgewählte Geometrie mit `Apply` bestätigen

!!! info inline
    
    Funktioniert auch für mehrere Geometrien (z.B. mehrere Flächen die über `STRG` selektiert worden)


<figure style="text-align:center;">
    <img src="../images/RB_Geo_change1.gif" alt="Geometrie bei Randbedingung tauschen" width="700">
</figure>

### Weg 2: Direkt im Grafikfenster Geometrie austauschen

!!! info inline
    
    Funktioniert nur mit einer Geometrie

<figure style="text-align:center;">
    <img src="../images/RB_Geo_change2.gif" alt="Geometrie bei Randbedingung tauschen" width="700">
</figure>

## Geometrie im Grafikfenster hinzufügen

<figure style="text-align:center;">
    <img src="../images/RB_Geo_add.gif" alt="Geometrie im Grafikfenster hinzufügen" width="700">
</figure>

## Geometrie im Grafikfenster entfernen

<figure style="text-align:center;">
    <img src="../images/RB_Geo_remove.gif" alt="Geometrie im Grafikfenster entfernen" width="700">
</figure>
## Konkret: Festlager anbringen

Die vollständige Klick-Anleitung — dieselbe findest du auch in der
[Anleitungen-Übersicht](../../../tutorials/):

<tutorial slug="festlager-anbringen"></tutorial>
