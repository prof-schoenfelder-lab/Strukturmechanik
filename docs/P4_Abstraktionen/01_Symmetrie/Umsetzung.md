---
icon: material/alpha-a-box
hide:
  - toc
---

# Umsetzung von Symmetrien in ANSYS

## Beta Optionen aktivieren

Folgende Einstellung der `Beta Optionen` im Workbench Projektmenü ermöglicht uns die Darstellung des Netzes und der Ergebnisse als Vollmodell. Diese einmal durchführen und ANSYS neustarten:

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2"><code>Workbench Projektmenü</code> In der Menüleiste  <code>Tools</code> und <code>Options</code>  auswählen</p>
    <figure style="text-align:center;">
    <img src="../images/ANSYS_Symmetrie4.png" alt="Options" width="600" class="no-lightbox">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Unter <code>Appearance</code> ganz nach unten scrollen und <code>Beta Options</code> auswählen und mit <code>OK</code> bestätigen</p>
    <figure style="text-align:center;">
    <img src="../images/ANSYS_Symmetrie5.png" alt="Options" width="700" class="no-lightbox">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2"><code>ANSYS Workbench 2024R2</code> neustarten</p>
  </div>

</div>

## Geometrie

<!-- --8<-- [start:Geometrie] -->
Wenn man bereits eine volle Geometrie hat kann man diese mit dem `Split Body` über Ebenen teilen ([Link zur Methodik](../../P2_Geometrie_Randbedingungen/01_Geometrie_anpassen/SplitBody.md)).

Wenn die Geometrie neu erstellt wird kann man natürlich gleich nur die Halb-/Viertel-/Achtelgeometrie erstellen.
<!-- --8<-- [end:Geometrie] -->


## Symmetrie

<!-- --8<-- [start:Symmetrie] -->
Zur Erstellung der Symmetrie-Randbedingungen:

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Symmetrieeintrag im Strukturbaum einfügen</p>
    <figure style="text-align:center;">
    <img src="../images/ANSYS_Symmetrie1.png" alt="Symmetrie im Strukturbaum einfügen" width="600" class="no-lightbox">
    </figure>
    <p>Im Strukturbaum <code>Rechtsklick</code> auf <code>Model</code> &gt; <code>Insert</code> &gt; <code>Symmetry</code></p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Symmetrie-Randbedingung einfügen</p>
    <figure style="text-align:center;">
    <img src="../images/ANSYS_Symmetrie2.png" alt="Symmetrieebene einfügen" width="600" class="no-lightbox">
    </figure>
    <p><code>Flächenauswahltool</code> auswählen und die <code>Symmetrieebene</code> auswählen.</p>
    <p>Im Strukturbaum <code>Rechtsklick</code> auf <code>Symmetry</code> &gt; <code>Insert</code> &gt; <code>Symmetry Region</code></p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Einstellungen zur Symmetrie-Randbedingung</p>
    <figure style="text-align:center;">
    <img src="../images/ANSYS_Symmetrie3.png" alt="Symmetrieebene einfügen" width="800" class="no-lightbox">
    </figure>
    <p>Im Detailfenster unter <code>Symmetry Normal</code> die Richtung auswählen, die <code>senkrecht auf der Symmetrieebene</code> steht.</p>
  </div>

</div>
<!-- --8<-- [end:Symmetrie] -->

## Darstellung von Netz & Lösung als Vollmodell

<!-- --8<-- [start:Darstellung] -->
Durch eingeschaltete Beta-Option (siehe oben), können wir das Netz und die Ergebnisse so spiegeln, als hätten wir das Vollmodell gerechnet.  

Dafür muss im Strukturbaum auf <code>Symmetry</code> geklickt werden und im Detailfenster eingestellt werden wie gespiegelt werden soll. 

- Es muss angegeben werden, wie oft gespiegelt wird (hier jeweils 2 Mal) mit der Methode <code>Half</code>.
- Es wird der Abstand senkrecht zur Symmetrieebene angegeben. Wenn die Symmetrieebene genau in der Koordinate 0 liegt muss einfach ein sehr kleiner Wert angegeben werden. Liegt die Symmetrieebene z.B. 20mm entfernt muss der Wert 20mm angegeben werden

<figure style="text-align:center;">
<img src="../images/Spiegelungseinstellung.png" alt="Spiegelungseinstellung" width="600" class="no-lightbox">
</figure>

Werden diese Einstellungen übernommen, wird das Viertelmodell (2 Symmetrieebenen) als Vollmodell im Netz und in den Lösungskonturen dargestellt.
<!-- --8<-- [end:Darstellung] -->
