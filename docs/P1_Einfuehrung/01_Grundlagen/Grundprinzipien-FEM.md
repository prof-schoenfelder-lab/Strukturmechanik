---
title: Grundprinzip FEM
icon: material/atom
---

# Grundprinzipien der Finiten-Elemente-Methode

Im folgenden ist die Vorgehensweise der Finiten-Elemente-Methode an Hand des Workflows in grob skizziert.

<div class="steps">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Geometrie</p>
    <figure style="text-align:center;">
      <img src="../images/Geometrie.png" alt="Geometrie" width="300">
    </figure>
    <p>Zunächst wird ein <strong>Bauteil erstellt</strong> (in ANSYS) oder ein bereits vorhandenes Bauteil <strong>eingeladen</strong> (z. B. aus CATIA).</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Material</p>
    <figure style="text-align:center;">
      <img src="../images/Material.png" alt="Material" width="400">
    </figure>
    <p>Es muss ein Material gewählt werden. Relevante Parameter sind das <strong>Elastizitätsmodul E</strong> und die <strong>Querkontraktion μ</strong>.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Elemente (Vernetzung)</p>
    <figure style="text-align:center;">
      <img src="../images/Netz.png" alt="Vernetzung" width="300">
    </figure>
    <p>Das Bauteil wird mit kleinen (finiten) Elementen vernetzt.</p>
    <figure style="text-align:center;">
      <img src="../images/Element.png" alt="Element" width="200">
    </figure>
    <p>Die Elemente bestehen aus Knoten.</p>
    <figure style="text-align:center;">
      <img src="../images/Raumrichtungen.png" alt="Raumrichtungen" width="100">
    </figure>
    <p>Jeder Knoten besitzt <strong>Freiheitsgrade</strong> (in der Strukturmechanik mit den 3D Elementen sind dies Verschiebungen in alle drei Raumrichtungen) .</p>
 </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Lagerung und Belastung</p>
    <figure style="text-align:center;">
      <img src="../images/Randbedingungen.png" alt="Randbedingungen" width="500">
    </figure>
    <p>Die Lagerung verhindert Starrkörperbewegungen …</p>
    <p>Die Belastung erfolgt hier über eine Kraft auf die oberen drei Knoten.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Bestimmung der Freiheitsgrade</p>
    <p>Nun wird mit Hilfe von mathematischen Operationen die Freiheitsgrade (also Verschiebungen in alle 3 Raumrichtungen) für alle restlichen Knoten im Bauteil bestimmt.</p>
  </div>

</div>

Im folgenden Video wird dies noch mal etwas detallierter erklärt:

<iframe width="900" height="506" src="https://www.youtube.com/embed/GHjopp47vvQ?si=Nn-hbm2-wN2xcWhx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
