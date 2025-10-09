// Local-only numeric answer checker (single clean IIFE)
(function () {
  'use strict';

  function safeJSONParse(s){ try { return JSON.parse(s); } catch (e) { return null; } }

  // Configuration: attempts allowed per question
  var ATTEMPTS_ALLOWED = 5;

  // Player/Per-page helpers
  function getPageId(){ try { return encodeURIComponent(window.location.pathname || window.location.href); } catch(e){ return String(window.location.pathname || window.location.href); } }
  function pageClaimKey(pid){ return 'page_claimed_' + pid; }
  function isPageClaimed(pid){ return localStorage.getItem(pageClaimKey(pid)) === '1'; }
  function setPageClaimed(pid){ try { localStorage.setItem(pageClaimKey(pid), '1'); } catch(e){} }
  function getPlayerLevel(){ return parseInt(localStorage.getItem('player_level')||'0',10) || 0; }
  function setPlayerLevel(n){ try { localStorage.setItem('player_level', String(n)); } catch(e){} }
  function incrementPlayerLevel(){ var l = getPlayerLevel(); l += 1; setPlayerLevel(l); updatePlayerBadge(); try{ showLevelUp(l); }catch(e){} }

  // ensure styles for level-up notification/animation exist
  function ensureLevelUpStyles(){
    try{
      if (window.__answerCheckerLevelStyles) return;
      var css = '\n' +
        '.ac-level-overlay{position:fixed;left:0;top:0;width:100%;height:100%;pointer-events:none;z-index:9999;overflow:hidden}\n' +
  '.ac-spark{position:absolute;left:50%;top:40%;width:10px;height:10px;border-radius:50%;transform:translate(-50%,-50%);opacity:1;filter:drop-shadow(0 3px 6px rgba(0,0,0,0.20))}\n' +
        '@keyframes ac-spark-move{0%{opacity:1;transform:translate(-50%,-50%) scale(1)}100%{opacity:0;transform:translate(var(--tx),var(--ty)) scale(0.6)}}\n' +
        '.ac-spark.move{animation:ac-spark-move 2200ms cubic-bezier(.22,.9,.4,1) forwards}\n' +
        '.ac-toast{position:fixed;right:20px;bottom:20px;background:linear-gradient(135deg,#111827,#1f2937);color:#fff;padding:12px 16px;border-radius:12px;box-shadow:0 8px 24px rgba(0,0,0,0.35);z-index:10001;pointer-events:auto;opacity:0;transform:translateY(10px);transition:opacity .24s,transform .24s;font-family:system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif}\n' +
        '.ac-toast.show{opacity:1;transform:translateY(0)}\n' +
        '.ac-toast .title{font-weight:700;margin-bottom:6px;display:block;font-size:1.05rem}\n' +
        '.ac-toast .desc{font-size:0.95rem;opacity:0.95}\n';
      var s = document.createElement('style'); s.id = 'answer-checker-level-styles'; s.appendChild(document.createTextNode(css)); document.head.appendChild(s);
      window.__answerCheckerLevelStyles = true;
    }catch(e){}
  }

  // show a small firework-like particle burst and a toast notification for level up
  function showLevelUp(level){
    try{
      ensureLevelUpStyles();
      // overlay
      var overlay = document.createElement('div'); overlay.className = 'ac-level-overlay';
      // create multi-colored sparks
      var colors = ['#ff7f50','#ffd700','#7cfc00','#00bfff','#ff6fbf','#ffa500'];
      for (var i = 0; i < 24; i++){
        var sp = document.createElement('span'); sp.className = 'ac-spark';
        var angle = (Math.PI * 2) * (i / 12) + (Math.random() * 0.5 - 0.25);
        var angleOffset = (Math.random()*0.8 - 0.4);
        angle = (Math.PI * 2) * (i / 24) + angleOffset;
        var dist = 140 + Math.random() * 420; // px (bigger spread)
        var tx = Math.round(Math.cos(angle) * dist) + 'px';
        var ty = Math.round(Math.sin(angle) * dist) + 'px';
        sp.style.setProperty('--tx', tx);
        sp.style.setProperty('--ty', ty);
        sp.style.background = colors[i % colors.length];
        overlay.appendChild(sp);
        // kick animation slightly staggered
        (function(el, delay){ setTimeout(function(){ try{ el.classList.add('move'); }catch(e){} }, delay); })(sp, i * 30 + Math.random()*140);
      }
      document.body.appendChild(overlay);
      // remove overlay after animation (allow some buffer)
      setTimeout(function(){ try{ overlay.parentNode && overlay.parentNode.removeChild(overlay); }catch(e){} }, 2600);

      // toast
      var toast = document.createElement('div'); toast.className = 'ac-toast';
      toast.innerHTML = '<span class="title">Level ' + (parseInt(level,10) || '') + ' erreicht!</span><span class="desc">Gut gemacht — weiter so!</span>';
      document.body.appendChild(toast);
  // show
  setTimeout(function(){ try{ toast.classList.add('show'); }catch(e){} }, 20);
  // hide and remove after longer display
  setTimeout(function(){ try{ toast.classList.remove('show'); setTimeout(function(){ try{ toast.parentNode && toast.parentNode.removeChild(toast); }catch(e){} }, 300); }catch(e){} }, 7000);
    }catch(e){}
  }

  function updatePlayerBadge(){
    var header = document.querySelector('.md-header__inner');
    if (!header) return;
    var id = 'player-badge';
    var el = document.getElementById(id);
    var level = getPlayerLevel();
    if (!el){
      el = document.createElement('div'); el.id = id; el.className = 'player-badge';
      // insert at the beginning of header title area if present
      var logo = document.querySelector('.md-header__button.md-logo');
      if (logo && logo.parentNode) logo.parentNode.insertBefore(el, logo.nextSibling);
      else header.insertBefore(el, header.firstChild);
    }
    // allow a stored/custom icon (svg or emoji) under player_icon key or data attribute on body
    var custom = localStorage.getItem('player_icon') || document.body && document.body.dataset.playerIcon;
    var iconHtml = custom ? '<span class="player-icon">' + custom + '</span>' : '<span class="player-icon">🛡️</span>';
    el.innerHTML = iconHtml + '<span class="player-level">' + level + '</span>';
  }

  // --- Per-page reset button (hidden by default) ---
  function createPerPageResetIfAllowed(){
    try{
      var allow = (document.body && document.body.dataset && document.body.dataset.showReset === '1') || location.hostname === 'localhost' || location.hostname === '127.0.0.1';
      if (!allow) return;
      var header = document.querySelector('.md-header__inner'); if (!header) return;
      var id = 'answer-reset-page-btn'; if (document.getElementById(id)) return;
      var btn = document.createElement('button'); btn.id = id; btn.className = 'answer-reset-page'; btn.type = 'button'; btn.textContent = 'Reset Ergebnisse (Seite)';
      btn.addEventListener('click', function(){
        if (!confirm('Alle lokalen Ergebnisse für diese Seite entfernen? Diese Aktion ist lokal und unwiderruflich.')) return;
        var path = location.pathname || location.href;
        var pathEnc = encodeURIComponent(path);
        var pathNoSlash = (path && path.length > 1 && path.endsWith('/')) ? path.slice(0,-1) : path;
        var removed = 0; var keys = Object.keys(localStorage);
        // prepare backup
        var backup = {};
        keys.forEach(function(k){ try{
            if (!k) return;
            // match keys that are answer_* and reference this page by either raw or encoded path
            if (k.indexOf('answer_') === 0 && (k.indexOf(path) !== -1 || k.indexOf(pathEnc) !== -1 || k.indexOf(pathNoSlash) !== -1)){
              backup[k] = localStorage.getItem(k);
            }
          }catch(e){}
        });
        // store backup (if any)
        try{
          var ts = Date.now();
          var bkey = 'answer_backup_' + encodeURIComponent(path) + '_' + ts;
          if (Object.keys(backup).length > 0){ try { localStorage.setItem(bkey, JSON.stringify(backup)); } catch(e){} }
        }catch(e){ console.warn('Could not save backup', e); }
        // remove keys (same matching as backup)
        keys.forEach(function(k){ try{
            if (!k) return;
            if (k.indexOf('answer_') === 0 && (k.indexOf(path) !== -1 || k.indexOf(pathEnc) !== -1 || k.indexOf(pathNoSlash) !== -1)){
              localStorage.removeItem(k); removed++;
            }
          }catch(e){}
        });
        // also remove the page-claimed marker so the nav icon is unset
        try{
          var pid = encodeURIComponent(path);
          var claimKey = pageClaimKey(pid);
          if (localStorage.getItem(claimKey)) { try { localStorage.removeItem(claimKey); } catch(e){} }
          // reset nav icon and stars for this page
          try { replaceNavIcon(pid, blankCircleOutlineSvg); } catch(e){}
          try { updateStarsForPage(pid); } catch(e){}
        }catch(e){}
        // also reset global player progress so the player level/rank returns to zero
        try{
          if (localStorage.getItem('player_level')) { try { localStorage.removeItem('player_level'); } catch(e){} }
          if (localStorage.getItem('player_icon')) { try { localStorage.removeItem('player_icon'); } catch(e){} }
        }catch(e){}
        /* removed debug logs */
        location.reload();
      });
      // place to the right in header
      header.appendChild(btn);
    }catch(e){ }
  }

  // --- Debug panel for authors: show localStorage and per-question state ---
  // debug panel removed

  // --- Stars for Selbsttests (0..3) ---
  function computePagePercent(pid){
    try{
      var pagePath = decodeURIComponent(pid);
      function normalizePath(p){ try{ var s = String(p||''); if (!s.startsWith('/')){ try{ s = new URL(s, location.href).pathname; }catch(e){} } s = decodeURIComponent(s); if (s.length > 1 && s.endsWith('/')) s = s.slice(0,-1); return s; }catch(e){ return String(p||''); } }
      var normPage = normalizePath(pagePath);
      var sumBest = 0, sumMax = 0;
      for (var i = 0; i < localStorage.length; i++){
        var k = localStorage.key(i);
        if (!k || k.indexOf('answer_best_') !== 0) continue;
        var qid = k.replace('answer_best_', '');
        var base = String(qid).split(':q')[0] || qid;
        var normBase = normalizePath(base);
        if (normBase !== normPage) continue; // only questions from this page
        var rec = safeJSONParse(localStorage.getItem(k));
        if (rec && typeof rec.points === 'number') sumBest += rec.points;
        var maxVal = parseFloat(localStorage.getItem('answer_max_' + qid));
        if (isFinite(maxVal)) sumMax += maxVal;
      }
      if (sumMax <= 0) return 0;
      return Math.max(0, Math.min(1, sumBest / sumMax));
    }catch(e){ return 0; }
  }

  function renderStarsForPercent(pct){
    // map pct (0..1) to 0..5 stars using rounding
    var stars = Math.round(Math.max(0, Math.min(1, pct)) * 5);
    var out = '<span class="page-stars" aria-hidden="true">';
    for (var i = 0; i < 5; i++){
      out += '<span class="star' + (i < stars ? ' filled' : '') + '">★</span>';
    }
    out += '</span>';
    return out;
  }

  function updateStarsForPage(pid){
    try{
      var pct = computePagePercent(pid);
      var starsHtml = renderStarsForPercent(pct);
      var links = document.querySelectorAll('.md-nav__link');
      links.forEach(function(link){
        var href = link.getAttribute('href'); if (!href) return;
        try{
          var url = new URL(href, location.href);
          var linkPath = url.pathname || '';
          if (linkPath.indexOf('/03_Selbsttests/') !== -1 || linkPath.indexOf('/Selbsttests/') !== -1){
            if (encodeURIComponent(url.pathname) === pid){
              var existing = link.querySelector('.page-stars');
              if (existing){
                // only replace if different to avoid triggering mutation observers
                try{ if ((existing.outerHTML || '').trim() !== (starsHtml || '').trim()) existing.outerHTML = starsHtml; }catch(e){}
              } else {
                var span = link.querySelector('.md-ellipsis') || link;
                // avoid inserting duplicate if already present
                if (!span.querySelector || !span.querySelector('.page-stars')){
                  var wrap = document.createElement('span'); wrap.innerHTML = starsHtml;
                  span.appendChild(wrap.firstChild);
                }
              }
            }
          }
        }catch(e){}
      });
    }catch(e){}
  }

  // Material-like SVGs for nav icon swapping
  var blankCircleOutlineSvg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 10 10A10.011 10.011 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8.009 8.009 0 0 1-8 8z"/></svg>';
  var markedCircleSvg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 10 10A10.011 10.011 0 0 0 12 2zm-1 15l-5-5 1.41-1.41L11 14.17l6.59-6.59L19 9z"/></svg>';
  // icon to show when a test is claimed but yields 0 stars (checkbox-blank-circle)
  var zeroStarCircleSvg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor"/><circle cx="12" cy="12" r="3" fill="currentColor"/></svg>';

  function initializeNavIcons(){
    try{
      var links = document.querySelectorAll('.md-nav__link');
      var pid = getPageId();
      links.forEach(function(link){
        var href = link.getAttribute('href'); if (!href) return;
        try{
          var url = new URL(href, location.href);
          var linkPath = url.pathname || '';
          // only initialize icons for Selbsttests navigation items
          if (linkPath.indexOf('/03_Selbsttests/') !== -1 || linkPath.indexOf('/Selbsttests/') !== -1){
            var linkPid = encodeURIComponent(url.pathname);
            try { updateStarsForPage(linkPid); } catch(e){}
            try{
              if (isPageClaimed(linkPid)){
                try{ var pct = computePagePercent(linkPid); if (pct === 0) replaceNavIcon(linkPid, zeroStarCircleSvg); else replaceNavIcon(linkPid, markedCircleSvg); } catch(e){ replaceNavIcon(linkPid, markedCircleSvg); }
              } else replaceNavIcon(linkPid, blankCircleOutlineSvg);
            }catch(e){}
          }
        }catch(e){}
      });
    }catch(e){}
  }

  function updateNavForPageClaim(pid){
    try{ updateStarsForPage(pid); } catch(e){}
    try{ var pct = computePagePercent(pid); if (pct === 0) replaceNavIcon(pid, zeroStarCircleSvg); else replaceNavIcon(pid, markedCircleSvg); } catch(e){}
  }

  // Ensure we re-apply nav icons/stars if the theme re-renders the nav.
  // Uses MutationObserver when available and safe; falls back to short polling.
  function ensureNavObserver(){
    try{
      if (window.__answerCheckerNavObserverInstalled) return;
      var attempts = 0;
      var maxAttempts = 8;
      function tryAttach(){
        var nav = document.querySelector('.md-nav') || document.querySelector('nav') || document.querySelector('.md-sidebar');
        if (nav && nav.nodeType === 1){
          try{
            if (typeof MutationObserver !== 'undefined'){
                var mo = new MutationObserver(function(){
                  try{
                    // schedule a single debounced nav update to avoid feedback loops
                    scheduleNavUpdate();
                  }catch(e){}
                });
              try{
                // guard observe call - ensure nav is a Node
                if (nav && typeof nav.nodeType === 'number') mo.observe(nav, { childList: true, subtree: true });
                window.__answerCheckerNavObserver = mo;
                window.__answerCheckerNavObserverInstalled = true;
              }catch(e){
                // if observe fails, fall back to polling
                console.warn('answer-checker: observer.observe failed, using polling fallback', e);
                var poll = setInterval(function(){ try{ initializeNavIcons(); }catch(e){} }, 500);
                window.__answerCheckerNavPoll = poll; window.__answerCheckerNavObserverInstalled = true;
              }
            } else {
              var poll2 = setInterval(function(){ try{ initializeNavIcons(); }catch(e){} }, 500);
              window.__answerCheckerNavPoll = poll2; window.__answerCheckerNavObserverInstalled = true;
            }
          }catch(e){}
        } else {
          attempts++;
          if (attempts <= maxAttempts) setTimeout(tryAttach, 300);
        }
      }
      tryAttach();
    }catch(e){ console.warn('answer-checker: ensureNavObserver failed', e); }
  }

    // Debounced and rate-limited nav update scheduler to avoid infinite mutation feedback loops
    function scheduleNavUpdate(){
      try{
        if (!window.__answerCheckerNavUpdateCount) window.__answerCheckerNavUpdateCount = 0;
        // limit total updates per page session to avoid runaway loops
        if (window.__answerCheckerNavUpdateCount > 50) return;
        window.__answerCheckerNavUpdateCount += 1;
        if (window.__answerCheckerNavUpdateTimer) clearTimeout(window.__answerCheckerNavUpdateTimer);
        window.__answerCheckerNavUpdateTimer = setTimeout(function(){
          try{ initializeNavIcons(); }catch(e){}
          window.__answerCheckerNavUpdateTimer = null;
        }, 250);
      }catch(e){}
    }

  // allow per-page nav icon override: data-page-icon on the page container
  // replace the nav link's inline SVG for a page identified by pid
  function replaceNavIcon(pid, svgHtml){
    try{
      var links = document.querySelectorAll('.md-nav__link');
      links.forEach(function(link){
        var href = link.getAttribute('href'); if (!href) return;
        try{
          var url = new URL(href, location.href);
          if (encodeURIComponent(url.pathname) === pid){
            var existing = link.querySelector('svg');
            if (existing){
              try{ if ((existing.outerHTML || '').trim() !== (svgHtml || '').trim()) existing.outerHTML = svgHtml; }catch(e){}
            } else {
              // avoid inserting duplicate if already first child equals svgHtml
              var first = link.firstElementChild;
              if (!(first && first.outerHTML && first.outerHTML.trim() === (svgHtml || '').trim())){
                var wrap = document.createElement('span'); wrap.innerHTML = svgHtml; link.insertBefore(wrap.firstChild, link.firstChild);
              }
            }
          }
        }catch(e){}
      });
    }catch(e){}
  }

  function checkPageCompletion(){
    var pid = getPageId();
    // If already claimed, ensure UI updated and return
    if (isPageClaimed(pid)){ updatePlayerBadge(); updateNavForPageClaim(pid); return; }
    var qs = document.querySelectorAll('.numeric-question');
    if (!qs || qs.length === 0) return;
    // All questions must have a stored best > 0
    for (var i = 0; i < qs.length; i++){
      var q = qs[i];
      var qid = q.dataset.qid || ((document.location.pathname || location.href) + ':q' + i);
      var rec = safeJSONParse(localStorage.getItem('answer_best_' + qid));
      if (!rec || !(rec.points > 0)) return; // not completed yet
    }
    // All completed → award level if not yet awarded for this page
    setPageClaimed(pid);
    incrementPlayerLevel();
    // if page provided a custom icon, use it
    var pageIcon = document.body && document.body.dataset.pageIcon;
    if (!pageIcon){
      // also check first question container for data-page-icon
      var first = document.querySelector('.numeric-question'); if (first && first.dataset.pageIcon) pageIcon = first.dataset.pageIcon;
    }
    // show marked checkbox when claimed; if pageIcon is present and is an SVG/string we could use it,
    // but default to material-like check-circle SVG replacement
    var markedSvg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 10 10A10.011 10.011 0 0 0 12 2zm-1 15l-5-5 1.41-1.41L11 14.17l6.59-6.59L19 9z"/></svg>';
    if (pageIcon){
      // if pageIcon is raw svg markup, use it; otherwise fall back to checked icon (but respect zero-star state)
      var chosen = pageIcon.indexOf && pageIcon.indexOf('<svg') === 0 ? pageIcon : markedSvg;
      try{ var pct2 = computePagePercent(pid); if (pct2 === 0) chosen = zeroStarCircleSvg; } catch(e){}
      replaceNavIcon(pid, chosen);
    } else {
      try{ var pct3 = computePagePercent(pid); if (pct3 === 0) replaceNavIcon(pid, zeroStarCircleSvg); else replaceNavIcon(pid, markedSvg); } catch(e){ replaceNavIcon(pid, markedSvg); }
    }
  }

  function computeTotals(){
    var all = 0, today = 0, details = [];
    var todayKey = new Date().toISOString().slice(0,10);
    for (var i = 0; i < localStorage.length; i++){
      var k = localStorage.key(i);
      if (!k || k.indexOf('answer_best_') !== 0) continue;
      var rec = safeJSONParse(localStorage.getItem(k));
      if (!rec || typeof rec.points !== 'number') continue;
      all += rec.points;
      var d = rec.updated ? new Date(rec.updated).toISOString().slice(0,10) : null;
      if (d === todayKey) today += rec.points;
      details.push({ qid: k.replace('answer_best_', ''), points: rec.points, updated: rec.updated });
    }
    details.sort(function(a,b){ return b.points - a.points; });
    return { allTime: all, today: today, details: details };
  }

  // Remove answer entries older than `maxAgeMs` (default 12h)
  function cleanupOldEntries(maxAgeMs) {
    maxAgeMs = typeof maxAgeMs === 'number' ? maxAgeMs : 12 * 60 * 60 * 1000; // 12h
    var now = Date.now();
    var toRemove = [];
    for (var i = 0; i < localStorage.length; i++){
      var k = localStorage.key(i);
      if (!k || k.indexOf('answer_best_') !== 0) continue;
      var rec = safeJSONParse(localStorage.getItem(k));
      if (!rec || !rec.updated) { continue; }
      var t = Date.parse(rec.updated);
      if (!isFinite(t)) continue;
      if ((now - t) > maxAgeMs) {
        toRemove.push(k);
      }
    }
    toRemove.forEach(function(k){
      try { localStorage.removeItem(k); localStorage.removeItem('answer_attempts_' + k.replace('answer_best_', '')); } catch(e){}
    });
  }

  function renderSummary(){
    var el = document.getElementById('leaderboard-summary'); if (!el) return;
    // cleanup old entries first (default 24h)
    cleanupOldEntries();
    var t = computeTotals(); el.innerHTML = '';
    var max = 0;
    for (var i = 0; i < localStorage.length; i++){
      var k = localStorage.key(i);
      if (!k) continue;
      if (k.indexOf('answer_max_') === 0){
        var mp = parseFloat(localStorage.getItem(k));
        if (isFinite(mp)) max += mp;
      }
    }
    if (max === 0){
      var questions = document.querySelectorAll('.numeric-question');
      for (var j = 0; j < questions.length; j++){
        var p = parseFloat(questions[j].dataset.points || 0);
        if (isFinite(p)) max += p;
      }
    }
    // If no explicit max could be determined (e.g. leaderboard opened standalone), try to infer
    // from stored per-question bests or per-question max entries. This avoids showing 0% when
    // the user does have stored points but no answer_max_* keys.
    if (max === 0 && t.details && t.details.length > 0){
      for (var d = 0; d < t.details.length; d++){
        var qid = t.details[d].qid;
        var mp2 = parseFloat(localStorage.getItem('answer_max_' + qid));
        if (isFinite(mp2)) max += mp2; else max += (parseFloat(t.details[d].points) || 0);
      }
    }
    var pct = (max > 0) ? Math.round((t.allTime / max) * 100) : (t.allTime > 0 ? 100 : 0);

    // Fun rank system
    var rank = '';
    var rankDesc = '';
    if (pct < 25) { rank = 'Finites-Element'; rankDesc = 'Willkommen in der Welt der Elemente!'; }
    else if (pct < 50) { rank = 'Knotenknacker'; rankDesc = 'Du knackst Knoten wie Nüsse.'; }
    else if (pct < 75) { rank = 'Balkenbändiger'; rankDesc = 'Balken zähmst du mit Stil.'; }
    else { rank = 'Elemente‑Meister'; rankDesc = 'Du herrschst über die Elemente!'; }

    var stats = document.createElement('div'); stats.className = 'leaderboard-stats';
    stats.innerHTML = '<div><strong>Deine Punkte (aktuell)</strong>: ' + t.allTime + ' Punkte</div>' +
                      '<div><strong>Max möglich</strong>: ' + max + ' Punkte</div>' +
                      '<div><strong>Erreicht</strong>: ' + pct + '%</div>' +
                      '<div class="leaderboard-badge">Rang: <strong>' + rank + '</strong> — ' + rankDesc + '</div>';
    el.appendChild(stats);

    // We intentionally do not show a per-question detail table here — only overall own score and max.
  }

  // Observe content changes and render summary when the leaderboard placeholder is inserted.
  function ensureContentObserver(){
    try{
      if (window.__answerCheckerContentObserverInstalled) return;
      var attempts = 0, maxAttempts = 8;
      function tryAttach(){
        var container = document.querySelector('main') || document.querySelector('.md-content') || document.body;
        if (container && container.nodeType === 1){
          if (typeof MutationObserver !== 'undefined'){
            var mo = new MutationObserver(function(muts){
              try{
                // if leaderboard placeholder is present, render summary
                if (document.getElementById('leaderboard-summary')) renderSummary();
              }catch(e){}
            });
            try{ mo.observe(container, { childList: true, subtree: true }); window.__answerCheckerContentObserver = mo; window.__answerCheckerContentObserverInstalled = true; }
            catch(e){ /* ignore */ window.__answerCheckerContentObserverInstalled = true; }
          } else {
            // fallback polling
            var poll = setInterval(function(){ try{ if (document.getElementById('leaderboard-summary')) renderSummary(); }catch(e){} }, 500);
            window.__answerCheckerContentObserverInstalled = true; window.__answerCheckerContentPoll = poll;
          }
        } else {
          attempts++; if (attempts <= maxAttempts) setTimeout(tryAttach, 300);
        }
      }
      tryAttach();
    }catch(e){}
  }

  function setupQuestion(q, index){
    var fallbackQid = (document.location.pathname || location.href) + ':q' + index;
    var qid = q.dataset.qid || fallbackQid;
    q.dataset.qid = qid;

    var answer = parseFloat(q.dataset.answer);
    var tol = parseFloat(q.dataset.tolerance || 0);
    var points = parseFloat(q.dataset.points || 1) || 1;
  // persist question max so leaderboard can compute total even from the leaderboard page
  try { localStorage.setItem('answer_max_' + qid, String(points)); } catch (e) {}
    var hints = (q.dataset.hints || '').split('|').map(function(h){ return h.trim(); });

  var attempts = parseInt(localStorage.getItem('answer_attempts_' + qid) || '0', 10) || 0;
  // allow per-question override for number of attempts via data-attempts or data-attempts-allowed
  var attemptsAllowed = parseInt(q.dataset.attempts || q.dataset.attemptsAllowed || ATTEMPTS_ALLOWED, 10) || ATTEMPTS_ALLOWED;
    var bestRec = safeJSONParse(localStorage.getItem('answer_best_' + qid)) || { points: 0, updated: null };

    var input = q.querySelector('.numeric-answer-input');
    if (!input){ input = document.createElement('input'); input.type = 'text'; input.className = 'numeric-answer-input'; q.appendChild(input); }
    var btn = q.querySelector('.numeric-answer-submit');
    if (!btn){ btn = document.createElement('button'); btn.type = 'button'; btn.className = 'numeric-answer-submit'; btn.textContent = 'Antwort prüfen'; q.appendChild(btn); }
    var fb = q.querySelector('.numeric-answer-feedback'); if (!fb){ fb = document.createElement('div'); fb.className = 'numeric-answer-feedback'; q.appendChild(fb); }
    var scoreEl = q.querySelector('.numeric-answer-score'); if (!scoreEl){ scoreEl = document.createElement('div'); scoreEl.className = 'numeric-answer-score'; q.appendChild(scoreEl); }

  // Per-question local-delete button removed to avoid easy reset by students.

    function saveAttempts(){ localStorage.setItem('answer_attempts_' + qid, String(attempts)); }
    function saveBest(pointsVal){ localStorage.setItem('answer_best_' + qid, JSON.stringify({ points: pointsVal, updated: new Date().toISOString() })); bestRec = { points: pointsVal, updated: new Date().toISOString() }; }

    function disableControls(){ if (btn) btn.disabled = true; if (input) input.disabled = true; }
    function enableControls(){ if (btn) btn.disabled = false; if (input) input.disabled = false; }

    function reveal(){ fb.innerHTML += '<div class="numeric-reveal">Lösung: <strong>' + answer + '</strong></div>'; disableControls(); }

    function updateUI(){
      bestRec = safeJSONParse(localStorage.getItem('answer_best_' + qid)) || { points: 0, updated: null };
      attempts = parseInt(localStorage.getItem('answer_attempts_' + qid) || '0', 10) || 0;
      if (bestRec.points > 0){
        scoreEl.textContent = 'Punkte: ' + bestRec.points + '/' + points;
        fb.innerHTML = '<span class="numeric-correct">Richtig — ' + bestRec.points + ' Punkte.</span>';
        disableControls();
      } else if (attempts >= attemptsAllowed){ scoreEl.textContent = 'Punkte: 0/' + points; reveal(); }
      else { scoreEl.textContent = 'Versuche: ' + attempts + '/' + attemptsAllowed; }
  // no per-question delete UI; we keep stored data immutable from the page
    }

    function submit(){
      if (attempts >= attemptsAllowed) { reveal(); return; }
  var raw = input && input.value;
  if (typeof raw === 'string') raw = raw.replace(',', '.');
  var val = parseFloat(raw);
      attempts += 1; saveAttempts();
      if (!isFinite(val)) { fb.innerHTML = '<span class="numeric-wrong">Bitte eine Zahl eingeben.</span>'; updateUI(); return; }
      if (Math.abs(val - answer) <= tol){
        // Linear scaling across allowed attempts (Option A):
        // earned = round(points * (attemptsAllowed - attemptNumber + 1) / attemptsAllowed)
        // `attempts` was incremented above and represents the current attempt number (1..attemptsAllowed)
        var attemptNumber = attempts;
        var earned;
        if (attemptNumber === 1) {
          earned = Math.round(points);
        } else {
          earned = Math.floor(points * ((attemptsAllowed - attemptNumber + 1) / attemptsAllowed));
        }
        if (!isFinite(earned) || earned < 0) earned = 0;
        if (earned > points) earned = Math.round(points);
    var prevRec = safeJSONParse(localStorage.getItem('answer_best_' + qid)) || { points: 0, updated: null };
    var prev = prevRec.points || 0;
    var didSave = false;
    if (earned > prev) { saveBest(earned); didSave = true; }
    // check if this completed the page (may set page claimed)
    try { checkPageCompletion(); } catch(e) {}
    // Immediately update stars/nav for this page so UI reflects new score without page switch
    try {
      var myPid = getPageId();
      updateStarsForPage(myPid);
      var pctNow = computePagePercent(myPid);
      if (isPageClaimed(myPid)){
        if (pctNow === 0) replaceNavIcon(myPid, zeroStarCircleSvg); else replaceNavIcon(myPid, markedCircleSvg);
      } else {
        replaceNavIcon(myPid, blankCircleOutlineSvg);
      }
    } catch(e){}
    // schedule a short retry to handle themes that re-render the nav after our change
    try { (function(pid){ setTimeout(function(){ try{ updateStarsForPage(pid); var pct2 = computePagePercent(pid); if (isPageClaimed(pid)){ if (pct2 === 0) replaceNavIcon(pid, zeroStarCircleSvg); else replaceNavIcon(pid, markedCircleSvg); } else { replaceNavIcon(pid, blankCircleOutlineSvg); } }catch(e){} }, 250); })(getPageId()); } catch(e){}
        fb.innerHTML = '<span class="numeric-correct">Richtig — ' + earned + ' Punkte.</span>';
        scoreEl.textContent = 'Punkte: ' + (safeJSONParse(localStorage.getItem('answer_best_' + qid)) || {points: earned}).points + '/' + points;
        disableControls();
      } else {
        var s = '<span class="numeric-wrong">Falsch (' + attempts + '/' + attemptsAllowed + ').</span>';
        if (hints[attempts - 1]) s += '<div class="numeric-hint">Hinweis: ' + hints[attempts - 1] + '</div>';
        fb.innerHTML = s;
  if (attempts >= attemptsAllowed){ scoreEl.textContent = 'Punkte: 0/' + points; reveal(); } else updateUI();
      }
      renderSummary();
    }

  // clear button removed; no event listener attached
    btn.addEventListener('click', submit);
    input.addEventListener('keydown', function(e){ if (e.key === 'Enter') submit(); });

    updateUI();
  }

  function onReady(fn){ if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn); else fn(); }

  onReady(function(){
    // remove old entries on load (24h default)
    cleanupOldEntries();
    // initialize nav icons according to localStorage (claimed vs not)
    try { initializeNavIcons(); } catch(e){}
    var questions = document.querySelectorAll('.numeric-question');
    for (var i = 0; i < questions.length; i++) setupQuestion(questions[i], i);
    // update player badge and nav
    try { updatePlayerBadge(); checkPageCompletion(); } catch(e){}

    // create reset UI for authors/local testing if allowed
    try{ createPerPageResetIfAllowed(); }catch(e){}
    try{ ensureNavObserver(); }catch(e){}

    // Global reset removed to prevent easy deletion of local results by students

    renderSummary();
  });

  // local debug tools removed

})();
