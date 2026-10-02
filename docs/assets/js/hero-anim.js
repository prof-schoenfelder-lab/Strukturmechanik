/* Startseiten-Animation im Kopfbereich: das erste Lösungsbeispiel aus
   Praktikum 1 im Zeitraffer. Zweiseitig gelagerter Balken aus Stahl mit
   Flächenlast, durch die sieben Schritte des Simulations-Workflows aus dem
   Kurs bis zur Auswertung (u_max = 0,922 mm). Läuft von selbst in Schleife,
   pausiert außerhalb des Sichtbereichs; bei reduzierter Bewegung steht das
   Endbild. Die Schritt-Leiste darunter ist anklickbar. */
(function () {
  'use strict';

  var STEPS = [
    { key: 'Material',   text: 'Stahl mit E = 210 GPa und ν = 0,3',           t0: 0.0,  t1: 1.8 },
    { key: 'Geometrie',  text: 'Balken 1000 × 30 × 30 mm, Profil und Extrusion', t0: 1.8,  t1: 4.2 },
    { key: 'Zuweisung',  text: 'Der Balken bekommt den Werkstoff Stahl',          t0: 4.2,  t1: 5.6 },
    { key: 'Netz',       text: 'Vernetzung mit Hexaeder-Elementen',               t0: 5.6,  t1: 7.8 },
    { key: 'Randbed.',   text: 'Festlager links, Loslager rechts, F = 1000 N',    t0: 7.8,  t1: 10.4 },
    { key: 'Lösen',      text: 'Das Gleichungssystem wird gelöst',                t0: 10.4, t1: 12.0 },
    { key: 'Auswertung', text: 'Maximale Durchbiegung 0,922 mm, überhöht dargestellt', t0: 12.0, t1: 18.0 }
  ];
  var LOOP = 18.8;
  var STILL = 15.2; // Endbild bei reduzierter Bewegung

  // ANSYS-Legende: neun Bänder von Blau nach Rot
  var BANDS = [[0, 0, 255], [0, 178, 255], [0, 255, 255], [0, 255, 178], [0, 255, 0],
               [178, 255, 0], [255, 255, 0], [255, 178, 0], [255, 0, 0]];
  var LABELS = ['0,922 Max', '0,820', '0,717', '0,615', '0,512', '0,410', '0,307', '0,205', '0,102', '0 Min'];
  var STEEL = [139, 156, 171];

  function clamp01(v) { return v < 0 ? 0 : v > 1 ? 1 : v; }
  function span(t, a, b) { return clamp01((t - a) / (b - a)); }
  function smooth(v) { v = clamp01(v); return v * v * (3 - 2 * v); }
  function backOut(v) { v = clamp01(v); var c = 1.70158; return 1 + (c + 1) * Math.pow(v - 1, 3) + c * Math.pow(v - 1, 2); }
  // Biegelinie unter Gleichlast, in Feldmitte auf 1 normiert
  function deflect(s) { return (s * (1 - 2 * s * s + s * s * s)) / 0.3125; }
  function deflectSlope(s) { return (1 - 6 * s * s + 4 * s * s * s) / 0.3125; }

  function init() {
    var host = document.querySelector('.kurs-anim');
    if (!host || !window.THREE || host.getAttribute('data-ready')) return;
    var renderer;
    try { renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true }); } catch (e) { return; }
    host.setAttribute('data-ready', '1');
    renderer.setPixelRatio(Math.min(2, window.devicePixelRatio || 1));
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    renderer.outputEncoding = THREE.sRGBEncoding;

    // ---------- DOM: Bühne, Einblendungen, Schritt-Leiste ----------
    var stage = document.createElement('div');
    stage.className = 'kurs-anim-stage';
    host.appendChild(stage);
    var canvas = renderer.domElement;
    canvas.className = 'kurs-anim-canvas';
    stage.appendChild(canvas);

    function overlay(cls, html) {
      var d = document.createElement('div');
      d.className = 'kurs-anim-ov ' + cls;
      d.innerHTML = '<div class="kurs-ov-in">' + html + '</div>';
      stage.appendChild(d);
      return d;
    }
    var ovMat = overlay('kurs-anim-tag', '<b>Stahl</b><span>E = 210 GPa · ν = 0,3</span>');
    var ovDim = overlay('kurs-anim-dimlabel', 'L = 1000 mm');
    var ovLoad = overlay('kurs-anim-loadlabel', 'F = 1000 N');
    var ovFest = overlay('kurs-anim-suplabel', 'Festlager');
    var ovLos = overlay('kurs-anim-suplabel', 'Loslager');
    var ovFlag = overlay('kurs-anim-flag', '<i></i><span><b>Max</b> 0,922 mm</span>');
    var bands = '', labs = '';
    for (var b = BANDS.length - 1; b >= 0; b--) bands += '<i style="background:rgb(' + BANDS[b].join(',') + ')"></i>';
    for (var l = 0; l < LABELS.length; l++) labs += '<span>' + LABELS[l] + '</span>';
    var legend = overlay('kurs-anim-legend',
      '<b>Gesamtverformung</b><em>Einheit: mm</em>' +
      '<div class="kurs-leg"><div class="kurs-leg-bar">' + bands + '</div><div class="kurs-leg-lab">' + labs + '</div></div>');

    var track = document.createElement('div');
    track.className = 'kurs-anim-track';
    track.innerHTML = STEPS.map(function (s, i) {
      return '<button type="button" data-i="' + i + '" title="' + (i + 1) + ' · ' + s.key + '"><i></i><span>' + s.key + '</span></button>';
    }).join('');
    host.appendChild(track);
    var trackBtns = track.querySelectorAll('button');
    var cap = document.createElement('div');
    cap.className = 'kurs-anim-cap';
    cap.setAttribute('aria-live', 'off');
    host.appendChild(cap);

    // ---------- Szene ----------
    var LEN = 8, H = 0.5, W = 0.5;
    var NX = 32, NY = 2, NZ = 2;
    var WMAX = 0.62;
    var SUP_H = 0.5;        // Lagerhöhe vom Boden bis zur Balkenunterkante
    var Y0 = -H / 2 - SUP_H; // Boden (Unterkante der Lagerplatten)

    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(30, 1.6, 0.1, 80);
    var hemi = new THREE.HemisphereLight(0xffffff, 0x7d8a94, 0.9);
    scene.add(hemi);
    var sun = new THREE.DirectionalLight(0xffffff, 0.9);
    sun.position.set(3.2, 8, 6);
    sun.castShadow = true;
    sun.shadow.mapSize.set(1024, 1024);
    sun.shadow.camera.left = -6; sun.shadow.camera.right = 6;
    sun.shadow.camera.top = 4; sun.shadow.camera.bottom = -4;
    scene.add(sun);
    var ground = new THREE.Mesh(new THREE.PlaneGeometry(30, 14), new THREE.ShadowMaterial({ opacity: 0.13 }));
    ground.rotation.x = -Math.PI / 2;
    ground.position.y = Y0;
    ground.receiveShadow = true;
    scene.add(ground);

    // 1 Material: Werkstoffprobe als Kugel
    var sphere = new THREE.Mesh(
      new THREE.SphereGeometry(0.3, 48, 32),
      new THREE.MeshStandardMaterial({ color: 0xa3b1bc, metalness: 0.55, roughness: 0.26 })
    );
    scene.add(sphere);
    var SPH0 = new THREE.Vector3(-1.9, 1.05, 0.6);

    // 2 Geometrie: CAD-Körper (durchscheinend) mit Kanten, wächst aus dem Profil
    var boxGeo = new THREE.BoxGeometry(LEN, H, W);
    var cadMat = new THREE.MeshStandardMaterial({ color: 0xa9d9f1, roughness: 0.6, metalness: 0, transparent: true, opacity: 0, depthWrite: false });
    var cad = new THREE.Mesh(boxGeo, cadMat);
    scene.add(cad);
    var edgeMat = new THREE.LineBasicMaterial({ color: 0x0070a6, transparent: true, opacity: 0 });
    var cadEdges = new THREE.LineSegments(new THREE.EdgesGeometry(boxGeo), edgeMat);
    scene.add(cadEdges);

    // Maßlinie vor dem Balken
    var dimMat = new THREE.LineBasicMaterial({ color: 0x0070a6, transparent: true, opacity: 0 });
    var dimConeMat = new THREE.MeshBasicMaterial({ color: 0x0070a6, transparent: true, opacity: 0 });
    var dimY = -H / 2, dimZ = W / 2 + 0.5;
    var dimGeo = new THREE.BufferGeometry().setFromPoints([
      new THREE.Vector3(-LEN / 2, dimY, dimZ), new THREE.Vector3(LEN / 2, dimY, dimZ),
      new THREE.Vector3(-LEN / 2, dimY, W / 2 + 0.06), new THREE.Vector3(-LEN / 2, dimY, dimZ + 0.12),
      new THREE.Vector3(LEN / 2, dimY, W / 2 + 0.06), new THREE.Vector3(LEN / 2, dimY, dimZ + 0.12)
    ]);
    var dim = new THREE.Group();
    dim.add(new THREE.LineSegments(dimGeo, dimMat));
    [-1, 1].forEach(function (sgn) {
      var c = new THREE.Mesh(new THREE.ConeGeometry(0.045, 0.16, 12), dimConeMat);
      c.rotation.z = sgn > 0 ? -Math.PI / 2 : Math.PI / 2;
      c.position.set(sgn * (LEN / 2 - 0.08), dimY, dimZ);
      dim.add(c);
    });
    scene.add(dim);

    // 3 Zuweisung: Stahlkörper füllt den Balken von der Mitte aus
    var steelMat = new THREE.MeshStandardMaterial({ color: 0x8c9cab, roughness: 0.42, metalness: 0.12 });
    var steel = new THREE.Mesh(new THREE.BoxGeometry(LEN, H, W), steelMat);
    steel.castShadow = true;
    scene.add(steel);

    // 4 Netz: Hexaeder-Elemente mit gemeinsamen Knoten
    var ex = LEN / NX, ey = H / NY, ez = W / NZ;
    var count = NX * NY * NZ;
    var CORNERS = [[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]];
    var FACES = [[1, 2, 6, 5], [0, 4, 7, 3], [3, 7, 6, 2], [0, 1, 5, 4], [4, 5, 6, 7], [0, 3, 2, 1]];
    var VPE = 36;
    var positions = new Float32Array(count * VPE * 3);
    var normals = new Float32Array(count * VPE * 3);
    var uvs = new Float32Array(count * VPE * 2);
    var vcols = new Float32Array(count * VPE * 3);
    var geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.BufferAttribute(positions, 3).setUsage(THREE.DynamicDrawUsage));
    geo.setAttribute('normal', new THREE.BufferAttribute(normals, 3).setUsage(THREE.DynamicDrawUsage));
    geo.setAttribute('uv', new THREE.BufferAttribute(uvs, 2).setUsage(THREE.DynamicDrawUsage));
    geo.setAttribute('color', new THREE.BufferAttribute(vcols, 3).setUsage(THREE.DynamicDrawUsage));

    // Farbtabelle: Texel 0 bis 8 = Legende, Rest = Stahl (scharfe Bänder wie in ANSYS)
    var tdata = new Uint8Array(16 * 4);
    for (var ti = 0; ti < 16; ti++) {
      var c = ti < 9 ? BANDS[ti] : STEEL;
      tdata[ti * 4] = c[0]; tdata[ti * 4 + 1] = c[1]; tdata[ti * 4 + 2] = c[2]; tdata[ti * 4 + 3] = 255;
    }
    var tex = new THREE.DataTexture(tdata, 16, 1, THREE.RGBAFormat);
    tex.magFilter = THREE.NearestFilter;
    tex.minFilter = THREE.NearestFilter;
    tex.generateMipmaps = false;
    tex.encoding = THREE.sRGBEncoding;
    tex.needsUpdate = true;
    var elemMat = new THREE.MeshStandardMaterial({
      map: tex, vertexColors: true, roughness: 0.5, metalness: 0.05,
      polygonOffset: true, polygonOffsetFactor: 1, polygonOffsetUnits: 1
    });
    var mesh = new THREE.Mesh(geo, elemMat);
    mesh.castShadow = true;
    mesh.frustumCulled = false;
    scene.add(mesh);

    var items = [];
    for (var i = 0; i < NX; i++) for (var j = 0; j < NY; j++) for (var k = 0; k < NZ; k++) {
      items.push({ i: i, j: j, k: k, xc: -LEN / 2 + (i + 0.5) * ex, order: (i + (j + k) * 0.35) / (NX + 1.4) });
    }
    var totalEdges = 0;
    items.forEach(function (it) {
      it.bFaces = [];
      if (it.i === NX - 1) it.bFaces.push(0);
      if (it.i === 0) it.bFaces.push(1);
      if (it.j === NY - 1) it.bFaces.push(2);
      if (it.j === 0) it.bFaces.push(3);
      if (it.k === NZ - 1) it.bFaces.push(4);
      if (it.k === 0) it.bFaces.push(5);
      totalEdges += it.bFaces.length * 4;
    });
    var edgePos = new Float32Array(totalEdges * 6);
    var lineGeo = new THREE.BufferGeometry();
    lineGeo.setAttribute('position', new THREE.BufferAttribute(edgePos, 3).setUsage(THREE.DynamicDrawUsage));
    var lineMat = new THREE.LineBasicMaterial({ color: 0x24323b, transparent: true, opacity: 0.5 });
    var lines = new THREE.LineSegments(lineGeo, lineMat);
    lines.frustumCulled = false;
    scene.add(lines);

    function deformNode(x, y, z, bend, out) {
      var s = (x + LEN / 2) / LEN;
      out[0] = x + y * (WMAX * bend / LEN) * deflectSlope(s);
      out[1] = y - WMAX * bend * deflect(s);
      out[2] = z;
      out[3] = s;
    }

    // 5 Randbedingungen: Festlager links, Loslager rechts, Flächenlast.
    // Hell mit dunkler Kontur, damit die Lagersymbole wie im Lehrbuch lesbar sind
    var supMat = new THREE.MeshStandardMaterial({ color: 0x9aa7b0, roughness: 0.5, transparent: true, opacity: 1 });
    var supEdgeMat = new THREE.LineBasicMaterial({ color: 0x1d262b, transparent: true, opacity: 0.85 });
    function solidPart(g, geom, x, y, rotX, rotY) {
      var m = new THREE.Mesh(geom, supMat);
      m.position.set(x, y, 0);
      if (rotX) m.rotation.x = rotX;
      if (rotY) m.rotation.y = rotY;
      m.castShadow = true;
      g.add(m);
      var e = new THREE.LineSegments(new THREE.EdgesGeometry(geom, 25), supEdgeMat);
      e.position.copy(m.position);
      e.rotation.copy(m.rotation);
      g.add(e);
    }
    function supportGroup(x, roller) {
      var g = new THREE.Group();
      g.position.set(x, Y0, 0);
      var plateH = 0.07, pyrH = roller ? 0.3 : 0.43;
      solidPart(g, new THREE.ConeGeometry(0.3, pyrH, 4), 0, SUP_H - pyrH / 2, 0, Math.PI / 4);
      solidPart(g, new THREE.BoxGeometry(0.92, plateH, 0.7), 0, plateH / 2);
      if (roller) {
        [-0.15, 0.15].forEach(function (dx) {
          solidPart(g, new THREE.CylinderGeometry(0.06, 0.06, 0.6, 20), dx, plateH + 0.06, Math.PI / 2);
        });
      }
      scene.add(g);
      return g;
    }
    var supL = supportGroup(-LEN / 2, false);
    var supR = supportGroup(LEN / 2, true);

    var loadMat = new THREE.MeshStandardMaterial({ color: 0xe53009, roughness: 0.45, transparent: true, opacity: 1 });
    var arrows = [];
    var NARR = 13;
    for (var av = 0; av < NARR; av++) {
      var ga = new THREE.Group();
      var shaft = new THREE.Mesh(new THREE.CylinderGeometry(0.016, 0.016, 0.34, 8), loadMat);
      shaft.position.y = 0.29;
      var tip = new THREE.Mesh(new THREE.ConeGeometry(0.048, 0.13, 12), loadMat);
      tip.rotation.x = Math.PI;
      tip.position.y = 0.065;
      ga.add(shaft); ga.add(tip);
      ga.userData.x = -LEN / 2 + LEN * av / (NARR - 1);
      arrows.push(ga);
      scene.add(ga);
    }
    var loadLine = new THREE.Mesh(new THREE.CylinderGeometry(0.014, 0.014, LEN, 8), loadMat);
    loadLine.rotation.z = Math.PI / 2;
    loadLine.position.set(0, H / 2 + 0.46, 0);
    scene.add(loadLine);

    // ---------- Farben je Hell/Dunkel ----------
    var lastDark = null;
    function applyTheme() {
      var dark = document.body.getAttribute('data-md-color-scheme') === 'slate';
      if (dark === lastDark) return;
      lastDark = dark;
      var ink = dark ? 0x62c9f5 : 0x0070a6;
      edgeMat.color.setHex(ink); dimMat.color.setHex(ink); dimConeMat.color.setHex(ink);
      cadMat.color.setHex(dark ? 0x2f5873 : 0xa9d9f1);
      lineMat.color.setHex(dark ? 0xd5e6f2 : 0x24323b);
      supMat.color.setHex(dark ? 0xb8c6d0 : 0x9aa7b0).convertSRGBToLinear();
      supEdgeMat.color.setHex(dark ? 0x0b1621 : 0x1d262b);
      loadMat.color.setHex(dark ? 0xff5a36 : 0xe53009).convertSRGBToLinear();
      steelMat.color.setRGB(STEEL[0] / 255, STEEL[1] / 255, STEEL[2] / 255).convertSRGBToLinear();
      ground.material.opacity = dark ? 0.32 : 0.13;
      hemi.groundColor.setHex(dark ? 0x3a4752 : 0x7d8a94);
    }

    // ---------- Größe ----------
    var cw = 0, ch = 0;
    function resize() {
      var w = Math.round(stage.clientWidth) || 560;
      var h = Math.max(250, Math.min(420, Math.round(w * 0.6)));
      if (w === cw && h === ch) return;
      cw = w; ch = h;
      renderer.setSize(w, h, true);
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
    }
    if (window.ResizeObserver) new ResizeObserver(function () { resize(); draw(curT); }).observe(stage);

    var v3 = new THREE.Vector3();
    function place(el, x, y, z, op) {
      el.style.opacity = op;
      if (op <= 0.001) return;
      v3.set(x, y, z).project(camera);
      var px = (v3.x * 0.5 + 0.5) * cw, py = (-v3.y * 0.5 + 0.5) * ch;
      el.style.transform = 'translate(' + px.toFixed(1) + 'px,' + py.toFixed(1) + 'px)';
    }

    // ---------- Ein Bild zum Zeitpunkt t ----------
    var corner = [], tmp = [0, 0, 0, 0];
    for (var cc = 0; cc < 8; cc++) corner.push([0, 0, 0, 0]);
    var lastStep = -1;

    function draw(t) {
      applyTheme();
      resize();

      // Ein- und Ausblenden der Schleife
      stage.style.opacity = Math.min(smooth(span(t, 0, 0.45)), 1 - smooth(span(t, 18.0, 18.8))).toFixed(3);

      // 1 Material und 3 Zuweisung: Kugel erscheint und fliegt in den Balken
      var sphIn = backOut(span(t, 0.15, 0.95));
      var fly = smooth(span(t, 4.25, 4.95));
      sphere.visible = t < 4.95 && sphIn > 0.001;
      var arc = Math.sin(fly * Math.PI) * 0.55;
      sphere.position.set(SPH0.x * (1 - fly), SPH0.y * (1 - fly) + arc, SPH0.z * (1 - fly));
      var ss = Math.max(0.001, sphIn * (1 - 0.8 * fly));
      sphere.scale.set(ss, ss, ss);
      sphere.rotation.y = t * 0.9;

      // 2 Geometrie: Profil, dann Extrusion von links nach rechts
      var prof = smooth(span(t, 1.85, 2.35));
      var ext = smooth(span(t, 2.35, 3.7));
      var e = 0.012 + 0.988 * ext;
      var cadFade = 1 - smooth(span(t, 5.1, 5.6));
      cad.scale.x = e; cad.position.x = -LEN / 2 + LEN * e / 2;
      cadEdges.scale.x = e; cadEdges.position.x = cad.position.x;
      cadMat.opacity = 0.78 * smooth(span(t, 2.4, 3.1)) * cadFade;
      edgeMat.opacity = prof * cadFade;
      cad.visible = cadMat.opacity > 0.003;
      cadEdges.visible = edgeMat.opacity > 0.003;

      var dimOp = smooth(span(t, 3.55, 3.95)) * (1 - smooth(span(t, 5.6, 6.0)));
      dimMat.opacity = dimOp; dimConeMat.opacity = dimOp;
      dim.visible = dimOp > 0.003;

      // 3 Zuweisung: Stahl füllt den Balken, 4 Netz schneidet ihn von links ab
      var fill = smooth(span(t, 4.85, 5.45));
      var net = span(t, 5.6, 7.5);
      var front = -LEN / 2 + LEN * Math.min(1, net * 1.05);
      var left = Math.max(-LEN / 2 * fill, front), right = LEN / 2 * fill;
      steel.visible = fill > 0.001 && right - left > 0.002 && t < 7.8;
      if (steel.visible) {
        steel.scale.set((right - left) / LEN, 1.002, 1.002);
        steel.position.x = (left + right) / 2;
      }

      // 4 bis 7: Elemente
      var showMesh = t >= 5.6;
      mesh.visible = lines.visible = showMesh;
      var bend = smooth(span(t, 12.3, 14.3));
      var sol = span(t, 10.45, 11.75);
      var waveX = -LEN / 2 - 0.6 + (LEN + 1.2) * sol;
      var waveOn = sol > 0 && sol < 1;
      var wipe = (LEN / 2 + 0.2) * smooth(span(t, 12.05, 12.7));
      if (showMesh) {
        var p = 0, q = 0, pc = 0, pe = 0;
        for (var n = 0; n < count; n++) {
          var it = items[n];
          var appear = clamp01((net * 1.12 - it.order) / 0.12);
          var contour = Math.abs(it.xc) <= wipe;
          var glow = waveOn ? Math.exp(-Math.pow((it.xc - waveX) / 0.5, 2)) : 0;
          var cx = 0, cy = 0, cz = 0;
          for (var c8 = 0; c8 < 8; c8++) {
            deformNode(-LEN / 2 + (it.i + CORNERS[c8][0]) * ex, -H / 2 + (it.j + CORNERS[c8][1]) * ey,
              -W / 2 + (it.k + CORNERS[c8][2]) * ez, bend, tmp);
            corner[c8][0] = tmp[0]; corner[c8][1] = tmp[1]; corner[c8][2] = tmp[2]; corner[c8][3] = tmp[3];
            cx += tmp[0]; cy += tmp[1]; cz += tmp[2];
          }
          cx /= 8; cy /= 8; cz /= 8;
          var shrink = Math.max(0.001, 1 - (0.014 + (1 - appear)));
          for (var c9 = 0; c9 < 8; c9++) {
            corner[c9][0] = cx + (corner[c9][0] - cx) * shrink;
            corner[c9][1] = cy + (corner[c9][1] - cy) * shrink;
            corner[c9][2] = cz + (corner[c9][2] - cz) * shrink;
          }
          var gr = 1 + glow * 0.25, gg = 1 + glow * 0.55, gb = 1 + glow * 0.8;
          for (var f = 0; f < 6; f++) {
            var fq = FACES[f];
            var A = corner[fq[0]], B = corner[fq[1]], C = corner[fq[2]], D = corner[fq[3]];
            var ux = B[0] - A[0], uy = B[1] - A[1], uz = B[2] - A[2];
            var vx = D[0] - A[0], vy = D[1] - A[1], vz = D[2] - A[2];
            var nx = uy * vz - uz * vy, ny = uz * vx - ux * vz, nz = ux * vy - uy * vx;
            var fx = (A[0] + B[0] + C[0] + D[0]) / 4 - cx, fy = (A[1] + B[1] + C[1] + D[1]) / 4 - cy, fz = (A[2] + B[2] + C[2] + D[2]) / 4 - cz;
            if (nx * fx + ny * fy + nz * fz < 0) { nx = -nx; ny = -ny; nz = -nz; }
            var nl = Math.sqrt(nx * nx + ny * ny + nz * nz) || 1;
            nx /= nl; ny /= nl; nz /= nl;
            var tri = [A, B, C, A, C, D];
            for (var tv = 0; tv < 6; tv++) {
              var P = tri[tv];
              positions[p] = P[0]; normals[p] = nx; vcols[p] = gr; p++;
              positions[p] = P[1]; normals[p] = ny; vcols[p] = gg; p++;
              positions[p] = P[2]; normals[p] = nz; vcols[p] = gb; p++;
              var val = contour ? Math.min(0.9999, deflect(P[3]) * bend) : -1;
              uvs[q++] = val < 0 ? 15.5 / 16 : val * 9 / 16;
              uvs[q++] = 0.5;
            }
          }
          for (var bf = 0; bf < it.bFaces.length; bf++) {
            var qe = FACES[it.bFaces[bf]];
            for (var e4 = 0; e4 < 4; e4++) {
              var P1 = corner[qe[e4]], P2 = corner[qe[(e4 + 1) % 4]];
              edgePos[pe++] = P1[0]; edgePos[pe++] = P1[1]; edgePos[pe++] = P1[2];
              edgePos[pe++] = P2[0]; edgePos[pe++] = P2[1]; edgePos[pe++] = P2[2];
            }
          }
          pc++;
        }
        geo.attributes.position.needsUpdate = true;
        geo.attributes.normal.needsUpdate = true;
        geo.attributes.uv.needsUpdate = true;
        geo.attributes.color.needsUpdate = true;
        lineGeo.attributes.position.needsUpdate = true;
        lineMat.opacity = (lastDark ? 0.3 : 0.5) - (lastDark ? 0.14 : 0.24) * smooth(span(t, 12.1, 12.8));
      }

      // 5 Randbedingungen: Lager wachsen aus dem Boden, Lastpfeile fallen ein
      var sup = backOut(span(t, 7.85, 8.6));
      [supL, supR].forEach(function (g) { g.visible = sup > 0.001; g.scale.set(1, Math.max(0.001, sup), 1); });
      var loadFade = 1 - smooth(span(t, 12.0, 12.5));
      arrows.forEach(function (ga, idx) {
        var a0 = 8.5 + 1.1 * idx / (NARR - 1);
        var drop = smooth(span(t, a0, a0 + 0.35));
        ga.visible = t > a0 && t < 12.5;
        ga.position.set(ga.userData.x, H / 2 + (1 - drop) * 0.7, 0);
      });
      loadMat.opacity = loadFade;
      var lineIn = smooth(span(t, 9.65, 10.05));
      loadLine.visible = lineIn > 0.001 && t < 12.5;
      loadLine.scale.set(1, Math.max(0.001, lineIn), 1);

      // Kamera: langsame Umrundung, zur Auswertung näher heran
      var az = -0.52 + 0.34 * (t / LOOP);
      var elv = 0.33 - 0.05 * bend;
      // schmale Bühne (Handy): weiter weg, damit der ganze Balken ins Bild passt,
      // und zur Auswertung tiefer, damit die Legende frei bleibt
      var narrow = Math.max(1, 1.62 / camera.aspect);
      var r = (10.3 - 0.4 * bend) * narrow;
      var ty = 0.06 + 0.34 * bend * narrow * narrow;
      camera.position.set(r * Math.sin(az) * Math.cos(elv), ty + r * Math.sin(elv), r * Math.cos(az) * Math.cos(elv));
      camera.lookAt(0, ty, 0);
      camera.updateMatrixWorld();

      renderer.render(scene, camera);

      // Einblendungen
      place(ovMat, sphere.position.x, sphere.position.y + 0.55, sphere.position.z,
        smooth(span(t, 0.6, 1.0)) * (1 - smooth(span(t, 4.2, 4.5))));
      place(ovDim, 0, dimY, dimZ, dimOp);
      place(ovLoad, 0, H / 2 + 0.66, 0, smooth(span(t, 9.8, 10.2)) * loadFade);
      var supLab = smooth(span(t, 8.2, 8.7)) * (1 - smooth(span(t, 12.0, 12.4)));
      place(ovFest, -LEN / 2, Y0, W / 2 + 0.4, supLab);
      place(ovLos, LEN / 2, Y0, W / 2 + 0.4, supLab);
      place(ovFlag, 0, -H / 2 - WMAX * bend, W / 2,
        smooth(span(t, 14.1, 14.6)) * (1 - smooth(span(t, 18.0, 18.6))));
      legend.style.opacity = (smooth(span(t, 12.4, 13.0)) * (1 - smooth(span(t, 18.0, 18.6)))).toFixed(3);

      // Schritt-Leiste und Beschriftung
      var cur = 0;
      for (var si = 0; si < STEPS.length; si++) if (t >= STEPS[si].t0) cur = si;
      for (var bi = 0; bi < trackBtns.length; bi++) {
        var st = STEPS[bi];
        trackBtns[bi].style.setProperty('--p', span(t, st.t0, st.t1).toFixed(3));
        trackBtns[bi].classList.toggle('on', bi === cur);
        trackBtns[bi].classList.toggle('done', bi < cur);
      }
      if (cur !== lastStep) {
        lastStep = cur;
        cap.innerHTML = '<b>' + (cur + 1) + ' · ' + STEPS[cur].key.replace('Randbed.', 'Randbedingungen') + '</b><span>' + STEPS[cur].text + '</span>';
      }
    }

    // ---------- Ablauf ----------
    var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var curT = reduced ? STILL : 0, running = false, last = 0, visible = true;
    function tick(now) {
      if (!running) return;
      var dt = last ? Math.min(0.05, (now - last) / 1000) : 0;
      last = now;
      curT = (curT + dt) % LOOP;
      draw(curT);
      requestAnimationFrame(tick);
    }
    function start() { if (running || reduced || !visible) return; running = true; last = 0; requestAnimationFrame(tick); }
    function stop() { running = false; }

    track.addEventListener('click', function (ev) {
      var btn = ev.target.closest('button');
      if (!btn) return;
      var st = STEPS[+btn.getAttribute('data-i')];
      curT = st.key === 'Auswertung' ? STILL : st.t0 + 0.02;
      draw(curT);
    });
    if (window.IntersectionObserver) {
      new IntersectionObserver(function (en) {
        visible = en[0].isIntersecting;
        if (visible) start(); else stop();
      }).observe(host);
    }
    new MutationObserver(function () { if (!running) draw(curT); })
      .observe(document.body, { attributes: true, attributeFilter: ['data-md-color-scheme'] });

    // Für Tests: Zeitpunkt setzen und anhalten (window.__heroAnim.seek(12.5))
    window.__heroAnim = {
      seek: function (t) { stop(); reduced = true; curT = t; draw(t); },
      play: function () { reduced = false; start(); }
    };

    draw(curT);
    start();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { setTimeout(init, 0); });
  else setTimeout(init, 0);
})();
