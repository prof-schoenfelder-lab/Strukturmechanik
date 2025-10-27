---
hide:
 - toc
---

# Wanddicke am Lenker erhöhen

Als zweites Beispiel verwenden wir den Lenker aus dem ersten Praktikum und wollen hier die Wandstärke um 2 mm erhöhen.

<figure style="text-align:center;">
  <img src="../images/Uebung-02b.png" alt="Lenker" width="700" class="no-lightbox">
</figure>

## Gegeben

Es ist das gesamte Projektarchiv gegeben (Material,Geometrie,Netz,Lagerung und Belastung):

[:material-paperclip: Uebung-02.wbpz](assets/Uebung-02.wbpz)

## Aufgabenstellung

Nach dem Import der Archivdatei öffnen Sie die Geometrie mit SpaceClaim und ändern die Geometrie wie folgt:

- [ ] Erhöhen Sie die Wanddicke im gesamten Lenker um 2mm (Innenradius um 2mm verkleinern)

## Hinweise

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2"><code>SpaceClaim</code>:  Körper an Übergangsstellen mit  <code>Split</code>  auftrennen und Übergang entfernen</p>
    <p>Im Übergangsbereich kann die Wandstärke nicht geändert werden (weil diese auf beiden Seiten auch unterschiedlich ist). Trennen Sie die Übergangsbereiche auf mit <code>Split</code>  und löschen Sie diesen und erzeugen Sie den Übergang nach der Anpassung der Wandstärke erneut</p>
    <figure style="text-align:center;">
    <img src="../images/Uebung-02c.png" alt="Lenker" width="600" class="no-lightbox">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2"><code>SpaceClaim</code>: Wanddicken um  2mm erhöhen</p>
    <p>Mit dem <code>Pull</code> Tool die Wandstärken um 2 mm erhöhen (Innenradius 2 mm kleiner).</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2"><code>SpaceClaim</code>: Übergangsbereiche erstellen</p>
    <p>Mit dem <code>Blend</code> Tool die Übergangsbereiche wieder erstellen</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2"><code>SpaceClaim</code>: Flächen für Randbedingungen erstellen</p>
    <p>Mit <code>Ebenen</code> und dem <code>Move</code> Tool und <code>Split</code> Tool die Flächen für die Randbedingungen neu erstellen. Für den mittleren Bereich die Ebenen durch anklicken der x-Achse erstellen.</p>
    <figure style="text-align:center;">
    <img src="../images/Uebung-02d.png" alt="Lenker" width="600" class="no-lightbox">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2"><code>Workbench Projektmenü</code>: Geometrie neu reinladen</p>
    <p><code>Rechtsklick</code> auf <code>Model</code> > <code>Update</code></p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2"><code>Mechanical</code>: Material neu zuordnen</p>
    <p>Im Strukturbaum: <code>Geometry</code> > <code>Lenker</code> anklicken und im Detailfenster unter <code>Asssignment</code> das Material <code>Alu</code> zuweisen</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2"><code>Mechanical</code>: Flächen in Randbedingungen wieder hinzufügen</p>
    <p></p>
      <figure style="text-align:center;">
    <img src="../images/Uebung-02Geometryzuordnung.gif" alt="Randbedingung Geometriezuordnung" width="800" class="no-lightbox">
    </figure>
  
  </div>

</div>

## Gesucht

Berechnen Sie anschließend die folgenden Größen:

### Die maximale Durchbiegung $u_{\max }$ in mm

<div class="numeric-question" data-answer="11.305" data-tolerance="0.5" data-points="5" data-attempts="5"  data-hints="Einheit auf mm gewechselt?">
</div>
