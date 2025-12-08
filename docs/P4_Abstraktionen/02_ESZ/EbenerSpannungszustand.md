---
icon: material/texture-box
hide:
  - toc
---

# Ebener Spannungszustand

Unser nächstes Thema ist die erste „richtige“ Abstraktionsmöglichkeit: die `2D-Abstraktion`.  
Dabei wird das 3D-Modell um eine Dimension reduziert und nur noch als Ebene/Fläche betrachtet.

<figure style="text-align:left;">
    <img src="../images/2D_ebener_Spannungszustand.excalidraw.png" alt="ebener Spannungszustand" width="800" class="no-lightbox">
</figure>

In diesem Fall ist die reduzierte Dimension – die Dicke des Balkens in z-Richtung – deutlich kleiner als die übrigen Bauteilabmessungen. Man spricht dann von einem `ebenen Spannungszustand`.

# Vergleich zum ebenen Verzerrungszustand

Wir schauen uns nun wieder das Beispiel mit dem Balken auf zwei Stützen an, um den Unterschied zwischen `ebenem Spannungszustand` und `ebenem Verzerrungszustand` zu verdeutlichen.   Ziel ist es, die Durchbiegung und die dadurch entstehenden Spannungen zu bestimmen.

Wie oben gelernt, betrachten wir beim **ebenen Spannungszustand** einen Schnitt, in dem die Dicke sehr gering ist (z-Richtung klein). Die Balkenlänge bleibt im 2D-Modell erhalten – die Biegelinie \(w(x)\) kann sich also ganz normal ausbilden. Das passt zu unserem Balkenbeispiel.

Beim **ebenen Verzerrungszustand** ist es genau umgekehrt:  
Hier wird angenommen, dass sich das Bauteil in einer Richtung praktisch **nicht** verformen darf (\(\varepsilon = 0\)) und alle Größen entlang dieser Richtung konstant sind. Man modelliert also einen Querschnitt eines „sehr langen“ Körpers, der sich in Längsrichtung nicht dehnt.

Übertragen auf unser Balkenbeispiel:  
Wenn wir den Balken so abstrahieren, dass gerade seine **Längsrichtung** zur „eingefrorenen“ Richtung des ebenen Verzerrungszustands wird, kann sich im Modell keine Krümmung mehr einstellen – es gibt keine Biegelinie und damit keine realistische Durchbiegung. Für die Berechnung der Durchbiegung ist der **ebene Verzerrungszustand** daher ungeeignet; hier ist der **ebene Spannungszustand** die richtige Abstraktion.

<figure style="text-align:left;">
    <img src="../images/2D_ebener_Spannungs_vs_Verzerrungszustand.excalidraw.png" alt="ebener Spannungs- vs. Verzerrungszustand" width="1100" class="no-lightbox">
</figure>

!!! info "Merksatz"

    **Ebener Spannungszustand:**  
    Dicke viel kleiner als die Querschnittsmaße  
    (z. B. Balken von der Seite, dünne Platten/Bleche)

    **Ebener Verzerrungszustand:**  
    Ausgedehnte Richtung viel größer als die Querschnittsmaße, Dehnung in dieser Richtung ≈ 0  
    (z. B. Staudamm im Querschnitt, sehr lange Tunnel-/Rohrsegmente)
