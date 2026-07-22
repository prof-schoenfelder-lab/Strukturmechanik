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

<div class="prakt-list">
  <a class="prakt-row" href="01_Symmetrie/Symmetrie/">
    <span class="prakt-body">
      <span class="prakt-title">Symmetrie</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="01_Symmetrie/images/SymmetrieBsp-Symmetrie-Lagerung.excalidraw.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="01_Symmetrie/Umsetzung/">
    <span class="prakt-body">
      <span class="prakt-title">Umsetzung</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="01_Symmetrie/images/ANSYS_Symmetrie1.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="01_Symmetrie/Uebung01/">
    <span class="prakt-body">
      <span class="prakt-title">Übung 1</span>
      <span class="prakt-desc">Zweiseitig gelagerter Balken mit Flächenlast</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="01_Symmetrie/images/Uebung01.excalidraw.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="01_Symmetrie/Uebung02/">
    <span class="prakt-body">
      <span class="prakt-title">Übung 2</span>
      <span class="prakt-desc">Kragarm mit Einzelkraft</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="01_Symmetrie/images/Uebung02.excalidraw.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
</div>


## 2D — Ebener Spannungszustand (Plane Stress)

<div class="prakt-list">
  <a class="prakt-row" href="02_ESZ/EbenerSpannungszustand/">
    <span class="prakt-body">
      <span class="prakt-title">2D Ebener Spannungszustand</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="02_ESZ/images/2D_ebener_Spannungszustand.excalidraw.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="02_ESZ/Umsetzung/">
    <span class="prakt-body">
      <span class="prakt-title">Umsetzung</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="02_ESZ/images/SpaceClaim1.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="02_ESZ/Uebung01-2D/">
    <span class="prakt-body">
      <span class="prakt-title">Übung 1</span>
      <span class="prakt-desc">Zweiseitig gelagerter Balken mit Flächenlast</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="01_Symmetrie/images/Uebung01.excalidraw.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="02_ESZ/Uebung02-2D/">
    <span class="prakt-body">
      <span class="prakt-title">Übung 2</span>
      <span class="prakt-desc">Kragarm mit Einzelkraft</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="01_Symmetrie/images/Uebung02.excalidraw.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
</div>


## 2D — Rotationssymmetrie

<div class="prakt-list">
  <a class="prakt-row" href="03_Rotationssymmetrie/Rotationssymmetrie/">
    <span class="prakt-body">
      <span class="prakt-title">2D Rotationssymmetrie</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="03_Rotationssymmetrie/images/rotationssymmetrie.excalidraw.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="03_Rotationssymmetrie/Umsetzung/">
    <span class="prakt-body">
      <span class="prakt-title">Umsetzung</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="02_ESZ/images/SpaceClaim1.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="03_Rotationssymmetrie/Uebung03/">
    <span class="prakt-body">
      <span class="prakt-title">Übung 3</span>
      <span class="prakt-desc">Kugel-Ring Versuch</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="03_Rotationssymmetrie/images/KugelRing.excalidraw.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
</div>


## Linienstrukturen (BEAM-Elemente)

<div class="prakt-list">
  <a class="prakt-row" href="04_Linienstrukturen/Linienstrukturen/">
    <span class="prakt-body">
      <span class="prakt-title">1D Linienstrukturen (BEAM)</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="04_Linienstrukturen/images/Linienstrukur.excalidraw.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="04_Linienstrukturen/Umsetzung/">
    <span class="prakt-body">
      <span class="prakt-title">Umsetzung</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="04_Linienstrukturen/images/SpaceClaim1.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="04_Linienstrukturen/Uebung01-BEAM/">
    <span class="prakt-body">
      <span class="prakt-title">Übung 1-BEAM</span>
      <span class="prakt-desc">Zweiseitig gelagerter Balken mit Flächenlast</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="02_ESZ/images/Uebung01-2D.excalidraw.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
</div>


## Flächenstrukturen (SHELL-Elemente)

<div class="prakt-list">
  <a class="prakt-row" href="05_Flaechenstrukturen/Flaechenstrukturen/">
    <span class="prakt-body">
      <span class="prakt-title">2D Flächenstrukturen (SHELL)</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="05_Flaechenstrukturen/images/SHELL.excalidraw.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="05_Flaechenstrukturen/Umsetzung/">
    <span class="prakt-body">
      <span class="prakt-title">Umsetzung</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="05_Flaechenstrukturen/images/SpaceClaim.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="05_Flaechenstrukturen/Uebung04/">
    <span class="prakt-body">
      <span class="prakt-title">Übung 4</span>
      <span class="prakt-desc">Durchbiegung von Photovoltaikwafern im Carrier</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="05_Flaechenstrukturen/images/Uebung04.excalidraw.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
</div>
