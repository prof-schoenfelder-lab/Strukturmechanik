---
title: Abstraktionen
icon: material/video-2d
hide:
  - toc
---

# :material-video-2d: Abstraktionen

Um Rechenzeit zu sparen, sollte immer versucht werden, das Modell so weit wie möglich zu vereinfachen. Dabei gibt es drei typische Schritte:

1. Welcher Teil des Systems muss wirklich modelliert werden?
2. Welche Symmetrien kann ich ausnutzen?
3. Kann ich das Modell durch Reduzierung einer Dimension abstrahieren?


!!! abstract "Lernziele"


    - [ ] Möglichkeiten kennenlernen, Simulationsmodelle so aufzubauen, dass sie deutlich Rechenzeit sparen


## Symmetrien

<div class="prakt-cards">
  <a class="prakt-card" href="01_Symmetrie/Symmetrie/">
    <img class="prakt-cimg no-lightbox" src="01_Symmetrie/images/SymmetrieBsp-Symmetrie-Lagerung.excalidraw.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Symmetrie</span>
    </span>
  </a>
  <a class="prakt-card" href="01_Symmetrie/Umsetzung/">
    <img class="prakt-cimg no-lightbox" src="01_Symmetrie/images/ANSYS_Symmetrie1.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Umsetzung</span>
    </span>
  </a>
  <a class="prakt-card" href="01_Symmetrie/Uebung01/">
    <img class="prakt-cimg no-lightbox" src="01_Symmetrie/images/Uebung01.excalidraw.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Übung 1</span>
      <span class="prakt-cdesc">Zweiseitig gelagerter Balken mit Flächenlast</span>
    </span>
  </a>
  <a class="prakt-card" href="01_Symmetrie/Uebung02/">
    <img class="prakt-cimg no-lightbox" src="01_Symmetrie/images/Uebung02.excalidraw.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Übung 2</span>
      <span class="prakt-cdesc">Kragarm mit Einzelkraft</span>
    </span>
  </a>
</div>


## 2D — Ebener Spannungszustand (Plane Stress)

<div class="prakt-cards">
  <a class="prakt-card" href="02_ESZ/EbenerSpannungszustand/">
    <img class="prakt-cimg no-lightbox" src="02_ESZ/images/2D_ebener_Spannungszustand.excalidraw.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">2D Ebener Spannungszustand</span>
    </span>
  </a>
  <a class="prakt-card" href="02_ESZ/Umsetzung/">
    <img class="prakt-cimg no-lightbox" src="02_ESZ/images/SpaceClaim1.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Umsetzung</span>
    </span>
  </a>
  <a class="prakt-card" href="02_ESZ/Uebung01-2D/">
    <img class="prakt-cimg no-lightbox" src="01_Symmetrie/images/Uebung01.excalidraw.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Übung 1</span>
      <span class="prakt-cdesc">Zweiseitig gelagerter Balken mit Flächenlast</span>
    </span>
  </a>
  <a class="prakt-card" href="02_ESZ/Uebung02-2D/">
    <img class="prakt-cimg no-lightbox" src="01_Symmetrie/images/Uebung02.excalidraw.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Übung 2</span>
      <span class="prakt-cdesc">Kragarm mit Einzelkraft</span>
    </span>
  </a>
</div>


## 2D — Rotationssymmetrie

<div class="prakt-cards">
  <a class="prakt-card" href="03_Rotationssymmetrie/Rotationssymmetrie/">
    <img class="prakt-cimg no-lightbox" src="03_Rotationssymmetrie/images/rotationssymmetrie.excalidraw.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">2D Rotationssymmetrie</span>
    </span>
  </a>
  <a class="prakt-card" href="03_Rotationssymmetrie/Umsetzung/">
    <img class="prakt-cimg no-lightbox" src="02_ESZ/images/SpaceClaim1.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Umsetzung</span>
    </span>
  </a>
  <a class="prakt-card" href="03_Rotationssymmetrie/Uebung03/">
    <img class="prakt-cimg no-lightbox" src="03_Rotationssymmetrie/images/KugelRing.excalidraw.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Übung 3</span>
      <span class="prakt-cdesc">Kugel-Ring Versuch</span>
    </span>
  </a>
</div>


## Linienstrukturen (BEAM-Elemente)

<div class="prakt-cards">
  <a class="prakt-card" href="04_Linienstrukturen/Linienstrukturen/">
    <img class="prakt-cimg no-lightbox" src="04_Linienstrukturen/images/Linienstrukur.excalidraw.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">1D Linienstrukturen (BEAM)</span>
    </span>
  </a>
  <a class="prakt-card" href="04_Linienstrukturen/Umsetzung/">
    <img class="prakt-cimg no-lightbox" src="04_Linienstrukturen/images/SpaceClaim1.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Umsetzung</span>
    </span>
  </a>
  <a class="prakt-card" href="04_Linienstrukturen/Uebung01-BEAM/">
    <img class="prakt-cimg no-lightbox" src="02_ESZ/images/Uebung01-2D.excalidraw.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Übung 1-BEAM</span>
      <span class="prakt-cdesc">Zweiseitig gelagerter Balken mit Flächenlast</span>
    </span>
  </a>
</div>


## Flächenstrukturen (SHELL-Elemente)

<div class="prakt-cards">
  <a class="prakt-card" href="05_Flaechenstrukturen/Flaechenstrukturen/">
    <img class="prakt-cimg no-lightbox" src="05_Flaechenstrukturen/images/SHELL.excalidraw.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">2D Flächenstrukturen (SHELL)</span>
    </span>
  </a>
  <a class="prakt-card" href="05_Flaechenstrukturen/Umsetzung/">
    <img class="prakt-cimg no-lightbox" src="05_Flaechenstrukturen/images/SpaceClaim.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Umsetzung</span>
    </span>
  </a>
  <a class="prakt-card" href="05_Flaechenstrukturen/Uebung04/">
    <img class="prakt-cimg no-lightbox" src="05_Flaechenstrukturen/images/Uebung04.excalidraw.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Übung 4</span>
      <span class="prakt-cdesc">Durchbiegung von Photovoltaikwafern im Carrier</span>
    </span>
  </a>
</div>
