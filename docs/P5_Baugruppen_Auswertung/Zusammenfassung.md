---
title: Zusammenfassung
icon: material/head-snowflake
hide:
  - toc
---

# :material-head-snowflake: Zusammenfassung

In diesem Praktikum kamen mehrere Bauteile zusammen, und es ging um das, was nach jeder Rechnung ansteht: prüfen, darstellen, bewerten.

!!! bug "ENTWURF: Kernaussagen sind ein Vorschlag"
    Die vier Kästen fassen die Seiten zusammen. Die Kernaussagen für den Spickzettel formuliert Felix.

Hier noch mal die wichtigsten Kernaussagen des fünften Praktikums:

<div class="steps" markdown="1" data-spickzettel="ja">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Verbindungen und Kontakte</p>
    <p>Wenn eine Baugruppe importiert wird, dann legt Mechanical alle Kontakte als Verbund (<code>Bonded</code>) an: Die Fugen sind verklebt und halten auch auf Zug.</p>
    <p><strong>1. Ansehen:</strong> <code>Strukturbaum → Connections → Contacts</code>, die Kontaktart steht unter <code>Detailfenster → Type</code>.</p>
    <p><strong>2. Prüfen:</strong> <code>Rechtsklick Strukturbaum Connections → Insert → Contact Tool</code>, dann <code>Rechtsklick Strukturbaum Initial Information → Generate Initial Contact Results</code>.</p>
    <p><strong>3. Wählen:</strong> Wenn die Fuge abheben kann und das für das Ergebnis zählt, dann <code>Frictional</code> mit Reibungszahl. Die Rechnung wird dadurch nichtlinear.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Schrauben</p>
    <p>Eine vorgespannte Schraube bekommt nur einen kleinen Teil der Betriebskraft ab, der Rest entlastet die verspannten Bauteile. Nachgewiesen wird mit der Schraubenkraft, nicht mit der Spannung aus dem Farbbild.</p>
    <p><strong>1. Kontakte:</strong> Reibung in der Trennfuge und unter dem Kopf. Mit Verbund zwischen den Platten trägt die Schraube fast nichts.</p>
    <p><strong>2. Zwei Lastschritte:</strong> <code>Analysis Settings → Number Of Steps: 2</code>.</p>
    <p><strong>3. Vorspannen und sperren:</strong> <code>Bolt Pretension</code> in Schritt 1 mit <code>Load</code>, in Schritt 2 mit <code>Lock</code>. Die Betriebskraft kommt erst in Schritt 2.</p>
    <p><strong>4. Auswerten:</strong> Probe <code>Bolt Pretension</code>, <code>Working Load</code> ist die Schraubenkraft.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Ergebnisse prüfen</p>
    <p>Nach jeder Rechnung dieselbe Reihenfolge: Verformung, Kräfte, Spannung, Netz, Bewertung.</p>
    <p><strong>1. Verformung:</strong> <code>Reiter Result → Edges → Show Undeformed Wireframe</code>, Maßstab <code>1.0 (True Scale)</code> und überhöht vergleichen.</p>
    <p><strong>2. Kräfte:</strong> <code>Rechtsklick Strukturbaum Solution → Insert → Probe → Force Reaction</code>, die Summe muss zu den Lasten passen.</p>
    <p><strong>3. Bewertung:</strong> Wenn die Vergleichsspannung über der Streckgrenze liegt, dann gilt die lineare Rechnung dort nicht mehr. Singularitäten werden nicht bewertet.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Spannungen darstellen</p>
    <p>Wenn eine Spitze die Farbskala beherrscht, dann die obere Grenze setzen, damit der Rest des Bauteils sichtbar wird.</p>
    <p><strong>1. Grenze:</strong> in der Legende den zweiten Wert von oben doppelklicken und eintippen.</p>
    <p><strong>2. Lokale Maxima:</strong> <code>Rechtsklick Grafikfenster → Create Local Max Probes</code>, jede Spitze erklären.</p>
    <p><strong>3. Vergleich:</strong> gleiche Skala über <code>Rechtsklick Legende → Named Legends</code>.</p>
    <p><strong>4. Bild:</strong> <code>Reiter Home → Images → Image to File</code>, ohne <code>Current Graphics Display</code>, mit <code>4:1</code> und weißem Hintergrund.</p>
  </div>

</div>
