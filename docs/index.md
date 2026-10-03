---
icon: material/home
title: Angewandte FEM in der Strukturmechanik
hide:
  - title
  - navigation
  - toc
  - footer
---

<div class="page--home" hidden></div>

<section class="kurs-hero">
  <div class="kurs-hero-text">
    <p class="kurs-kicker">HTWK Leipzig · Fakultät Ingenieurwissenschaften</p>
    <h1 class="kurs-hero-title">Angewandte FEM in der <span>Strukturmechanik</span></h1>
    <div class="kurs-hero-actions">
      <a class="kurs-btn kurs-btn--primary" href="P1_Einfuehrung/">Mit Praktikum 1 starten <span aria-hidden="true">→</span></a>
      <a class="kurs-btn" href="Fortschritt/">Mein Fortschritt</a>
    </div>
    <div class="kurs-opal" id="kurs-opal">
      <div class="kurs-opal-out">
        <span class="kurs-opal-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M10 17l5-5-5-5v3H3v4h7v3zm9 2h-6v2h6c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2h-6v2h6v14z"/></svg></span>
        <div>
          <p class="kurs-opal-title">Fortschritt mit OPAL sichern</p>
          <p>Mit OPAL-Anmeldung werden Ihre Punkte gespeichert und sind auf jedem Gerät verfügbar.</p>
          <p class="kurs-opal-perk"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13,2.05V5.08C16.39,5.57 19,8.47 19,12C19,12.9 18.82,13.75 18.5,14.54L21.12,16.07C21.68,14.83 22,13.45 22,12C22,6.82 18.05,2.55 13,2.05M12,19A7,7 0 0,1 5,12C5,8.47 7.61,5.57 11,5.08V2.05C5.94,2.55 2,6.81 2,12A10,10 0 0,0 12,22C15.3,22 18.23,20.39 20.05,17.91L17.45,16.38C16.17,18 14.21,19 12,19Z"/></svg><span><b>Kursfortschritt:</b> Für jede gelöste Aufgabe gibt es Punkte. Unter Mein Fortschritt sehen Sie Ihren Stand je Praktikum und sammeln Abzeichen.</span></p>
          <p class="kurs-opal-perk"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7,6H17A6,6 0 0,1 23,12A6,6 0 0,1 17,18C15.22,18 13.63,17.23 12.53,16H11.47C10.37,17.23 8.78,18 7,18A6,6 0 0,1 1,12A6,6 0 0,1 7,6M6,9V11H4V13H6V15H8V13H10V11H8V9H6M15.5,12A1.5,1.5 0 0,0 14,13.5A1.5,1.5 0 0,0 15.5,15A1.5,1.5 0 0,0 17,13.5A1.5,1.5 0 0,0 15.5,12M18.5,9A1.5,1.5 0 0,0 17,10.5A1.5,1.5 0 0,0 18.5,12A1.5,1.5 0 0,0 20,10.5A1.5,1.5 0 0,0 18.5,9Z"/></svg><span><b>Minispiele:</b> Im Knackpunkt nehmen Sie Material weg, bis das Bauteil bricht, und spielen um die Bestenliste. Die Runde am Ende jedes Praktikums schalten Sie mit der Anmeldung frei.</span></p>
          <p class="kurs-opal-note">Außerhalb des HTWK-Netzes muss dafür das VPN aktiv sein: <a href="https://itsz.htwk-leipzig.de/dienste/vpn-zugriff-auf-das-hochschulnetz/" target="_blank" rel="noopener">Anleitung des ITSZ</a> (mit HTWK-Login).</p>
          <a class="kurs-opal-link" href="https://bildungsportal.sachsen.de/opal/auth/RepositoryEntry/18448121873/CourseNode/1784428828536783012">Über OPAL anmelden →</a>
        </div>
      </div>
      <div class="kurs-opal-in">
        <span class="kurs-opal-icon kurs-opal-icon--ok" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4z"/></svg></span>
        <div>
          <p class="kurs-opal-title">Über OPAL angemeldet</p>
          <p>Ihre Punkte werden gespeichert und sind auf jedem Gerät verfügbar. Ihre Knackpunkt-Plätze finden Sie unter Mein Fortschritt.</p>
          <p class="kurs-opal-note">Außerhalb des HTWK-Netzes muss für den Abgleich das VPN aktiv sein: <a href="https://itsz.htwk-leipzig.de/dienste/vpn-zugriff-auf-das-hochschulnetz/" target="_blank" rel="noopener">Anleitung des ITSZ</a> (mit HTWK-Login).</p>
          <a class="kurs-opal-link" href="Fortschritt/">Mein Fortschritt →</a>
        </div>
      </div>
    </div>
    <script>
      // Angemeldet (Token gespeichert oder gerade von OPAL zurück): zweite Karte zeigen
      try { if (localStorage.getItem('ac_backend_token') || /[#&]ac_token=/.test(location.hash)) document.getElementById('kurs-opal').classList.add('is-in'); } catch (e) { }
    </script>
  </div>
  <div class="kurs-hero-media"><div class="kurs-anim" role="img" aria-label="Animation: das erste Lösungsbeispiel aus Praktikum 1 durch alle sieben Schritte des Simulations-Workflows"></div></div>
</section>

## Die Praktika

<!-- Daten der Praktika: extra.praktika in mkdocs.yml (auch für die Abschluss-Karte am Ende jedes Praktikums) -->
<div class="prakt-list">
{%- for p in praktika %}
  <a class="prakt-row" href="{{ p.link }}">
    <span class="prakt-body">
      <span class="prakt-label">Praktikum {{ p.nr }}</span>
      <span class="prakt-title">{{ p.titel }}</span>
      <span class="prakt-desc">{{ p.text }}</span>
    </span>
    <img class="prakt-thumb no-lightbox" src="{{ p.bild }}" alt="">
  </a>
{%- endfor %}
</div>

<a class="home-faq" href="00_FAQ/">Fragen? Antworten auf die häufigsten gibt es im <strong>FAQ</strong> →</a>

## Dozenten

<div class="doz-list">
  <a class="doz-item" href="https://bildungsportal.sachsen.de/opal/auth/RepositoryEntry/18448121873/CourseNode/1633401058120725004" target="_blank" rel="noopener noreferrer">
    <img src="assets/people/Felix_Kaule.jpg" alt="Felix Kaule" class="no-lightbox">
    <span class="doz-body">
      <span class="doz-name">M.Eng. Felix Kaule</span>
      <span class="doz-mail">Felix(dot)Kaule(at)htwk-leipzig.de</span>
    </span>
  </a>
  <a class="doz-item" href="https://bildungsportal.sachsen.de/opal/auth/RepositoryEntry/18448121873/CourseNode/1760236690964595011" target="_blank" rel="noopener noreferrer">
    <img src="assets/people/Klaus_Schneller.jpeg" alt="Klaus Schneller" class="no-lightbox">
    <span class="doz-body">
      <span class="doz-name">M.Eng. Klaus Schneller</span>
      <span class="doz-mail">Klaus(dot)Schneller(at)htwk-leipzig(.)de</span>
    </span>
  </a>
  <a class="doz-item" href="https://bildungsportal.sachsen.de/opal/auth/RepositoryEntry/18448121873/CourseNode/98344428551217" target="_blank" rel="noopener noreferrer">
    <img src="assets/people/Stephan_Schoenfelder.png" alt="Prof. Dr.-Ing. Stephan Schönfelder" class="no-lightbox">
    <span class="doz-body">
      <span class="doz-name">Prof. Dr.-Ing. Stephan Schönfelder</span>
      <span class="doz-mail">Stephan(dot)Schoenfelder(at)htwk-leipzig.de</span>
    </span>
  </a>
</div>
