---
hide:
 - toc
---

# Zweiseitig gelagerter Balken mit Flächenlast

Wieder unser bekanntes Beispiel – diesmal in 1D-Abstraktion mit `BEAM`-Elementen:

<figure style="text-align:center;">
  <img src="../../02_ESZ/images/Uebung01-2D.excalidraw.png" alt="Uebung 1 2D" width="400" class="no-lightbox">
</figure>

## Gegeben

### Material

Stahl

- Elastizitätsmodul: \(E = 210\,\mathrm{GPa}\)
- Querkontraktionszahl: \(\nu = 0{,}3\)

### Geometrie

Balken mit rechteckigem Querschnitt

- Länge \(L = 1000\,\mathrm{mm}\)
- Breite \(b = 30\,\mathrm{mm}\)
- Höhe \(h = 30\,\mathrm{mm}\)

### Vernetzung

- Netzgröße global: \(10\,\mathrm{mm}\)

### Randbedingungen

**Lagerung:**

- entsprechend Skizze  
- Darauf achten, dass der Balken sich nicht um seine Längsachse dreht

**Belastung:**

- Gleichmäßig verteilte Belastung mit einer resultierenden Kraft  
  \(F = 1000\,\mathrm{N}\) über die gesamte Balkenlänge.

## Aufgabenstellung

!!! abstract "Die Aufgabe mit der 1D-Abstraktion mit BEAM-Elementen lösen."

!!! abstract "Zusatz: Alle möglichen Symmetrien verwenden."

## Hinweise

??? tip "<code>HINWEIS</code> – Geometrie mit Linie erstellen (klicken zum Aufklappen)"

    --8<-- "P4_Abstraktionen/04_Linienstrukturen/Umsetzung.md:Linienstruktur_erstellen"

??? tip "<code>HINWEIS</code> – Geometrie aus Volumengeometrie ableiten (klicken zum Aufklappen)"

    --8<-- "P4_Abstraktionen/04_Linienstrukturen/Umsetzung.md:Linienstruktur_umwandeln"

??? tip "<code>HINWEIS</code> – Profil anpassen (klicken zum Aufklappen)"

    --8<-- "P4_Abstraktionen/04_Linienstrukturen/Umsetzung.md:ProfilAnpassen"

??? tip "<code>HINWEIS</code> – Elementdarstellung (klicken zum Aufklappen)"

    --8<-- "P4_Abstraktionen/04_Linienstrukturen/Umsetzung.md:Elementdarstellung"

??? tip "<code>HINWEIS</code> – Ergebnisdarstellung (klicken zum Aufklappen)"

    --8<-- "P4_Abstraktionen/04_Linienstrukturen/Umsetzung.md:Ergebnisdarstellung"

??? tip "<code>HINWEIS</code> – Randbedingungen (klicken zum Aufklappen)"

    --8<-- "P4_Abstraktionen/04_Linienstrukturen/Umsetzung.md:Randbedingungen"

## Gesucht

Die folgenden Größen berechnen:

### Die maximale Durchbiegung im Bauteil \(u_\text{max}\) in mm

<div class="numeric-question" data-answer="0.92055" data-tolerance="0.05" data-points="5" data-attempts="5"  data-hints="Anstieg (Rotation) am Lager fälschlich durch Fixed Support auf Null gesetzt?">
</div>

### Die maximale von-Mises-Vergleichsspannung im Bauteil \(\sigma_\text{von Mises}\) in MPa

<div class="numeric-question" data-answer="27.778" data-tolerance="0.25" data-points="5" data-attempts="5"  data-hints="Anstieg (Rotation) am Lager fälschlich durch Fixed Support auf Null gesetzt?">
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<figure style="text-align:center;">
  <img src="../images/Uebung01_BEAM_umax.png" alt="maximale Durchbiegung" width="900">
  <figcaption>Maximale Durchbiegung</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="../images/Uebung01_BEAM_sigmamax.png" alt="maximale Vergleichsspannung" width="900">
  <figcaption>Maximale Vergleichsspannung</figcaption>
</figure>

</div>
