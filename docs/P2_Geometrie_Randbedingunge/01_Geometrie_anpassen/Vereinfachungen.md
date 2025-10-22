---
icon: material/close-circle
hide:
  - toc
---

# Geometrien vereinfachen

Oft haben Geometrien nicht benötige Teile oder Features (z.B.  Bohrungen oder Kantenverrundungen) die nicht benötigt werden. In SpaceClaim gibt es dazu eine Funktion die ähnliche Geometrien (Volumen/Flächen/..) auswählen lässt und sich damit auch große Baugruppen leicht entrümpeln lassen.

## Beispielgeometrie Fahrradrahmen

Wir starten in diese Fall mit einer Step Datei eines Fahrradrahmens:

<figure style="text-align:center;">
    <img src="../images/Trekkingrahmen.png" alt="Trekkingrahmen" width="300">
</figure>

[:material-paperclip: TrekkingRahmen_Original_v2.stp](../assets/TrekkingRahmen_Original_v2.stp)

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2"><code>Workbench Projektmenü</code>: Neue Strukturmechanische Analyse hinzufügen</p>
    <p>Im Workbench Projektmenü in der Liste der Analysen <code>Doppelklick</code> auf <code>Static Structural</code></p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2"><code>Workbench Projektmenü</code>: Geometrie importieren</p>
    <p>In der neuen Analyse <code>Rechtsklick</code> auf <code>Geometry</code> > <code>Import</code> und geladene Datei auswählen</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2"><code>Workbench Projektmenü</code>: Geometrie mit SpaceClaim bearbeiten</p>
    <p>In der neuen Analyse <code>Rechtsklick</code> auf <code>Geometry</code> > <code>Edit with SpaceClaim...</code> auswählen</p>
  </div>

</div>

## Unnötige Teile löschen mit `Select`

- [ ] Löschen Sie alle nicht benötigten Kleinteile aus der Geometrie (Anleitung siehe unten)

!!! hint "Hinweis zum Selektieren von Volumenkörpern"

    Allgemein kann man mit 3x <code>Anklicken einer Fläche</code> das gesamte Volumen selektieren.

<figure style="text-align:center;">
    <img src="../images/Kleinteile_entfernen.png" alt="Übersicht der zu entfernenden Teile" width="600">
</figure>

<figure style="text-align:center;">
    <img src="../images/Select_same_volume_and_Delete.gif" alt="gleiche Körper entfernen" width="800">
</figure>

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Volumenkörper (Body) auswählen</p>
    <p>In der Menüleiste <code>Select</code> auswählen und 3x auf eine Fläche des zu löschenden Objektes wählen</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Volumenkörper mit gleichem Volumen auswählen</p>
    <p>In der Seitenleiste den Tab <code>Selection</code> auswählen und auf <code>All Bodies with volume ...</code> klicken</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Alle selektierten Volumenkörper löschen</p>
    <p>Mit der Taste <code>ENTF</code> alle selektierten Volumenkörper löschen</p>
  </div>

</div>

## Unnötige Features löschen mit `Select`

- [ ] Entfernen Sie die Bohrungen im Steuerrohr

<figure style="text-align:center;">
    <img src="../images/Select_same_radius_and_Fill.gif" alt="gleiche Features entfernen" width="800">
</figure>

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Bohrungsfläche auswählen</p>
    <p>In der Menüleiste <code>Select</code> auswählen und Fläche einer Bohrung auswählen</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Flächen mit gleichem Radius auswählen</p>
    <p>In der Seitenleiste den Tab <code>Selection</code> auswählen und auf <code>Equal radius cylinder</code> klicken</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Alle selektierten Flächen füllen</p>
    <p>In der Menüleiste oben auf <code>Fill</code> klicken</p>
    <p>Hinweis: Mit der Taste <code>ENTF</code> kommt man zum gleichen Ergebnis</p>
  </div>

</div>