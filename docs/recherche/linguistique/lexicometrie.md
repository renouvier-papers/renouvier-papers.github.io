---
title: "Lexicométrie"
description: "Trois états de la langue de Renouvier (1875, 1885-1886, 1903), comptés, mesurés, confrontés."
---

# Lexicométrie

La philologie lit ; la lexicométrie compte. Trois livres de Renouvier transcrits sur ce site — les **Essais** dans leur seconde édition de 1875, l'**Esquisse** de 1885-1886, **Le Personnalisme** de 1903 — forment trois états datés de la même langue : près d'un million de mots passés dans un seul appareil de mesure. Fréquences, longueur des phrases, spécificités de chaque époque, trajectoires d'un livre à l'autre.

Le pari du comptage : un auteur ne sait pas tout ce que sa langue fait. Chaque pli ci-dessous donne ses chiffres, ses exemples — en romain à empattements quand c'est Renouvier lettre à lettre — et sa règle de calcul. **Rien ne disparaît quand vous ouvrez.**

<div class="dp" id="dp">
<style>
/* ===================== LE DÉPLIANT — feuille de style locale =====================
   Sélecteurs préfixés par #dp : le dépliant l’emporte sur le style natif des details de
   Material sans recourir à !important, et n'affecte aucune autre page du site.
   ================================================================================= */

/* --- Remise à zéro du details de Material --- */
#dp details {
  display: block; margin: 0; padding: 0; border: 0; border-radius: 0;
  background: none; box-shadow: none; font-size: inherit;
}
#dp summary {
  display: block; margin: 0; padding: 0; border: 0; border-radius: 0;
  background: none; box-shadow: none; font-size: inherit; font-weight: inherit;
  list-style: none; cursor: pointer;
}
#dp summary::-webkit-details-marker { display: none; }

#dp {
  /* Le dépliant emprunte ses couleurs au thème du site : il vit en clair comme en sombre. */
  --dp-fg:      var(--md-typeset-color, #1c1c1c);
  --dp-bg:      var(--md-default-bg-color, #ffffff);
  --dp-accent:  var(--md-accent-fg-color, #37474f);
  --dp-muted:   var(--md-default-fg-color--light, rgba(0,0,0,.54));
  --dp-rule:    var(--md-default-fg-color--lighter, rgba(0,0,0,.24));
  --dp-faint:   var(--md-default-fg-color--lightest, rgba(0,0,0,.06));
  --dp-serif:   "Iowan Old Style", "Palatino Linotype", Palatino, "Book Antiqua", Georgia, "Times New Roman", serif;
  --dp-sans:    var(--md-text-font-family, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif);
  --dp-pas:     1.1rem;
  font-family: var(--dp-sans);
  color: var(--dp-fg);
  line-height: 1.62;
  margin: 2.2rem 0 3rem;
}
#dp *, #dp *::before, #dp *::after { box-sizing: border-box; }

/* --- Barre d'outils --- */
#dp .dp-outils {
  position: sticky; top: 0; z-index: 5;
  display: flex; flex-wrap: wrap; align-items: center; gap: .45rem;
  padding: .5rem 0 .55rem; margin-bottom: 1.3rem;
  border-bottom: 1px solid var(--dp-rule); background: var(--dp-bg);
}
#dp .dp-bouton {
  font: inherit; font-size: .7rem; letter-spacing: .04em;
  padding: .28rem .68rem; cursor: pointer;
  color: var(--dp-fg); background: none;
  border: 1px solid var(--dp-rule); border-radius: 2px;
}
#dp .dp-bouton:hover { border-color: var(--dp-accent); color: var(--dp-accent); }
#dp .dp-bouton:focus-visible { outline: 2px solid var(--dp-accent); outline-offset: 2px; }
#dp .dp-compteur {
  margin-left: auto; font-size: .68rem; color: var(--dp-muted);
  font-variant-numeric: tabular-nums; letter-spacing: .02em;
}

/* --- Le pli --- */
#dp .dp-pli { display: block; margin: .05rem 0; }
#dp .dp-pli + .dp-pli { margin-top: .2rem; }
#dp .dp-titre { display: flex; align-items: baseline; gap: .5rem; padding: .34rem 0; border-radius: 2px; }
#dp .dp-titre:hover .dp-texte { color: var(--dp-accent); }
#dp .dp-titre:focus-visible { outline: 2px solid var(--dp-accent); outline-offset: 2px; }

/* Le chevron du pli */
#dp .dp-titre::before {
  content: ""; flex: 0 0 auto; position: relative; top: -.14em;
  width: .32em; height: .32em;
  border-right: 1.5px solid var(--dp-muted); border-bottom: 1.5px solid var(--dp-muted);
  border-top: 0; border-left: 0; background: none;
  transform: rotate(-45deg); transform-origin: center;
  transition: transform .18s ease, border-color .18s ease;
}
#dp .dp-pli[open] > .dp-titre::before { transform: rotate(45deg); border-color: var(--dp-accent); }
#dp .dp-titre:hover::before { border-color: var(--dp-accent); }
#dp .dp-texte { font-weight: 600; transition: color .15s ease; }

/* La marque de lecture : pleine tant que le pli n'a jamais été ouvert, creuse ensuite.
   C'est la mémoire du parcours : d'un coup d'œil, on voit ce qu'on n'a pas encore vu. */
#dp .dp-titre::after {
  content: ""; flex: 0 0 auto; margin-left: auto; align-self: center;
  width: .4em; height: .4em; border-radius: 50%;
  background: var(--dp-accent); opacity: .5; border: 0;
  transition: background .2s ease, box-shadow .2s ease, opacity .2s ease;
}
#dp .dp-pli.dp-vu > .dp-titre::after {
  background: transparent; box-shadow: inset 0 0 0 1px var(--dp-rule); opacity: 1;
}

/* Le corps : chaque niveau ajoute un filet à gauche. Les filets s'empilent comme
   les plis d'un papier qu'on ouvre : la profondeur se compte à l'œil. */
#dp .dp-corps {
  margin: .05rem 0 .5rem .16rem;
  padding: .15rem 0 .15rem var(--dp-pas);
  border-left: 1px solid var(--dp-rule);
}
#dp .dp-pli[open] > .dp-corps { animation: dp-ouvre .22s ease both; }
@keyframes dp-ouvre { from { opacity: 0; transform: translateY(-2px); } to { opacity: 1; transform: none; } }
#dp .dp-corps > p { margin: .5rem 0; }
#dp .dp-corps > p:first-child { margin-top: .2rem; }

/* --- Rangs : le rang encode la nature du pli, il ne le décore pas --- */
#dp .dp-rang {
  flex: 0 0 auto; min-width: 5.4rem;
  font-size: .61rem; letter-spacing: .11em; text-transform: uppercase;
  color: var(--dp-muted); font-weight: 500; white-space: nowrap;
}
@media (max-width: 44rem) { #dp .dp-rang { min-width: 0; } }

/* Le titre du livre : trois mots empilés, en sérif, comme une page de titre de 1854.
   Ce sont les mots de Renouvier — ils prennent donc sa voix. */
#dp .dp-pli[data-rang="titre"] > .dp-titre .dp-texte {
  font-family: var(--dp-serif); font-size: 1.35rem; font-weight: 400; letter-spacing: .01em;
}
#dp .dp-pli[data-rang="titre"] > .dp-titre { padding: .1rem 0; }
#dp .dp-pli[data-rang="titre"] > .dp-titre .dp-rang { display: none; }
#dp .dp-pli[data-rang="titre"] > .dp-titre::before { top: -.3em; }
#dp .dp-pli[data-rang="titre"]:first-of-type { margin-top: .3rem; }
#dp .dp-pli[data-rang="titre"] + .dp-pli[data-rang="titre"] { margin-top: -.1rem; }
#dp .dp-pli[data-rang="titre"] > .dp-corps { margin-top: .3rem; margin-bottom: .9rem; }
#dp .dp-pli[data-rang="essai"] > .dp-titre .dp-texte { font-size: 1.05rem; }
#dp .dp-pli[data-rang="essai"] > .dp-corps { border-left-color: var(--dp-accent); }

/* --- La voix de Renouvier ---
   Sérif : Renouvier parle. Sans sérif : on parle de lui. La typographie dit qui parle. */
#dp .dp-cite {
  font-family: var(--dp-serif); font-size: .95rem; line-height: 1.72;
  margin: .75rem 0; padding: .5rem 0 .5rem .9rem;
  border-left: 2px solid var(--dp-rule); color: var(--dp-fg);
}
#dp .dp-cite p { margin: .5rem 0; }
#dp .dp-cite p:first-child { margin-top: 0; }
#dp .dp-cite p:last-child { margin-bottom: 0; }
#dp .dp-source {
  display: block; margin-top: .45rem; font-family: var(--dp-sans);
  font-size: .66rem; letter-spacing: .04em; color: var(--dp-muted); font-style: normal;
}

/* --- Les encarts didactiques --- */
#dp .dp-note {
  margin: .8rem 0; padding: .65rem .85rem;
  background: var(--dp-faint); border-radius: 2px;
  font-size: .87rem; line-height: 1.58;
}
#dp .dp-note p { margin: .4rem 0; }
#dp .dp-note p:first-of-type { margin-top: 0; }
#dp .dp-note p:last-child { margin-bottom: 0; }
#dp .dp-etiquette {
  display: block; margin-bottom: .32rem;
  font-size: .61rem; letter-spacing: .13em; text-transform: uppercase;
  font-weight: 700; color: var(--dp-accent);
}
#dp .dp-note--cle { box-shadow: inset 2px 0 0 var(--dp-accent); }

/* --- La charnière : la forme de toute catégorie ---
   Chaque catégorie de Renouvier a la même forme : deux contraires, et leur synthèse.
   C'est une machine. La montrer, c'est expliquer neuf chapitres d'un coup. */
#dp .dp-machine { margin: 1rem 0; display: grid; gap: .4rem; }
#dp .dp-charniere {
  display: grid; grid-template-columns: 1fr auto 1fr auto 1.05fr;
  align-items: center; gap: .45rem; padding: .48rem .7rem;
  border: 1px solid var(--dp-rule); border-radius: 2px; font-size: .82rem;
}
#dp .dp-terme { text-align: center; font-family: var(--dp-serif); }
#dp .dp-op { color: var(--dp-muted); font-size: .82em; text-align: center; }
#dp .dp-synthese { text-align: center; font-family: var(--dp-serif); font-weight: 700; color: var(--dp-accent); }
#dp .dp-nom { font-size: .61rem; letter-spacing: .1em; text-transform: uppercase; color: var(--dp-muted); text-align: right; }
@media (max-width: 44rem) {
  #dp .dp-charniere { grid-template-columns: 1fr auto 1fr; row-gap: .25rem; }
  #dp .dp-charniere .dp-op--fleche { display: none; }
  #dp .dp-synthese, #dp .dp-nom { grid-column: 1 / -1; text-align: center; }
  #dp .dp-synthese::before { content: "↓ "; color: var(--dp-muted); font-weight: 400; }
  #dp .dp-nom { order: -1; text-align: center; margin-bottom: .15rem; }
}

/* --- Le miroir III / IV --- */
#dp .dp-cadre { overflow-x: auto; margin: .85rem 0; -webkit-overflow-scrolling: touch; }
#dp .dp-miroir { width: 100%; min-width: 30rem; border-collapse: collapse; font-size: .79rem; display: table; }
#dp .dp-miroir th, #dp .dp-miroir td {
  padding: .38rem .5rem; text-align: left; vertical-align: top;
  border-bottom: 1px solid var(--dp-faint);
}
#dp .dp-miroir th {
  font-size: .61rem; letter-spacing: .09em; text-transform: uppercase;
  color: var(--dp-muted); font-weight: 600; border-bottom-color: var(--dp-rule);
}
#dp .dp-miroir td:first-child { font-family: var(--dp-serif); font-weight: 700; white-space: nowrap; }
#dp .dp-ch { font-size: .68rem; color: var(--dp-muted); letter-spacing: .03em; white-space: nowrap; }

/* --- La thèse : mise en avant, mais en linéale. C'est un commentaire, pas Renouvier. --- */
#dp .dp-these {
  font-size: 1.02rem; line-height: 1.55; font-weight: 500;
  margin: .4rem 0 1.3rem; padding: .6rem 0 .6rem .9rem;
  border-left: 2px solid var(--dp-accent);
}

/* --- Divers --- */
#dp .dp-chapo { font-size: .84rem; color: var(--dp-muted); margin: .1rem 0 .65rem; }
#dp .dp-epigraphe {
  font-family: var(--dp-serif); font-size: .76rem; letter-spacing: .06em;
  text-transform: uppercase; color: var(--dp-accent); margin: .25rem 0 .75rem;
}
#dp .dp-liste { margin: .55rem 0; padding-left: 1.05rem; }
#dp .dp-liste li { margin: .28rem 0; }
#dp .dp-legende {
  display: flex; flex-wrap: wrap; gap: 1rem;
  font-size: .68rem; color: var(--dp-muted);
  margin-top: 1.6rem; padding-top: .8rem; border-top: 1px solid var(--dp-faint);
}
#dp .dp-puce { display: inline-block; width: .4em; height: .4em; border-radius: 50%; background: var(--dp-accent); opacity: .5; margin-right: .35em; vertical-align: middle; }
#dp .dp-puce--vue { background: transparent; box-shadow: inset 0 0 0 1px var(--dp-rule); opacity: 1; }

@media (prefers-reduced-motion: reduce) {
  #dp *, #dp *::before, #dp *::after { animation: none !important; transition: none !important; }
}
/* --- Le double miroir : le même outil sur le monde, puis sur l'homme.
   À gauche il échoue (gris), à droite il réussit (accent). La couleur porte l'argument. --- */
#dp .dp-double td.dp-non { color: var(--dp-muted); }
#dp .dp-double td.dp-oui { color: var(--dp-accent); font-weight: 600; font-family: var(--dp-serif); }
#dp .dp-double th.dp-tete-non, #dp .dp-double th.dp-tete-oui { text-align: left; }
#dp .dp-double th.dp-tete-oui { color: var(--dp-accent); }

/* --- L'escalier des formulaires : quatre marches, un pli à chaque charnière --- */
#dp .dp-escalier { margin: 1rem 0; display: grid; gap: .3rem; }
#dp .dp-marche {
  display: grid; grid-template-columns: 4.6rem 1fr; gap: .7rem; align-items: baseline;
  padding: .45rem .7rem; border-left: 2px solid var(--dp-rule); font-size: .84rem;
}
#dp .dp-marche--pli {
  border-left-color: var(--dp-accent); background: var(--dp-faint);
  font-family: var(--dp-serif); font-size: .8rem;
}
#dp .dp-marche-num { font-size: .61rem; letter-spacing: .1em; text-transform: uppercase; color: var(--dp-muted); }
#dp .dp-marche--pli .dp-marche-num { color: var(--dp-accent); font-family: var(--dp-sans); }
@media (max-width: 44rem) {
  #dp .dp-marche { grid-template-columns: 1fr; gap: .15rem; }
}
/* --- L'appareil critique ---
   Deux états d'une même phrase, l'un sous l'autre, la variante seule en relief.
   C'est la figure de cette page : tout le reste du texte est identique, et c'est
   précisément ce qui rend le mot changé lisible. */
#dp .dp-variante {
  margin: 1rem 0; border: 1px solid var(--dp-rule); border-radius: 2px; overflow: hidden;
}
#dp .dp-var-ligne {
  display: grid; grid-template-columns: 3.2rem 1fr; gap: .7rem; align-items: baseline;
  padding: .6rem .8rem; font-family: var(--dp-serif); font-size: .92rem; line-height: 1.55;
}
#dp .dp-var-ligne + .dp-var-ligne { border-top: 1px solid var(--dp-faint); }
#dp .dp-var-an {
  font-family: var(--dp-sans); font-size: .63rem; letter-spacing: .09em;
  color: var(--dp-muted); font-variant-numeric: tabular-nums; white-space: nowrap;
}
#dp .dp-var-ligne--neuf { background: var(--dp-faint); }
#dp .dp-var-ligne--neuf .dp-var-an { color: var(--dp-accent); font-weight: 700; }
#dp .dp-avant { text-decoration: line-through; text-decoration-thickness: 1px; opacity: .55; }
#dp .dp-apres { color: var(--dp-accent); font-weight: 700; }
#dp .dp-ajout {
  color: var(--dp-accent); box-shadow: inset 0 -.5em 0 -.1em var(--dp-faint);
}
@media (max-width: 44rem) {
  #dp .dp-var-ligne { grid-template-columns: 1fr; gap: .1rem; }
}

/* --- La balance : ce qui entre, ce qui sort, ce qui ne bouge pas --- */
#dp .dp-balance { display: grid; gap: .35rem; margin: 1rem 0; }
#dp .dp-poste {
  display: grid; grid-template-columns: 1.5rem 1fr; gap: .6rem; align-items: baseline;
  padding: .42rem .7rem; border-left: 2px solid var(--dp-rule); font-size: .85rem;
}
#dp .dp-poste--plus { border-left-color: var(--dp-accent); }
#dp .dp-poste--socle { border-left-style: dotted; }
#dp .dp-signe { font-family: var(--dp-serif); font-weight: 700; text-align: center; color: var(--dp-muted); }
#dp .dp-poste--plus .dp-signe { color: var(--dp-accent); }
#dp .dp-renvoi { margin: .95rem 0 0; font-size: .8rem; color: var(--dp-muted); }
#dp .dp-renvoi a { color: var(--dp-accent); }

/* --- tableaux de chiffres (ajout lexicométrie) --- */
#dp table.dp-tab{border-collapse:collapse;margin:.9rem 0;font-size:.86em;line-height:1.45;width:auto}
#dp table.dp-tab th,#dp table.dp-tab td{border:1px solid var(--md-default-fg-color--lightest);padding:.28rem .6rem;text-align:right;font-variant-numeric:tabular-nums}
#dp table.dp-tab th:first-child,#dp table.dp-tab td:first-child{text-align:left;font-style:normal}
#dp table.dp-tab thead th{background:var(--md-code-bg-color);font-weight:600}
#dp table.dp-tab td.dp-t92{color:var(--dp-muted);font-style:italic}
</style>
<div class="dp-outils">
<button class="dp-bouton" type="button" data-dp="tout">Tout déplier</button>
<button class="dp-bouton" type="button" data-dp="rien">Tout replier</button>
<button class="dp-bouton" type="button" data-dp="neufs">Aller au premier pli non ouvert</button>
<span class="dp-compteur" id="dp-compteur" aria-live="polite"></span>
</div>

<details class="dp-pli" data-rang="corpus">
<summary class="dp-titre"><span class="dp-rang">la règle du jeu</span><span class="dp-texte">Trois états d'une langue, délimités avant de compter</span></summary>
<div class="dp-corps">
<p>Un corpus mal borné produit des chiffres exacts qui ne veulent rien dire. Celui-ci est donc délimité avant tout calcul, et une fois pour toutes : trois strates datées, chacune faite de volumes entiers, tels que transcrits sur ce site.</p>
<table class="dp-tab">
<thead><tr><th>strate</th><th>œuvres</th><th>édition</th><th>mots</th></tr></thead>
<tbody>
<tr><td><strong>1875</strong></td><td>Premier Essai, t. II–III · Deuxième Essai, t. II–III</td><td>2ᵉ éd., Bureau de la Critique philosophique</td><td>376 259</td></tr>
<tr><td><strong>1885-1886</strong></td><td>Esquisse d'une classification systématique des doctrines philosophiques, t. I–II</td><td>éd. originale</td><td>399 690</td></tr>
<tr><td><strong>1903</strong></td><td>Le Personnalisme, avec l'étude sur la perception externe et sur la force</td><td>éd. originale, Alcan</td><td>174 042</td></tr>
<tr><td class="dp-t92"><em>contrôle 1892</em></td><td class="dp-t92">Troisième Essai, t. I</td><td class="dp-t92">2ᵉ éd., remaniée d'un texte de 1864</td><td class="dp-t92">88 913</td></tr>
</tbody>
</table>
<p>Deux strates de taille presque égale, une troisième moitié moindre mais largement suffisante ; toutes les fréquences de cette page sont donc rapportées <em>pour 10 000 mots</em>, ce qui rend les trois livres comparables. Le tome de 1892 est mis à part : c'est la révision tardive d'un texte écrit sous l'Empire, un composé de deux dates — on le garde comme <em>point de contrôle</em>, et il jouera ce rôle à merveille dans la page voisine.</p>
<div class="dp-note">
<span class="dp-etiquette">Ce qui est compté, ce qui ne l'est pas</span>
<p>Est compté : tout le texte de Renouvier, préfaces, formulaires et notes comprises — y compris les passages où il cite autrui (Mill, Spencer, Hume…), qui font partie du livre publié et qu'aucun procédé automatique ne saurait excommunier proprement. N'est pas compté : l'appareil du site (titres de chapitres reproduits en balisage, indications de pagination, mentions d'édition). Les mots coupés par les changements de page ou de ligne des transcriptions — trois cent vingt et une césures — ont été recollés avant tout calcul.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="mesure">
<summary class="dp-titre"><span class="dp-rang">première surprise</span><span class="dp-texte">La phrase s'allonge de dix mots</span></summary>
<div class="dp-corps">
<p>Les mesures d'ensemble d'abord. La richesse du vocabulaire est remarquablement stable — par tranches de 10 000 mots, on rencontre environ 2 000 mots différents dans les <em>Essais</em>, 2 080 dans les deux livres suivants : Renouvier n'appauvrit ni n'enfle sa langue. Ce qui change, c'est la phrase.</p>
<table class="dp-tab">
<thead><tr><th>strate</th><th>phrases</th><th>longueur moyenne</th><th>médiane</th></tr></thead>
<tbody>
<tr><td><strong>1875</strong></td><td>9 747</td><td>38,5 mots</td><td>32</td></tr>
<tr><td><strong>1885-1886</strong></td><td>8 076</td><td><strong>49,4 mots</strong></td><td><strong>42</strong></td></tr>
<tr><td><strong>1903</strong></td><td>3 711</td><td>46,9 mots</td><td>41</td></tr>
<tr><td class="dp-t92"><em>1892</em></td><td class="dp-t92">2 215</td><td class="dp-t92">40,1 mots</td><td class="dp-t92">33</td></tr>
</tbody>
</table>
<p>Dix mots de plus en moyenne, dix de plus en médiane : entre les <em>Essais</em> et l'<em>Esquisse</em>, la phrase de Renouvier change de gabarit, et ne reviendra plus en arrière. La raison saute aux yeux dès qu'on lit : le traité de 1875 découpe — propositions numérotées, formulaires, définitions — quand l'<em>Esquisse</em> déroule, balance les doctrines l'une contre l'autre, tient des séries entières dans une seule période. En voici une, prise à la première page du tome II :</p>
<div class="dp-cite">
<p>Il m'a semblé qu'à la condition de faire mes plus sincères efforts pour qu'aucune ne perdit rien de sa véritable physionomie et de son énergie propre, je ne pourrais qu'ajouter à la clarté de toutes les thèses d'une même série : — <em>la cause</em>, <em>l'infini</em>, <em>l'évolution</em>, <em>la nécessité</em>, <em>le bonheur</em>, — en les considérant du point de vue des thèses de la série opposée : — <em>l'idée</em>, <em>le fait</em>, <em>la création</em>, <em>la liberté</em>, <em>le devoir</em>, — sans m'obliger à balancer cette critique par une critique inverse, et feindre une indifférence que je n'éprouve pas.</p>
<span class="dp-source">Esquisse, t. II, p. 1</span>
</div>
<p>Quatre-vingt-quatorze mots, deux séries de cinq thèses, une confession finale : la phrase est devenue l'unité de la comparaison des doctrines. Et le point de contrôle confirme par l'absurde : le tome révisé en 1892, texte d'origine impériale, garde la phrase courte des <em>Essais</em> — 40 mots de moyenne, 33 de médiane. La longueur de phrase date un texte mieux que sa page de titre.</p>
</div>
</details>

<details class="dp-pli" data-rang="spécificités">
<summary class="dp-titre"><span class="dp-rang">l'empreinte de chaque livre</span><span class="dp-texte">Ce que chaque époque est seule à dire</span></summary>
<div class="dp-corps">
<p>Pour chaque mot, on peut calculer la probabilité que sa fréquence dans une strate soit due au hasard de la répartition (méthode dite des spécificités, loi hypergéométrique). On note S l'ordre de grandeur de cette improbabilité : S&nbsp;=&nbsp;20 signifie une chance sur 10²⁰. Voici, pour chaque époque, les mots pleins les plus sur-représentés — l'empreinte digitale de chaque livre :</p>
<table class="dp-tab">
<thead><tr><th>1875 — le traité</th><th>1885-1886 — la classification</th><th>1903 — la physique</th></tr></thead>
<tbody>
<tr><td>syllogisme (51)</td><td>bonheur (98)</td><td>corps (126)</td></tr>
<tr><td>catégories (45)</td><td>évolution (51)</td><td>forces (62)</td></tr>
<tr><td>expérience (44)</td><td>doctrine (51)</td><td>perception (60)</td></tr>
<tr><td>synthèse (38)</td><td>plaisir (48)</td><td>monades (52)</td></tr>
<tr><td>proposition (36)</td><td>morale (46)</td><td>chaleur (47)</td></tr>
<tr><td>induction (32)</td><td>devoir (45)</td><td>Boscovich (47)</td></tr>
<tr><td>prémisses (25)</td><td>Platon (44)</td><td>molécules (34)</td></tr>
<tr><td>Mill (24)</td><td>infini (35)</td><td>gravitation (26)</td></tr>
<tr><td>tout-être (28)</td><td>Hume (23)</td><td>Reid (26)</td></tr>
</tbody>
</table>
<p>Rien de forcé dans ces colonnes : elles sortent du calcul aveugle, et elles récitent pourtant la table des matières d'une vie. Le traité de logique a pour signature ses outils (<em>syllogisme</em>, <em>prémisses</em>, <em>catégories</em>) et son adversaire de travail (<em>Mill</em>) ; l'<em>Esquisse</em>, ses thèses morales (<em>bonheur</em>, <em>devoir</em>, <em>plaisir</em>) et ses classiques (<em>Platon</em>, <em>Hume</em>) ; <em>Le Personnalisme</em>, sa matière (<em>corps</em>, <em>molécules</em>, <em>chaleur</em>) et ses alliés tardifs (<em>Boscovich</em>, <em>Reid</em>).</p>
<div class="dp-note">
<span class="dp-etiquette">Les intruses : q, b, m</span>
<p>En tête absolue des spécificités de 1875 ne figurent pas des mots, mais des lettres : <em>q</em> (S&nbsp;=&nbsp;118), <em>b</em> (82), <em>m</em> (77), et des paires comme <em>eq</em>. Ce sont les variables des formules logiques du Premier Essai — le calcul les détecte comme un vocabulaire à part entière, propre à 1875 et à lui seul. Il a raison : c'est exactement ce qu'elles sont.</p>
<p class="dp-renvoi">Ces lettres ont leur page : <a href="/recherche/logique-philosophique/systeme-en-formules/">Le système en formules</a> les déplie une à une.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="trajectoires">
<summary class="dp-titre"><span class="dp-rang">le film</span><span class="dp-texte">Quatre mouvements, mot à mot</span></summary>
<div class="dp-corps">
<p>Les spécificités photographient chaque livre ; les trajectoires font le film. Fréquences pour 10 000 mots, de gauche à droite : 1875, 1885-1886, 1903 — la colonne italique donne le point de contrôle de 1892.</p>
<p><strong>1. L'appareil technique se replie.</strong> Le vocabulaire qui fait la machinerie des <em>Essais</em> n'est plus guère prononcé ensuite : le système est posé, il n'est plus répété.</p>
<table class="dp-tab">
<thead><tr><th>mot</th><th>1875</th><th>1886</th><th>1903</th><th>1892</th></tr></thead>
<tbody>
<tr><td>catégorie(s)</td><td>8,4</td><td>0,9</td><td>1,7</td><td class="dp-t92">5,3</td></tr>
<tr><td>représentation(s)</td><td>12,0</td><td>4,3</td><td>5,7</td><td class="dp-t92">13,8</td></tr>
<tr><td>fonction(s)</td><td>10,9</td><td>3,0</td><td>5,8</td><td class="dp-t92">18,9</td></tr>
<tr><td>science(s)</td><td>20,1</td><td>9,3</td><td>7,9</td><td class="dp-t92">18,0</td></tr>
<tr><td>vérité(s)</td><td>12,0</td><td>7,2</td><td>2,8</td><td class="dp-t92">4,4</td></tr>
<tr><td><strong>certitude</strong></td><td><strong>6,5</strong></td><td><strong>3,0</strong></td><td><strong>0,6</strong></td><td class="dp-t92">4,6</td></tr>
</tbody>
</table>
<p>La chute de <em>certitude</em> est la plus parlante : le Deuxième Essai lui consacrait son sous-titre même, et le mot s'éteint — divisé par dix. Non que la chose soit abandonnée : elle est acquise, donc tue.</p>
<p><strong>2. Le tournant théologique s'imprime dans les mots.</strong> En 1875, <em>création</em> est un mot presque introuvable (sa rareté y est elle-même une spécificité : S&nbsp;=&nbsp;−46). Après la bascule des années 1880, il s'installe et ne repart plus.</p>
<table class="dp-tab">
<thead><tr><th>mot</th><th>1875</th><th>1886</th><th>1903</th><th>1892</th></tr></thead>
<tbody>
<tr><td>Dieu</td><td>2,8</td><td>8,4</td><td>6,5</td><td class="dp-t92">4,7</td></tr>
<tr><td>création</td><td>0,8</td><td>6,1</td><td>6,3</td><td class="dp-t92">4,2</td></tr>
<tr><td>créateur</td><td>0,4</td><td>2,3</td><td>4,3</td><td class="dp-t92">0,9</td></tr>
<tr><td>péché</td><td>0,0</td><td>0,5</td><td>1,1</td><td class="dp-t92">0,2</td></tr>
<tr><td>mal</td><td>2,9</td><td>8,6</td><td>5,3</td><td class="dp-t92">2,7</td></tr>
</tbody>
</table>
<p><strong>3. La physique fait irruption.</strong> Le dernier livre parle un lexique que les <em>Essais</em> ne connaissaient presque pas :</p>
<table class="dp-tab">
<thead><tr><th>mot</th><th>1875</th><th>1886</th><th>1903</th><th>1892</th></tr></thead>
<tbody>
<tr><td>corps</td><td>7,6</td><td>3,2</td><td><strong>27,8</strong></td><td class="dp-t92">30,0</td></tr>
<tr><td>force(s)</td><td>14,7</td><td>7,6</td><td><strong>35,8</strong></td><td class="dp-t92">31,3</td></tr>
<tr><td>matière</td><td>5,7</td><td>9,6</td><td>18,4</td><td class="dp-t92">24,6</td></tr>
<tr><td>monade(s)</td><td>0,5</td><td>0,7</td><td><strong>10,1</strong></td><td class="dp-t92">1,8</td></tr>
</tbody>
</table>
<p><strong>4. Les chassés-croisés.</strong> <em>Liberté</em> tombe de 12,5 à 3,3 — non par reniement : parce que la cause est entendue, le mot cède la place au mot d'exécution, <em>volonté</em>, qui reste imperturbable (8,8 → 9,2 → 10,9). <em>Croyance</em> culmine dans l'<em>Esquisse</em> (6,0 → 11,5 → 6,5), le livre du pari ; <em>infini</em> aussi (5,2 → 16,2 → 9,4), le livre qui classe les doctrines selon leur réponse à l'infini ; <em>nécessité</em> de même (5,7 → 8,3 → 1,3) — on ne discute la nécessité que tant qu'elle est l'adversaire du jour.</p>
<p>Quant au tome de contrôle, il est exactement l'hybride que sa date double annonçait : l'appareil des <em>Essais</em> (<em>fonction</em> 18,9, <em>représentation</em> 13,8) sur le sujet du dernier livre (<em>corps</em> 30,0, <em>matière</em> 24,6) — c'est le tome des principes de la nature, révisé tard.</p>
<p class="dp-renvoi">Ces courbes chiffrent ce que la page <a href="/recherche/complications/evolution/">Comment je suis arrivé à cette conclusion</a> établissait par les textes : la lecture datait la bascule, le comptage en donne l'amplitude.</p>
</div>
</details>

<details class="dp-pli" data-rang="paradoxe">
<summary class="dp-titre"><span class="dp-rang">contre-épreuve</span><span class="dp-texte">Le personnalisme sans le mot « personne »</span></summary>
<div class="dp-corps">
<p>On attendrait que le livre nommé <em>Le Personnalisme</em> soit saturé de son propre nom. Les chiffres disent autre chose : <em>personne(s)</em> passe de 6,2 à 7,8 pour 10 000 mots — une hausse à peine perceptible — et <em>personnalisme</em> lui-même, mot que Renouvier invente pour son titre, n'atteint que 0,6. Pendant ce temps <em>conscience</em>, le grand mot des <em>Essais</em>, recule de moitié (21,4 → 11,0), et c'est <em>monade</em> qui fait le travail (0,5 → 10,1).</p>
<p>Le baptême est donc l'inverse d'une inflation : en 1903, la personne n'est plus un thème qu'on martèle, c'est la maison qu'on habite — et l'on ne prononce pas le nom de sa maison à chaque phrase. Le vocabulaire qui monte est celui de l'ameublement : corps, forces, perception, monades.</p>
<p class="dp-renvoi">La contre-épreuve grammaticale est plus étonnante encore — le pronom <em>je</em> s'efface au moment même où la doctrine prend le nom de la personne : voir <a href="/recherche/linguistique/etiquetage-morphosyntaxique/">Étiquetage morpho-syntaxique</a>, où l'on compte non plus les mots pleins, mais la grammaire.</p>
</div>
</details>

<details class="dp-pli" data-rang="méthode">
<summary class="dp-titre"><span class="dp-rang">tout est refaisable</span><span class="dp-texte">Note de méthode</span></summary>
<div class="dp-corps">
<p><strong>Corpus.</strong> Trois strates closes avant tout calcul : quatre tomes de la seconde édition des <em>Essais</em> (Premier Essai t. II–III, Deuxième Essai t. II–III, 1875) ; les deux tomes de l'<em>Esquisse</em> (1885-1886) ; <em>Le Personnalisme</em> avec son Étude (1903). Le Troisième Essai t. I (2ᵉ éd., 1892) sert de point de contrôle et n'entre dans aucun calcul de spécificité. Tout le texte de Renouvier est compté, citations d'autrui comprises ; l'appareil du site (balisage des titres, marqueurs de pagination, notices d'édition) est retiré.</p>
<p><strong>Préparation.</strong> Les mots coupés par les changements de page ou de ligne des transcriptions ont été recollés (321 césures). Les élisions sont détachées (<em>l'espace</em> → <em>l'</em> + <em>espace</em>), le trait d'union d'époque après <em>très-</em> est dénoué, les inversions du type <em>est-il</em>, <em>dit-on</em> sont rendues à leurs deux mots. Pas de lemmatisation : <em>force</em> et <em>forces</em> sont comptés séparément, puis regroupés à la main quand la ligne du tableau l'indique.</p>
<p><strong>Mesures.</strong> Fréquences rapportées pour 10 000 mots. Richesse lexicale par tranches de 10 000 mots (moyenne des tranches), seule façon de comparer des livres de tailles différentes. Longueur des phrases après protection des abréviations courantes (M., ch., t., etc.). Spécificités calculées par la loi hypergéométrique (méthode Lafon) : chaque strate contre la réunion des trois ; S est le logarithme décimal, changé de signe, de la probabilité d'obtenir par hasard une fréquence au moins aussi extrême.</p>
<p><strong>Limites.</strong> Le comptage ignore le sens : il ne distingue pas <em>mal</em> substantif de <em>mal</em> adverbe, ni ne sait qui parle quand Renouvier cite. Les ordres de grandeur sont robustes à ces flous ; les décimales, non. On ne conclut ici que sur les premiers.</p>
<p><strong>Reproductibilité.</strong> Toutes les valeurs de cette page sortent d'un unique programme de dépouillement appliqué aux transcriptions publiées sur ce site ; quiconque refait le comptage avec les mêmes règles retrouvera les mêmes nombres.</p>
</div>
</details>

<div class="dp-legende">
<span><span class="dp-puce"></span> pli jamais ouvert</span>
<span><span class="dp-puce dp-puce--vue"></span> pli déjà ouvert</span>
<span>texte en sérif = Renouvier</span>
<span>texte en linéale = commentaire</span>
</div>
</div>

<script>
(function () {
  var racine = document.getElementById("dp");
  if (!racine) return;
  var plis = Array.prototype.slice.call(racine.querySelectorAll("details.dp-pli"));
  var compteur = document.getElementById("dp-compteur");

  function majCompteur() {
    if (!compteur) return;
    var ouverts = plis.filter(function (p) { return p.open; }).length;
    var vus = plis.filter(function (p) { return p.classList.contains("dp-vu"); }).length;
    var reste = plis.length - vus;
    compteur.textContent = ouverts + (ouverts > 1 ? " plis ouverts sur " : " pli ouvert sur ")
      + plis.length + " · " + reste + (reste > 1 ? " jamais ouverts" : " jamais ouvert");
  }

  plis.forEach(function (pli) {
    pli.addEventListener("toggle", function () {
      if (pli.open) pli.classList.add("dp-vu");
      majCompteur();
    });
  });

  racine.addEventListener("click", function (e) {
    var b = e.target.closest("[data-dp]");
    if (!b) return;
    var action = b.getAttribute("data-dp");
    if (action === "tout") {
      plis.forEach(function (p) { p.open = true; p.classList.add("dp-vu"); });
    } else if (action === "rien") {
      plis.forEach(function (p) { p.open = false; });
    } else if (action === "neufs") {
      var cible = plis.filter(function (p) { return !p.classList.contains("dp-vu"); })[0];
      if (!cible) return;
      var parent = cible.parentElement;
      while (parent && parent !== racine) {
        if (parent.tagName === "DETAILS") parent.open = true;
        parent = parent.parentElement;
      }
      cible.scrollIntoView({ behavior: "smooth", block: "center" });
      var t = cible.querySelector("summary");
      if (t) t.focus({ preventScroll: true });
    }
    majCompteur();
  });

  majCompteur();
})();
</script>

---

## Note de méthode

Cette page suit les règles de ses deux sœurs — [Compliquer les Essais pour les expliquer](../complications/essais.md) et [La physique du personnalisme](../complications/physique-tardive.md) : le pli conserve tout ; les voies non prises restent visibles ; la profondeur se compte aux filets ; le parcours se souvient ; la typographie dit qui parle, sérif pour Renouvier, linéale pour le commentaire.

Elle en ajoute une, qui lui est propre. **Ici, le commentaire porte une accusation** — celle d'avoir bougé sans le dire. Il ne peut donc rien avancer qui ne soit vérifiable dans les fichiers du site : chaque variante est donnée dans ses deux états, chaque expression déclarée absente d'un état a été comptée dans les deux, et l'appareil de comparaison est décrit sous le pli « l'outil », avec ce qu'il a dû écarter.

**Sources.** *Essais de critique générale*, 2ᵉ éd., Au Bureau de la Critique philosophique, 1875 : *Premier Essai*, t. II–III ; *Deuxième Essai*, t. II–III. — *Esquisse d'une classification systématique des doctrines philosophiques*, t. I (1885) et t. II (1886). — *Le Personnalisme, suivi d'une étude sur la perception externe et sur la force*, Félix Alcan, 1903. — Point de contrôle : *Troisième Essai, Les Principes de la nature*, 2ᵉ éd. corrigée et augmentée, 1892, t. I. Transcriptions intégrales de ce site ; comptages sur ces transcriptions.
