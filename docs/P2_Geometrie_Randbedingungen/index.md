---
title: Geometrieaufbereitung und Randbedingungen
icon: material/cube
hide:
  - toc
---

# Geometrieaufbereitung und Randbedingungen


!!! abstract "Lernziele"


    - [ ] Kennenlernen der grundlegenden Methoden zur Veränderung und Vereinfachung von CAD Geometrien mit SpaceClaim 
    - [ ] Kennenlernen der möglichen Lagerungs- und Belastungsmethoden in ANSYS Mechanical


## Geometrieanpassungen

<div class="prakt-list">
  <a class="prakt-row" href="01_Geometrie_anpassen/Move/">
    <span class="prakt-body">
      <span class="prakt-title">Längen & Positionen ändern</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="01_Geometrie_anpassen/images/Laenge_aendern.gif" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="01_Geometrie_anpassen/Pull/">
    <span class="prakt-body">
      <span class="prakt-title">Radius ändern</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="01_Geometrie_anpassen/images/Radius_aendern.gif" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="01_Geometrie_anpassen/Uebung-1/">
    <span class="prakt-body">
      <span class="prakt-title">Übung 1</span>
      <span class="prakt-desc">L-Profil verlängern und verrunden</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="01_Geometrie_anpassen/images/Uebung-01.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="01_Geometrie_anpassen/Split/">
    <span class="prakt-body">
      <span class="prakt-title">Flächen teilen für Randbedingungen</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="01_Geometrie_anpassen/images/Flaeche_erstellen.gif" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="01_Geometrie_anpassen/SplitBody/">
    <span class="prakt-body">
      <span class="prakt-title">Körper teilen</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="01_Geometrie_anpassen/images/Koerper_teilen.gif" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="01_Geometrie_anpassen/Blend/">
    <span class="prakt-body">
      <span class="prakt-title">Übergänge erstellen</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="01_Geometrie_anpassen/images/Blend.gif" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="01_Geometrie_anpassen/Uebung-2/">
    <span class="prakt-body">
      <span class="prakt-title">Übung 2</span>
      <span class="prakt-desc">Wanddicke am Lenker erhöhen</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="01_Geometrie_anpassen/images/Uebung-02.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="01_Geometrie_anpassen/Vereinfachungen/">
    <span class="prakt-body">
      <span class="prakt-title">Vereinfachungen</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="01_Geometrie_anpassen/images/Select_same_volume_and_Delete.gif" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="01_Geometrie_anpassen/Combine/">
    <span class="prakt-body">
      <span class="prakt-title">Körper zusammenfügen</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="01_Geometrie_anpassen/images/Koerper_zusammenfuegen.gif" alt="">
    <span class="prakt-arrow">→</span>
  </a>
</div>


## Lagerungen

<div class="prakt-list">
  <a class="prakt-row" href="02_Lagerungen/Einfuehrung/">
    <span class="prakt-body">
      <span class="prakt-title">Einführung</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="02_Lagerungen/images/Starrkoerperbewegungen.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="02_Lagerungen/Displacement/">
    <span class="prakt-body">
      <span class="prakt-title">Lager</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="02_Lagerungen/images/Lager.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="02_Lagerungen/Uebung-3/">
    <span class="prakt-body">
      <span class="prakt-title">Übung 3</span>
      <span class="prakt-desc">Lagerungsbeispiel Lineal über Kante belastet</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="02_Lagerungen/images/Lagerungsbeispiel_Lineal.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="02_Lagerungen/RemoteDisplacement/">
    <span class="prakt-body">
      <span class="prakt-title">externe Lager</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="02_Lagerungen/images/FixedSupport_vs_RemoteDisplacement.excalidraw.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="02_Lagerungen/Uebung-4/">
    <span class="prakt-body">
      <span class="prakt-title">Übung 4</span>
      <span class="prakt-desc">Externe Lagerung am Fahrradrahmen</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="02_Lagerungen/images/Uebung-04.excalidraw.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="02_Lagerungen/Cylindrical/">
    <span class="prakt-body">
      <span class="prakt-title">zylindrische Lager</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="02_Lagerungen/images/Radial_Axial_Tangential.excalidraw.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="02_Lagerungen/Elastic/">
    <span class="prakt-body">
      <span class="prakt-title">elastische Lager</span>
    </span>
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="02_Lagerungen/Uebung-5/">
    <span class="prakt-body">
      <span class="prakt-title">Übung 5</span>
      <span class="prakt-desc">vereinfachte Fahrradbremse (V-Brake)</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="02_Lagerungen/images/Uebung-05.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="02_Lagerungen/Uebung-6/">
    <span class="prakt-body">
      <span class="prakt-title">Übung 6</span>
      <span class="prakt-desc">Vergleich verschiedener Lagerungsbedingungen am Beispiel des Inbus</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="02_Lagerungen/images/Uebung-06.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
</div>


## Belastungen

<div class="prakt-list">
  <a class="prakt-row" href="03_Belastungen/DisplacementLoad/">
    <span class="prakt-body">
      <span class="prakt-title">Verschiebungen als Last</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="03_Belastungen/images/Verschiebung_Kraft.excalidraw.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="03_Belastungen/Force/">
    <span class="prakt-body">
      <span class="prakt-title">Kräfte</span>
    </span>
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="03_Belastungen/RemoteForce/">
    <span class="prakt-body">
      <span class="prakt-title">externe Kräfte</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="03_Belastungen/images/RemoteForce_Fahrradbeispiel.excalidraw.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="03_Belastungen/Uebung-7/">
    <span class="prakt-body">
      <span class="prakt-title">Übung 7</span>
      <span class="prakt-desc">Lenkkopfsteifigkeit Fahrradrahmen</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="03_Belastungen/images/Uebung-07.excalidraw.png" alt="">
    <span class="prakt-arrow">→</span>
  </a>
  <a class="prakt-row" href="03_Belastungen/Pressure/">
    <span class="prakt-body">
      <span class="prakt-title">Druck</span>
    </span>
    <span class="prakt-arrow">→</span>
  </a>
</div>
