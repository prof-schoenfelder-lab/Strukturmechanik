---
hide:
---

# Kragarm mit Einzelkraft

Die zweite Übung ist auch ein klassisches Beispiel der Technischen Mechanik: ein Kragarm mit Einzelkraft. Diesmal mit andererem Material (Alu), leicht anderer Geometrie, kleinerem Netz und anderer Lagerung (feste Einspannung).

<figure style="text-align:center;">
  <img src="../images/Uebung-02.png" alt="Kragarm mit Einzelkraft" width="400" class="no-lightbox">
</figure>

## Gegeben

### Material

Aluminium

- Elastizitätsmodul $E=70 \mathrm{GPa}$
- Querkontraktionszahl $\nu=0{,}34$

### Geometrie

Balken mit rechteckigem Querschnitt

- Länge $L=500 \mathrm{mm}$
- Breite $b=30 \mathrm{mm}$
- Breite $h=60 \mathrm{mm}$

### Vernetzung

- Netzgröße global: 5 mm

### Randbedingungen

Lagerung:

- Feste Einspannung auf der Stirnseite links

Belastung:

- Kraft $F=5000 \mathrm{N}$ auf der Kante rechts

## Hinweise

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Neue Analyse anlegen</p>
    <p>Im Workbench Projektmenü <code>Doppelklick</code> auf <code>Static Structural</code> und anschließend in <code>Übung 2</code> umbennen.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Lagerung: Feste Einspannung</p>
    <p>Bei einer festen Einspannung werden alle Freiheitsgrade auf der Stirnseite (Fläche) links untedrückt.</p>
  </div>
</div>

## Gesucht

### Die maximale Durchbiegung $u_{\max }$ in mm

<div class="numeric-question" data-answer="3.3462" data-tolerance="0.1" data-points="5" data-attempts="5"  data-hints="Material definiert und zugeordnet? Einheit auf mm gewechselt? Kraft auf Kante in z-Richtung?">
</div>

### Die maximale Spannung in y-Richtung $\sigma_{y, \max }$ in MPa

<div class="numeric-question" data-answer="142.47" data-tolerance="0.5" data-points="5" data-attempts="5"  data-hints="Material definiert und zugeordnet? Einheit auf mm gewechselt? Kraft auf Kante in z-Richtung? Spannung in y-Richtung (Längsrichtung des Balkens) ausgewertet?">
</div>

## Analytische Lösung 

Vergleichen wir den Spannungswert mit der analytischen Lösung. Dafür brauchen wir das maximale Moment:

$$
M_{M a x}=F L=3000 \mathrm{~N} \cdot 500  \mathrm{~mm}=1.500.000\,\mathrm{Nmm}
$$

Das Flächenträgheitsmoment ergibt sich wieder aus:

$$
I=\frac{b h^3}{12}=\frac{30 \mathrm{~mm}(60 \mathrm{~mm})^3}{12}=540.000 \mathrm{~mm}^4
$$

$$
\sigma_{\max }=M_{M a x} \frac{\frac{h}{2}}{I}=1.500.000\,\mathrm{Nmm} \frac{(60 \mathrm{~mm}) / 2}{540.000 \mathrm{~mm}^4}=83{,}3\,\mathrm{MPa}
$$


!!! failure "Starke Abweichung!"

    Scheinbar gibt es eine sehr große Abweichung zur analytischen Lösung. Den Grund dafür schauen wir uns jetzt an.

## Singularität an einer festen Einspannung 

Auf der Stirnseite werden durch den `Fixed Support` (oder `Displacement` mit x=0,y=0 & z=0) alle Verformungen unterdrückt. Normalerweise würden sich in diesem Bereich der Querschnitt auf Grund der Querkontraktion verformen:

<figure style="text-align:center;">
  <img src="../images/FesteEinspannungsProblem.png" alt="Kragarm mit Einzelkraft" width="500" class="no-lightbox">
</figure>

Durch die `sprunghafte Änderung der Randbedingung an den Ecken` entsteht dort eine `Singularität`. Die Spannung an der Singularität steigt mit immer kleinere Netzgröße immer weiter an:

<center>
<iframe title="Maximale Spannung bei unterschiedlicher Netzgröße" aria-label="Liniendiagramm" id="datawrapper-chart-2WMO0" src="https://datawrapper.dwcdn.net/KckxX/2/" scrolling="no" frameborder="0" style="width: 0; min-width: 80% !important; border: none;" height="400" data-external="1"></iframe><script type="text/javascript">window.addEventListener("message",function(a){if(void 0!==a.data["datawrapper-height"]){var e=document.querySelectorAll("iframe");for(var t in a.data["datawrapper-height"])for(var r,i=0;r=e[i];i++)if(r.contentWindow===a.source){var d=a.data["datawrapper-height"][t]+"px";r.style.height=d}}});</script>
</center>
An solchen `Singularitäten` dürfen die Spannungen also nicht ausgewertet werden. Wie können wir diese also verhindern?

## Alternative Randbedingungen für feste Einspannung ohne Singularität 

Um den Unterschied zur `Fixed Support` zu sehen fügen wir eine weitere Analyse hinzu:

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Neue Analyse anlegen</p>
    <p>Im Workbench Projektmenü: <code>Static Structural</code> per <code>Drag&Drop</code> auf  <code>Übung 2</code> umbennen.</p>
  <figure style="text-align:center;">
  <img src="../images/Analyse_auf_Model.png" alt="Analyse auf Model" width="400" class="no-lightbox">
  </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Kraft-Randbedingung kopieren</p>
    <p>Im Mechanical: Im Strukturbaum erscheint jetzt eine zweite Analyse, die sich mit der ersten die Geometrie, das Material und das Netz teilt. Randbedingungen und Lösungen sind jedoch separat</p>
    <p>Um die Kraft nicht neu einzugeben kann die Randbedingung <code>Force</code> kann per <code>Drag&Drop</code> auf die Static Stuctural gezogen werden</p>
  <figure style="text-align:center;">
  <img src="../images/RB_drag_n_drop.png" alt="Analyse auf Model" width="300" class="no-lightbox">
  </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Randbedingung Frictionless Support einfügen</p>
    <p>Im Mechanical: Auf die Fläche der Einspannung die Randbedingung <code>Frictionless Support</code> anbringen.</p>
    <figure style="text-align:center;">
    <img src="../images/Frictionless_Support.png" alt="Frictionless Support" width="500" class="no-lightbox">
    </figure>
    <p>Dadurch kann sich die Fläche nur noch in der x-z Ebene bewegen</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Randbedingung Remote Displacement einfügen</p>
    <p>Im Mechanical: Auf die Fläche der Einspannung die Randbedingung <code>Remote Displacement</code> anbringen.</p>
    <figure style="text-align:center;">
    <img src="../images/Remote_Displacement.png" alt="Remote Displacement" width="550" class="no-lightbox">
    </figure>
    <p>Im Detailfenster <code>Verschiebungen</code> und <code>Rotationen</code> auf <code>Null</code> setzen.</p>
    <figure style="text-align:center;">
    <img src="../images/Remote_Displacement_Details.png" alt="Remote Displacement Details" width="300" class="no-lightbox">
    </figure>
    <p>Dadurch wird dauch die Bewegung des gesamten Querschnitts in der x-y Ebene unterdrückt, jedoch kann sich der Balken im Querschnitt trotzdem verformen.</p>
  </div>
</div>

### Die maximale Spannung in y-Richtung $\sigma_{y, \max }$ in MPa

Berechnen Sie nun erneut die Spannung:

<div class="numeric-question" data-answer="87.7" data-tolerance="0.5" data-points="5" data-attempts="5"  data-hints="Spannung in y-Richtung (Längsrichtung des Balkens) ausgewertet?">
</div>

Hier noch mal die neue Lösung im Vergleich mit unterschiedlichen Netzgrößen

<center>
<iframe title="Maximale Spannung bei unterschiedlicher Netzgröße" aria-label="Liniendiagramm" id="datawrapper-chart-2WMO0" src="https://datawrapper.dwcdn.net/2WMO0/6/" scrolling="no" frameborder="0" style="width: 0; min-width: 80% !important; border: none;" height="400" data-external="1"></iframe><script type="text/javascript">window.addEventListener("message",function(a){if(void 0!==a.data["datawrapper-height"]){var e=document.querySelectorAll("iframe");for(var t in a.data["datawrapper-height"])for(var r,i=0;r=e[i];i++)if(r.contentWindow===a.source){var d=a.data["datawrapper-height"][t]+"px";r.style.height=d}}});</script>
</center>