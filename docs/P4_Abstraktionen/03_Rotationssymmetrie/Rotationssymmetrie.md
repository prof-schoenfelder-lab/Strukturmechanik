---
icon: material/horizontal-rotate-clockwise
hide:
  - toc
---

# Rotationssymmetrie

Die nächste 2D-Abstraktion ist die `Rotationssymmetrie` (achsen-symmetrische Modellierung).

<figure style="text-align:left;">
    <img src="../images/rotationssymmetrie.excalidraw.png" alt="Rotationssymmetrie" width="800" class="no-lightbox">
</figure>

Hierbei wird ein voll dreidimensionaler Körper, der um eine Achse gedreht entsteht (z. B. Welle, Druckbehälter, Rohr), durch seinen **2D-Querschnitt** im \(r\)-\(z\)-System beschrieben. Das FE-Programm berechnet daraus automatisch den zugehörigen dreidimensionalen Spannungszustand eines rotationssymmetrischen Körpers.

Wichtig ist:

- die **Geometrie** ist rotationssymmetrisch,
- die **Lagerung** ist rotationssymmetrisch,
- die **Lasten** sind rotationssymmetrisch (z. B. Innendruck, Eigengewicht, gleichmäßige Auflagerung).

Sind diese Bedingungen erfüllt, beschreibt das achsensymmetrische 2D-Modell das reale 3D-Problem **ohne nennenswerten Genauigkeitsverlust**, spart aber sehr viel Rechenzeit.

Nicht geeignet ist die Rotationssymmetrie hingegen für nicht-rotationssymmetrische Effekte, z. B. lokale Einzellasten, Kerben oder Bohrungen, die nur an einer Stelle des Umfangs auftreten.
