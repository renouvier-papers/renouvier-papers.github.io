---
title: "La physique du personnalisme"
description: "Le Personnalisme, suivi d'une étude sur la perception externe et sur la force (1903), déplié."
---

# La physique du personnalisme

En 1854, un homme de trente-neuf ans entreprend de démolir la métaphysique. Il y passera un demi-siècle : pas de chose en soi, pas de substance, pas d'infini, pas d'absolu — des fétiches, tous, des mots qu'on a pris pour des dieux.

En 1903, à quatre-vingt-huit ans, mourant, il publie son dernier livre. Les derniers mots en sont : *et c'est l'harmonie préétablie*.

Cette page déplie le livre qui va de l'un à l'autre. Ce n'est pas un reniement — c'est le seul endroit où le fil pouvait aboutir. Fermée, la page tient en un titre. Chaque terme s'ouvre sur ce qu'il contient ; ce qu'il contient s'ouvre encore. **Rien ne disparaît quand vous ouvrez** : les voies que vous n'avez pas prises restent là, repliées, à côté de celle que vous avez prise.

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
/* --- Le pont, qui n'existe pas ---
   Deux questions, deux sens, un trou au milieu. C'est tout le livre, et c'est
   la seule figure dont cette page a besoin : le vide y est un élément, pas un blanc. */
#dp .dp-pont {
  display: grid; grid-template-columns: 1fr 8.5rem 1fr; align-items: stretch;
  margin: 1.2rem 0; border: 1px solid var(--dp-rule); border-radius: 2px; overflow: hidden;
}
#dp .dp-rive {
  padding: 1.1rem .8rem; display: flex; flex-direction: column; justify-content: center; gap: .55rem;
}
#dp .dp-rive-nom {
  font-family: var(--dp-serif); font-size: .95rem; font-weight: 700; text-align: center;
}
#dp .dp-fleche {
  font-size: .78rem; color: var(--dp-accent); text-align: center; line-height: 1.35;
}
#dp .dp-fleche em { color: var(--dp-muted); font-style: normal; font-size: .92em; }
#dp .dp-trou {
  padding: 1.1rem .5rem;
  display: flex; flex-direction: column; justify-content: center; gap: .3rem;
  border-left: 1px dashed var(--dp-rule); border-right: 1px dashed var(--dp-rule);
  background: var(--dp-faint); text-align: center;
}
#dp .dp-trou-titre {
  font-size: .61rem; letter-spacing: .13em; text-transform: uppercase;
  font-weight: 700; color: var(--dp-accent);
}
#dp .dp-trou-texte { font-size: .78rem; color: var(--dp-muted); line-height: 1.4; }
@media (max-width: 44rem) {
  #dp .dp-pont { grid-template-columns: 1fr; }
  #dp .dp-trou { border-left: 0; border-right: 0; border-top: 1px dashed var(--dp-rule); border-bottom: 1px dashed var(--dp-rule); min-width: 0; }
  #dp .dp-rive { padding: .85rem .8rem; }
}
</style>
<div class="dp-outils">
<button class="dp-bouton" type="button" data-dp="tout">Tout déplier</button>
<button class="dp-bouton" type="button" data-dp="rien">Tout replier</button>
<button class="dp-bouton" type="button" data-dp="neufs">Aller au premier pli non ouvert</button>
<span class="dp-compteur" id="dp-compteur" aria-live="polite"></span>
</div>

<p class="dp-chapo">Charles Renouvier — <em>Le Personnalisme, suivi d'une étude sur la perception externe et sur la force</em>, Paris, Félix Alcan, 1903. Publié l'année de sa mort.</p>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">Le Personnalisme</span></summary>
<div class="dp-corps">
<p>Le mot arrive à la fin, sur la couverture du dernier livre — mais la chose était là dès 1854, dans une liste de neuf. La neuvième catégorie de la <em>Logique générale</em> s'appelait <em>personnalité</em> : soi, non-soi, conscience. Il aura fallu quarante-neuf ans pour que le titre rattrape la trouvaille.</p>
<div class="dp-cite">
<p>[…] la connaissance de la personne en tant que conscience et volonté est le fondement de toutes les connaissances humaines.</p>
<span class="dp-source">Le Personnalisme, préface</span>
</div>
<div class="dp-note">
<span class="dp-etiquette">Trois parties, et la troisième surprend</span>
<p>Le Personnalisme proprement dit tient en trois parties : la <strong>métaphysique</strong>, la <strong>sociologie</strong>, l'<strong>eschatologie</strong>. Une doctrine de la connaissance, une doctrine de la société, une doctrine des fins dernières. Le même homme, dans le même livre, fonde la logique et se demande ce que deviennent les personnes après la fin du monde.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">suivi d'une étude</span></summary>
<div class="dp-corps">
<p>Voilà le mot qui trompe, et il faut le désamorcer tout de suite. « Suivi de » annonce un appendice, un supplément, une pièce jointe. Cette étude fait <strong>cinquante chapitres</strong> — plus que le livre qu'elle est censée suivre. Et Renouvier prévient dès sa première phrase :</p>
<div class="dp-cite">
<p>Les deux questions réunies par le titre de cet ouvrage en composent réellement une seule, avec ses principales dépendances.</p>
<span class="dp-source">Le Personnalisme, préface, première phrase</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Les deux sens d'une seule relation</span>
<p>Le <em>Personnalisme</em> part de la personne et descend vers les objets : il « déduit » ce qu'on peut connaître des choses à partir du rapport du sujet à l'objet mental. L'<em>Étude</em> « prend la question de la connaissance <strong>sous l'aspect inverse</strong>, en considérant les objets externes comme donnés par eux-mêmes ».</p>
<p>Un aller, un retour. Ce n'est pas un livre et son annexe : c'est une relation parcourue dans les deux sens.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Mais laquelle des deux porte l'autre ? Renouvier tranche</span>
<p>On serait tenté de dire les deux moitiés indissociables. Ce serait aller plus loin que le texte. La préface dit que l'Étude « a pour objet l'éclaircissement de ce problème <strong>en rapport avec la doctrine personnaliste</strong> » : la doctrine est là <em>avant</em>, l'Étude l'éclaire. Et la même préface date le personnalisme de 1854 — donc bien avant toute théorie de la force.</p>
<p>Le rapport juste n'est pas la dépendance, c'est la <strong>convergence par l'autre bout</strong>. Le personnalisme est établi par la logique, puis par la morale. L'Étude part de l'extrémité opposée — les corps, la thermodynamique, l'éther — et retombe sur des personnes. Ce n'est pas un fondement : c'est une vérification indépendante, et c'est plus fort qu'une indissociabilité. Deux routes qui ne se ressemblent pas, un seul point d'arrivée.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">sur la perception externe et sur la force</span></summary>
<div class="dp-corps">
<p>Deux sujets, dit le titre. Un seul, dit le livre — et c'est là toute l'affaire. Ce sont les deux sens du même trajet, entre une conscience et un corps.</p>
<ul class="dp-liste">
<li><strong>La perception externe</strong> — comment se peut-il que les changements d'un objet, « qui sont autre chose que ces sensations », soient <em>suivis</em> de sensations en moi ? <em>(le corps vers moi)</em></li>
<li><strong>La force</strong> — comment se fait-il que « des désirs et des actes de volonté, phénomènes internes d'une conscience, soient régulièrement suivis de certains changements de l'objet externe » ? <em>(moi vers le corps)</em></li>
</ul>
<p>Renouvier pose la seconde question dans la préface et la laisse tomber sans ménagement :</p>
<div class="dp-cite">
<p>Qu'est-ce que ce mécanisme ? La question de la <em>force</em>, ou de la <em>nature de la force</em>, se pose à cet endroit.</p>
<span class="dp-source">Le Personnalisme, préface</span>
</div>
<p>Cinquante chapitres plus loin, la réponse tiendra en un mot de Leibniz.</p>
</div>
</details>

<p class="dp-epigraphe">— le livre en une phrase —</p>
<p class="dp-these">Entre ma volonté et mon bras qui se lève, rien ne passe. Entre le caillou et ma sensation du caillou, rien ne passe non plus. Cinquante chapitres pour établir ce vide — et, pour finir, une seule doctrine qui puisse s'en accommoder : le monde physique est fait de personnes.</p>

<details class="dp-pli" data-rang="palier">
<summary class="dp-titre"><span class="dp-rang">↓ déplier</span><span class="dp-texte">Le livre en un paragraphe</span></summary>
<div class="dp-corps">
<p>Renouvier pose <strong>deux questions qui n'en font qu'une</strong> : comment un corps produit-il ma sensation, et comment ma volonté produit-elle un mouvement ? Il consacre dix-huit chapitres à examiner toutes les réponses données depuis Descartes — Locke, Condillac, Maine de Biran, Berkeley, Reid, Hamilton, Bain, Mill, Taine, Kant, James — puis vingt-cinq de plus à examiner toutes les physiques : l'inertie, la masse, l'énergie, la thermodynamique, l'éther, la gravitation. Le résultat est partout le même : <strong>rien ne passe</strong>. Aucun intermédiaire n'est perçu, aucune transmission n'est intelligible. Alors il retourne le problème. Le seul endroit au monde où nous connaissions une force par le dedans, c'est le vouloir : <strong>la force est la volonté</strong>, et le mot que la physique emploie lui est « secrètement emprunté ». Donc les forces de la nature sont des volontés ; donc les éléments du monde physique sont des agents mentaux — « on peut les appeler des <strong>monades</strong> ». Mais des monades ne peuvent pas se toucher, puisque rien ne passe : il faut donc que leurs états s'accordent sans agir les uns sur les autres, et <strong>c'est l'harmonie préétablie</strong>. Celle de Leibniz, à deux corrections près, qui sont les deux thèses de toute une vie : pas d'<strong>infini</strong>, et une <strong>variable indépendante</strong> dans les équations du monde.</p>
<p class="dp-chapo">Chacun des sept termes en gras s'ouvre ci-dessous. Vous pouvez vous arrêter ici : ce paragraphe est vrai. Vous pouvez aussi tirer sur un fil.</p>

<details class="dp-pli" data-rang="la figure">
<summary class="dp-titre"><span class="dp-rang">le pont</span><span class="dp-texte">deux questions qui n'en font qu'une</span></summary>
<div class="dp-corps">
<p>Tout le livre tient dans cette figure, et le plus important y est le milieu.</p>
<div class="dp-pont">
<div class="dp-rive">
<span class="dp-rive-nom">une conscience</span>
<span class="dp-fleche"><em>la force</em><br>ma volonté →</span>
<span class="dp-fleche"><em>la perception externe</em><br>ma sensation ←</span>
</div>
<div class="dp-trou">
<span class="dp-trou-titre">rien</span>
<span class="dp-trou-texte">aucun intermédiaire<br>n'est perçu</span>
</div>
<div class="dp-rive">
<span class="dp-rive-nom">un corps</span>
<span class="dp-fleche"><em>&nbsp;</em><br>→ un mouvement</span>
<span class="dp-fleche"><em>&nbsp;</em><br>← un changement</span>
</div>
</div>
<p>Lisez-la dans les deux sens. Vers la droite, c'est la <strong>force</strong> : je veux lever le bras, le bras se lève. Vers la gauche, c'est la <strong>perception externe</strong> : le caillou est là, j'en ai une sensation. Ce sont les deux seules relations que nous ayons avec le monde, et ce sont les deux mêmes, retournées.</p>
<div class="dp-cite">
<p>Entre cette cause consciente et les phénomènes objectivement représentés du monde physique […] aucun intermédiaire n'est perçu, aucune hypothèse rationnelle ne s'offre, au delà du fait lui-même, et de notre idée de cause, et d'une liaison vérifiée, qui puisse nous faire comprendre cette liaison elle-même.</p>
<span class="dp-source">Étude, ch. L — Résumé des thèses principales</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Ce que le trou n'est pas</span>
<p>Ce n'est pas une ignorance provisoire que la science comblera. Renouvier ne dit pas : <em>on ne sait pas encore comment le vouloir meut le bras</em>. Il dit qu'aucune hypothèse ne peut être formée, parce qu'il n'y a rien à passer d'un côté à l'autre — et que les cinquante chapitres de l'Étude sont l'inventaire méthodique des tentatives ratées pour combler ce trou. L'impuissance n'est pas dans notre savoir : elle est dans la question.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="le résultat">
<summary class="dp-titre"><span class="dp-rang">l'inventaire</span><span class="dp-texte">rien ne passe</span></summary>
<div class="dp-corps">
<p>Dix-huit chapitres, dix-huit théories de la perception externe, dix-huit échecs. Renouvier les prend une par une, dans l'ordre historique, et il n'en sort aucune debout : le XVII<sup>e</sup> siècle, Locke, Condillac, Destutt de Tracy, Maine de Biran, Berkeley, Reid, Brown, Hamilton, Spencer, Bain, Stuart Mill, Taine, Kant, les Allemands — Herbart, Lotze, Wundt, Helmholtz — et pour finir William James.</p>
<p>La conclusion tombe au chapitre L, et elle est plus radicale qu'on ne l'attend :</p>
<div class="dp-cite">
<p>Une telle perception n'existe pas, mais seulement des idées que la présence de ces corps fait naître en nous, et qui sont des signes de cette présence et de leur extériorité, dont nous ne doutons pas.</p>
<span class="dp-source">Étude, ch. L</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">En clair</span>
<p>Vous ne percevez pas le caillou. Vous avez, à l'occasion du caillou, des <strong>signes</strong> — et vous ne doutez pas qu'il soit là, mais cette certitude ne vient d'aucune perception de lui. La dureté, la résistance, l'impénétrabilité : ce ne sont pas des propriétés du caillou qui vous parviendraient, ce sont vos manières de sentir.</p>
<p>Notez la précision, qui empêche le contresens : Renouvier ne dit pas que le corps n'existe pas. Il dit que son existence n'est pas ce que la perception nous donne. Nous n'en doutons pas — mais nous ne le percevons pas.</p>
</div>
<p>Et le même vide se retrouve du côté de la physique. La transmission du mouvement d'un corps à l'autre, qui semble le fait le plus évident du monde, ne résiste pas non plus :</p>
<div class="dp-cite">
<p>[…] ni l'idée de transmission, ni celle de transition n'expriment rien d'intelligible qui passe de la cause à l'effet, pour expliquer celui-ci ; ou de la force au mouvement […].</p>
<span class="dp-source">Étude, ch. L</span>
</div>
<p>Deux boules de billard se rencontrent, l'une s'arrête, l'autre part. Qu'est-ce qui a <em>passé</em> de la première à la seconde ? Rien qu'on puisse nommer. Nous avons une loi, très exacte, très prédictive — et pas l'ombre d'une explication.</p>
</div>
</details>

<details class="dp-pli" data-rang="le retournement">
<summary class="dp-titre"><span class="dp-rang">le pivot</span><span class="dp-texte">la force est la volonté</span></summary>
<div class="dp-corps">
<p>Voici le geste du livre. Si rien ne passe, d'où tenons-nous cette idée si assurée de <em>force</em> ? D'un seul endroit. Un seul.</p>
<div class="dp-cite">
<p>Le fondement unique et la source pour nous de cette idée de force qui s'entremêle entre des phénomènes dont le rapport de succession, comme d'antécédent à conséquent, est constant, est la volonté.</p>
<span class="dp-source">Étude, ch. L</span>
</div>
<p>Nous ne connaissons la force que du dedans, dans l'effort de vouloir. Partout ailleurs, nous ne constatons que des successions constantes. Et quand la physique dit qu'une boule en « pousse » une autre « avec force », elle emploie un mot qu'elle a pris chez nous sans le dire :</p>
<div class="dp-cite">
<p>[…] c'est par une illusion mentale seulement, que nous appliquons à leurs rapports […] les idées de force, impulsive ou résistante, avec une signification secrètement empruntée aux cas où les agents seraient supposés volontaires.</p>
<span class="dp-source">Étude, ch. XX — L'idée de force au point de vue scientifique</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">« Secrètement emprunté »</span>
<p>C'est l'expression décisive, et il faut mesurer ce qu'elle fait. La physique se croit débarrassée de l'anthropomorphisme ; elle l'a mis dans son vocabulaire de base. Chaque fois qu'un mécanicien écrit <em>F</em>, il parle en douce le langage du vouloir — car il n'y en a pas d'autre pour dire ce que ce signe désigne.</p>
<p>Deux issues, alors. Ou bien on avoue l'emprunt et l'on retire le mot : reste une pure succession constante, une loi sans force, et c'est ce que les physiciens ont fini par faire, « réduire [la force] à sa valeur nominale ». Ou bien on prend l'emprunt au sérieux, et l'on demande si les agents ne <em>seraient</em> pas volontaires. Renouvier choisit la seconde.</p>
</div>
<p>Il n'est pas seul à ce carrefour. Le chapitre XX s'ouvre sur William James, qui vient de « répudier l'hypothèse de l'entité-force, cause transitive, et fixer l'idée de force dans l'effort mental ». Le vieux Français de quatre-vingt-huit ans et l'Américain de soixante-et-un se rencontrent là, à la même date, sur la même intuition.</p>
</div>
</details>

<details class="dp-pli" data-rang="la conséquence">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">monades</span></summary>
<div class="dp-corps">
<p>Si la force est volonté, et si les corps sont faits de forces, alors les corps sont faits de volontés. Renouvier lâche le mot au dernier chapitre, entre deux tirets, comme on pose une évidence dont on sait qu'elle va coûter cher :</p>
<div class="dp-cite">
<p>Il faut donc, après avoir défini les forces de la nature par des agents mentaux, — on peut les appeler des <em>monades</em>, — définir l'efficacité externe de leurs actions, phénomènes internes, par un ordre général de la nature […].</p>
<span class="dp-source">Étude, ch. L</span>
</div>
<p>Et la marche qui y conduit est proprement logique. Elle passe par une définition de la substance qu'il faut lire lentement :</p>
<div class="dp-cite">
<p>Une substance, si nous voulons conserver ce nom, est une conscience, c'est-à-dire une relation encore, mais de soi à soi, de soi comme sujet à soi comme objet. Et cette relation fondamentale est la condition et le principe de toute autre relation possible représentée en une conscience sous forme objective externe.</p>
<span class="dp-source">Étude, ch. L</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le renversement complet, en une ligne</span>
<p><strong>« Une substance est une conscience. »</strong> En 1854, la substance était le premier des fétiches — un mot abstrait qu'on avait pris pour une chose. En 1903, le mot est rendu, mais son sens a été retourné comme un gant : ce qui subsiste sous les phénomènes n'est pas une matière, c'est un rapport de soi à soi. Le socle du monde n'est pas dessous : il est dedans, et c'est quelqu'un.</p>
<p>Reconnaissez la formule. « Personnalité : soi, non-soi, conscience » — la neuvième catégorie de 1854. Cinquante ans plus tard, elle a cessé d'être une loi de la représentation pour devenir la texture du réel.</p>
</div>
<p>Trois chapitres portent la doctrine : <strong>XLV</strong>, <em>Les monades et l'harmonie préétablie dans le monde physique</em> ; <strong>XLVI</strong>, <em>De la correction à apporter à la monadologie leibnitienne</em> ; <strong>XLVII</strong>, <em>La doctrine des monades et les idées générales de la physique moderne</em>. Une doctrine de 1714 confrontée à la thermodynamique et à la théorie cinétique des gaz.</p>
</div>
</details>

<details class="dp-pli" data-rang="la fin">
<summary class="dp-titre"><span class="dp-rang">le dernier mot</span><span class="dp-texte">c'est l'harmonie préétablie</span></summary>
<div class="dp-corps">
<p>Si les monades sont des consciences, et si rien ne passe d'une conscience à l'autre, comment le monde tient-il ensemble ? Comment ma volonté meut-elle mon bras, et mon bras la pierre ?</p>
<p>Il ne reste qu'une réponse possible, et c'est celle de Leibniz : les états des unes s'accordent avec les actes des autres, sans que rien ne circule. Voici les derniers mots de la dernière page du dernier livre :</p>
<div class="dp-cite">
<p>[…] définir l'efficacité externe de leurs actions, phénomènes internes, par un ordre général de la nature, partout semblable à celui dont nous vérifions la donnée générale dans les cas particuliers de nos désirs et de nos volontés, en rapport avec les déterminations de nos centres nerveux, les mouvements de nos viscères et de nos membres, phénomènes externes ; et c'est l'<em>harmonie préétablie</em>.</p>
<span class="dp-source">Étude, ch. L — dernière phrase de l'ouvrage</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Mesurez la chute</span>
<p>Un homme a écrit six mille pages contre la métaphysique. Il a démoli la chose en soi, la substance, l'absolu, l'infini, l'atome, l'entité-force ; il a traité de fétichisme toute philosophie qui prend un mot pour une chose ; il a corrigé Kant, réfuté Hegel, mis Comte au-dessous de Ptolémée. Il meurt en 1903. Le dernier mot qu'il ait fait imprimer est <em>harmonie préétablie</em>.</p>
<p>Ce n'est pas une conversion tardive. C'est ce qui reste sur la table quand on a tout enlevé. Renouvier n'a pas rejoint Leibniz : il est arrivé, en démolissant, au seul endroit où Leibniz avait campé.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="la correction">
<summary class="dp-titre"><span class="dp-rang">contre Leibniz</span><span class="dp-texte">variable indépendante</span></summary>
<div class="dp-corps">
<p>Renouvier prend les monades, mais il n'accepte pas le paquet. Le chapitre XLVI s'appelle <em>De la correction à apporter à la monadologie leibnitienne</em>, et il isole exactement deux pièces à retirer :</p>
<div class="dp-cite">
<p>Deux points de doctrine des plus considérables, qui peuvent sembler inhérents à la monadologie, parce qu'ils le sont au leibnitianisme, sont cependant tout à fait indépendants de la théorie […] des monades, et doivent en être séparés. L'une concerne la notion de l'activité, l'autre la notion de l'infini.</p>
<span class="dp-source">Étude, ch. XLVI</span>
</div>
<p>La première correction porte sur la liberté, et Renouvier en donne la formule la plus nette de toute son œuvre — une formule d'algébriste :</p>
<div class="dp-cite">
<p>Leibniz ne formule pas l'harmonie comme loi de causalité, simplement en ce sens que les actes et les états des êtres soient fonctions les uns des autres dans le cours des phénomènes. Il demande qu'il ne puisse entrer <em>aucune variable indépendante</em> dans les équations qui règlent les déterminations mutuelles.</p>
<span class="dp-source">Étude, ch. XLVI</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La liberté, définie en langage d'équation</span>
<p>Voilà ce qu'est la liberté chez Renouvier, dépouillée de toute éloquence : <strong>une variable indépendante dans les équations du monde.</strong> Chez Leibniz, il n'y en a aucune — la monade est un « automate incorporel », son développement est spontané mais entièrement prédéterminé par Dieu, et « rien ne peut entrer dans aucune ou sortir d'aucune ». L'accord est parfait parce que tout a été calculé d'avance.</p>
<p>Renouvier garde l'accord et y introduit une variable libre. Le monde reste harmonique ; il cesse d'être écrit.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Et la formule l'attendait depuis trente-neuf ans</span>
<p>On croirait la trouvaille d'un vieillard qui règle enfin son compte à Leibniz. Elle est de <strong>1864</strong>, dans le <em>Formulaire</em> qui résume le Deuxième Essai, et Renouvier ne l'a pas retouchée en trois éditions :</p>
<div class="dp-cite">
<p>En tant que la <em>Volonté</em> intervient dans les autres fonctions de la conscience (et que l'apparence est fidèle), ces fonctions ont des <em>variables indépendantes</em> réelles, et elles-mêmes ne <em>sont</em> pas simplement, mais <em>se font</em>.</p>
<span class="dp-source">Formulaire du Traité de Psychologie rationnelle, 1864 — inchangé en 1875 et 1892</span>
</div>
<p>Il n'a donc pas cherché sa réponse à Leibniz : il l'avait sous la main depuis quarante ans, et il la sort au moment exact où elle sert. « Elles ne <em>sont</em> pas simplement, mais <em>se font</em> » — la phrase de 1864 dit déjà tout ce que 1903 opposera à l'automate incorporel.</p>
</div>
<p>Et Renouvier remarque, ce qui est le trait de génie du chapitre, que les deux défauts n'en font qu'un : l'infinitisme de Leibniz est « bien lié d'ailleurs au plan de prédéterminisme absolu de l'harmonie préétablie, telle qu'il l'a définie ». L'infini et la nécessité tiennent ensemble. Retirez l'un, l'autre tombe.</p>
</div>
</details>

<details class="dp-pli" data-rang="cinquante ans après">
<summary class="dp-titre"><span class="dp-rang">le fil</span><span class="dp-texte">infini</span></summary>
<div class="dp-corps">
<p>Ouvrez le Premier Essai, 1854 : « l'infini et le nombre sont contradictoires entre eux ». Ouvrez le chapitre L du dernier livre, 1903 :</p>
<div class="dp-cite">
<p>Parmi les hypothèses qui ont le plus grand cours dans les doctrines philosophiques et dans les sciences physiques, celle qui définit les corps comme composés de parties infinies réelles d'une matière indéfiniment divisible — ou encore d'éléments eux-mêmes non corporels, mais en nombre infini — sont réfutables par le principe du tout et du nombre. Le tout actuel de parties sans fin est un concept contradictoire en soi.</p>
<span class="dp-source">Étude, ch. L</span>
</div>
<p><strong>Quarante-neuf ans, et pas une virgule de changée.</strong> C'est le même argument, servant au même office : interdire qu'une chose réelle soit composée d'une infinité de parties. En 1854 il abolissait la chose en soi ; en 1903 il abolit la matière continue — et il abolit aussi, du même coup, l'infinité des monades de Leibniz.</p>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Il n'a pourtant pas cessé d'y travailler</span>
<p>Une note du livre montre un homme de quatre-vingt-huit ans en train d'affiner l'outil de sa jeunesse. Il y concède que pour la <em>quantité géométrique</em> — le continu de l'espace et du temps — l'infini actuel ne se réfute pas directement par contradiction : le continu se divise « à l'infini », ce qui est justement, note-t-il, « le contraire d'être <em>en nombre infini</em> ». La démonstration directe ne vaut que « pour les choses, pour les phénomènes positifs et distincts ».</p>
<p>Un demi-siècle de polémique aura donc servi à cela : distinguer <em>aller à l'infini</em> (permis) et <em>être en nombre infini</em> (contradictoire). C'est une correction, et elle est de sa main.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Et il répond à ses adversaires vivants</span>
<p>Une autre note prend Leibniz sur le fait, en latin — <em>l'infini, à proprement parler, composé de parties, n'est ni un, ni un tout</em> —, et Renouvier ajoute : « C'est la même que nous retrouvons, pour le fond, chez les partisans actuels de cet infini. Elle lève, d'après eux, la contradiction impliquée par l'infini actuel ». Sa riposte tient en une ligne : « les notions de tout et de partie étant incontestablement corrélatives », un infini composé de parties qui ne serait pas un tout n'est pas une réponse, c'est un refus de la question.</p>
<p>Il ne nomme personne. Il n'en avait pas besoin : en 1903, tout le monde savait de qui il parlait — et ce site héberge les deux camps, Évellin pour le fini, Couturat pour l'infini.</p>
</div>
</div>
</details>

</div>
</details>

<p class="dp-epigraphe">— le livre —</p>

<details class="dp-pli" data-rang="essai">
<summary class="dp-titre"><span class="dp-rang">1903 · première moitié</span><span class="dp-texte">Le Personnalisme</span></summary>
<div class="dp-corps">
<p class="dp-chapo">Trois parties. Du sujet vers l'objet : la personne d'abord, le monde ensuite.</p>
<ul class="dp-liste">
<li><strong>Première partie — La métaphysique du personnalisme.</strong> Démontrer, « par des raisons, logiques d'abord, morales ensuite », que la personne est le fondement de toute connaissance ; puis en déduire ce qu'on peut savoir des objets.</li>
<li><strong>Deuxième partie — La sociologie du personnalisme.</strong> Ce que devient la société quand ses éléments sont des personnes et non des forces.</li>
<li><strong>Troisième partie — L'eschatologie du personnalisme.</strong> Les fins dernières : les destinées des personnes, la fin du monde.</li>
</ul>
<div class="dp-note">
<span class="dp-etiquette">L'ordre est le même que celui des Essais</span>
<p>Métaphysique, sociologie, eschatologie : la connaissance, la société, les fins. C'est, en trois parties et cinquante ans plus tard, le trajet des quatre <em>Essais de critique générale</em> — la logique, l'homme, la nature, l'histoire. Renouvier a passé sa vie à refaire le même parcours, chaque fois plus vite et plus bas.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="essai">
<summary class="dp-titre"><span class="dp-rang">1903 · seconde moitié</span><span class="dp-texte">Étude sur la perception externe et sur la force</span></summary>
<div class="dp-corps">
<p class="dp-chapo">Cinquante chapitres. De l'objet vers le sujet : le même trajet, à l'envers. Sept mouvements, et le dernier chapitre replie tout.</p>

<details class="dp-pli" data-rang="I-XVIII">
<summary class="dp-titre"><span class="dp-rang">le procès</span><span class="dp-texte">Deux siècles de théories de la perception, une par une</span></summary>
<div class="dp-corps">
<p>C'est la plus grande histoire critique de la perception externe écrite en français, et elle est enterrée dans l'appendice d'un livre que personne ne lit. Renouvier avait quatre-vingt-huit ans.</p>
<ul class="dp-liste">
<li><strong>I</strong> — La perception externe dans les doctrines du XVII<sup>e</sup> siècle.</li>
<li><strong>II-V</strong> — Locke et Condillac ; Destutt de Tracy ; <em>La volonté locomotrice de Maine de Biran</em>.</li>
<li><strong>VI-IX</strong> — Berkeley ; Reid ; Brown ; Reid, Brown et Hamilton.</li>
<li><strong>X-XIII</strong> — Hamilton et Herbert Spencer ; Alexandre Bain ; Stuart Mill ; H. Taine.</li>
<li><strong>XIV-XV</strong> — L'idéalisme kantien ; les théories génésiques en Allemagne : Herbart, Lotze, Wundt, Helmholtz.</li>
<li><strong>XVI</strong> — Point de vue physique et point de vue métaphysique de la perception externe.</li>
<li><strong>XVII-XVIII</strong> — Théorie de la spatialité de W. James ; théorie de la perception externe et de la volonté de W. James.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La forme du procès</span>
<p>Ce n'est pas une revue de littérature, c'est un réquisitoire, et il est monté comme tel. Chaque doctrine est prise à l'endroit où elle croit avoir comblé le trou, et c'est toujours là qu'elle casse. Il faut dix-huit chapitres non parce que les réponses sont nombreuses, mais parce qu'il faut les avoir <em>toutes</em> épuisées pour avoir le droit de dire, au chapitre L, qu'il n'y en a aucune.</p>
<p>Et l'ordre n'est pas neutre : le dernier examiné est James, le seul vivant, le seul qui ait mis la force dans l'effort mental. Le procès s'achève sur le seul allié.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="XIX-XXV">
<summary class="dp-titre"><span class="dp-rang">les mots</span><span class="dp-texte">Force, cause, mouvement, temps, continuité, masse</span></summary>
<div class="dp-corps">
<ul class="dp-liste">
<li><strong>XIX</strong> — Digression sur la liberté du vouloir.</li>
<li><strong>XX</strong> — L'idée de force au point de vue scientifique.</li>
<li><strong>XXI</strong> — L'idée de cause au point de vue scientifique.</li>
<li><strong>XXII</strong> — L'idée du mouvement. Relativité du mouvement.</li>
<li><strong>XXIII</strong> — L'idée du temps. La mesure du temps.</li>
<li><strong>XXIV</strong> — De la continuité par rapport aux forces naturelles.</li>
<li><strong>XXV</strong> — La loi de l'inertie et la communication du mouvement. L'idée de masse. L'expression mathématique de la force.</li>
</ul>
<div class="dp-note">
<span class="dp-etiquette">Une digression qui n'en est pas une</span>
<p>Le chapitre XIX s'intitule <em>Digression sur la liberté du vouloir</em>, et il tombe pile à la charnière : juste après le dernier chapitre sur la perception, juste avant le premier sur la force. Ce n'est pas une digression, c'est le pivot. Il fallait avoir établi que la volonté est libre avant de pouvoir dire que la force est la volonté — sans quoi les monades seraient les automates de Leibniz.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="XXVI-XLIV">
<summary class="dp-titre"><span class="dp-rang">les physiques</span><span class="dp-texte">Hirn, l'éther, l'énergie, Descartes, Kant, Boscovich, la gravitation</span></summary>
<div class="dp-corps">
<p>Dix-neuf chapitres, et c'est un cours de physique théorique de 1903 — vu par un philosophe de quatre-vingt-huit ans qui vérifie, un par un, si les mots des savants veulent dire quelque chose.</p>
<ul class="dp-liste">
<li><strong>XXVII-XXXI</strong> — Le système de l'entité force de A. Hirn ; le système du potentiel de R. Pictet ; la théorie physique de l'éther ; <em>doutes sur l'existence d'un milieu matériel interplanétaire</em> ; la force comme travail et comme chaleur.</li>
<li><strong>XXXII-XXXIV</strong> — Question des forces vives, théorie de l'énergie ; <em>accord des actions libres avec la constance de l'énergie</em> ; les origines de la thermodynamique.</li>
<li><strong>XXXV-XXXVI</strong> — La cosmogonie et la physique de Descartes, les tourbillons ; la matière et les forces dans la cosmogonie de Kant.</li>
<li><strong>XXXVII-XXXIX</strong> — Le système mathématique des forces de Boscovich ; sa théorie de la continuité ; ses thèses théologiques.</li>
<li><strong>XL-XLIV</strong> — Du sujet abstrait de la physique ; la gravitation et les actions à distance ; les forces naturelles et les états des corps ; la matière selon les cosmogonies physiques et la théorie cinétique des gaz ; l'application du principe de relativité aux notions physiques premières.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le chapitre XXXIII, qui est le plus courageux</span>
<p><em>Accord des actions libres avec la constance de l'énergie.</em> C'est l'objection qu'on lui oppose depuis toujours, et il l'affronte de face : si l'énergie se conserve, une volonté libre qui ferait quoi que ce soit dans le monde physique en créerait ou en détruirait. Toute la physique du XIX<sup>e</sup> siècle est contre lui, et il le sait, et il n'esquive pas.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Pourquoi Boscovich occupe trois chapitres</span>
<p>Parce que le jésuite dalmate avait fait, en 1758, exactement ce que Renouvier cherche : une physique sans matière, où les corps se réduisent à des points sans étendue et à des lois de force. C'est le précédent, et Renouvier l'examine jusque dans ses « thèses théologiques » — car une physique de points inétendus mène quelque part, et il veut savoir où.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="XLV-XLIX">
<summary class="dp-titre"><span class="dp-rang">l'issue</span><span class="dp-texte">Les monades, l'origine et les fins du monde</span></summary>
<div class="dp-corps">
<ul class="dp-liste">
<li><strong>XLV</strong> — Les monades et l'harmonie préétablie dans le monde physique.</li>
<li><strong>XLVI</strong> — De la correction à apporter à la monadologie leibnitienne.</li>
<li><strong>XLVII</strong> — La doctrine des monades et les idées générales de la physique moderne.</li>
<li><strong>XLVIII</strong> — De l'origine du monde au point de vue mécanique.</li>
<li><strong>XLIX</strong> — Des fins possibles du monde mécanique.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le titre du chapitre XLVII est un défi</span>
<p><em>La doctrine des monades et les idées générales de la physique moderne.</em> Une métaphysique de 1714 mise en face de la thermodynamique, de la théorie cinétique des gaz et du principe de relativité. Renouvier ne demande pas qu'on l'excuse : il soutient que la monadologie, corrigée, est la seule doctrine où les notions premières de la physique cessent d'être des mots.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="le pli de Renouvier">
<summary class="dp-titre"><span class="dp-rang">ch. L</span><span class="dp-texte">Résumé des thèses principales. Conclusion</span></summary>
<div class="dp-corps">
<p>Il l'a encore fait. Comme à la fin du Premier Essai, comme à la fin du Deuxième, le dernier chapitre replie le livre entier en propositions nues — sans preuves, sans exemples, sans polémique. Il ne l'appelle plus <em>Formulaire</em> ; c'en est un.</p>
<p>Vingt-cinq paragraphes, et voici les articulations dans l'ordre :</p>
<ul class="dp-liste">
<li>La volonté ne peut être ni définie ni expliquée ; elle peut seulement être <em>évoquée</em> chez ceux qui l'ont comme nous.</li>
<li>Entre elle et le mouvement, aucun intermédiaire n'est perçu.</li>
<li>La perception externe des corps « n'existe pas » : nous n'avons que des signes.</li>
<li>Les corps faits de parties infinies, ou d'éléments en nombre infini, sont réfutés par le principe du tout et du nombre.</li>
<li>Les qualités n'existent pas hors d'une conscience ; les réaliser au dehors est illogique.</li>
<li><strong>Une substance est une conscience</strong> — une relation de soi à soi.</li>
<li>Dans toute conscience entrent des perceptions, des appétitions, et des rapports de force.</li>
<li>Le fondement unique de l'idée de force est la volonté.</li>
<li>Ce que nous appelons <em>cause</em>, hors du vouloir, n'est qu'une condition nécessaire et suffisante — pas une force.</li>
<li>La transmission du mouvement n'exprime rien d'intelligible.</li>
<li>Donc : des agents mentaux, des monades, et l'harmonie préétablie.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Trois formulaires, trois époques, un seul geste</span>
<p>1875 : <em>Formulaire du Traité de logique générale</em>, à la fin du Premier Essai. 1875 : <em>Formulaire du Traité de Psychologie rationnelle</em>, à la fin du Deuxième, et repris en tête du Troisième en 1892. 1903 : <em>Résumé des thèses principales</em>, à la fin du dernier livre.</p>
<p>Renouvier a plié chacun de ses livres et rangé le pli à la sortie. Il l'a fait trois fois en trente ans, sans jamais le dire, et personne ne le lui a demandé. C'est un homme qui, à chaque fois qu'il achevait un ouvrage, en fabriquait le dépliant.</p>
</div>
<p class="dp-chapo">Si vous ne deviez lire qu'une page de ce livre de six cents, ce serait celle-là. Elle commence à la page 531.</p>
</div>
</details>
</div>
</details>

<p class="dp-epigraphe">— le fil, sur cinquante ans —</p>

<details class="dp-pli" data-rang="palier">
<summary class="dp-titre"><span class="dp-rang">1854 → 1903</span><span class="dp-texte">Ce que ce livre doit aux Essais, et ce qu'il leur fait</span></summary>
<div class="dp-corps">
<p>Cette page a une sœur, qui déplie les <em>Essais de critique générale</em>. On peut lire l'une sans l'autre, mais on perdrait la seule chose qui compte : ce livre-ci est l'aboutissement d'une déduction commencée un demi-siècle plus tôt, et il ne s'en cache pas une seconde.</p>
<div class="dp-cadre">
<table class="dp-miroir dp-double">
<thead><tr><th>Ce qui est posé</th><th class="dp-tete-non">Dans les Essais</th><th class="dp-tete-oui">Dans le dernier livre</th></tr></thead>
<tbody>
<tr><td>Le pivot</td><td class="dp-non">1854 — « l'infini et le nombre sont contradictoires entre eux »</td><td class="dp-oui">1903 — « le tout actuel de parties sans fin est un concept contradictoire en soi »</td></tr>
<tr><td>La substance</td><td class="dp-non">1854 — un fétiche : un mot pris pour une chose</td><td class="dp-oui">1903 — « une substance est une conscience »</td></tr>
<tr><td>La personnalité</td><td class="dp-non">1854 — la neuvième catégorie : soi, non-soi, conscience</td><td class="dp-oui">1903 — la texture du monde physique : les monades</td></tr>
<tr><td>La force</td><td class="dp-non">1854 — la septième catégorie : acte, puissance, force</td><td class="dp-oui">1903 — la volonté, et rien d'autre</td></tr>
<tr><td>La liberté</td><td class="dp-non">1875 — « c'est à la liberté qu'il appartient de déclarer si la liberté est ou non »</td><td class="dp-oui">1903 — une variable indépendante dans les équations</td></tr>
<tr><td>Le pli</td><td class="dp-non">1875 — <em>Formulaire du Traité de logique générale</em></td><td class="dp-oui">1903 — <em>Résumé des thèses principales</em></td></tr>
</tbody>
</table>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Ce que la colonne de droite fait à celle de gauche</span>
<p>On lit d'ordinaire les <em>Essais</em> comme une critique : un inventaire de ce qu'on ne peut pas savoir. La colonne de droite montre à quoi servait l'inventaire. Les neuf catégories de 1854 étaient données comme des lois de la <em>représentation</em> — des formes de notre connaissance, pas des propriétés des choses. En 1903, la neuvième est devenue ce dont le monde est fait.</p>
<p>Autrement dit, le criticisme a fini en métaphysique. Non par fatigue, ni par une faiblesse de vieillard : parce que après avoir démontré que rien ne passe entre une conscience et un corps, il ne restait qu'une façon de tenir le monde ensemble — que le corps aussi soit une conscience. Renouvier n'a pas abandonné sa critique. Il l'a suivie jusqu'au bout, et elle l'a mené là.</p>
</div>
<p class="dp-chapo">Un homme qui aurait voulu se contredire aurait mis cinquante ans à s'en apercevoir. Celui-là a mis cinquante ans à arriver.</p>
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

Cette page suit les mêmes six règles que sa sœur, [Compliquer les Essais pour les expliquer](essais.md) : le pli conserve tout ; les sœurs restent visibles ; la profondeur se compte aux filets ; le parcours se souvient ; la typographie dit qui parle — sérif pour Renouvier, linéale pour le commentaire ; et les paliers sont de l'auteur quand ils existent.

Ici, ils existent. Le chapitre L, *Résumé des thèses principales*, est le troisième formulaire de Renouvier, et l'essentiel de cette page en vient.

**Deux réserves d'établissement du texte.** La numérisation a perdu le titre d'un chapitre entre le III (Destutt de Tracy) et le VI (Berkeley) : le seul titre subsistant dans cet intervalle est *La volonté locomotrice de Maine de Biran*, dont le numéro manque. Les regroupements « II-V » et « XXVI-XLIV » proposés ci-dessus sont donc des commodités de lecture, pas des divisions de l'auteur : Renouvier n'a pas donné de titres de parties à son Étude, seulement cinquante chapitres à la file.

**Ce qui reste à faire.** *Le Personnalisme* proprement dit — métaphysique, sociologie, eschatologie — n'est ici qu'esquissé : cette page déplie l'Étude, c'est-à-dire la moitié du volume que son titre présente comme un appendice. Le reste attend son étage.

**Source.** Charles Renouvier, *Le Personnalisme, suivi d'une étude sur la perception externe et sur la force*, Paris, Félix Alcan, 1903. Numérisation Gallica / Bibliothèque nationale de France. Renouvier meurt le 1<sup>er</sup> septembre de la même année.
