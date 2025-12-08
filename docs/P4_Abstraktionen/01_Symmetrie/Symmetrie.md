---
icon: material/math-norm
hide:
  - toc
---

# Ausnutzung von Symmetrien

Der einfachste Weg, Rechenzeit zu sparen, ist die Ausnutzung von Symmetrien. Schauen wir uns das an einem Beispiel an:

<figure style="text-align:left;">
    <img src="../images/SymmetrieBsp.excalidraw.png" alt="Beispielmodell" width="500" class="no-lightbox">
</figure>

Die erste offensichtliche **Symmetrieebene** liegt in der Mitte zwischen den Lagern:

<figure style="text-align:left;">
    <img src="../images/SymmetrieBsp-Symmetrie.excalidraw.png" alt="Symmetrieebene" width="600" class="no-lightbox">
</figure>

Um eine Symmetrie zu verwenden, müssen bei der Spiegelung um diese Symmetrieebene folgende Komponenten identisch zum Vollmodell bleiben:

- [ ] Geometrie  
- [ ] Lasten  
- [ ] Lagerung  

Prüfen wir dies nun im Folgenden:

<figure style="text-align:left;">
    <img src="../images/SymmetrieBsp-Geometrie.excalidraw.png" alt="Geometrieprüfung Symmetrie" width="600" class="no-lightbox">
</figure>

!!! success "Geometrie ist symmetrisch"

<figure style="text-align:left;">
    <img src="../images/SymmetrieBsp-Lasten.excalidraw.png" alt="Lasten Symmetrie" width="600" class="no-lightbox">
</figure>

!!! success "Lasten sind symmetrisch"

<figure style="text-align:left;">
    <img src="../images/SymmetrieBsp-Lagerung.excalidraw.png" alt="Lagerung Symmetrie" width="800" class="no-lightbox">
</figure>

!!! failure "Lagerung ist nicht symmetrisch"

    Wir haben jetzt rechts und links jeweils ein Festlager. Das entspricht nicht dem Originalmodell.

Auf den ersten Blick scheint das ein Problem zu sein. Das ursprüngliche Festlager (egal ob rechts oder links im Vollmodell) haben wir jedoch nur eingeführt, um **Starrkörperbewegungen** zu verhindern, also um zu vermeiden, dass sich das Bauteil als Ganzes in y-Richtung verschiebt.

Hier hilft uns nun die Definition der Symmetrieebene selbst:

!!! info "Definition Symmetrieebene"

    Punkte, die auf der Symmetrieebene liegen, bleiben bei einer symmetrischen Belastung **in dieser Ebene**.  
    Das bedeutet:
    
    - die Verschiebung **senkrecht zur Ebene** ist dort null  
    - die Verformung ist zur Ebene hin **spiegelsymmetrisch** (keine „Knicke“ in der Ebene)

Da die Symmetrieebene nun dafür sorgt, dass sich die Geometrie in der Mitte nicht mehr nach rechts und links bewegen kann, brauchen wir das Festlager nicht mehr – die Symmetriebedingungen übernehmen diesen Job.  

Wir können an dieser Stelle daher ein **Loslager** verwenden:

<figure style="text-align:left;">
    <img src="../images/SymmetrieBsp-Symmetrie-Lagerung.excalidraw.png" alt="Lagerung mit Symmetrie" width="1100" class="no-lightbox">
</figure>

Man kann es sich auch so vorstellen: Durch die Symmetrie verhalten sich die beiden „Hälften“ rechts und links identisch:

<figure style="text-align:left;">
    <img src="../images/SymmetrieBsp-Symmetrie-Voll.excalidraw.png" alt="Volle Symmetrie" width="600" class="no-lightbox">
</figure>

Da es jedoch unnötig wäre, zwei Systeme zu berechnen, die sich ohnehin gleich verhalten, berechnet man nur **eine Hälfte** (z.&nbsp;B. die linke) mit passenden Symmetrie-Randbedingungen.

# Aufteilung von Kräften

Werden Kräfte auf Linien oder Flächen angebracht und diese durch Symmetrieebenen geteilt, so müssen die Kraftwerte auch durch die Anzahl der Teilungen geteilt werden. Hier folgendes Beispiel:

<figure style="text-align:left;">
    <img src="../images/Kraft.excalidraw.png" alt="Kraftaufteilung" width="400" class="no-lightbox">
</figure>

Werden jedoch Drücke angegeben, müssen diese nicht geteilt werden weil diese ja bereits Flächennormiert sind.