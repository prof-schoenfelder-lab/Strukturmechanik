---
icon: connectdevelop
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
---

# Grundprinzipien der Finiten-Elemente-Methode

Im folgenden ist die Vorgehensweise der Finiten-Elemente-Methode an Hand des Workflows in grob skizziert.

{% stepper %}
{% step %}
### Geometrie

Zunächst wird ein **Bauteil erstellt** (in ANSYS) oder ein bereits vorhandes Bauteil **eingeladen** (z.B. aus CATIA)

<figure><img src="../.gitbook/assets/image (1).png" alt="" width="340"><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Material

Es muss ein Material gewählt werden. Die relevanten Materialparameter sind dabei das **Elastizitätsmodul** **E** und die **Querkontraktion µ**.

<figure><img src="../.gitbook/assets/image (2).png" alt="" width="375"><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Elemente (Vernetzung)

Das Bauteil wird nun mit kleinen (finiten) Elementen vernetzt.&#x20;

<figure><img src="../.gitbook/assets/image (3).png" alt="" width="340"><figcaption></figcaption></figure>

Die Elemente bestehen aus Knoten .&#x20;

<figure><img src="../.gitbook/assets/image (4).png" alt="" width="186"><figcaption></figcaption></figure>

Jeder Knoten besitzt **Freiheitsgrade** (in unserem Falle sind es Verschiebungen in alle drei Raumrichtungen).&#x20;

<figure><img src="../.gitbook/assets/image (5).png" alt="" width="95"><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Lagerung und Belastung

Die **Lagerung** dient dazu, dass das Bauteil keine Starrkörperbewegung ausführt und dem realen System entspricht. In unserem Beispiel wird dies durch die feste Einspannung gelöst. Dabei werden für alle Knoten am linken Ende die Verschiebungen in alle 3 Raumrichtungen auf Null gesetzt.&#x20;

Die **Belastung** kommt in dem Beispiel durch die Kraft, die sich auf die oberen 3 Knoten verteilt.

<div data-full-width="false"><figure><img src="../.gitbook/assets/image (6).png" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
### Bestimmung der offenen Freheitsgrade&#x20;

Nun wird mit Hilfe von mathematischen Operationen die Freiheitsgrade (also Verschiebungen in alle 3 Raumrichtungen) für alle restlichen Knoten im Bauteil bestimmt.
{% endstep %}
{% endstepper %}

### Weiterführendes Material

In folgendem Video (auf englisch) wird dies noch mal etwas genauer verdeutlicht.

{% embed url="https://youtu.be/GHjopp47vvQ?si=A3tWgas6YkJ74YEL" %}
