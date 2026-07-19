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

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Projekt speichern</p>
    <p>Im Workbench-Projektmenü in der Menüleiste auf <code>File</code> und <code>Save As...</code> klicken, um das aktuelle Projekt zu speichern.</p>
    <p>Am besten unter <code>D:\Studierende\</code> einen Ordner mit dem eigenen Namen anlegen und dort das Projekt unter dem Namen <code>Praktikum3</code> speichern. Daran denken, keine Umlaute und keine Leerzeichen zu verwenden!</p>
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
   
    Im Strukturbaum: <code>Rechtsklick</code> auf <code>Solution</code> und anschließend  
    <code>Insert</code> → <code>Stress</code> → <code>Equivalent (von-Mises)</code> auswählen.

Die maximale Spannung liegt für die Netzgröße von 2&nbsp;mm im Knick und beträgt  
\(\sigma_\text{von Mises} = 354{,}48\,\mathrm{MPa}\).

<figure style="text-align:center;">
  <img src="../images/Inbus_ShowMaxStress.png" alt="maximale Spannung darstellen" width="800" class="no-lightbox">
</figure>

- [ ] Die von-Mises-Vergleichsspannung in MPa im <code>gesamten Bauteil</code> für eine Netzgröße von <code>1&nbsp;mm</code> berechnen.

<div class="numeric-question" data-answer="393.35" data-tolerance="1" data-points="5" data-attempts="5" data-hints="Einheit in mm gewechselt?">
</div>

- [ ] Die von-Mises-Vergleichsspannung in MPa im <code>gesamten Bauteil</code> für eine Netzgröße von <code>0,5&nbsp;mm</code> berechnen.

<div class="numeric-question" data-answer="562.21" data-tolerance="1" data-points="5" data-attempts="5" data-hints="Einheit in mm gewechselt?">
</div>

Zwischen den beiden Spannungswerten ergibt sich eine Steigerung von rund 43 %. Die Spannung nimmt also mit Netzverfeinerung stark zu – ein typischer Hinweis auf eine Singularität. Da die maximale Spannung außerdem an der festen Einspannung auftritt, können wir diesen Verdacht hier bestätigen.

## Spannungsauswertung außerhalb der Singularität

Wir verwenden nun unsere erste Lösungsstrategie und werten die Spannung außerhalb der Einspannung aus. Dafür nur die Fläche im Knick für die Spannungsauswertung auswählen:

<figure style="text-align:center;">
  <img src="../images/Inbus_Spannungsauswertung_lokal.png" alt="Lokale Spannungsauswertung im Knick" width="800" class="no-lightbox">
</figure>

- [ ] Die von-Mises-Vergleichsspannung in MPa im <code>Bereich des Knicks</code> für eine Netzgröße von <code>1&nbsp;mm</code> berechnen.

<div class="numeric-question" data-answer="353.11" data-tolerance="1" data-points="5" data-attempts="5" data-hints="Einheit in mm gewechselt?">
</div>

- [ ] Die von-Mises-Vergleichsspannung in MPa im <code>Bereich des Knicks</code> für eine Netzgröße von <code>0,5&nbsp;mm</code> berechnen.

<div class="numeric-question" data-answer="355.06" data-tolerance="1" data-points="5" data-attempts="5" data-hints="Einheit in mm gewechselt?">
</div>

Nun haben wir nur noch einen Unterschied von etwa 0,5 % zwischen den Spannungswerten. Damit können wir ab einer Netzgröße von 0,5 mm von einer ausreichenden Konvergenz ausgehen und haben ein geeignet feines Netz für die Bewertung der Spannung im Knick gefunden.

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<table border="1">
  <tr>
    <th>Netzgröße</th>
    <th>global</th>
    <th>im Knick</th>
  </tr>
  <tr>
    <td>4&nbsp;mm</td>
    <td>354,48&nbsp;MPa</td>
    <td>354,48&nbsp;MPa</td>
  </tr>
  <tr>
    <td>2&nbsp;mm</td>
    <td>393,35&nbsp;MPa</td>
    <td>353,11&nbsp;MPa</td>
  </tr>
  <tr>
    <td>1&nbsp;mm</td>
    <td>562,21&nbsp;MPa</td>
    <td>355,06&nbsp;MPa</td>
  </tr>
</table>

</div>
