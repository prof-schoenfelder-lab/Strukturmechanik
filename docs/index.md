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
    <p class="kurs-hero-lead">Vier Praktika von der ersten eigenen Simulation bis zum passenden Modell. Mit Schritt-für-Schritt-Anleitungen für ANSYS Workbench und Selbsttests zu jedem Praktikum.</p>
    <div class="kurs-hero-actions">
      <a class="kurs-btn kurs-btn--primary" href="P1_Einfuehrung/">Mit Praktikum 1 starten <span aria-hidden="true">→</span></a>
      <a class="kurs-btn" href="Fortschritt/">Mein Fortschritt</a>
    </div>
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
