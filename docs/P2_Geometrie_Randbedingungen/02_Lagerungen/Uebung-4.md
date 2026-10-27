---
hide:
 - toc
sektion: Lagerungen
title: Übung 3
order: 140
kurz: Prüfstands-Dummies am Fahrradrahmen durch Remote Displacement ersetzen
thumb: images/Pruefstand_Rahmen.webp
---

<!-- ENTWURF (Zweig p2-uebung3-dummies): Archiv, Koordinatensysteme, Lagerung der Dummies und Sollwerte kommen von Felix (SM-35). Stellen mit TODO ersetzen. -->

# Prüfstands-Dummies durch Remote Displacement ersetzen

Im Prüfstand der HTWK sitzt der Fahrradrahmen nicht auf Rädern, sondern auf zwei **Dummies**: Vorne steckt ein steifer Gabeldummy, im Steuerrohr geklemmt und unten in einem Festlager gelagert. Hinten hält ein Achsdummy die Ausfallenden und stützt sich über ein Kugelgelenk ab.

<figure style="text-align:center;">
  <img src="../images/Pruefstand_Rahmen.webp" alt="Fahrradrahmen im Prüfstand mit Gabeldummy vorne und Achsdummy hinten" width="700">
  <figcaption>Rahmen im Prüfstand: vorne Gabeldummy mit Festlager, hinten Achsdummy mit Kugelgelenk</figcaption>
</figure>

Die Dummies lassen sich mitmodellieren, aber sie kosten Geometrie, Kontakte und Elemente. In dieser Übung rechnen Sie den Rahmen zuerst **mit** Dummies und ersetzen sie dann durch je ein `Remote Displacement`. Der Vergleich zeigt, was Remote Displacement eigentlich tut: Es ersetzt ein Bauteil, das man nicht modellieren will.

<figure style="text-align:center;">
<svg viewBox="0 0 760 260" width="760" style="max-width:100%;height:auto" role="img" aria-label="Rahmen mit Dummies und Rahmen mit Remote Displacement">
  <g font-family="Source Sans Pro, sans-serif" font-size="14" fill="#2E3639" text-anchor="middle">
    <text x="180" y="20" font-weight="700" fill="#022541">1. Mit Dummies</text>
    <g stroke="#004699" stroke-width="5" stroke-linecap="round" fill="none">
      <line x1="140" y1="70" x2="260" y2="70"/><line x1="140" y1="70" x2="165" y2="150"/><line x1="260" y1="70" x2="165" y2="150"/>
      <line x1="140" y1="70" x2="80" y2="140"/><line x1="80" y1="140" x2="165" y2="150"/>
    </g>
    <path d="M258,62 L270,66 L300,196 L288,200 Z" fill="#BEC3C6" stroke="#2E3639"/>
    <rect x="74" y="140" width="12" height="60" fill="#BEC3C6" stroke="#2E3639"/>
    <circle cx="294" cy="205" r="5" fill="#fff" stroke="#2E3639" stroke-width="2"/>
    <path d="M294,210 L284,226 L304,226 z" fill="none" stroke="#2E3639" stroke-width="1.5"/>
    <circle cx="80" cy="205" r="5" fill="#fff" stroke="#2E3639" stroke-width="2"/><circle cx="80" cy="205" r="1.5" fill="#2E3639"/>
    <path d="M80,210 L70,226 L90,226 z" fill="none" stroke="#2E3639" stroke-width="1.5"/>
    <text x="330" y="140" text-anchor="start" font-size="13">Gabeldummy</text>
    <text x="40" y="250" text-anchor="start" font-size="13">Achsdummy, Kugelgelenk</text>
    <text x="265" y="250" text-anchor="start" font-size="13">Festlager</text>
    <line x1="165" y1="110" x2="165" y2="144" stroke="#E53009" stroke-width="2.5"/><path d="M160,138 L165,148 L170,138 z" fill="#E53009"/>
    <text x="178" y="120" fill="#E53009" text-anchor="start">F</text>

    <text x="560" y="20" font-weight="700" fill="#022541">2. Dummies ersetzt</text>
    <g stroke="#004699" stroke-width="5" stroke-linecap="round" fill="none">
      <line x1="520" y1="70" x2="640" y2="70"/><line x1="520" y1="70" x2="545" y2="150"/><line x1="640" y1="70" x2="545" y2="150"/>
      <line x1="520" y1="70" x2="460" y2="140"/><line x1="460" y1="140" x2="545" y2="150"/>
    </g>
    <line x1="644" y1="66" x2="674" y2="200" stroke="#009EE3" stroke-width="2" stroke-dasharray="6 4"/>
    <line x1="460" y1="140" x2="460" y2="200" stroke="#009EE3" stroke-width="2" stroke-dasharray="6 4"/>
    <circle cx="674" cy="205" r="6" fill="#fff" stroke="#009EE3" stroke-width="3"/>
    <circle cx="460" cy="205" r="6" fill="#fff" stroke="#009EE3" stroke-width="3"/>
    <text x="690" y="140" text-anchor="start" font-size="13" fill="#009EE3">Remote</text>
    <text x="690" y="156" text-anchor="start" font-size="13" fill="#009EE3">Displacement</text>
    <text x="420" y="250" text-anchor="start" font-size="13" fill="#009EE3">Punkt am Gelenk des Dummys</text>
    <line x1="545" y1="110" x2="545" y2="144" stroke="#E53009" stroke-width="2.5"/><path d="M540,138 L545,148 L550,138 z" fill="#E53009"/>
    <text x="558" y="120" fill="#E53009" text-anchor="start">F</text>
  </g>
</svg>
</figure>

## Gegeben

### Archiv mit Rahmen, Dummies, Material, Netz und Belastung

[:material-paperclip: Uebung-04.wbpz](assets/Uebung-04.wbpz) <!-- TODO Felix: neues Archiv mit Dummies -->

Wie das Archiv importiert wird, steht in [Übung 1](../01_Geometrie_anpassen/Uebung-1.md#archiv-importieren).

Im Archiv ist alles vorbereitet:

- Rahmen aus Aluminiumlegierung 6061-T6 ($E=68{,}3\,\mathrm{GPa}$, $\nu=0{,}33$), Dummies aus Stahl <!-- TODO Felix: Material der Dummies prüfen -->
- Netzgröße global: 10 mm
- Gabeldummy unten mit Festlager, Achsdummy mit Kugelgelenk gelagert, wie im Prüfstand <!-- TODO Felix: Lagerung der Dummies im Archiv -->
- Kraft $F=800\,\mathrm{N}$ senkrecht nach unten auf die Innenseite des Tretlagers
- zwei Koordinatensysteme `Gelenk vorne` und `Gelenk hinten`, jeweils im Gelenkpunkt des Dummys. Ihre Achsen zeigen wie die globalen Achsen, verschoben ist nur der Ursprung.

## Aufgabenstellung

### 1. Mit Dummies rechnen

- [ ] Das Modell so rechnen, wie es im Archiv steht
- [ ] Die Verschiebung des Rahmens in negative y-Richtung (Richtung Boden) auswerten, **nur am Rahmen**: vor dem Einfügen der Verschiebung den Körper `Rahmen` auswählen

### Die maximale Verschiebung des Rahmens in negative y-Richtung $u_{y}$ mit Dummies in mm

<div class="steps" markdown="1" data-kategorie="Auswertung" data-titel="Verschiebung in y-Richtung nur am Rahmen auswerten">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Rahmen auswählen</p>
    <p>Mit dem Selektionstool <code>Body</code> den Körper <code>Rahmen</code> anklicken</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Directional Deformation einfügen</p>
    <p>Im Strukturbaum: <code>Rechtsklick</code> auf <code>Solution</code> > <code>Insert</code> > <code>Deformation</code> > <code>Directional</code>, im Detailfenster unter <code>Orientation</code> die <code>y-Achse</code> auswählen</p>
  </div>

</div>

<div class="numeric-question" data-answer="TODO" data-tolerance="TODO" data-points="5" data-attempts="5" data-hints="Nur den Rahmen ausgewertet? Den Betrag des kleinsten (negativen) Werts angeben. Einheit auf mm gewechselt?">
</div>

### 2. Dummies durch Remote Displacement ersetzen

- [ ] Beide Dummies unterdrücken: im Strukturbaum unter `Geometry` jeweils `Rechtsklick` auf den Dummy > `Suppress Body`. Die Lager an den Dummies werden damit wirkungslos, auch sie unterdrücken.
- [ ] **Hinten:** `Remote Displacement` auf die Innenseiten der beiden Ausfallenden (dort, wo der Achsdummy anlag)
    - Koordinatensystem `Gelenk hinten`
    - $u_x = u_y = u_z = 0$, alle Rotationen frei (Kugelgelenk)
    - Verhalten `rigid`
- [ ] **Vorne:** `Remote Displacement` auf die Innenseite des Steuerrohrs (dort, wo der Gabeldummy geklemmt war)
    - Koordinatensystem `Gelenk vorne`
    - $u_x = u_y = u_z = 0$, Rotation um die x-Achse frei (Festlager), die beiden anderen Rotationen gesperrt <!-- TODO Felix: Freiheitsgrade vorne bestätigen -->
    - Verhalten `rigid`

!!! question "Warum `rigid`?"
    Prüffrage von der Seite [Externe Lager](RemoteDisplacement.md#rigid-oder-deformable-was-ist-der-unterschied): Was sitzt in Wirklichkeit an der Fläche, und ist es deutlich steifer als der Rahmen? Hinten hält der Achsdummy die Ausfallenden zusammen, vorne steckt der Gabeldummy fest im Steuerrohr. Beide sind massive Stahlteile.

### Die maximale Verschiebung des Rahmens in negative y-Richtung $u_{y}$ mit Remote Displacement (rigid) in mm

<div class="numeric-question" data-answer="TODO" data-tolerance="TODO" data-points="5" data-attempts="5" data-hints="Beide Dummies und ihre Lager unterdrückt? Koordinatensysteme Gelenk vorne und Gelenk hinten gewählt? Verhalten rigid?">
</div>

### 3. Zum Vergleich: deformable

- [ ] Bei beiden Remote Displacements das Verhalten auf `deformable` stellen und erneut rechnen

### Die maximale Verschiebung des Rahmens in negative y-Richtung $u_{y}$ mit Remote Displacement (deformable) in mm

<div class="numeric-question" data-answer="TODO" data-tolerance="TODO" data-points="5" data-attempts="5" data-hints="Bei beiden Remote Displacements deformable eingestellt?">
</div>

### Welche Einstellung bildet die Dummies besser ab?

<div class="multiple-choice-question" data-correct="TODO" data-points="5" data-attempts="2">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="q3a" name="q3">
      <label for="q3a"><code>rigid</code>: Die steifen Dummies halten die Flächen am Rahmen in Form</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="q3b" name="q3">
      <label for="q3b"><code>deformable</code>: Die Flächen am Rahmen dürfen sich frei verformen</label>
    </div>
    <div class="mc-option" data-value="C">
      <input type="checkbox" id="q3c" name="q3">
      <label for="q3c">Beide gleich gut, der Unterschied ist vernachlässigbar</label>
    </div>
  </div>
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<!-- TODO Felix: Bilder der Verschiebung mit Dummies, rigid und deformable; dazu ein Satz, wie groß die Abweichungen sind -->

</div>

Im Prüfstand sitzt die Last nicht immer am Tretlager, sondern zum Beispiel am Sattel, also oberhalb und hinter dem Sitzrohr. Wie man eine Kraft an einem Punkt außerhalb der Geometrie anbringt, zeigt [Übung 5](../03_Belastungen/Uebung-7.md) mit `Remote Force`.
