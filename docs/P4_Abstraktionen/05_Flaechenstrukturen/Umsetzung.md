---
icon: material/alpha-a-box
hide:
  - toc
---

# Umsetzung von SHELL-Elementen in ANSYS

Analog wie bei BEAM-Elementen können wir hier wieder über zwei Wege die Geometrie erstellen: 

1. Fläche direkt erstellen (Dicke wird in Mechanical eingestellt)
2. Vorhandene Geometrie in eine Flächentruktur umwandeln (Dicke wird automatisch bestimmt)

## Variante 1: Fläche erstellen (SpaceClaim)

<!-- --8<-- [start:Flaechen_erstellen] -->
In SpaceClaim Flächen in einer beliebigen Ebene erstellen

!!! warning "Im Workbench Projektmenü Analyse Typ **NICHT** ummstellen!"

<!-- --8<-- [end:Flaechen_erstellen] -->

## Variante 2: Vorhandene Geometrie in Flächenstruktur umwandeln (SpaceClaim)

<!-- --8<-- [start:Flaechen_ableiten] -->

Diese Option ist besonders praktisch wenn man bereits viele Flächenstrukturen hat und diese schnell mit SHELL Elementen modellieren möchte.
<figure style="text-align:left;">
    <img src="../images/SpaceClaim.png" alt="SHELL in SpaceClaim erstellen mit Extract" width="1000">
</figure>

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Volumenkörper muss vorhanden sein</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Im Reiter <code>Prepare</code> auf <code>Midsurface</code> klicken</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Im Detailfenster <code>Use Range</code> auswählen und Dickenbereich des Bauteils angeben</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Im Stukturbaum <code>Volumenkörper</code> auswählen (ggf. mehrere) und im Grafikfenster mit <code>OK</code> bestätigen</p>
  </div>

</div>
<!-- --8<-- [end:Flaechen_ableiten] -->

!!! info "Ab hier ist das weitere Vorgehen für beide Varianten gleich"

## Dicke einstellen

<!-- --8<-- [start:Dicke_einstellen] -->
In Mechanical im Strukturbaum die jeweilige <code>Fläche (Surface)</code> auswählen und im Detailfenster unter <code>Thickness</code> die Dicke einstellen.

<figure style="text-align:left;">
    <img src="../images/Dicke.png" alt="Einstellung Mechanical Dicke" width="400">
</figure>
<!-- --8<-- [end:Dicke_einstellen] -->

## Elementdarstellung (nur optisch, also optional)

<!-- --8<-- [start:Elementdarstellung] -->
Analog zum BEAM Element können wir hier auch die Darstellung einstellen:

In Mechanical im Strukturbaum `Mesh` auswählen und in der Menüleiste oben im Reiter <code>Display</code> den Eintrag <code>Thick Shells and Beams</code> auswählen.

<figure style="text-align:left;">
    <img src="../images/ThickShells.png" alt="Thick Shells and Beams" width="700">
</figure>

Im Netz werden die SHELL-Elemente dann mit Dicke dargestellt (statt nur als Fläche).
<!-- --8<-- [end:Elementdarstellung] -->

## Randbedingungen

<!-- --8<-- [start:Randbedingungen] -->
Analog zu den `BEAM` Elementen gilt auch hier:

Durch den zusätzlichen Rotationsfreiheitsgrad setzt ein `Fixed Support` jetzt sowohl die Verschiebungen als auch die Rotationen auf Null.  

Außerdem muss ggf. mit dem Lagerungstyp `Fixed Rotation` darauf geachtet werden, dass Bauteile nicht unerwünscht um ihre Längsachse rotieren (Starrkörperbewegung verhindern).

<figure style="text-align:left;">
    <img src="../../04_Linienstrukturen/images/FixedRotation.png" alt="Fixed Rotation" width="500">
</figure>

Im Detailfenster können dort die entsprechenden Rotationsachsen wieder freigegeben werden wenn gewünscht.
<!-- --8<-- [end:Randbedingungen] -->
