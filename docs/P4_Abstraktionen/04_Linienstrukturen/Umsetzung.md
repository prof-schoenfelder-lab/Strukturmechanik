---
icon: material/alpha-a-box
hide:
  - toc
---

# Umsetzung von BEAM-Elementen in ANSYS

Linienstrukturen mit BEAM-Elementen können auf zwei Arten erstellt werden:

1. Linie erstellen und Profil zuweisen
2. Vorhandene Geometrie in eine Linienstruktur umwandeln (Profil wird automatisch zugeordnet)

## Variante 1: Linie erstellen und Profil zuweisen (SpaceClaim)

<!-- --8<-- [start:Linienstruktur_erstellen] -->
<figure style="text-align:left;">
    <img src="../images/SpaceClaim1.png" alt="Balken in SpaceClaim erstellen" width="800">
</figure>

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Linie zeichnen</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Linie auswählen und im Reiter <code>Prepare</code> unter <code>Profiles</code> das gewünschte Profil zuweisen</p>
  </div>

</div>
<!-- --8<-- [end:Linienstruktur_erstellen] -->

## Variante 2: Vorhandene Geometrie in Linienstruktur umwandeln (SpaceClaim)

<!-- --8<-- [start:Linienstruktur_umwandeln] -->

Diese Option ist besonders praktisch wenn man bereits viele Linienstrukturen hat und diese schnell mit BEAM Elementen modellieren möchte.

<figure style="text-align:left;">
    <img src="../images/SpaceClaim2.png" alt="Balken in SpaceClaim erstellen mit Extract" width="800">
</figure>

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Volumenkörper muss vorhanden sein</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Im Reiter <code>Prepare</code> auf <code>Extract</code> klicken und den Volumenkörper auswählen</p>
  </div>

</div>
<!-- --8<-- [end:Linienstruktur_umwandeln] -->

!!! info "Ab hier ist das weitere Vorgehen für beide Varianten gleich"

## Profilgeometrie anpassen

<!-- --8<-- [start:ProfilAnpassen] -->
In Mechanical im Strukturbaum unter <code>Cross Sections</code> das jeweilige `Profil` auswählen und im Detailfenster unter <code>Dimensions</code> die Größe anpassen.

<figure style="text-align:left;">
    <img src="../images/Mechanical1.png" alt="Einstellung Mechanical 1" width="300">
</figure>
<!-- --8<-- [end:ProfilAnpassen] -->

## Elementdarstellung (nur optisch, also optional)

<!-- --8<-- [start:Elementdarstellung] -->
In Mechanical im Strukturbaum `Mesh` auswählen und in der Menüleiste oben im Reiter <code>Display</code> den Eintrag <code>Thick Shells and Beams</code> auswählen.

<figure style="text-align:left;">
    <img src="../images/Mechanical2.png" alt="Thick Shells and Beams" width="700">
</figure>

Im Netz werden die BEAM-Elemente dann mit ihrem Querschnitt dargestellt (statt nur als Linie).
<!-- --8<-- [end:Elementdarstellung] -->

## Ergebnisdarstellung (nur optisch, aber empfohlen)

<!-- --8<-- [start:Ergebnisdarstellung] -->
In Mechanical im Strukturbaum `Solution` auswählen und im Detailfenster den Eintrag <code>Beam Section Results</code> auf <code>Yes</code> stellen.

<figure style="text-align:left;">
    <img src="../images/Mechanical3.png" alt="Beam Section Results" width="400">
</figure>

Die Ergebnisse werden dann auf den Querschnitt gemappt (für Standardprofile), wodurch die Ergebnisdarstellung den bisherigen 3D-Analysen ähnlicher wird.
<!-- --8<-- [end:Ergebnisdarstellung] -->

## Randbedingungen

<!-- --8<-- [start:Randbedingungen] -->
Durch den zusätzlichen Rotationsfreiheitsgrad setzt ein `Fixed Support` jetzt sowohl die Verschiebungen als auch die Rotationen auf Null.  

Außerdem muss ggf. mit dem Lagerungstyp `Fixed Rotation` darauf geachtet werden, dass Bauteile nicht unerwünscht um ihre Längsachse rotieren (Starrkörperbewegung verhindern).

<figure style="text-align:left;">
    <img src="../images/FixedRotation.png" alt="Fixed Rotation" width="500">
</figure>

Im Detailfenster können dort die entsprechenden Rotationsachsen wieder freigegeben werden wenn gewünscht.
<!-- --8<-- [end:Randbedingungen] -->
