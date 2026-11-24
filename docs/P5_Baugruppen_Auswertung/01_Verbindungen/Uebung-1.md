---
hide:
  - toc
sektion: Verbindungen und Kontakte
title: Übung 1
order: 40
kurz: Inbus im Schraubkopf, verbunden auf drei Arten
thumb: ../../P2_Geometrie_Randbedingungen/02_Lagerungen/images/Uebung-06.png
typ: uebung
---

# Übung 1: Inbus im Schraubkopf, verbunden auf drei Arten

In [Praktikum 2, Übung 4](../../P2_Geometrie_Randbedingungen/02_Lagerungen/Uebung-6.md) war der Schraubkopf die Referenz für alle Lagerungen. Dort waren Inbus und Schraubkopf über gemeinsame Topologie verbunden, also ein Stück. Jetzt sind es zwei Bauteile mit einem Kontakt dazwischen, und Sie vergleichen drei Verbindungen:

- A: gemeinsame Topologie (das Ergebnis aus Praktikum 2)
- B: Kontakt mit Verbund (`Bonded`)
- C: Kontakt mit Reibung (`Frictional`)

<figure style="text-align:center;">
  <img src="../../../P2_Geometrie_Randbedingungen/02_Lagerungen/images/Uebung-06.png" alt="Inbus im Schraubkopf" width="700" class="no-lightbox">
</figure>

!!! bug "ENTWURF: Archiv und Sollwerte fehlen"
    - Das Archiv `Uebung-01.wbpz` gibt es noch nicht: Inbus und Schraubkopf als zwei Bauteile ohne gemeinsame Topologie, mit Netz, Lagerung und Kraft.
    - Die Werte für B und C kommen aus dem Pool (ANSYS 2025 R2). Ob C mit Reibung rechnet, ist noch nicht ausprobiert.

## Gegeben

### Archiv mit Geometrie, Material, Netz, Lagerung und Kraft

[:material-paperclip: Uebung-01.wbpz](assets/Uebung-01.wbpz)

Wie das Archiv importiert wird, steht in [Praktikum 2, Übung 1](../../P2_Geometrie_Randbedingungen/01_Geometrie_anpassen/Uebung-1.md#archiv-importieren).

### Material

Stahl

- Elastizitätsmodul $E=210 \mathrm{GPa}$
- Querkontraktionszahl $\nu=0{,}3$

### Vernetzung

- Netzgröße global: 1 mm

### Randbedingungen

- Lagerung: feste Einspannung (`Fixed Support`) an der unteren Stirnseite des Schraubkopfs
- Belastung: Kraft 200 N am langen Ende, in negative y-Richtung
- Reibungszahl für Variante C: $\mu = 0{,}15$

## Aufgabenstellung

- [ ] Archiv importieren und Mechanical öffnen
- [ ] Den Kontakt zwischen Inbus und Schraubkopf im Strukturbaum ansehen
- [ ] Den Kontakt vor der Rechnung prüfen (`Initial Information`)
- [ ] Variante B rechnen und die Gesamtverformung des Inbus ablesen
- [ ] Kontaktart auf Reibung umstellen, Reibungszahl 0,15 eintragen, Variante C rechnen

## Hinweise

??? tip "<code>HINWEIS</code>: Kontakt ansehen und Kontaktart ändern (klicken zum Aufklappen)"

    --8<-- "P5_Baugruppen_Auswertung/01_Verbindungen/Umsetzung.md:Kontakt"

??? tip "<code>HINWEIS</code>: Kontakt vor der Rechnung prüfen (klicken zum Aufklappen)"

    --8<-- "P5_Baugruppen_Auswertung/01_Verbindungen/Umsetzung.md:Pruefen"

## Gesucht

### Welche Kontaktart hat Mechanical beim Import angelegt?

<div class="multiple-choice-question" data-correct="A" data-points="5" data-attempts="2" data-hints="Den Kontakt unter Connections, Contacts auswählen. Die Kontaktart steht im Detailfenster unter Type.">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="p5u1a_a" name="p5u1a">
      <label for="p5u1a_a">Verbund (<code>Bonded</code>)</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="p5u1a_b" name="p5u1a">
      <label for="p5u1a_b">Reibung (<code>Frictional</code>)</label>
    </div>
    <div class="mc-option" data-value="C">
      <input type="checkbox" id="p5u1a_c" name="p5u1a">
      <label for="p5u1a_c">reibungsfrei (<code>Frictionless</code>)</label>
    </div>
    <div class="mc-option" data-value="D">
      <input type="checkbox" id="p5u1a_d" name="p5u1a">
      <label for="p5u1a_d">Keine, den Kontakt muss man selbst anlegen</label>
    </div>
  </div>
</div>

### Die maximale Gesamtverformung des Inbus mit Verbund (B) in mm

!!! bug "ENTWURF: Sollwert fehlt"
    Erwartung: nahe am Wert mit gemeinsamer Topologie aus Praktikum 2 (2,066 mm). Die Frage wird eingefügt, sobald der Wert aus dem Pool vorliegt.

<!-- ENTWURF Frage B, sobald der Wert vorliegt: Zahlenfrage mit Toleranz 0,03, 5 Punkte, 5 Versuche.
     Hinweise: Fixed Support an der unteren Stirnseite des Schraubkopfs? Kontaktart Bonded? Gesamtverformung nur am Inbus ausgewertet? Einheit mm? -->

### Die maximale Gesamtverformung des Inbus mit Reibung (C) in mm

!!! bug "ENTWURF: Sollwert fehlt"
    Erwartung: größer als mit Verbund, weil die Fuge jetzt nachgeben kann. Die Frage wird eingefügt, sobald der Wert aus dem Pool vorliegt.

<!-- ENTWURF Frage C, sobald der Wert vorliegt: Zahlenfrage mit Toleranz 0,03, 5 Punkte, 5 Versuche.
     Hinweise: Type auf Frictional gestellt? Friction Coefficient 0,15? Neu gerechnet?
     Diagnose: Wert von B: Das ist der Wert mit Verbund. Steht Type auf Frictional, und ist neu gerechnet? -->

### Welche der drei Rechnungen ist nichtlinear?

<div class="multiple-choice-question" data-correct="C" data-points="5" data-attempts="2" data-hints="Nichtlinear wird die Rechnung, wenn die Fuge abheben kann.">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="p5u1n_a" name="p5u1n">
      <label for="p5u1n_a">A: gemeinsame Topologie</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="p5u1n_b" name="p5u1n">
      <label for="p5u1n_b">B: Kontakt mit Verbund</label>
    </div>
    <div class="mc-option" data-value="C">
      <input type="checkbox" id="p5u1n_c" name="p5u1n">
      <label for="p5u1n_c">C: Kontakt mit Reibung</label>
    </div>
  </div>
</div>

### Wofür reicht Verbund?

Kreuzen Sie alle Aufgabenstellungen an, für die der Kontakt mit Verbund ausreicht.

<div class="multiple-choice-question" data-correct="A" data-points="5" data-attempts="2" data-hints="Verbund hält die Fuge überall zusammen. Wo spielt es eine Rolle, ob die Fuge aufgehen kann?">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="p5u1v_a" name="p5u1v">
      <label for="p5u1v_a">Ich will die Spannung im langen Schenkel wissen, weit weg vom Schraubkopf.</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="p5u1v_b" name="p5u1v">
      <label for="p5u1v_b">Ich will wissen, an welchen Flanken der Inbus im Schraubkopf anliegt.</label>
    </div>
    <div class="mc-option" data-value="C">
      <input type="checkbox" id="p5u1v_c" name="p5u1v">
      <label for="p5u1v_c">Ich will den Druck zwischen Inbus und Schraubkopf wissen.</label>
    </div>
  </div>
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images" markdown="1">

🎯 <strong>Lösung</strong>

| Verbindung | max. Gesamtverformung | Rechnung |
|---|---|---|
| A: gemeinsame Topologie (Praktikum 2) | 2,066 mm | linear |
| B: Kontakt mit Verbund | Wert folgt | linear |
| C: Kontakt mit Reibung, $\mu = 0{,}15$ | Wert folgt | nichtlinear |

- Gemeinsame Topologie und Verbund halten die Fuge überall zusammen, auch dort, wo der Inbus in Wirklichkeit abheben würde.
- Mit Reibung liegt der Inbus nur noch an den Flanken an, gegen die er gedrückt wird. Die Verbindung gibt mehr nach.
- Weit weg vom Schraubkopf ändert sich die Spannung im Inbus kaum. Dort reicht Verbund.

</div>
