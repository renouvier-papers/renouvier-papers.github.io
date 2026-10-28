---
title: "La physique du personnalisme"
description: "Le Personnalisme, suivi d'une étude sur la perception externe et sur la force (1903), déplié."
---

# La physique du personnalisme

En 1854, un homme de trente-neuf ans entreprend de démolir la métaphysique. Il passera un demi-siècle à récuser la chose en soi, la substance, l'infini et l'absolu, autant de fétiches, de mots pris pour des dieux.

En 1903, l'année de sa mort, il publie à quatre-vingt-huit ans le dernier livre paru de son vivant, qui s'achève sur les mots *et c'est l'harmonie préétablie*.

Cette page déplie ce dernier livre, qui n'est pas un reniement mais l'aboutissement d'un chemin dont la page Comment je suis arrivé à cette conclusion montre le tournant, en 1886. Fermé, le dépliant tient en un titre ; chaque terme s'ouvre sur ce qu'il contient, qui s'ouvre à son tour. **Ouvrir un pli ne fait rien disparaître** : les voies écartées demeurent, repliées, à côté de celle que l'on suit.

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
#dp .dp-renvoi { margin: .95rem 0 0; font-size: .8rem; color: var(--dp-muted); }
#dp .dp-renvoi a { color: var(--dp-accent); }
</style>
<div class="dp-outils">
<button class="dp-bouton" type="button" data-dp="tout">Tout déplier</button>
<button class="dp-bouton" type="button" data-dp="rien">Tout replier</button>
<button class="dp-bouton" type="button" data-dp="neufs">Aller au premier pli non ouvert</button>
<span class="dp-compteur" id="dp-compteur" aria-live="polite"></span>
</div>

<p class="dp-chapo">Charles Renouvier, <em>Le Personnalisme, suivi d'une étude sur la perception externe et sur la force</em>, Paris, Félix Alcan, 1903, l'année de sa mort.</p>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">Le Personnalisme</span></summary>
<div class="dp-corps">
<p>Le mot vient à la fin, sur la couverture du dernier livre, mais la chose figurait dès 1854 dans une liste de neuf. La neuvième catégorie de la <em>Logique générale</em> s'appelait <em>personnalité</em> (soi, non-soi, conscience). Il aura fallu quarante-neuf ans pour que le titre rattrape la trouvaille.</p>
<div class="dp-cite">
<p>[…] la connaissance de la personne en tant que conscience et volonté est le fondement de toutes les connaissances humaines.</p>
<span class="dp-source">Le Personnalisme, préface</span>
</div>
<div class="dp-note">
<span class="dp-etiquette">Trois parties, la troisième inattendue</span>
<p>Le Personnalisme proprement dit comprend trois parties, la <strong>métaphysique</strong>, la <strong>sociologie</strong> et l'<strong>eschatologie</strong>, doctrines de la connaissance, de la société et des fins dernières. Dans le même livre, le même homme fonde la connaissance sur la personne et se demande ce que deviennent les personnes après la fin du monde.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">suivi d'une étude</span></summary>
<div class="dp-corps">
<p>Le mot trompe. « Suivi de » fait attendre un appendice, un supplément, une pièce jointe ; or cette étude compte <strong>cinquante chapitres</strong>, plus que le livre qu'elle est censée suivre. Renouvier prévient dès sa première phrase :</p>
<div class="dp-cite">
<p>Les deux questions réunies par le titre de cet ouvrage en composent réellement une seule, avec ses principales dépendances.</p>
<span class="dp-source">Le Personnalisme, préface, première phrase</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Les deux sens d'une seule relation</span>
<p>Le <em>Personnalisme</em>, qui « déduit » ce qu'on peut connaître des choses à partir du rapport du sujet à l'objet mental, part de la personne et descend vers les objets. L'<em>Étude</em> « prend la question de la connaissance <strong>sous l'aspect inverse</strong>, en considérant les objets externes comme donnés par eux-mêmes ».</p>
<p>À l'aller répond un retour. Plutôt qu'un livre et son annexe, le volume présente une relation parcourue dans les deux sens.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Le rapport des deux moitiés selon Renouvier</span>
<p>On serait tenté de déclarer les deux moitiés indissociables, mais ce serait excéder le texte. Selon la préface, l'Étude « a pour objet l'éclaircissement de ce problème <strong>en rapport avec la doctrine personnaliste</strong> » ; la doctrine vient donc <em>avant</em>, et l'Étude l'éclaire. La même préface date en outre le personnalisme de 1854, soit bien avant la théorie de la force que développe l'Étude.</p>
<p>Le rapport juste est la <strong>convergence par l'autre bout</strong>, non la dépendance. Tandis que le personnalisme est établi par la logique, puis par la morale, l'Étude part de l'extrémité opposée (les corps, la thermodynamique, l'éther) et aboutit à des personnes, ce qui confirme la doctrine sans la fonder. Deux routes dissemblables mènent à un seul point d'arrivée.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">sur la perception externe et sur la force</span></summary>
<div class="dp-corps">
<p>Le titre nomme deux sujets, le livre un seul, et là réside l'essentiel. Ce sont les deux sens d'un même trajet entre une conscience et un corps.</p>
<ul class="dp-liste">
<li><strong>La perception externe</strong> — comment se peut-il que les changements d'un objet, « qui sont autre chose que ces sensations », soient <em>suivis</em> de sensations en moi ? <em>(le corps vers moi)</em></li>
<li><strong>La force</strong> — comment se fait-il que « des désirs et des actes de volonté, phénomènes internes d'une conscience, soient régulièrement suivis de certains changements de l'objet externe » ? <em>(moi vers le corps)</em></li>
</ul>
<p>Renouvier pose la seconde question dans la préface, sans détour :</p>
<div class="dp-cite">
<p>Qu'est-ce que ce mécanisme ? La question de la <em>force</em>, ou de la <em>nature de la force</em>, se pose à cet endroit.</p>
<span class="dp-source">Le Personnalisme, préface</span>
</div>
<p>Cinquante chapitres plus loin, la réponse tiendra en un mot de Leibniz.</p>
</div>
</details>

<p class="dp-epigraphe">— le livre en une phrase —</p>
<p class="dp-these">Entre ma volonté et mon bras qui se lève, rien ne passe, pas plus qu'entre le caillou et la sensation que j'en ai. Cinquante chapitres établissent ce vide, et, pour finir, une seule doctrine peut s'en accommoder, celle qui compose le monde physique d'êtres conscients à tous les degrés, de monades.</p>

<details class="dp-pli" data-rang="palier">
<summary class="dp-titre"><span class="dp-rang">↓ déplier</span><span class="dp-texte">Le livre en un paragraphe</span></summary>
<div class="dp-corps">
<p>Renouvier pose <strong>deux questions qui n'en font qu'une</strong>, en demandant comment un corps produit ma sensation, et ma volonté un mouvement. Il consacre dix-huit chapitres à examiner toutes les réponses données depuis Descartes (Locke, Condillac, Maine de Biran, Berkeley, Reid, Hamilton, Bain, Mill, Taine, Kant, James), puis vingt-cinq autres à toutes les physiques (l'inertie, la masse, l'énergie, la thermodynamique, l'éther, la gravitation). Partout, il constate que <strong>rien ne passe</strong>, aucun intermédiaire n'étant perçu ni aucune transmission intelligible. Il retourne alors le problème. Le vouloir étant le seul endroit au monde où nous connaissions une force par le dedans, <strong>la force est la volonté</strong>, et le mot qu'emploie la physique lui doit une signification « secrètement empruntée ». Les forces de la nature sont donc des volontés, et les éléments du monde physique des agents mentaux, dont il écrit qu'« on peut les appeler des <strong>monades</strong> ». Or des monades ne peuvent se toucher, puisque rien ne passe. Il faut dès lors que leurs états s'accordent sans agir les uns sur les autres, et <strong>c'est l'harmonie préétablie</strong>. Cette harmonie est celle de Leibniz, à deux corrections près, qui sont les deux thèses de toute une vie, le refus de l'<strong>infini</strong> et l'affirmation d'une <strong>variable indépendante</strong> dans les équations du monde.</p>
<p class="dp-chapo">Chacun des sept termes en gras s'ouvre ci-dessous. Ce paragraphe dit l'essentiel ; on peut s'en tenir là ou tirer sur un fil.</p>

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
<p>La figure se lit dans les deux sens. Vers la droite va la <strong>force</strong> (je veux lever le bras, le bras se lève) ; vers la gauche, la <strong>perception externe</strong> (le caillou est là, j'en ai une sensation). Ce sont nos deux seules relations avec le monde, et toutes deux n'en font qu'une, retournée.</p>
<div class="dp-cite">
<p>Entre cette cause consciente et les phénomènes objectivement représentés du monde physique […] aucun intermédiaire n'est perçu, aucune hypothèse rationnelle ne s'offre, au delà du fait lui-même, et de notre idée de cause, et d'une liaison vérifiée, qui puisse nous faire comprendre cette liaison elle-même.</p>
<span class="dp-source">Étude, ch. L — Résumé des thèses principales</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La nature du trou</span>
<p>Renouvier n'écrit pas <em>on ne sait pas encore comment le vouloir meut le bras</em>, formule qui ferait du trou une ignorance provisoire que la science comblerait. Il affirme qu'aucun intermédiaire n'est perçu et qu'aucune hypothèse rationnelle ne s'offre pour faire comprendre cette liaison, et une bonne part de l'Étude passe en revue les tentatives faites en ce sens. L'impuissance tient donc à la nature de la question.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="le résultat">
<summary class="dp-titre"><span class="dp-rang">l'inventaire</span><span class="dp-texte">rien ne passe</span></summary>
<div class="dp-corps">
<p>En dix-huit chapitres, Renouvier examine une à une les théories de la perception externe, par écoles plutôt que chronologiquement, et presque aucune ne résiste à l'épreuve. Le parcours mène du XVII<sup>e</sup> siècle à William James, en passant par Locke, Condillac, Destutt de Tracy, Maine de Biran, Berkeley, Reid, Brown, Hamilton, Spencer, Bain, Stuart Mill, Taine, Kant et les Allemands (Herbart, Lotze, Wundt, Helmholtz).</p>
<p>La conclusion, formulée au chapitre L, est plus radicale qu'on ne l'attend :</p>
<div class="dp-cite">
<p>Une telle perception n'existe pas, mais seulement des idées que la présence de ces corps fait naître en nous, et qui sont des signes de cette présence et de leur extériorité, dont nous ne doutons pas.</p>
<span class="dp-source">Étude, ch. L</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le sens de la conclusion</span>
<p>Le caillou n'est pas perçu. À son occasion, nous avons des <strong>signes</strong>, et si nous ne doutons pas qu'il soit là, cette certitude ne vient d'aucune perception de lui. La dureté, la résistance, l'impénétrabilité sont nos manières de sentir, et non des propriétés du caillou qui nous parviendraient.</p>
<p>Une précision du texte écarte le contresens. Renouvier ne nie pas que le corps existe ; il dit que son existence n'est pas ce que la perception nous donne. Nous n'en doutons pas, sans pour autant le percevoir.</p>
</div>
<p>Le même vide se retrouve du côté de la physique, où la transmission du mouvement d'un corps à l'autre, fait en apparence le plus évident du monde, ne résiste pas davantage :</p>
<div class="dp-cite">
<p>[…] ni l'idée de transmission, ni celle de transition n'expriment rien d'intelligible qui passe de la cause à l'effet, pour expliquer celui-ci ; ou de la force au mouvement […].</p>
<span class="dp-source">Étude, ch. L</span>
</div>
<p>Deux boules de billard se rencontrent ; l'une s'arrête, l'autre part. De la première à la seconde, rien n'a <em>passé</em> que l'on puisse nommer. Nous disposons d'une loi très exacte, très prédictive, sans l'ombre d'une explication.</p>
</div>
</details>

<details class="dp-pli" data-rang="le retournement">
<summary class="dp-titre"><span class="dp-rang">le pivot</span><span class="dp-texte">la force est la volonté</span></summary>
<div class="dp-corps">
<p>Ici s'accomplit le geste du livre. Si rien ne passe, cette idée si assurée de <em>force</em> nous vient d'un seul endroit.</p>
<div class="dp-cite">
<p>Le fondement unique et la source pour nous de cette idée de force qui s'entremêle entre des phénomènes dont le rapport de succession, comme d'antécédent à conséquent, est constant, est la volonté.</p>
<span class="dp-source">Étude, ch. L</span>
</div>
<p>Nous ne connaissons la force que du dedans, dans l'effort de vouloir ; partout ailleurs, nous constatons seulement des successions constantes. Lorsque la physique dit qu'une boule en « pousse » une autre « avec force », elle emploie un mot qu'elle a pris chez nous sans le dire :</p>
<div class="dp-cite">
<p>[…] c'est par une illusion mentale seulement, que nous appliquons à leurs rapports […] les idées de force, impulsive ou résistante, avec une signification secrètement empruntée aux cas où les agents seraient supposés volontaires.</p>
<span class="dp-source">Étude, ch. XX — L'idée de force au point de vue scientifique</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">« Secrètement empruntée »</span>
<p>L'expression est déterminante. La physique se croit débarrassée de l'anthropomorphisme, alors qu'elle l'a logé dans son vocabulaire de base. Tant que le mécanicien entend par <em>F</em> autre chose qu'un terme de sa loi, il parle à son insu le langage du vouloir.</p>
<p>Deux issues s'offrent alors. L'une consiste à avouer l'emprunt et à retirer le mot, ce qui ne laisse qu'une pure succession constante, une loi sans force ; les physiciens ont fini par s'y résoudre et par « réduire [la force] à sa valeur nominale ». L'autre revient à prendre l'emprunt au sérieux et à demander si les agents ne <em>seraient</em> pas volontaires. Renouvier choisit la seconde.</p>
</div>
<p>Il n'est pas seul à ce carrefour, puisque le chapitre XX s'ouvre sur William James, dont on a vu la théorie « répudier l'hypothèse de l'entité-force, cause transitive, et fixer l'idée de force dans l'effort mental ». Le Français et l'Américain, son cadet de vingt-sept ans, se rencontrent sur la même intuition.</p>
</div>
</details>

<details class="dp-pli" data-rang="la conséquence">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">monades</span></summary>
<div class="dp-corps">
<p>Si la force est volonté et si les corps sont faits de forces, les corps sont faits de volontés. Renouvier, qui a déjà placé le mot dans les titres des chapitres XLV à XLVII (et, dans la première partie du volume, au chapitre XI), le reprend au dernier chapitre, entre deux tirets :</p>
<div class="dp-cite">
<p>Il faut donc, après avoir défini les forces de la nature par des agents mentaux, — on peut les appeler des <em>monades</em>, — définir l'efficacité externe de leurs actions, phénomènes internes, par un ordre général de la nature […].</p>
<span class="dp-source">Étude, ch. L</span>
</div>
<p>La marche qui y conduit est proprement logique et passe par une définition de la substance qui demande à être lue lentement :</p>
<div class="dp-cite">
<p>Une substance, si nous voulons conserver ce nom, est une conscience, c'est-à-dire une relation encore, mais de soi à soi, de soi comme sujet à soi comme objet. Et cette relation fondamentale est la condition et le principe de toute autre relation possible représentée en une conscience sous forme objective externe.</p>
<span class="dp-source">Étude, ch. L</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le renversement complet, en une ligne</span>
<p><strong>« Une substance est une conscience. »</strong> En 1854, la substance était le premier des fétiches, un mot abstrait pris pour une chose ; en 1903, le mot est rendu, mais son sens a été retourné comme un gant, puisque ce qui subsiste sous les phénomènes est un rapport de soi à soi, et non une matière. Le socle du monde se trouve ainsi au-dedans plutôt qu'au-dessous, et c'est quelqu'un.</p>
<p>On y reconnaît la formule « Personnalité : soi, non-soi, conscience », la neuvième catégorie de 1854. Cinquante ans plus tard, elle a cessé d'être une loi de la représentation pour devenir la texture du réel.</p>
</div>
<p>Trois chapitres portent la doctrine, <strong>XLV</strong> (<em>Les monades et l'harmonie préétablie dans le monde physique</em>), <strong>XLVI</strong> (<em>De la correction à apporter à la monadologie leibnitienne</em>) et <strong>XLVII</strong> (<em>La doctrine des monades et les idées générales de la physique moderne</em>). Une métaphysique de 1714 y est confrontée à la thermodynamique et à la théorie cinétique des gaz.</p>
</div>
</details>

<details class="dp-pli" data-rang="la fin">
<summary class="dp-titre"><span class="dp-rang">le dernier mot</span><span class="dp-texte">c'est l'harmonie préétablie</span></summary>
<div class="dp-corps">
<p>Si les monades sont des consciences et si rien ne passe d'une conscience à l'autre, il faut comprendre comment le monde tient ensemble, comment ma volonté meut mon bras, et mon bras la pierre.</p>
<p>Il ne reste qu'une réponse possible, celle de Leibniz, selon laquelle les états des unes s'accordent avec les actes des autres, sans que rien ne circule. Le dernier livre s'achève, à sa dernière page, sur ces mots :</p>
<div class="dp-cite">
<p>[…] définir l'efficacité externe de leurs actions, phénomènes internes, par un ordre général de la nature, partout semblable à celui dont nous vérifions la donnée générale dans les cas particuliers de nos désirs et de nos volontés, en rapport avec les déterminations de nos centres nerveux, les mouvements de nos viscères et de nos membres, phénomènes externes ; et c'est l'<em>harmonie préétablie</em>.</p>
<span class="dp-source">Étude, ch. L — dernière phrase de l'ouvrage</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La portée de la chute</span>
<p>Renouvier a écrit des milliers de pages contre la métaphysique. Il a démoli la chose en soi, la substance, l'absolu, l'infini et l'entité-force, traité de fétichisme toute philosophie qui prend un mot pour une chose, corrigé Kant, réfuté Hegel et mis Comte au-dessous de Ptolémée. Quand il meurt, en 1903, le dernier mot qu'il ait fait imprimer est <em>harmonie préétablie</em>.</p>
<p>L'harmonie préétablie est ce qui reste sur la table quand on a tout enlevé. Loin de s'être converti sur le tard à Leibniz, Renouvier est arrivé, en démolissant, au seul endroit où celui-ci avait campé.</p>
</div>
</div>
<p class="dp-renvoi">L'enchaînement complet (la force est volonté, rien ne passe, donc des monades, donc une harmonie) est mis en notation, avec le statut logique de chaque pas, sur <a href="/recherche/logique-philosophique/systeme-en-formules/">Le système en formules</a>.</p>
</details>

<details class="dp-pli" data-rang="la correction">
<summary class="dp-titre"><span class="dp-rang">contre Leibniz</span><span class="dp-texte">variable indépendante</span></summary>
<div class="dp-corps">
<p>Renouvier adopte les monades sans accepter la doctrine en bloc. Le chapitre XLVI, intitulé <em>De la correction à apporter à la monadologie leibnitienne</em>, isole exactement deux pièces à retirer :</p>
<div class="dp-cite">
<p>Deux points de doctrine des plus considérables, qui peuvent sembler inhérents à la monadologie, parce qu'ils le sont au leibnitianisme, sont cependant tout à fait indépendants de la théorie […] des monades, et doivent en être séparés. L'une concerne la notion de l'activité, l'autre la notion de l'infini.</p>
<span class="dp-source">Étude, ch. XLVI, p. 497</span>
</div>
<p>La première correction porte sur la liberté. Renouvier procède par contraste et en algébriste, énonçant « en termes mathématiques rigoureux » ce que Leibniz exige et que lui-même refuse :</p>
<div class="dp-cite">
<p>Leibniz ne formule pas l'harmonie comme loi de causalité, simplement en ce sens que les actes et les états des êtres soient fonctions les uns [des] autres dans le cours des phénomènes. Il demande qu'il ne puisse entrer <em>aucune variable indépendante</em> dans les équations qui règlent les déterminations mutuelles.</p>
<span class="dp-source">Étude, ch. XLVI, p. 497 — « [des] » : la transcription porte « les », coquille de numérisation</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La liberté, définie en langage d'équation</span>
<p>Dépouillée de toute éloquence, la liberté est chez Renouvier <strong>une variable indépendante dans les équations du monde.</strong> Leibniz n'en admet aucune, car la monade est un « automate incorporel » dont le développement, quoique spontané, est entièrement prédéterminé par Dieu, et les monades « n'ont point de fenêtres, par lesquelles quelque chose y puisse entrer ou sortir » (Leibniz, Monadologie, § 7). L'accord est parfait parce que tout a été calculé d'avance.</p>
<p>Renouvier garde l'accord et y introduit une variable libre. Le monde reste harmonique ; il cesse d'être écrit.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Une formule vieille de trente-neuf ans</span>
<p>La formule semble la trouvaille tardive d'un homme qui en finit avec Leibniz. Elle figure pourtant dès <strong>1864</strong> dans le <em>Formulaire</em> qui résume le Deuxième Essai, et Renouvier ne l'a pas retouchée en trois éditions :</p>
<div class="dp-cite">
<p>En tant que la <em>Volonté</em> intervient dans les autres fonctions de la conscience (et que l'apparence est fidèle), ces fonctions ont des <em>variables indépendantes</em> réelles, et elles-mêmes ne <em>sont</em> pas simplement, mais <em>se font</em>.</p>
<span class="dp-source">Formulaire du Traité de Psychologie rationnelle, 1864 ; même texte en 1875 (Deuxième Essai, t. III, p. 292) et en 1892 (Troisième Essai, t. I, p. XXVI)</span>
</div>
<p>Il avait donc sous la main, depuis trente-neuf ans, sa réponse à Leibniz, et il la produit au moment exact où elle sert. La phrase de 1864, « Elles ne <em>sont</em> pas simplement, mais <em>se font</em> », contient tout ce que le livre de 1903 oppose à l'automate incorporel.</p>
</div>
<p>Renouvier remarque aussi que les deux défauts se tiennent, l'infinitisme de Leibniz étant « bien lié d'ailleurs au plan de prédéterminisme absolu de l'harmonie préétablie, telle qu'il l'a définie ». L'infini et la nécessité vont ensemble chez Leibniz ; Renouvier rejette l'un et l'autre.</p>
</div>
</details>

<details class="dp-pli" data-rang="cinquante ans après">
<summary class="dp-titre"><span class="dp-rang">le fil</span><span class="dp-texte">infini</span></summary>
<div class="dp-corps">
<p>Le Formulaire du Premier Essai (rédigé en 1859, cité dans l'état de 1875) énonce que « l'infini et le nombre sont contradictoires entre eux ». On lit au chapitre L du dernier livre (1903) :</p>
<div class="dp-cite">
<p>Parmi les hypothèses qui ont le plus grand cours dans les doctrines philosophiques et dans les sciences physiques, celle qui définit les corps comme composés de parties infinies réelles d'une matière indéfiniment divisible — ou encore d'éléments eux-mêmes non corporels, mais en nombre infini — sont réfutables par le principe du tout et du nombre. Le tout actuel de parties sans fin est un concept contradictoire en soi.</p>
<span class="dp-source">Étude, ch. L</span>
</div>
<p><strong>Quarante-neuf ans, et le même argument</strong>. Sous deux formules différentes, il sert au même office, qui est d'interdire qu'une chose réelle soit composée d'une infinité de parties. En 1854, il abolissait la chose en soi ; en 1903, il abolit la matière continue et, du même coup, l'infinité des monades de Leibniz.</p>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Un argument encore retravaillé</span>
<p>Une note du livre montre un homme de quatre-vingt-huit ans occupé à affiner l'outil de sa jeunesse. Il y concède que, pour la <em>quantité géométrique</em> (le continu de l'espace et du temps), l'infini actuel ne se réfute pas directement par contradiction, puisque le continu se divise « à l'infini », ce qui est, remarque-t-il, « le contraire d'être <em>en nombre infini</em> ». La démonstration directe ne vaut que « pour les choses, pour les phénomènes positifs et distincts ».</p>
<p>La distinction entre <em>aller à l'infini</em> (l'indéfini, permis) et <em>être en nombre infini</em> (contradictoire) est aussi vieille que le Premier Essai. L'aveu que la démonstration directe ne vaut pas pour le continu géométrique est en revanche nouveau, et cette précision est de sa main.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">La réponse aux adversaires vivants</span>
<p>Une autre note prend Leibniz sur le fait, quand il écrit en latin que <em>l'infini, à proprement parler, composé de parties, n'est ni un, ni un tout</em>. « C'est la même que nous retrouvons, pour le fond, chez les partisans actuels de cet infini. Elle lève, d'après eux, la contradiction impliquée par l'infini actuel », ajoute Renouvier. Sa riposte, qui tient en une ligne, est que, « les notions de tout et de partie étant incontestablement corrélatives », un infini composé de parties qui ne serait pas un tout revient à refuser la question au lieu d'y répondre.</p>
<p>Il ne nomme personne, mais ses lecteurs pouvaient mettre des noms ; ce site héberge d'ailleurs les deux camps, Évellin pour le fini, Couturat pour l'infini.</p>
</div>
</div>
</details>

</div>
</details>

<p class="dp-epigraphe">— le livre —</p>

<details class="dp-pli" data-rang="essai">
<summary class="dp-titre"><span class="dp-rang">1903 · première moitié</span><span class="dp-texte">Le Personnalisme</span></summary>
<div class="dp-corps">
<p class="dp-chapo">Trois parties vont du sujet vers l'objet, la personne d'abord, le monde ensuite.</p>
<ul class="dp-liste">
<li><strong>Première partie — La métaphysique du personnalisme.</strong> Démontrer, « par des raisons, logiques d'abord, morales ensuite », que la personne est le fondement de toute connaissance ; puis en déduire ce qu'on peut savoir des objets.</li>
<li><strong>Deuxième partie — La sociologie du personnalisme.</strong> Ce que devient la société quand ses éléments sont des personnes et non des forces.</li>
<li><strong>Troisième partie — L'eschatologie du personnalisme.</strong> Les fins dernières (destinées des personnes, fin du monde).</li>
</ul>
<div class="dp-note">
<span class="dp-etiquette">Le même ordre que dans les Essais</span>
<p>Métaphysique, sociologie et eschatologie traitent de la connaissance, de la société et des fins. On y reconnaît, en raccourci, le trajet des <em>Essais de critique générale</em>, de la connaissance à l'histoire.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="essai">
<summary class="dp-titre"><span class="dp-rang">1903 · seconde moitié</span><span class="dp-texte">Étude sur la perception externe et sur la force</span></summary>
<div class="dp-corps">
<p class="dp-chapo">Cinquante chapitres parcourent le même trajet à l'envers, de l'objet vers le sujet, en quatre mouvements, et le dernier chapitre replie tout.</p>

<details class="dp-pli" data-rang="I-XVIII">
<summary class="dp-titre"><span class="dp-rang">le procès</span><span class="dp-texte">Deux siècles de théories de la perception, une par une</span></summary>
<div class="dp-corps">
<p>Ces chapitres forment l'une des plus amples histoires critiques de la perception externe écrites en français, restée dans l'ombre d'un titre qui la présente comme une suite. Renouvier avait alors quatre-vingt-huit ans.</p>
<ul class="dp-liste">
<li><strong>I</strong> — La perception externe dans les doctrines du XVII<sup>e</sup> siècle.</li>
<li><strong>II-V</strong> — Locke et Condillac ; Destutt de Tracy ; Maine de Biran : la perception externe, puis <em>la volonté locomotrice</em>.</li>
<li><strong>VI-IX</strong> — Berkeley ; Reid ; Brown ; Reid, Brown et Hamilton.</li>
<li><strong>X-XIII</strong> — Hamilton et Herbert Spencer ; Alexandre Bain ; Stuart Mill ; H. Taine.</li>
<li><strong>XIV-XV</strong> — L'idéalisme kantien ; les théories génésiques en Allemagne : Herbart, Lotze, Wundt, Helmholtz.</li>
<li><strong>XVI</strong> — Point de vue physique et point de vue métaphysique de la perception externe.</li>
<li><strong>XVII-XVIII</strong> — Théorie de la spatialité de W. James ; théorie de la perception externe et de la volonté de W. James.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La forme du procès</span>
<p>L'ensemble est un réquisitoire, monté comme tel, et non une revue de littérature. Chaque doctrine y est saisie à l'endroit où elle croit avoir comblé le trou, et c'est toujours là qu'elle cède. Dix-huit chapitres sont nécessaires, non que les réponses soient nombreuses, mais parce qu'il faut les avoir <em>toutes</em> épuisées pour être en droit de dire, au chapitre L, qu'il n'y en a aucune.</p>
<p>L'ordre a lui-même un sens. Le dernier examiné est James, qui met la force dans l'effort mental, comme l'avait fait avant lui Maine de Biran, et le procès s'achève ainsi sur un allié.</p>
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
<span class="dp-etiquette">Une digression à la charnière</span>
<p>Intitulé <em>Digression sur la liberté du vouloir</em>, le chapitre XIX se place exactement à la charnière, entre le dernier chapitre sur la perception et le premier sur la force. Le mot de digression trompe sur ce qui est en réalité le pivot. Il fallait avoir posé la liberté du vouloir avant de pouvoir dire que la force est la volonté, sans quoi les monades seraient les automates de Leibniz.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="XXVI-XLIV">
<summary class="dp-titre"><span class="dp-rang">les physiques</span><span class="dp-texte">Hirn, l'éther, l'énergie, Descartes, Kant, Boscovich, la gravitation</span></summary>
<div class="dp-corps">
<p>Dix-neuf chapitres composent une revue critique de la physique, de Descartes et Boscovich à la thermodynamique, menée par un philosophe de quatre-vingt-huit ans qui vérifie, un par un, si les mots des savants veulent dire quelque chose.</p>
<ul class="dp-liste">
<li><strong>XXVI</strong> — chapitre dont la numérisation n'a pas conservé le titre.</li>
<li><strong>XXVII-XXXI</strong> — Le système de l'entité force de A. Hirn ; le système du potentiel de R. Pictet ; la théorie physique de l'éther ; <em>doutes sur l'existence d'un milieu matériel interplanétaire</em> ; la force comme travail et comme chaleur.</li>
<li><strong>XXXII-XXXIV</strong> — Question des forces vives, théorie de l'énergie ; <em>accord des actions libres avec la constance de l'énergie</em> ; les origines de la thermodynamique.</li>
<li><strong>XXXV-XXXVI</strong> — La cosmogonie et la physique de Descartes, les tourbillons ; la matière et les forces dans la cosmogonie de Kant.</li>
<li><strong>XXXVII-XXXIX</strong> — Le système mathématique des forces de Boscovich ; sa théorie de la continuité ; ses thèses théologiques.</li>
<li><strong>XL-XLIV</strong> — Du sujet abstrait de la physique ; la gravitation et les actions à distance ; les forces naturelles et les états des corps ; la matière selon les cosmogonies physiques et la théorie cinétique des gaz ; l'application du principe de relativité aux notions physiques premières.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le chapitre XXXIII et la constance de l'énergie</span>
<p><em>Accord des actions libres avec la constance de l'énergie.</em> Si l'énergie se conserve, une volonté libre qui ferait quoi que ce soit dans le monde physique semble devoir en créer ou en détruire. Renouvier affronte de face cette objection classique, et sa réponse est double. La loi n'est démontrée que pour un système fermé, « sans qu'aucune force nouvelle s'introduise du dehors », et l'invoquer contre le libre arbitre est un cercle, qu'il reproche aux philosophes déterministes, non aux physiciens. La volonté, d'autre part, n'a pas à créer d'énergie, car elle peut n'être que la « cause occasionnelle » d'un passage du potentiel au cinétique (un déclic, une « rupture d'équilibre ») qui laisse la somme intacte.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Pourquoi Boscovich occupe trois chapitres</span>
<p>Le jésuite dalmate avait fait, en 1758, exactement ce que Renouvier cherche, une physique sans matière, où les corps se réduisent à des points sans étendue et à des lois de force. Renouvier examine ce précédent jusque dans ses « thèses théologiques », car une physique de points inétendus mène quelque part, et il veut savoir où.</p>
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
<span class="dp-etiquette">Le défi du chapitre XLVII</span>
<p><em>La doctrine des monades et les idées générales de la physique moderne.</em> Une métaphysique de 1714 y est mise en face de la thermodynamique et de la théorie cinétique des gaz. Sans demander qu'on l'excuse, Renouvier soutient que la monadologie, corrigée, est la seule doctrine où les notions premières de la physique cessent d'être des mots.</p>
</div>
</div>
<div class="dp-note">
<span class="dp-etiquette">Le chaînon de 1899, désigné par l'auteur lui-même</span>
<p>Entre l'<em>Esquisse</em> (1886) et ce livre-ci (1903), la préface du <em>Personnalisme</em> nomme elle-même deux étapes, dont un livre entier :</p>
<div class="dp-cite">
<p>La théorie cosmogonique et eschatologique du personnalisme, abordée dans les <em>Essais de critique générale</em>, <em>Troisième Essai</em> (2<sup>e</sup> édit.) et exposée dans la <em>Nouvelle monadologie</em> est reprise à fond dans l'ouvrage que nous publions aujourd'hui.</p>
<span class="dp-source">Le Personnalisme, préface</span>
</div>
<p>« Exposée » en 1899, la théorie est « reprise à fond » en 1903, si bien que la généalogie est signée. Ce dossier s'en tient au dernier des trois ouvrages que la préface relie.</p>
</div>
</details>

<details class="dp-pli" data-rang="le pli de Renouvier">
<summary class="dp-titre"><span class="dp-rang">ch. L</span><span class="dp-texte">Résumé des thèses principales. Conclusion</span></summary>
<div class="dp-corps">
<p>Le geste se répète. Comme à la fin du Premier Essai et à celle du Deuxième, le dernier chapitre replie l'Étude entière en propositions nues, sans preuves, sans exemples, sans polémique. Renouvier ne le nomme plus <em>Formulaire</em>, mais c'en est un.</p>
<p>Le chapitre tient en quatre pages (p. 531-534) et douze paragraphes, dont les articulations se succèdent ainsi :</p>
<ul class="dp-liste">
<li>La volonté ne peut être ni définie ni expliquée ; elle peut seulement être <em>évoquée</em> chez ceux qui l'ont comme nous.</li>
<li>Entre elle et le mouvement, aucun intermédiaire n'est perçu.</li>
<li>La perception externe des corps « n'existe pas », et nous n'avons que des signes.</li>
<li>Les corps faits de parties infinies, ou d'éléments en nombre infini, sont réfutés par le principe du tout et du nombre.</li>
<li>Les qualités n'existent pas hors d'une conscience ; les réaliser au dehors est illogique.</li>
<li><strong>Une substance est une conscience</strong>, relation de soi à soi.</li>
<li>Dans toute conscience entrent des perceptions, des appétitions et des rapports de force.</li>
<li>Le fondement unique de l'idée de force est la volonté.</li>
<li>Ce que nous appelons <em>cause</em>, hors du vouloir, n'est qu'une condition nécessaire et suffisante, non une force.</li>
<li>La transmission du mouvement n'exprime rien d'intelligible.</li>
<li>D'où des agents mentaux, des monades et l'harmonie préétablie.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Trois formulaires, trois époques, un seul geste</span>
<p>Publié en 1859 avec le Deuxième Essai, le <em>Formulaire du Traité de logique générale</em> est placé en 1875 à la fin du Premier. Le <em>Formulaire du Traité de Psychologie rationnelle</em>, paru en 1864 en tête du Troisième, passe en 1875 à la fin du Deuxième et revient en 1892 en tête du Troisième. En 1903, le <em>Résumé des thèses principales</em> clôt le dernier livre.</p>
<p>Renouvier a plié trois de ses livres de 1859 à 1903 et rangé le pli à la sortie ; il en a fait état dans la Note finale du Deuxième Essai, qui raconte le déplacement du premier Formulaire. Au terme de ses grands ouvrages, il en fabriquait volontiers le dépliant.</p>
</div>
<p class="dp-chapo">S'il ne fallait lire qu'un chapitre de ce livre de plus de cinq cents pages, ce serait celui-là, qui commence à la page 531.</p>
</div>
</details>
</div>
</details>

<p class="dp-epigraphe">— le fil, sur cinquante ans —</p>

<details class="dp-pli" data-rang="palier">
<summary class="dp-titre"><span class="dp-rang">1854 → 1903</span><span class="dp-texte">Ce que ce livre doit aux Essais, et ce qu'il leur fait</span></summary>
<div class="dp-corps">
<p>Cette page a une sœur, qui déplie les <em>Essais de critique générale</em>. On peut lire l'une sans l'autre, mais on perdrait la seule chose qui compte, à savoir que ce livre-ci est l'aboutissement d'une déduction commencée un demi-siècle plus tôt, ce qu'il revendique dès sa préface.</p>
<div class="dp-cadre">
<table class="dp-miroir dp-double">
<thead><tr><th>Ce qui est posé</th><th class="dp-tete-non">Dans les Essais</th><th class="dp-tete-oui">Dans le dernier livre</th></tr></thead>
<tbody>
<tr><td>Le pivot</td><td class="dp-non">1859 (Formulaire) — « l'infini et le nombre sont contradictoires entre eux »</td><td class="dp-oui">1903 — « le tout actuel de parties sans fin est un concept contradictoire en soi »</td></tr>
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
<p>On lit d'ordinaire les <em>Essais</em> comme une critique, inventaire de ce qu'on ne peut pas savoir. La colonne de droite montre à quoi servait cet inventaire. Les neuf catégories de 1854 étaient données comme des lois de la <em>représentation</em>, formes de notre connaissance et non propriétés des choses ; en 1903, la neuvième est devenue ce dont le monde est fait.</p>
<p>Le criticisme a ainsi fini en métaphysique, non par fatigue ni par faiblesse de vieillard, mais parce que, une fois établi qu'aucun intermédiaire n'est perçu ni intelligible entre une conscience et un corps, il ne restait, pour tenir le monde ensemble, qu'à admettre que le corps, lui aussi, est fait d'êtres conscients. Fidèle à sa critique, Renouvier l'a suivie jusqu'au bout, et elle l'a mené là.</p>
</div>
<p class="dp-chapo">Il a mis cinquante ans à arriver, sans quitter sa méthode.</p>
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

Cette page suit les mêmes six règles que sa sœur, [Compliquer les Essais pour les expliquer](essais.md), selon lesquelles le pli conserve tout, les sœurs restent visibles, la profondeur se compte aux filets, le parcours se souvient, la typographie dit qui parle (sérif pour Renouvier, linéale pour le commentaire), et les paliers sont de l'auteur quand ils existent.

Ici, ils existent. Le chapitre L, *Résumé des thèses principales*, est le troisième formulaire de Renouvier, et l'essentiel de cette page en procède.

**Deux réserves d'établissement du texte.** La numérisation a perdu le titre du chapitre XXVI, et le XXV y est directement suivi du XXVII. Les regroupements « II-V » et « XXVI-XLIV » proposés ci-dessus sont des commodités de lecture et non des divisions de l'auteur, car Renouvier n'a donné à son Étude aucun titre de partie, seulement cinquante chapitres à la file.

**Ce qui reste à déplier.** *Le Personnalisme* proprement dit (métaphysique, sociologie, eschatologie) n'est ici qu'esquissé, cette page dépliant l'Étude, c'est-à-dire la moitié du volume que son titre présente comme une suite.

**Source.** Charles Renouvier, *Le Personnalisme, suivi d'une étude sur la perception externe et sur la force*, Paris, Félix Alcan, 1903. Numérisation Gallica / Bibliothèque nationale de France. Renouvier meurt le 1<sup>er</sup> septembre de la même année.
