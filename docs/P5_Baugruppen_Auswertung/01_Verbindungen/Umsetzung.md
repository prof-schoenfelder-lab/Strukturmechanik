---
icon: material/alpha-a-box
hide:
  - toc
sektion: Verbindungen und Kontakte
title: Umsetzung in ANSYS
order: 30
kurz: Kontakte ansehen, ändern und prüfen
thumb: images/Kontaktarten.excalidraw.png
---

# :material-alpha-a-box: Kontakte in ANSYS Mechanical

<!-- ENTWURF: Bildschirmfotos aus 2025 R2 fehlen (Contact Region im Baum mit Detailfenster, Tabelle Initial Information). Die Klickwege stammen aus der ANSYS-Hilfe 2025 R2 und sind im Programm noch nicht geprüft. -->

## Kontakt ansehen und ändern

<!-- --8<-- [start:Kontakt] -->
<div class="steps" markdown="1" data-kategorie="Verbindungen" data-titel="Kontakt ansehen und Kontaktart ändern">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Kontakt im Strukturbaum auswählen</p>
    <p><code>Strukturbaum → Connections → Contacts → Contact Region</code>. Im Grafikfenster sind die beiden Seiten des Kontakts farbig markiert, im Detailfenster heißen sie <code>Contact</code> und <code>Target</code>.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Kontaktart ablesen oder ändern</p>
    <p><code>Detailfenster → Type</code>. Nach dem Import steht dort <code>Bonded</code>.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Bei Reibung die Reibungszahl eintragen</p>
    <p>Mit <code>Type: Frictional</code> erscheint <code>Detailfenster → Friction Coefficient</code>.</p>
  </div>

</div>
<!-- --8<-- [end:Kontakt] -->

## Kontakt vor der Rechnung prüfen

<!-- --8<-- [start:Pruefen] -->
<div class="steps" markdown="1" data-kategorie="Verbindungen" data-titel="Kontakt vor der Rechnung prüfen">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Contact Tool einfügen</p>
    <p><code>Rechtsklick Strukturbaum Connections → Insert → Contact Tool</code></p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Anfangszustand berechnen</p>
    <p><code>Rechtsklick Strukturbaum Initial Information → Generate Initial Contact Results</code></p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Tabelle lesen</p>
    <p>Je Kontakt stehen dort Zustand (<code>Status</code>), Spalt (<code>Gap</code>) und Durchdringung (<code>Penetration</code>).</p>
  </div>

</div>
<!-- --8<-- [end:Pruefen] -->

Die Zeilen der Tabelle sind eingefärbt:

| Farbe | Bedeutung | Was tun |
|---|---|---|
| keine | Kontakt ist geschlossen | nichts |
| Gelb | Kontakt ist offen, das kann gewollt sein | prüfen, ob dort ein Spalt sein soll |
| Rot | Kontakt ist offen, obwohl die Kontaktart geschlossen sein müsste (Verbund, kein Abheben) | Geometrie oder Kontaktflächen prüfen |
| Orange | Kontakt ist geschlossen, aber mit großem Spalt oder großer Durchdringung | Geometrie prüfen |
| Grau | Kontakt ist nicht aktiv | prüfen, ob er unterdrückt ist |

## Bauteile ohne Kontakt finden

`Rechtsklick Grafikfenster → Go To → Bodies Without Contacts in Tree` markiert im Strukturbaum alle Körper, an denen kein Kontakt hängt. Wenn ein solcher Körper auch kein Lager hat, dann hat er keinen Halt.

## Kontakt nach der Rechnung auswerten

- `Rechtsklick Strukturbaum Solution → Insert → Contact Tool` zeigt nach der Rechnung den Zustand der Fuge (`Status`), den Druck (`Pressure`) und den Spalt (`Gap`).
- Bei Verbund zwischen zwei Volumenkörpern bleibt der Druck null: Mechanical koppelt die Flächen dann über Zwangsgleichungen und rechnet keinen Kontaktdruck aus.
