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

<div class="prakt-cards">
  <a class="prakt-card" href="01_Geometrie_anpassen/Move/">
    <img class="prakt-cimg no-lightbox" src="01_Geometrie_anpassen/images/Laenge_aendern.gif" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Längen & Positionen ändern</span>
    </span>
  </a>
  <a class="prakt-card" href="01_Geometrie_anpassen/Pull/">
    <img class="prakt-cimg no-lightbox" src="01_Geometrie_anpassen/images/Radius_aendern.gif" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Radius ändern</span>
    </span>
  </a>
  <a class="prakt-card" href="01_Geometrie_anpassen/Uebung-1/">
    <img class="prakt-cimg no-lightbox" src="01_Geometrie_anpassen/images/Uebung-01.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Übung 1</span>
      <span class="prakt-cdesc">L-Profil verlängern und verrunden</span>
    </span>
  </a>
  <a class="prakt-card" href="01_Geometrie_anpassen/Split/">
    <img class="prakt-cimg no-lightbox" src="01_Geometrie_anpassen/images/Flaeche_erstellen.gif" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Flächen teilen für Randbedingungen</span>
    </span>
  </a>
  <a class="prakt-card" href="01_Geometrie_anpassen/SplitBody/">
    <img class="prakt-cimg no-lightbox" src="01_Geometrie_anpassen/images/Koerper_teilen.gif" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Körper teilen</span>
    </span>
  </a>
  <a class="prakt-card" href="01_Geometrie_anpassen/Blend/">
    <img class="prakt-cimg no-lightbox" src="01_Geometrie_anpassen/images/Blend.gif" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Übergänge erstellen</span>
    </span>
  </a>
  <a class="prakt-card" href="01_Geometrie_anpassen/Uebung-2/">
    <img class="prakt-cimg no-lightbox" src="01_Geometrie_anpassen/images/Uebung-02.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Übung 2</span>
      <span class="prakt-cdesc">Wanddicke am Lenker erhöhen</span>
    </span>
  </a>
  <a class="prakt-card" href="01_Geometrie_anpassen/Vereinfachungen/">
    <img class="prakt-cimg no-lightbox" src="01_Geometrie_anpassen/images/Select_same_volume_and_Delete.gif" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Vereinfachungen</span>
    </span>
  </a>
  <a class="prakt-card" href="01_Geometrie_anpassen/Combine/">
    <img class="prakt-cimg no-lightbox" src="01_Geometrie_anpassen/images/Koerper_zusammenfuegen.gif" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Körper zusammenfügen</span>
    </span>
  </a>
</div>


## Lagerungen

<div class="prakt-cards">
  <a class="prakt-card" href="02_Lagerungen/Einfuehrung/">
    <img class="prakt-cimg no-lightbox" src="02_Lagerungen/images/Starrkoerperbewegungen.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Einführung</span>
    </span>
  </a>
  <a class="prakt-card" href="02_Lagerungen/Displacement/">
    <img class="prakt-cimg no-lightbox" src="02_Lagerungen/images/Lager.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Lager</span>
    </span>
  </a>
  <a class="prakt-card" href="02_Lagerungen/Uebung-3/">
    <img class="prakt-cimg no-lightbox" src="02_Lagerungen/images/Lagerungsbeispiel_Lineal.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Übung 3</span>
      <span class="prakt-cdesc">Lagerungsbeispiel Lineal über Kante belastet</span>
    </span>
  </a>
  <a class="prakt-card" href="02_Lagerungen/RemoteDisplacement/">
    <img class="prakt-cimg no-lightbox" src="02_Lagerungen/images/FixedSupport_vs_RemoteDisplacement.excalidraw.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">externe Lager</span>
    </span>
  </a>
  <a class="prakt-card" href="02_Lagerungen/Uebung-4/">
    <img class="prakt-cimg no-lightbox" src="02_Lagerungen/images/Uebung-04.excalidraw.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Übung 4</span>
      <span class="prakt-cdesc">Externe Lagerung am Fahrradrahmen</span>
    </span>
  </a>
  <a class="prakt-card" href="02_Lagerungen/Cylindrical/">
    <img class="prakt-cimg no-lightbox" src="02_Lagerungen/images/Radial_Axial_Tangential.excalidraw.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">zylindrische Lager</span>
    </span>
  </a>
  <a class="prakt-card" href="02_Lagerungen/Elastic/">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">elastische Lager</span>
    </span>
  </a>
  <a class="prakt-card" href="02_Lagerungen/Uebung-5/">
    <img class="prakt-cimg no-lightbox" src="02_Lagerungen/images/Uebung-05.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Übung 5</span>
      <span class="prakt-cdesc">vereinfachte Fahrradbremse (V-Brake)</span>
    </span>
  </a>
  <a class="prakt-card" href="02_Lagerungen/Uebung-6/">
    <img class="prakt-cimg no-lightbox" src="02_Lagerungen/images/Uebung-06.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Übung 6</span>
      <span class="prakt-cdesc">Vergleich verschiedener Lagerungsbedingungen am Beispiel des Inbus</span>
    </span>
  </a>
</div>


## Belastungen

<div class="prakt-cards">
  <a class="prakt-card" href="03_Belastungen/DisplacementLoad/">
    <img class="prakt-cimg no-lightbox" src="03_Belastungen/images/Verschiebung_Kraft.excalidraw.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Verschiebungen als Last</span>
    </span>
  </a>
  <a class="prakt-card" href="03_Belastungen/Force/">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Kräfte</span>
    </span>
  </a>
  <a class="prakt-card" href="03_Belastungen/RemoteForce/">
    <img class="prakt-cimg no-lightbox" src="03_Belastungen/images/RemoteForce_Fahrradbeispiel.excalidraw.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">externe Kräfte</span>
    </span>
  </a>
  <a class="prakt-card" href="03_Belastungen/Uebung-7/">
    <img class="prakt-cimg no-lightbox" src="03_Belastungen/images/Uebung-07.excalidraw.png" alt="">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Übung 7</span>
      <span class="prakt-cdesc">Lenkkopfsteifigkeit Fahrradrahmen</span>
    </span>
  </a>
  <a class="prakt-card" href="03_Belastungen/Pressure/">
    <span class="prakt-cbody">
      <span class="prakt-ctitle">Druck</span>
    </span>
  </a>
</div>
