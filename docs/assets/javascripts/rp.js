/* =========================================================================
   RENOUVIER PAPERS — comportements portés depuis le site Just the Docs :
   marqueurs de page [p. N], panneau Réglages (4 thèmes + 3 polices),
   sections pliables, titre pixel-art colorisé.
   ========================================================================= */
(function () {
  var COLORS = ['var(--accent)', 'var(--accent2)', 'var(--accent3)', 'var(--accent4)'];

  /* ---- application thème / police (persistées, mêmes clés qu'avant) ---- */
  function applyTheme(t) {
    document.body.classList.remove('theme-dark', 'theme-cb-light', 'theme-cb-dark');
    if (t && t !== 'light') document.body.classList.add('theme-' + t);
  }
  function applyFont(f) {
    document.body.classList.remove('font-hyperlegible', 'font-opendyslexic');
    if (f === 'hyperlegible') document.body.classList.add('font-hyperlegible');
    if (f === 'opendyslexic') document.body.classList.add('font-opendyslexic');
  }
  // appliquer tôt (évite le flash)
  applyTheme(localStorage.getItem('themeChoice') || 'light');
  applyFont(localStorage.getItem('fontChoice') || 'default');

  function makeTitleHome() {
    var el = document.querySelector('.md-header__title');
    if (!el || el.dataset.rpHome) return;
    el.dataset.rpHome = '1';
    el.style.cursor = 'pointer';
    el.setAttribute('title', "Retour à l'accueil");
    el.addEventListener('click', function () { window.location.href = window.location.origin + '/'; });
  }

  function pageMarkers(root) {
    if (!root) return;
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null, false);
    var nodes = []; while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function (node) {
      if (node.parentNode && node.parentNode.classList && node.parentNode.classList.contains('page-marker')) return;
      if (!/\[p\.\s[^\]]+\]/.test(node.textContent)) return;
      var frag = document.createDocumentFragment();
      node.textContent.split(/(\[p\.\s[^\]]+\])/g).forEach(function (part) {
        if (/^\[p\.\s[^\]]+\]$/.test(part)) {
          var s = document.createElement('span'); s.className = 'page-marker'; s.textContent = part; frag.appendChild(s);
        } else { frag.appendChild(document.createTextNode(part)); }
      });
      node.parentNode.replaceChild(frag, node);
    });
  }

  function collapsibleSections(root) {
    if (!root) return;
    var hs = root.querySelectorAll('h2, h3, h4');
    if (hs.length < 4) return;
    hs.forEach(function (h) {
      if (h.dataset.rpCollap) return; h.dataset.rpCollap = '1';
      h.classList.add('collapsible-heading', 'open');
      var lvl = parseInt(h.tagName.charAt(1), 10);
      var wrap = document.createElement('div'); wrap.className = 'collapsible-content';
      var sib = h.nextElementSibling;
      while (sib) {
        if (/^H[1-6]$/.test(sib.tagName) && parseInt(sib.tagName.charAt(1), 10) <= lvl) break;
        var nxt = sib.nextElementSibling; wrap.appendChild(sib); sib = nxt;
      }
      if (wrap.children.length) h.parentNode.insertBefore(wrap, h.nextSibling);
      h.addEventListener('click', function () {
        this.classList.toggle('open');
        var c = this.nextElementSibling;
        if (c && c.classList.contains('collapsible-content')) c.classList.toggle('collapsed');
      });
    });
  }

  function buildToolbar() {
    if (document.getElementById('rp-toolbar')) return;
    var bar = document.createElement('div'); bar.id = 'rp-toolbar';
    bar.innerHTML =
      '<button class="btn-fold" id="rp-fold">± Sections</button>' +
      '<button class="btn-settings" id="rp-settings-btn">Réglages</button>';
    document.body.appendChild(bar);

    var ov = document.createElement('div'); ov.id = 'rp-settings-overlay'; document.body.appendChild(ov);
    var panel = document.createElement('div'); panel.id = 'rp-settings';
    panel.innerHTML =
      '<label>Affichage</label>' +
      '<select id="rp-theme">' +
        '<option value="light">Clair</option><option value="dark">Sombre</option>' +
        '<option value="cb-light">Daltonien jour</option><option value="cb-dark">Daltonien nuit</option>' +
      '</select>' +
      '<label>Police</label>' +
      '<select id="rp-font">' +
        '<option value="default">Par défaut (Solway)</option>' +
        '<option value="hyperlegible">Malvoyance (Atkinson Hyperlegible)</option>' +
        '<option value="opendyslexic">Dyslexie (OpenDyslexic)</option>' +
      '</select>';
    document.body.appendChild(panel);

    document.getElementById('rp-settings-btn').addEventListener('click', function (e) {
      e.stopPropagation(); panel.classList.toggle('open'); ov.classList.toggle('open');
    });
    ov.addEventListener('click', function () { panel.classList.remove('open'); ov.classList.remove('open'); });

    var ts = document.getElementById('rp-theme');
    ts.value = localStorage.getItem('themeChoice') || 'light';
    ts.addEventListener('change', function () { localStorage.setItem('themeChoice', this.value); applyTheme(this.value); });
    var fs = document.getElementById('rp-font');
    fs.value = localStorage.getItem('fontChoice') || 'default';
    fs.addEventListener('change', function () { localStorage.setItem('fontChoice', this.value); applyFont(this.value); });

    var allOpen = true;
    document.getElementById('rp-fold').addEventListener('click', function () {
      var root = document.querySelector('.md-content');
      if (!root) return;
      var secs = root.querySelectorAll('.collapsible-content');
      var hds = root.querySelectorAll('.collapsible-heading');
      allOpen = !allOpen;
      secs.forEach(function (s) { s.classList.toggle('collapsed', !allOpen); });
      hds.forEach(function (h) { h.classList.toggle('open', allOpen); });
    });
  }

  /* ---- tiroir mobile : sur l'accueil, ouvrir sur les grandes rubriques ----
     Material « zoome » le tiroir sur la rubrique de la page courante. Sur
     l'accueil (qui vit dans la rubrique « Accueil »), on n'y voyait donc que
     Contribuer et Licence, et il fallait la flèche de retour pour atteindre
     Œuvres, Revues, etc. On remonte d'un cran, mais UNIQUEMENT à l'ouverture
     du tiroir et sur l'accueil : ailleurs, le tiroir garde son rôle utile
     (afficher le menu latéral de la rubrique où l'on se trouve), et la barre
     latérale du bureau n'est pas concernée. */
  function drawerRootOnHome() {
    var drawer = document.getElementById('__drawer');
    if (!drawer || drawer.dataset.rpHomeNav) return;
    drawer.dataset.rpHomeNav = '1';
    drawer.addEventListener('change', function () {
      if (!this.checked) return;                                  // seulement à l'ouverture
      if (location.pathname.replace(/\/+$/, '') !== '') return;    // seulement sur l'accueil
      var nav = document.querySelector('.md-nav--primary');
      if (!nav) return;
      nav.querySelectorAll('.md-nav__toggle').forEach(function (t) { t.checked = false; });
    });
  }

  function init() {
    var content = document.querySelector('.md-content');
    makeTitleHome();
    buildToolbar();
    pageMarkers(content);
    collapsibleSections(content);
    drawerRootOnHome();
  }

  // instant-nav de Material si présent, sinon chargement classique
  if (window.document$ && typeof window.document$.subscribe === 'function') {
    window.document$.subscribe(function () { init(); });
  } else if (document.readyState !== 'loading') {
    init();
  } else {
    document.addEventListener('DOMContentLoaded', init);
  }
})();
