---
title: ANSYS Installation
icon: material/download-box
hide:
  - toc
---


!!! warning "Studentenversion"

    Es gibt neben der Version die im PC Pool installiert ist auch eine kostenlose Studentenversion. Die ist zum einen immer die aktuellste Version, hat aber den Nachteil, dass die Anzahl an Knoten limitiert ist. Dadurch sind manche Praktika eventuell nicht möglich. Die Empfehlung für das Praktikum ist deshalb die Nicht-Studenten Version zu installieren (Anleitung unten)



# ANSYS Installations Anleitung für Version im PC Pool ANSYS2025R2

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">VPN-Client installieren und aktivieren</p>
    <p>Auf dem nachfolgenden Link mit dem HTWK Login anmelden um Download Link zu sehen: <a href="https://itsz.htwk-leipzig.de/dienste/vpn-zugriff-auf-das-hochschulnetz" target="_blank">HTWK-ITSZ-VPN</a></p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">ANSYS2025R2 runterladen</p>
    <p>ANSYS Downloadlink im OPAL: <a href="https://bildungsportal.sachsen.de/opal/auth/RepositoryEntry/18448121873/CourseNode/102618893872254" target="_blank">HTWK OPAL LINK</a></p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">ZIP entpacken, alle ISO-Dateien (bei 2025R2 acht Stück, DISK1 bis DISK8) mounten und die setup.exe der ersten ausführen</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Lizenzserver angeben</p>
    <p>Server: ansys.htwk-leipzig.de</p>
    <p>Port: 1055</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Zwingend notwendige Installationspakete</p>
    <p> Design / SpaceClaim </p>
    <p> Structures / Mechanical Products </p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">SpaceClaim-Paket installieren</p>
    <p>Nach der Grundinstallation im Download den Ordner <code>SPACECLAIM_2025R2_WINX64</code> öffnen und dort die <code>setup.exe</code> ausführen. Als Lizenzserver wieder <code>ansys.htwk-leipzig.de</code> mit Port <code>1055</code> angeben.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Service Pack 05 installieren (immer als Letztes)</p>
    <p>Im Download den Ordner <code>ANSYS_2025R2.05_WINX64</code> öffnen und die <code>setup.exe</code> ausführen. Das Service Pack bringt alle installierten Teile, auch SpaceClaim, auf den aktuellen Stand. Deshalb erst nach dem SpaceClaim-Paket installieren.</p>
  </div>

</div>

!!! warning "Discovery nicht zusätzlich installieren"

    Liegt im Download auch ein Einzelpaket für Discovery, dieses nicht installieren: Discovery ist in der Grundinstallation schon enthalten, und das zusätzliche Paket bricht bei einer bestehenden Installation mit einem Fehler ab.



