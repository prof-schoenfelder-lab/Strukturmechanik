---
hide:
---

# Globale Netzverfeinerung

Zur globalen Netzverfeinerung verwenden wir unser bekanntes Beispiel mit dem Inbus, das hier heruntergeladen werden kann.

Es ist das gesamte Projektarchiv gegeben (Material,Geometrie,Netz und Belastung):

[:material-paperclip: Übung-01–Inbus.wbpz](assets/Uebung-01-Inbus.wbpz)

<figure style="text-align:center;">
  <img src="../images/Uebung01-Inbus.png" alt="Inbus" width="400" class="no-lightbox">
</figure>

## Import der Archivdatei

<div class="steps" markdown="1" data-kategorie="Setup">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Projekt speichern</p>
    <p>Im Workbench-Projektmenü in der Menüleiste auf <code>File</code> und <code>Save As...</code> klicken, um das aktuelle Projekt zu speichern.</p>
    <p>Am besten lokal auf dem PC in einem Ordner, auf den Sie Zugriff haben, das Projekt unter dem Namen <code>Praktikum3</code> speichern. Daran denken, keine Umlaute und keine Leerzeichen zu verwenden!</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Archivdatei importieren</p>
    <p>Im Workbench-Projektmenü in der Menüleiste auf <code>File</code> und anschließend auf <code>Import</code> klicken.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Archivdatei auswählen</p>
    <p>Im Datei-Explorer zum Speicherort der Archivdatei <code>navigieren</code>, rechts unten als Typ <code>Workbench Project Archive File (*.wbpz)</code> auswählen, die <code>zu importierende Datei</code> markieren und auf <code>Open</code> klicken.</p>
  </div>

</div>

## Globale Netzgröße einstellen

Mit globaler Netzverfeinerung ist gemeint, dass wir die Netzgröße für das gesamte Bauteil einheitlich vorgeben. Zu Beginn setzt ANSYS einen Standardwert für die Vernetzung, der in der Regel deutlich zu grob ist.

<figure style="text-align:center;">
  <img src="../images/Inbus_Defaultnetz.png" alt="Inbus mit Standardnetz" width="800" class="no-lightbox">
</figure>

- [ ] Nun eine Elementgröße von <strong>2&nbsp;mm</strong> einstellen.

<figure style="text-align:center;">
  <img src="../images/Inbus_2mm_einstellen.png" alt="Inbus mit 2 mm Netz" width="800" class="no-lightbox">
</figure>

- [ ] Die Problemstellung lösen und die <code>von-Mises-Spannung</code> darstellen.

!!! info "Erinnerung zur Darstellung der von-Mises-Spannung"
   
    <code>Rechtsklick Strukturbaum Solution → Insert → Stress → Equivalent (von-Mises)</code>

Die maximale Spannung liegt für die Netzgröße von 2&nbsp;mm im Knick und beträgt  
\(\sigma_\text{von Mises} = 354{,}48\,\mathrm{MPa}\).

<figure style="text-align:center;">
  <img src="../images/Inbus_ShowMaxStress.png" alt="maximale Spannung darstellen" width="800" class="no-lightbox">
</figure>

- [ ] Die von-Mises-Vergleichsspannung in MPa im <code>gesamten Bauteil</code> für eine Netzgröße von <code>1&nbsp;mm</code> berechnen.

<div class="numeric-question" data-answer="393.35" data-tolerance="1" data-points="5" data-attempts="5" data-hints="Einheit in mm gewechselt?" data-diagnose="353.8: Das ist nicht das Maximum im gesamten Bauteil bei 1 mm: noch 2 mm eingestellt oder nur der Knick ausgewertet? | 562.21: Das ist der Wert für 0,5 mm. Hier ist die Netzgröße 1 mm gefragt.">
</div>

- [ ] Die von-Mises-Vergleichsspannung in MPa im <code>gesamten Bauteil</code> für eine Netzgröße von <code>0,5&nbsp;mm</code> berechnen.

<div class="numeric-question" data-answer="562.21" data-tolerance="1" data-points="5" data-attempts="5" data-hints="Einheit in mm gewechselt?" data-diagnose="393.35: Das ist der Wert für 1 mm. Netzgröße auf 0,5 mm stellen. | 354.5: Das ist der Wert im Knick. Gefragt ist das Maximum im gesamten Bauteil.">
</div>

Zwischen den beiden Spannungswerten ergibt sich eine Steigerung von rund 43 %. Die Spannung nimmt also mit Netzverfeinerung stark zu – ein typischer Hinweis auf eine Singularität. Da die maximale Spannung außerdem an der festen Einspannung auftritt, können wir diesen Verdacht hier bestätigen.

## Spannungsauswertung außerhalb der Singularität

Wir verwenden nun unsere erste Lösungsstrategie und werten die Spannung außerhalb der Einspannung aus. Dafür nur die Fläche im Knick für die Spannungsauswertung auswählen:

<figure style="text-align:center;">
  <img src="../images/Inbus_Spannungsauswertung_lokal.png" alt="Lokale Spannungsauswertung im Knick" width="800" class="no-lightbox">
</figure>

- [ ] Die von-Mises-Vergleichsspannung in MPa im <code>Bereich des Knicks</code> für eine Netzgröße von <code>1&nbsp;mm</code> berechnen.

<div class="numeric-question" data-answer="353.11" data-tolerance="1" data-points="5" data-attempts="5" data-hints="Einheit in mm gewechselt?" data-diagnose="393.35: Das ist das Maximum im gesamten Bauteil, an der Einspannung. Nur die Fläche im Knick auswerten.">
</div>

- [ ] Die von-Mises-Vergleichsspannung in MPa im <code>Bereich des Knicks</code> für eine Netzgröße von <code>0,5&nbsp;mm</code> berechnen.

<div class="numeric-question" data-answer="355.06" data-tolerance="1" data-points="5" data-attempts="5" data-hints="Einheit in mm gewechselt?" data-diagnose="562.21: Das ist das Maximum im gesamten Bauteil, an der Einspannung. Nur die Fläche im Knick auswerten.">
</div>

Nun haben wir nur noch einen Unterschied von etwa 0,5 % zwischen den Spannungswerten. Damit können wir ab einer Netzgröße von 0,5 mm von einer ausreichenden Konvergenz ausgehen und haben ein geeignet feines Netz für die Bewertung der Spannung im Knick gefunden.

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<figure style="text-align:center;">
<svg viewBox="0 0 720 392" width="720" style="max-width:100%;height:auto" role="img" aria-label="Liniendiagramm: maximale von-Mises-Spannung über der Elementgröße. Im gesamten Bauteil steigt sie von 354,48 über 393,35 auf 562,21 MPa, im Knick bleibt sie bei rund 354 MPa. Alle Werte stehen auch in der Tabelle unter dem Diagramm.">
  <g stroke="var(--kurs-line, #e2e8ec)">
    <line x1="62" y1="40" x2="488" y2="40"/>
    <line x1="62" y1="136.7" x2="488" y2="136.7"/>
    <line x1="62" y1="233.3" x2="488" y2="233.3"/>
    <line x1="62" y1="330" x2="488" y2="330" stroke="var(--kurs-line-2, #cdd6dc)"/>
  </g>
  <g font-size="13" fill="var(--kurs-text-2, #566166)">
    <text x="0" y="16">maximale von-Mises-Spannung in MPa</text>
    <text x="330" y="16">gesamtes Bauteil</text>
    <text x="480" y="16">im Knick</text>
    <g text-anchor="end">
      <text x="54" y="45">600</text>
      <text x="54" y="141">500</text>
      <text x="54" y="238">400</text>
      <text x="54" y="335">300</text>
    </g>
    <g text-anchor="middle">
      <text x="100" y="352">2 mm</text>
      <text x="290" y="352">1 mm</text>
      <text x="480" y="352">0,5 mm</text>
      <text x="290" y="380">Elementgröße, nach rechts feiner →</text>
    </g>
    <text x="92" y="318">Maximum noch im Knick</text>
    <text x="496" y="99">gesamtes Bauteil</text>
    <text x="496" y="116">43 % mehr als bei 1 mm:</text>
    <text x="496" y="132">Hinweis auf eine Singularität</text>
    <text x="496" y="300">im Knick</text>
    <text x="496" y="317">etwa 0,5 % mehr als bei 1 mm:</text>
    <text x="496" y="333">ausreichend konvergiert</text>
  </g>
  <g font-size="16" font-weight="700" fill="var(--kurs-text, #2e3639)">
    <text x="92" y="302">354,48 MPa</text>
    <text x="496" y="81">562,21 MPa</text>
    <text x="496" y="282">355,06 MPa</text>
  </g>
  <g fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path stroke="#E5007D" d="M300 11h24"/>
    <path stroke="#009EE3" d="M450 11h24"/>
    <polyline stroke="#E5007D" points="100,277.3 290,239.8 480,76.5"/>
    <polyline stroke="#009EE3" points="100,277.3 290,278.7 480,276.8"/>
  </g>
  <g stroke="var(--kurs-surface, #fff)" stroke-width="2">
    <g fill="#E5007D">
      <circle cx="312" cy="11" r="5"/>
      <circle cx="290" cy="239.8" r="5"/>
      <circle cx="480" cy="76.5" r="5"/>
    </g>
    <g fill="#009EE3">
      <circle cx="462" cy="11" r="5"/>
      <circle cx="100" cy="277.3" r="5"/>
      <circle cx="290" cy="278.7" r="5"/>
      <circle cx="480" cy="276.8" r="5"/>
    </g>
  </g>
  <g fill="transparent">
    <circle cx="100" cy="277.3" r="14"><title>2 mm: 354,48 MPa, gesamtes Bauteil und im Knick</title></circle>
    <circle cx="290" cy="239.8" r="14"><title>1 mm, gesamtes Bauteil: 393,35 MPa</title></circle>
    <circle cx="290" cy="278.7" r="14"><title>1 mm, im Knick: 353,11 MPa</title></circle>
    <circle cx="480" cy="76.5" r="14"><title>0,5 mm, gesamtes Bauteil: 562,21 MPa</title></circle>
    <circle cx="480" cy="276.8" r="14"><title>0,5 mm, im Knick: 355,06 MPa</title></circle>
  </g>
</svg>
<figcaption>Spannung über der Elementgröße</figcaption>
</figure>

<table border="1">
  <tr>
    <th>Netzgröße</th>
    <th>global</th>
    <th>im Knick</th>
  </tr>
  <tr>
    <td>2&nbsp;mm</td>
    <td>354,48&nbsp;MPa</td>
    <td>354,48&nbsp;MPa</td>
  </tr>
  <tr>
    <td>1&nbsp;mm</td>
    <td>393,35&nbsp;MPa</td>
    <td>353,11&nbsp;MPa</td>
  </tr>
  <tr>
    <td>0,5&nbsp;mm</td>
    <td>562,21&nbsp;MPa</td>
    <td>355,06&nbsp;MPa</td>
  </tr>
</table>

</div>
