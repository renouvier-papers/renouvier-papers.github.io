---
title: "Étiquetage morpho-syntaxique"
description: "La grammaire de Renouvier comptée à découvert — pronoms, négations, connecteurs, temps — et ce qu'elle date."
---

# Étiquetage morpho-syntaxique

Étiqueter un texte, c'est écrire sous chaque mot sa nature — pronom, préposition, verbe à l'imparfait. Les étiqueteuses automatiques le font par apprentissage statistique, au prix d'une part d'erreur invérifiable. Cette page fait le choix inverse : **n'étiqueter que ce qui est sûr, et publier chaque règle.** Classes grammaticales fermées (on peut lister *tous* les déterminants du français), désinences verbales sans ambiguïté, dictionnaires de décision établis mot par mot. Couverture : 59 % des mots du corpus ; le reste est laissé sans étiquette plutôt qu'étiqueté au risque d'erreur.

Le corpus est celui de la page [Lexicométrie](/recherche/linguistique/lexicometrie/) : les **Essais** de 1875, l'**Esquisse** de 1885-1886, **Le Personnalisme** de 1903, et le tome révisé de 1892 en point de contrôle. Mais on ne compte plus ici les mots pleins — on compte la grammaire : les pronoms, les négations, les connecteurs, les temps. C'est la couche de la langue qu'un auteur ne surveille pas. Elle a beaucoup à dire. **Rien ne disparaît quand vous ouvrez.**

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

<details class="dp-pli" data-rang="protocole">
<summary class="dp-titre"><span class="dp-rang">la règle du jeu</span><span class="dp-texte">Étiqueter à découvert</span></summary>
<div class="dp-corps">
<p>Trois familles d'étiquettes, trois degrés de certitude — et rien d'autre.</p>
<p><strong>Les classes fermées.</strong> Déterminants, pronoms, prépositions, conjonctions, négations, formes conjuguées d'<em>être</em> et d'<em>avoir</em> : ces listes sont finies et connues en entier. Un mot y figure ou n'y figure pas ; l'étiquette est sûre. Elles couvrent à elles seules plus de la moitié de tout texte français.</p>
<p><strong>Les désinences sans ambiguïté.</strong> Une forme en <em>-erait</em> est un conditionnel ; une forme en <em>-aient</em> hors conditionnel est un imparfait ; une forme en <em>-èrent</em> est un passé simple — <em>sauf exceptions, toutes listées</em>. Car le français tend des pièges : <em>fait</em>, <em>sait</em> et <em>parfait</em> ne sont pas des imparfaits ; <em>diffèrent</em> et <em>considèrent</em> sont des présents, non des passés simples ; <em>vrai</em> n'est pas un futur, et <em>considérons</em> non plus ; <em>considérait</em> (imparfait de <em>considérer</em>) se distingue de <em>considérerait</em> (conditionnel) par un seul <em>e</em>. Chaque piège rencontré dans le corpus a été tranché individuellement, et la liste des décisions est publiée au dernier pli.</p>
<p><strong>Les adverbes en <em>-ment</em>.</strong> <em>Nécessairement</em> est un adverbe, <em>mouvement</em> est un nom, <em>forment</em> est un verbe : aucune règle mécanique ne les départage tous. Les terminaisons sûres (<em>-quement</em>, <em>-ellement</em>, <em>-amment</em>…) sont traitées par règle ; le reste, mot par mot. Résidu non classé : 910 occurrences sur plus d'un million — moins d'un mot sur mille.</p>
<table class="dp-tab">
<thead><tr><th>strate</th><th>mots étiquetés</th></tr></thead>
<tbody>
<tr><td>1875</td><td>59,1 %</td></tr>
<tr><td>1885-1886</td><td>59,3 %</td></tr>
<tr><td>1903</td><td>58,3 %</td></tr>
<tr><td class="dp-t92"><em>1892</em></td><td class="dp-t92">58,4 %</td></tr>
</tbody>
</table>
<p>Les 41 % restants — l'essentiel des noms, adjectifs et verbes au présent — demeurent volontairement sans étiquette. On perd en couverture ce qu'on gagne en certitude : chaque chiffre des plis suivants est vérifiable à la main.</p>
</div>
</details>

<details class="dp-pli" data-rang="voix">
<summary class="dp-titre"><span class="dp-rang">le paradoxe</span><span class="dp-texte">Le « je » s'efface dans <em>Le Personnalisme</em></span></summary>
<div class="dp-corps">
<p>Fréquences pour 10 000 mots des pronoms personnels — la mesure la plus simple de l'appareil, et le résultat le plus étonnant de toute l'étude :</p>
<table class="dp-tab">
<thead><tr><th>pronom</th><th>1875</th><th>1886</th><th>1903</th><th>1892</th></tr></thead>
<tbody>
<tr><td><strong>je, j'</strong></td><td><strong>53,6</strong></td><td><strong>27,2</strong></td><td><strong>5,4</strong></td><td class="dp-t92">19,7</td></tr>
<tr><td>me, m', moi</td><td>21,2</td><td>10,7</td><td>4,9</td><td class="dp-t92">7,1</td></tr>
<tr><td>nous</td><td>66,4</td><td>47,0</td><td>65,8</td><td class="dp-t92">52,0</td></tr>
<tr><td>on</td><td>71,7</td><td>65,2</td><td>44,1</td><td class="dp-t92">72,2</td></tr>
<tr><td>il, ils</td><td>127,8</td><td>136,3</td><td>117,9</td><td class="dp-t92">109,5</td></tr>
</tbody>
</table>
<p>D'un livre à l'autre, le <em>je</em> est divisé par dix. L'auteur des <em>Essais</em> parle en son nom à chaque page — il expose, il maintient, il répond :</p>
<div class="dp-cite">
<p>Il est vrai que je ne comprends la loi de finalité que sous condition d'une conscience posée, apte à poursuivre un but.</p>
<span class="dp-source">Deuxième Essai, t. III, p. 247</span>
</div>
<p>L'auteur du <em>Personnalisme</em> a quasiment cessé de dire <em>je</em>. Sa phrase type est impersonnelle, à sujet abstrait :</p>
<div class="dp-cite">
<p>La justice subjective comporte donc une limitation mutuelle des actes des agents moraux.</p>
<span class="dp-source">Le Personnalisme, p. 36</span>
</div>
<p>Voilà le paradoxe : la doctrine prend le nom de la <em>personne</em> au moment précis où la première personne quitte la prose. Il se dissout si l'on distingue deux choses que le mot <em>personnel</em> confond : la thèse et le ton. La thèse — toute vérité est affirmée par quelqu'un — n'a jamais été aussi ferme ; le ton n'a plus besoin de la porter, car elle est portée par le système entier. Le <em>je</em> des <em>Essais</em> était un instrument de combat ; le combat gagné, l'instrument se range. Reste le <em>nous</em> de méthode, imperturbable d'un bout à l'autre (66,4 → 47,0 → 65,8) : l'auteur et son lecteur marchant ensemble — ce pronom-là était constitutif, il demeure.</p>
</div>
</details>

<details class="dp-pli" data-rang="négation">
<summary class="dp-titre"><span class="dp-rang">l'archaïsme tenu</span><span class="dp-texte">Point ou pas</span></summary>
<div class="dp-corps">
<p>Le français du XIXᵉ siècle a deux négations pleines : <em>ne… pas</em>, la moderne, et <em>ne… point</em>, l'ancienne, déjà littéraire. Part de <em>point</em> parmi les deux, et densité totale de la négation :</p>
<table class="dp-tab">
<thead><tr><th>strate</th><th>ne… pas</th><th>ne… point</th><th>part de <em>point</em></th><th><em>ne</em> pour 10 000 mots</th></tr></thead>
<tbody>
<tr><td>1875</td><td>2 613</td><td>554</td><td><strong>17,5 %</strong></td><td>163</td></tr>
<tr><td>1885-1886</td><td>2 288</td><td>329</td><td>12,6 %</td><td>135</td></tr>
<tr><td>1903</td><td>951</td><td>143</td><td>13,1 %</td><td>135</td></tr>
<tr><td class="dp-t92"><em>1892</em></td><td class="dp-t92">499</td><td class="dp-t92">86</td><td class="dp-t92">14,7 %</td><td class="dp-t92">138</td></tr>
</tbody>
</table>
<p>Deux faits. D'abord, <em>point</em> recule après les <em>Essais</em> mais ne meurt pas : il se stabilise autour d'une négation sur huit, jusqu'au bout — l'élégance d'époque est tenue, pas abandonnée. En 1903 encore :</p>
<div class="dp-cite">
<p>Elle n'est pas positivement logique, et c'est pour cette raison qu'on ne voit point le devoir figurer dans les tables de catégories.</p>
<span class="dp-source">Le Personnalisme, p. 47</span>
</div>
<p>— où l'on notera que les deux négations cohabitent dans la même phrase, <em>pas</em> pour le constat, <em>point</em> pour la pointe. Ensuite, la densité globale : les <em>Essais</em> nient davantage (163 <em>ne</em> pour 10 000 mots contre 135 ensuite). Un traité polémique se construit contre — contre Hume, contre Hegel, contre l'infini actuel ; la prose tardive expose plus qu'elle ne réfute, et sa grammaire le sait.</p>
</div>
</details>

<details class="dp-pli" data-rang="démonstration">
<summary class="dp-titre"><span class="dp-rang">l'armature</span><span class="dp-texte">L'appareil démonstratif décline</span></summary>
<div class="dp-corps">
<p>Les connecteurs sont l'armature visible du raisonnement. Presque tous baissent — et le détail est instructif (pour 10 000 mots) :</p>
<table class="dp-tab">
<thead><tr><th>connecteur</th><th>1875</th><th>1886</th><th>1903</th><th>1892</th></tr></thead>
<tbody>
<tr><td><strong>donc</strong></td><td><strong>15,7</strong></td><td>10,4</td><td><strong>8,4</strong></td><td class="dp-t92">11,6</td></tr>
<tr><td>si</td><td>36,4</td><td>27,2</td><td>24,9</td><td class="dp-t92">29,2</td></tr>
<tr><td>mais</td><td>46,8</td><td>42,2</td><td>37,2</td><td class="dp-t92">42,8</td></tr>
<tr><td>ainsi</td><td>16,7</td><td>16,3</td><td>11,9</td><td class="dp-t92">14,0</td></tr>
<tr><td>en effet</td><td>6,2</td><td>4,0</td><td>3,7</td><td class="dp-t92">6,9</td></tr>
<tr><td>lorsque</td><td>3,6</td><td>1,8</td><td>0,9</td><td class="dp-t92">3,6</td></tr>
<tr><td>au contraire</td><td>3,3</td><td>2,3</td><td>1,9</td><td class="dp-t92">2,4</td></tr>
<tr><td>pourtant</td><td>2,8</td><td>1,7</td><td>1,3</td><td class="dp-t92">1,9</td></tr>
<tr><td>car</td><td>8,5</td><td>7,5</td><td>8,6</td><td class="dp-t92">7,2</td></tr>
<tr><td>cependant</td><td>3,5</td><td>3,3</td><td>4,6</td><td class="dp-t92">3,1</td></tr>
<tr><td>parce que</td><td>3,2</td><td>3,0</td><td>4,3</td><td class="dp-t92">1,1</td></tr>
</tbody>
</table>
<p><em>Donc</em> presque divisé par deux, <em>si</em> et <em>ainsi</em> en net repli, <em>lorsque</em> divisé par quatre : la machine à inférer tourne moins vite. Mais <em>car</em> tient, et <em>cependant</em> comme <em>parce que</em> montent — les liens de justification et de concession survivent au déclin des liens de déduction. On passe d'une prose qui <em>démontre</em> à une prose qui <em>explique</em>.</p>
<p>La ponctuation raconte la même histoire : 20,8 points d'interrogation pour 10 000 mots dans les <em>Essais</em>, 9,6 dans l'<em>Esquisse</em>, 6,8 dans <em>Le Personnalisme</em> — divisés par trois. Le traité de 1875 pense par questions, en salves :</p>
<div class="dp-cite">
<p>Mais qu'est-ce qu'une probabilité morale ? Qu'est-ce qu'un motif de croire ? Qu'est-ce que croire ?</p>
<span class="dp-source">Deuxième Essai, t. II, p. 90</span>
</div>
<p>Trois questions en douze mots, chacune creusant sous la précédente — c'est la respiration même du criticisme militant. La prose de 1903 a rangé ce soufflet : elle pose, elle déroule, elle conclut sans interpeller.</p>
</div>
</details>

<details class="dp-pli" data-rang="temps">
<summary class="dp-titre"><span class="dp-rang">les modes</span><span class="dp-texte">Le traité conjecture, l'histoire raconte</span></summary>
<div class="dp-corps">
<p>Quatre paradigmes verbaux identifiables par leur seule terminaison, une fois les pièges écartés (pour 10 000 mots) :</p>
<table class="dp-tab">
<thead><tr><th>strate</th><th>imparfait</th><th>conditionnel</th><th>futur</th><th>passé simple</th></tr></thead>
<tbody>
<tr><td>1875</td><td>29,3</td><td><strong>50,5</strong></td><td><strong>24,7</strong></td><td>1,9</td></tr>
<tr><td>1885-1886</td><td>48,8</td><td>38,6</td><td>14,8</td><td>3,8</td></tr>
<tr><td>1903</td><td><strong>54,0</strong></td><td>44,5</td><td>9,2</td><td>4,5</td></tr>
<tr><td class="dp-t92"><em>1892</em></td><td class="dp-t92">39,8</td><td class="dp-t92">48,4</td><td class="dp-t92">19,6</td><td class="dp-t92">0,6</td></tr>
</tbody>
</table>
<p>Chaque livre a son mode dominant, et c'est son portrait. Les <em>Essais</em> sont le règne du <strong>conditionnel</strong> : un traité critique pèse des hypothèses, envisage ce qui s'ensuivrait, écarte ce qu'on ne saurait conclure —</p>
<div class="dp-cite">
<p>La réciproque simple <em>eq</em> = <em>e</em> (non <em>m</em>) n'est pas généralement vraie, et de ce qu'une espèce de <em>m</em> est espèce de l'autre que <em>q</em>, on ne saurait conclure qu'une espèce de <em>q</em> soit espèce de l'autre que <em>m</em>.</p>
<span class="dp-source">Premier Essai, t. II, p. 18</span>
</div>
<p>L'<em>Esquisse</em> fait basculer la prose dans l'<strong>imparfait</strong>, le temps de l'historien des doctrines — ce que tel penseur <em>admettait</em>, ce qu'il <em>démontrait</em> :</p>
<div class="dp-cite">
<p>Il démontrait que la pluralité est impossible, à l'aide toujours du grand axiome éléatique de la <em>non existence du non être</em>.</p>
<span class="dp-source">Esquisse, t. I, p. 41</span>
</div>
<p>Et <em>Le Personnalisme</em>, livre-bilan, reste dans l'imparfait — celui, désormais, de sa propre histoire. Le <strong>futur</strong>, lui, s'éteint (divisé par 2,7). C'est qu'il était pour une bonne part le futur d'architecte, celui qui annonce la suite du traité :</p>
<div class="dp-cite">
<p>Puis des considérations accessoires la corroborent, notamment celle qui se tire des faits dits de hasard et de la loi des grands nombres, comme nous le verrons tout à l'heure.</p>
<span class="dp-source">Deuxième Essai, t. II, p. 90</span>
</div>
<p>Moins d'annonces, c'est moins d'échafaudage : le dernier livre n'a plus de chantier à promettre. Quant au <strong>passé simple</strong>, il est marginal partout — deux à quatre formes pour 10 000 mots, presque zéro dans le tome de contrôle : Renouvier ne narre pas, même quand il fait de l'histoire ; il tient les doctrines au bout de son imparfait, à distance constante du présent où il juge.</p>
</div>
</details>

<details class="dp-pli" data-rang="datation">
<summary class="dp-titre"><span class="dp-rang">le clou</span><span class="dp-texte">La grammaire date les textes : le test de 1892</span></summary>
<div class="dp-corps">
<p>Dernière expérience, la plus forte. La stylométrie sait depuis longtemps que les mots-outils — <em>de</em>, <em>que</em>, <em>mais</em>, <em>ne</em>, <em>donc</em>… — forment une signature involontaire, stable chez un auteur mais sensible à ses époques. On a donc découpé chaque strate en segments de 20 000 mots, mesuré la fréquence des 120 mots-outils les plus courants dans chaque segment, et calculé la distance moyenne entre segments (Delta de Burrows) :</p>
<table class="dp-tab">
<thead><tr><th>comparaison</th><th>distance</th></tr></thead>
<tbody>
<tr><td>à l'intérieur d'une même strate</td><td>0,94 – 1,12</td></tr>
<tr><td>1875 ↔ 1885-1886</td><td>1,164</td></tr>
<tr><td>1885-1886 ↔ 1903</td><td><strong>1,074</strong></td></tr>
<tr><td>1875 ↔ 1903</td><td><strong>1,279</strong></td></tr>
</tbody>
</table>
<p>Les distances entre époques dépassent les distances internes — les trois états de langue sont réels, pas un artefact de sujets différents, puisque les mots-outils ignorent les sujets. Et elles s'ordonnent comme le calendrier : 1875 et 1903 sont les plus éloignés, 1886 et 1903 les plus proches. La grammaire profonde de Renouvier a dérivé continûment pendant trente ans.</p>
<p>D'où le test. Le tome de contrôle porte la date de 1892, mais c'est la révision d'un texte écrit sous l'Empire, vers 1864 — un composé de deux mains du même homme à trente ans d'écart. Si la signature grammaticale date vraiment les textes, elle doit voir sous la date de couverture. On a demandé à chacun de ses quatre segments de quelle strate il est le plus proche :</p>
<table class="dp-tab">
<thead><tr><th>segment</th><th>dist. 1875</th><th>dist. 1886</th><th>dist. 1903</th><th>verdict</th></tr></thead>
<tbody>
<tr><td>1892 — 1ᵉʳ</td><td><strong>0,826</strong></td><td>0,889</td><td>0,902</td><td><strong>1875</strong></td></tr>
<tr><td>1892 — 2ᵉ</td><td><strong>0,638</strong></td><td>0,894</td><td>0,925</td><td><strong>1875</strong></td></tr>
<tr><td>1892 — 3ᵉ</td><td><strong>0,909</strong></td><td>1,018</td><td>1,040</td><td><strong>1875</strong></td></tr>
<tr><td>1892 — 4ᵉ</td><td>0,797</td><td><strong>0,728</strong></td><td>0,742</td><td><strong>1886</strong></td></tr>
</tbody>
</table>
<p>Trois segments sur quatre votent 1875 : la syntaxe du tome révisé est restée celle de l'époque des <em>Essais</em> — la main de 1892 a changé des thèses, elle n'a pas récrit la grammaire de 1864. Le dernier segment penche vers la langue tardive : une inflexion que la statistique constate sans pouvoir, seule, l'assigner à telle ou telle couche de la révision — c'est ici que le comptage passe le relais à la philologie.</p>
<p class="dp-renvoi">Laquelle a déjà fait sa part : la page <a href="/recherche/complications/evolution/">Comment je suis arrivé à cette conclusion</a> compare mot à mot les états successifs du même texte — les repentirs que la grammaire vient de détecter à l'aveugle, elle les montre au grand jour.</p>
</div>
</details>

<details class="dp-pli" data-rang="méthode">
<summary class="dp-titre"><span class="dp-rang">les décisions</span><span class="dp-texte">Note de méthode, pièges et dictionnaires</span></summary>
<div class="dp-corps">
<p><strong>Corpus et préparation</strong> : identiques à la page <a href="/recherche/linguistique/lexicometrie/">Lexicométrie</a> (strates closes, césures recollées, élisions détachées, inversions <em>est-il</em> dénouées — sans quoi les pronoms inversés échapperaient au comptage).</p>
<p><strong>Classes fermées retenues.</strong> Déterminants (articles, démonstratifs, possessifs, indéfinis) ; pronoms personnels, dont les formes sujets seules servent au pli sur la voix ; prépositions ; conjonctions de coordination et de subordination ; adverbes de négation ; formes conjuguées d'<em>être</em> et d'<em>avoir</em> ; une liste d'adverbes de haute fréquence (<em>ainsi</em>, <em>aussi</em>, <em>encore</em>, <em>toujours</em>…).</p>
<p><strong>Ambiguïtés assumées.</strong> <em>Il</em> inclut l'impersonnel (<em>il faut</em>) : la chute du <em>je</em> n'en dépend pas. <em>Que</em> n'est pas ventilé entre relatif, conjonction et adverbe : on ne l'interprète jamais seul. <em>En</em>, <em>le</em>, <em>leur</em> cumulent leurs emplois : ils ne portent aucune conclusion de cette page. La segmentation en phrases protège les abréviations courantes ; ses erreurs résiduelles pèsent également sur les quatre strates, donc pas sur leurs écarts.</p>
<p><strong>Dictionnaires de décision (extraits).</strong> Écartés de l'imparfait : <em>fait, ait, sait, aient, parfait, satisfait, imparfait, bienfait, souhait, trait, attrait, extrait, portrait, abstrait, soustrait, retrait, distrait</em>. Écartés du passé simple (présents en <em>-èrent</em> et voisins) : <em>diffèrent, demeurent, tirent, figurent, suggèrent, opèrent, concourent, altèrent, meurent, attirent, acquièrent, mesurent, considèrent, préfèrent, espèrent</em>. Écartés du futur : <em>vrai, barbara</em> (le mode syllogistique !), et les présents en <em>-rons</em> des verbes en <em>-rer</em> (<em>considérons, ignorons, comparons…</em>). Distinction fine : <em>-erait</em> = conditionnel, <em>-érait</em> = imparfait (<em>considérerait</em> / <em>considérait</em>). Imparfaits repêchés hors règle : <em>offrait, découvrait, démontrait, souffrait, ouvrait</em>. En <em>-ment</em>, classés noms : <em>mouvement, sentiment, développement, moment, jugement, fondement, entendement, commencement, changement, raisonnement, élément, événement…</em> ; classés verbes : <em>forment, réclament, affirment, expriment…</em> ; <em>comment</em> à part. Toute forme non couverte par une règle ou une liste reste sans étiquette et compte au résidu (0,088 % des mots).</p>
<p><strong>Delta de Burrows.</strong> Segments de 20 000 mots (18 pour 1875, 19 pour 1886, 8 pour 1903, 4 pour 1892) ; 120 mots-outils les plus fréquents du corpus commun ; fréquences centrées-réduites sur l'ensemble des segments ; distance = moyenne des écarts absolus. Le classement d'un segment se fait par distance au profil moyen de chaque strate.</p>
<p><strong>Reproductibilité.</strong> Comme pour la page voisine : un unique programme de dépouillement, des règles toutes énoncées ci-dessus, les transcriptions publiques de ce site. Refaites le comptage : vous retrouverez ces nombres — c'est la définition même du protocole.</p>
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

**Sources.** *Essais de critique générale*, 2ᵉ éd., Au Bureau de la Critique philosophique, 1875 : *Premier Essai*, t. II–III ; *Deuxième Essai*, t. II–III. — *Esquisse d'une classification systématique des doctrines philosophiques*, t. I (1885) et t. II (1886). — *Le Personnalisme, suivi d'une étude sur la perception externe et sur la force*, Félix Alcan, 1903. — Point de contrôle : *Troisième Essai, Les Principes de la nature*, 2ᵉ éd. corrigée et augmentée, 1892, t. I. Transcriptions intégrales de ce site ; étiquetage et comptages sur ces transcriptions.
