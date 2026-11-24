---
hide:
  - toc
sektion: Ergebnisse prüfen und darstellen
title: Übung 2
order: 240
kurz: Kragarm aus Praktikum 4 prüfen, darstellen und bewerten
thumb: ../../P4_Abstraktionen/02_ESZ/images/Uebung02-2D.excalidraw.png
typ: uebung
---

# Übung 2: Kragarm prüfen, darstellen und bewerten

Der Kragarm aus [Praktikum 4](../../P4_Abstraktionen/02_ESZ/Uebung02-2D.md) (2D, ebener Spannungszustand) ist schnell gerechnet. Jetzt geht es darum, was das Ergebnis taugt: Sie gehen die fünf Schritte der Seite [Ergebnisse prüfen](Pruefen.md) durch.

<figure style="text-align:center;">
  <img src="../../../P4_Abstraktionen/02_ESZ/images/Uebung02-2D.excalidraw.png" alt="Kragarm mit Einzelkraft" width="400" class="no-lightbox">
</figure>

!!! bug "ENTWURF: Archiv fehlt, Sollwerte nur nachgerechnet"
    - Das Archiv `Uebung-02.wbpz` gibt es noch nicht (Lösung von Praktikum 4, ESZ Übung 2).
    - Die Sollwerte stammen aus einer eigenen Nachrechnung ohne ANSYS und sind im Pool zu bestätigen.

## Gegeben

### Archiv mit dem fertigen Modell aus Praktikum 4

[:material-paperclip: Uebung-02.wbpz](assets/Uebung-02.wbpz)

Wer das eigene Modell aus Praktikum 4 noch hat, kann auch damit arbeiten.

### Modell

- Kragarm 500 mm × 60 mm, Dicke 30 mm, ebener Spannungszustand
- Aluminium: Elastizitätsmodul $E=70 \mathrm{GPa}$, Querkontraktionszahl $\nu=0{,}34$
- feste Einspannung links, Kraft $F=3000 \mathrm{N}$ nach unten am Eckpunkt oben rechts

### Neu gegenüber Praktikum 4

- Netzgröße global: 1 mm statt 5 mm
- Dehngrenze des Werkstoffs für die Bewertung: $R_{p0{,}2}=240 \mathrm{MPa}$

## Aufgabenstellung

- [ ] Netzgröße auf 1 mm stellen und neu rechnen
- [ ] Verformung prüfen: Ausgangsgeometrie einblenden, einmal im wahren Maßstab und einmal überhöht ansehen
- [ ] Kräfte prüfen: Lagerkraft an der Einspannung ablesen
- [ ] Vergleichsspannung (von Mises) anzeigen und die lokalen Maxima einblenden
- [ ] Jedes lokale Maximum einordnen: physikalischer Grund oder Singularität?
- [ ] Den zweiten Legendenwert von oben auf 80 MPa setzen
- [ ] Das Bild mit weißem Hintergrund und Auflösung 4:1 speichern

## Gesucht

### Die Lagerkraft an der Einspannung in y-Richtung in N

<div class="numeric-question" data-answer="3000" data-tolerance="5" data-points="5" data-attempts="5" data-hints="Force Reaction unter Solution, Insert, Probe eingefügt? Als Boundary Condition den Fixed Support gewählt? Gefragt ist die y-Komponente.">
</div>

### Welche lokalen Maxima sind Singularitäten?

Mechanical zeigt fünf lokale Maxima mit nennenswerter Spannung. Kreuzen Sie alle an, die Singularitäten sind.

<div class="multiple-choice-question" data-correct="A,B" data-points="5" data-attempts="3" data-hints="Wo greift eine Einzelkraft an? Wo ist eine Ecke fest eingespannt? Dort steigt die Spannung mit jedem feineren Netz weiter.">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="p5u2s_a" name="p5u2s">
      <label for="p5u2s_a">Das Maximum am Kraftangriffspunkt oben rechts</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="p5u2s_b" name="p5u2s">
      <label for="p5u2s_b">Die beiden Maxima an den Ecken der Einspannung</label>
    </div>
    <div class="mc-option" data-value="C">
      <input type="checkbox" id="p5u2s_c" name="p5u2s">
      <label for="p5u2s_c">Die beiden Maxima an Ober- und Unterseite, rund 20 mm neben der Einspannung</label>
    </div>
  </div>
</div>

### Die größte Vergleichsspannung, die keine Singularität ist, in MPa

<div class="numeric-question" data-answer="78.4" data-tolerance="1.5" data-points="5" data-attempts="5" data-hints="Lokale Maxima eingeblendet (Create Local Max Probes)? Gesucht ist das größte Maximum, das weder am Kraftangriffspunkt noch an einer Ecke der Einspannung liegt.">
</div>

<!-- ENTWURF: Sollwert 78,4 MPa aus eigener Nachrechnung (78,51 bei 5 mm, 78,42 bei 2,5 bis 1 mm), im Pool bestätigen.
     Diagnose ergänzen, sobald die ANSYS-Werte bei 1 mm vorliegen (Nachrechnung: Kraftangriffspunkt 545, Ecken der Einspannung 160 MPa):
     Kraftangriffspunkt: Das ist die Spitze am Kraftangriffspunkt, eine Singularität durch die Einzelkraft.
     Ecke: Das ist die Spitze an einer Ecke der Einspannung, eine Singularität. -->

### Die Sicherheit gegen Fließen an dieser Stelle

<div class="numeric-question" data-answer="3.06" data-tolerance="0.1" data-points="5" data-attempts="5" data-hints="Sicherheit gleich Dehngrenze geteilt durch Vergleichsspannung. Die Dehngrenze steht unter Gegeben.">
</div>

<!-- ENTWURF: Diagnose ergänzen, sobald die ANSYS-Werte vorliegen: Sicherheit mit der Spitze am Kraftangriffspunkt (Nachrechnung 0,44) und an der Ecke der Einspannung (1,5). -->

### Die Verformung sieht im Bild riesig aus. Was prüfen Sie zuerst?

<div class="multiple-choice-question" data-correct="B" data-points="5" data-attempts="2">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="p5u2v_a" name="p5u2v">
      <label for="p5u2v_a">Das Netz, es ist vermutlich zu grob</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="p5u2v_b" name="p5u2v">
      <label for="p5u2v_b">Den Maßstab der Darstellung und den Zahlenwert der größten Verformung</label>
    </div>
    <div class="mc-option" data-value="C">
      <input type="checkbox" id="p5u2v_c" name="p5u2v">
      <label for="p5u2v_c">Die Farbskala der Spannung</label>
    </div>
  </div>
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images" markdown="1">

🎯 <strong>Lösung</strong>

<figure style="text-align:center;">
  <img src="../images/Uebung-02-Lokale-Maxima.png" alt="Kragarm mit fünf lokalen Maxima der Vergleichsspannung: am Kraftangriffspunkt, an beiden Ecken der Einspannung und an Ober- und Unterseite neben der Einspannung" width="900">
  <figcaption>Lokale Maxima der Vergleichsspannung bei 1 mm Netzgröße</figcaption>
</figure>

| Stelle | Vergleichsspannung bei 5 mm | bei 1 mm | Einordnung |
|---|---|---|---|
| Kraftangriffspunkt | 109 MPa | 545 MPa | Singularität: Einzelkraft auf einem Punkt |
| Ecken der Einspannung | 108 MPa | 160 MPa | Singularität: Die feste Einspannung behindert die Querdehnung |
| Ober- und Unterseite neben der Einspannung | 78,5 MPa | 78,4 MPa | Biegespannung, bleibt mit feinerem Netz gleich |

- Die Lagerkraft ist so groß wie die Last: 3000 N. Damit ist die Last richtig aufgebracht.
- Zwei der drei Stellen wachsen mit jedem feineren Netz weiter. Ihre Werte sagen nichts über das Bauteil.
- Die Biegespannung ändert sich nicht mehr. Das ist die Spannung, die bewertet wird: Sicherheit 240 MPa / 78,4 MPa = 3,06.
- Mit der Spitze am Kraftangriffspunkt käme eine Sicherheit unter 1 heraus, und das Bauteil sähe überlastet aus.
- Erst mit der gesetzten Grenze von 80 MPa zeigt das Farbbild, wie sich die Biegespannung über den Kragarm verteilt.

<!-- ENTWURF: Werte der Tabelle aus eigener Nachrechnung, im Pool gegen ANSYS 2025 R2 prüfen. -->

</div>
