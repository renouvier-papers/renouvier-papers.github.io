---
title: "Le système en formules"
description: "La charpente logique du néocriticisme, terme à terme et joint à joint — un instrument de vérification, pas un résumé."
---

# Le système en formules

Renouvier a lui-même fixé le cahier des charges de cette page, au seuil du Deuxième Essai :

> **« J'arrive aux catégories empiriquement ; je les fixe par hypothèse, et je les propose pour être vérifiées. »**
> 
> Charles Renouvier, *Essais de critique générale. Deuxième Essai. Traité de psychologie rationnelle d'après les principes du criticisme*, 2e éd. revue et considérablement augmentée, Paris, Bueau de la *Critique philosophique*, t. I, p. 2.

Cette page prend l'offre au mot. Elle ne raconte pas le système : elle le démonte, avec l'outil que Renouvier respectait par-dessus tout — la logique formelle. Le système entier tient d'abord en **une formule** ; chaque terme s'ouvre ensuite sur sa dérivation, jusqu'aux définitions.

Mais l'essentiel est ailleurs. Tous les « donc » ne se valent pas, et le but de cette page est précisément de les distinguer : il y a ceux qui **déduisent**, ceux qui **définissent**, celui qui **suppose** sans le dire, ceux qui **choisissent** — et un qui **raccorde** deux époques du système sous tension. Le style du trait qui souligne chaque connecteur dit de quel joint il s'agit.

**Mode d'emploi.** Touchez un <strong>terme</strong> : sa définition s'affiche, dans les mots de Renouvier quand ils existent. Touchez un <strong>connecteur</strong> : l'opération logique qu'il exécute, et le statut de *ce pas-ci*. Les chevrons, eux, descendent d'un étage, comme sur les autres pages du site.

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
/* ═══ La couche logique (lg-) ═══
   Une formule est une rangée de jetons : termes (lg-t) et connecteurs (lg-c).
   Chaque jeton est un bouton ; le clic remplit la console du bloc.
   Le STATUT d'un connecteur est porté par le style de son soulignement :
   plein = déduction · pointillé = définition · tirets = prémisse à découvert
   · double = choix · ondulé = raccord sous tension. */
#dp .lg-bloc { margin: 1.1rem 0 1.4rem; }
#dp .lg-formule {
  display: flex; flex-wrap: wrap; align-items: baseline; gap: .05rem .34rem;
  padding: .85rem 1rem; border: 1px solid var(--dp-rule); border-radius: 2px;
  font-family: var(--dp-sans); font-size: .98rem; line-height: 2;
}
#dp .lg-formule--maitre { border-color: var(--dp-accent); font-size: 1.05rem; padding: 1rem 1.1rem; }
#dp .lg-t, #dp .lg-c {
  font: inherit; background: none; border: 0; margin: 0; padding: .02rem .16rem;
  color: inherit; cursor: pointer; border-radius: 2px;
  text-decoration-line: underline; text-underline-offset: .34em; text-decoration-thickness: 1px;
}
#dp .lg-t { font-weight: 640; text-decoration-style: dotted; text-decoration-color: color-mix(in srgb, var(--dp-muted) 60%, transparent); }
#dp .lg-c { color: var(--dp-accent); font-weight: 520; text-decoration-thickness: 1.7px; text-decoration-color: var(--dp-accent); }
#dp .lg-c--val    { text-decoration-style: solid; }
#dp .lg-c--def    { text-decoration-style: dotted; }
#dp .lg-c--cache  { text-decoration-style: dashed; }
#dp .lg-c--choix  { text-decoration-style: double; }
#dp .lg-c--raccord{ text-decoration-style: wavy; }
#dp .lg-c--op     { text-decoration-line: none; }
#dp .lg-t:hover, #dp .lg-c:hover { background: var(--dp-faint); }
#dp .lg-t:focus-visible, #dp .lg-c:focus-visible { outline: 2px solid var(--dp-accent); outline-offset: 2px; }
#dp .lg-actif { background: var(--dp-faint); }
#dp .lg-x { color: var(--dp-muted); }               /* parenthèses et ponctuation */
#dp .lg-console {
  display: none; margin-top: .55rem; padding: .8rem .95rem;
  border-left: 2px solid var(--dp-accent); background: var(--dp-faint);
  font-size: .875rem; line-height: 1.62;
}
#dp .lg-console.lg-ouverte { display: block; }
#dp .lg-console .dp-cite { margin: .6rem 0; background: transparent; }
#dp .lg-etat {
  margin: .55rem 0 0; font-size: .72rem; letter-spacing: .07em; text-transform: uppercase;
  color: var(--dp-accent);
}
#dp .lg-lib { display: none; }
#dp .lg-legende {
  display: flex; flex-wrap: wrap; gap: .4rem 1.1rem; margin: .8rem 0 1.2rem;
  font-size: .78rem; color: var(--dp-muted);
}
#dp .lg-legende .lg-c { pointer-events: none; font-size: .9rem; }
#dp .lg-invite { margin: .3rem 0 0; font-size: .78rem; color: var(--dp-muted); font-style: italic; }
@media (max-width: 44rem) {
  #dp .lg-formule { font-size: .92rem; padding: .7rem .75rem; }
  #dp .lg-formule--maitre { font-size: .96rem; }
}
</style>
<div class="dp-outils">
<button class="dp-bouton" type="button" data-dp="tout">Tout déplier</button>
<button class="dp-bouton" type="button" data-dp="rien">Tout replier</button>
<button class="dp-bouton" type="button" data-dp="neufs">Aller au premier pli non ouvert</button>
<span class="dp-compteur" id="dp-compteur" aria-live="polite"></span>
</div>

<div class="lg-legende" aria-label="Légende des joints">
<span><span class="lg-c lg-c--val">⊢</span> déduction</span>
<span><span class="lg-c lg-c--def">⊢</span> définition</span>
<span><span class="lg-c lg-c--cache">⊢</span> prémisse à découvert</span>
<span><span class="lg-c lg-c--choix">⊢</span> choix</span>
<span><span class="lg-c lg-c--raccord">⊢</span> raccord sous tension</span>
</div>

<p class="dp-chapo">Le système, de 1854 à 1903, en une ligne. Sept « donc » — et un seul est souligné double.</p>

<div class="lg-bloc">
<p class="lg-formule lg-formule--maitre" role="group" aria-label="La charpente en une formule">
<span class="lg-x">(</span>
<button class="lg-t" type="button" data-lg="infini">Infini</button>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-t" type="button" data-lg="nombre">Nombre</button>
<button class="lg-c lg-c--op" type="button" data-lg="implique">→</button>
<button class="lg-t" type="button" data-lg="absurde">⊥</button>
<span class="lg-x">)</span>
<button class="lg-c lg-c--cache" type="button" data-lg="d1">⊢₁</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="ensoi">ChoseEnSoi</button>
<button class="lg-c lg-c--def" type="button" data-lg="d2">⊢₂</button>
<span class="lg-x">(</span>
<button class="lg-t" type="button" data-lg="connaitre">Connaître := Relier</button>
<span class="lg-x">)</span>
<button class="lg-c lg-c--val" type="button" data-lg="d3">⊢₃</button>
<span class="lg-x">(</span>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="omega">Savoir(Ω)</button>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-t" type="button" data-lg="commencement">Commencement</button>
<span class="lg-x">)</span>
<button class="lg-c lg-c--val" type="button" data-lg="d4">⊢₄</button>
<button class="lg-c lg-c--op" type="button" data-lg="poss">◇</button><button class="lg-t" type="button" data-lg="liberte">Liberté</button>
<button class="lg-c lg-c--val" type="button" data-lg="d5">⊢₅</button>
<button class="lg-t" type="button" data-lg="croyable">Croyable(Liberté)</button>
<button class="lg-c lg-c--choix" type="button" data-lg="d6">⊢₆</button>
<button class="lg-t" type="button" data-lg="liberte">Liberté</button>
<button class="lg-c lg-c--def" type="button" data-lg="d7">⊢₇</button>
<button class="lg-t" type="button" data-lg="personne">Personne</button>
</p>
<div class="lg-console" aria-live="polite"></div>
<p class="lg-invite">— touchez un terme ou un connecteur —</p>
</div>

<div class="lg-lib" hidden>

<div id="lg-infini">
<span class="dp-etiquette">terme — Infini</span>
<p><strong>Infini</strong> := ce qui ne s'achève pas. Toute la doctrine tient à ne jamais confondre deux énoncés que le langage mélange : <em>aller</em> à l'infini — pour tout n, un n+1 est possible — et <em>être</em> en nombre infini — un tout achevé de parties sans fin. Le premier est permis ; le second est ⊥.</p>
<div class="dp-cite"><p>[…] l'infini et le nombre sont contradictoires entre eux […]</p><span class="dp-source">Formulaire du Traité de logique générale</span></div>
<p class="lg-etat">rôle : définition porteuse — voir le pli « le pivot »</p>
</div>

<div id="lg-nombre">
<span class="dp-etiquette">terme — Nombre</span>
<p><strong>Nombre</strong> := un tout — la synthèse de l'un et du multiple, σ(Un, Multiple). Dire « il y en a sept », c'est avoir <em>fini</em> de compter : le nombre est un achèvement.</p>
<div class="dp-cite"><p>[…] le <em>nombre</em>, c'est-à-dire […] le <em>tout</em> qui est la synthèse de l'un et du multiple […]</p><span class="dp-source">Formulaire du Traité de logique générale</span></div>
<p class="lg-etat">rôle : le « := » sur lequel Cantor divergera — voir « le pivot »</p>
</div>

<div id="lg-et">
<span class="dp-etiquette">connecteur — ∧ (« et »)</span>
<p>La conjonction : « A ∧ B » n'est vraie que si A et B le sont ensemble. C'est l'opération la plus innocente de la logique — et c'est elle que le pivot met en accusation : peut-on poser <em>ensemble</em> Infini et Nombre ?</p>
</div>

<div id="lg-implique">
<span class="dp-etiquette">connecteur — → (« si… alors »)</span>
<p>L'implication : « A → B » n'est fausse que si A est vrai et B faux. Ici : si quelque chose était à la fois nombre et infini, alors contradiction. La contraposée fait tout le travail du système : puisque ⊥ est inacceptable, l'antécédent ne l'est pas non plus.</p>
</div>

<div id="lg-absurde">
<span class="dp-etiquette">terme — ⊥ (la contradiction)</span>
<p>Le faux absolu : une proposition et sa négation tenues ensemble. C'est <strong>l'unique arme du système</strong>. Renouvier n'interdit jamais l'inconnu, l'invérifiable, l'étrange — il n'interdit que le contradictoire. Tout ce qui n'implique pas ⊥ reste ouvert, et c'est de cette ouverture que vivra la croyance (⊢₅).</p>
</div>

<div id="lg-non">
<span class="dp-etiquette">connecteur — ¬ (« non »)</span>
<p>La négation renverse la valeur de ce qui la suit. Dans cette charpente elle frappe deux fois : la chose en soi, et le savoir du Tout. Deux renoncements — dont le système fait ses deux ressources.</p>
</div>

<div id="lg-d1">
<span class="dp-etiquette">⊢₁ — de « pas d'infini actuel » à « pas de chose en soi »</span>
<p>Le pas passe par une prémisse que la déduction ne prononce pas : <strong>dans l'en soi, tout est actuel</strong> — le « possible » n'existe que pour un esprit. Alors seulement « divisible sans fin » devient, en soi, « divisé en une infinité », et le pivot mord.</p>
<p class="lg-etat">statut : prémisse à découvert — voir « la serrure de l'en-soi »</p>
</div>

<div id="lg-ensoi">
<span class="dp-etiquette">terme — ChoseEnSoi</span>
<p>Ce qui existerait hors de toute représentation, tel quel, sans témoin. Le kantisme la garde inconnaissable ; Renouvier la déclare contradictoire — quatre fois, sur ses quatre supports :</p>
<div class="dp-cite"><p>L'espace, le temps, la matière, le mouvement, s'ils étaient en soi, impliqueraient le continu en soi, et par suite un nombre infini de parties en soi de ce continu, ce qui est absurde […]</p><span class="dp-source">Formulaire du Traité de logique générale</span></div>
</div>

<div id="lg-d2">
<span class="dp-etiquette">⊢₂ — de « pas d'en soi » à « connaître, c'est relier »</span>
<p>Si rien n'est donné en soi, tout est donné <em>en rapport</em> — et connaître ne peut plus être atteindre une chose, seulement déterminer des relations. Ce pas ne démontre pas : il redéfinit. C'est le geste fondateur, et il s'assume comme tel.</p>
<p class="lg-etat">statut : définition</p>
</div>

<div id="lg-connaitre">
<span class="dp-etiquette">terme — Connaître := Relier</span>
<p>La thèse des thèses. Les neuf catégories ne sont rien d'autre que la table des manières de relier — voir le pli « σ, la seule opération ».</p>
<div class="dp-cite"><p>Ainsi, Tout phénomène est donné par rapport à d'autres phénomènes.</p><span class="dp-source">Formulaire du Traité de logique générale</span></div>
</div>

<div id="lg-d3">
<span class="dp-etiquette">⊢₃ — la limite, déduite</span>
<p>Si connaître := relier, alors connaître exige un vis-à-vis. Le Tout, par définition, n'en a pas. La conclusion tombe toute seule — c'est la plus propre des déductions du système.</p>
<p class="lg-etat">statut : déduction — voir « Ω, le lemme et les deux théorèmes »</p>
</div>

<div id="lg-omega">
<span class="dp-etiquette">terme — Savoir(Ω)</span>
<p><strong>Ω</strong> := le tout des phénomènes. Rien n'est hors de lui — c'est sa définition. Donc aucun rapport ne le détermine, et ce qui ne peut être déterminé par aucun rapport ne peut être su.</p>
<div class="dp-cite"><p>[…] la relation composant la synthèse totale, ou le tout du monde, existe toute entre ses propres éléments, cela par définition ; le monde n'est donc pas l'un des termes d'un rapport […]</p><span class="dp-source">Formulaire du Traité de logique générale</span></div>
</div>

<div id="lg-commencement">
<span class="dp-etiquette">terme — Commencement</span>
<p>Le passé n'est pas une possibilité : c'est une série <em>effective</em>. Une série effective est achevée de fait ; achevée, elle est nombrée ; nombrée, elle est finie (pivot). Donc il y a un premier terme.</p>
<div class="dp-cite"><p>Nous devons poser en fait le premier commencement, parce qu'une suite indéfinie et effective de phénomènes antérieurs est contradictoire ; mais il ne nous est pas possible d'embrasser et d'expliquer cette limite.</p><span class="dp-source">Formulaire du Traité de logique générale</span></div>
</div>

<div id="lg-d4">
<span class="dp-etiquette">⊢₄ — du commencement au possible de la liberté</span>
<p>Un commencement appelle des causes premières ; une cause première n'est pas causée ; donc « commencer sans être déterminé » est <em>instancié</em> dans le monde. Dès lors la liberté — ce même pouvoir, logé dans une conscience — n'implique aucune contradiction : ◇Liberté.</p>
<p class="lg-etat">statut : déduction — voir « la liberté »</p>
</div>

<div id="lg-poss">
<span class="dp-etiquette">connecteur — ◇ (« possible »)</span>
<p>Chez Renouvier, le possible est strictement logique : est possible ce dont la position n'implique pas ⊥. ◇Liberté ne dit donc pas que la liberté <em>est</em> — seulement qu'elle a le droit d'être. Toute la différence entre ⊢₄ et ⊢₆ tient dans ce losange.</p>
</div>

<div id="lg-liberte">
<span class="dp-etiquette">terme — Liberté</span>
<p>Le pouvoir de commencer une série. En langage de 1864, jamais retouché en trois éditions :</p>
<div class="dp-cite"><p>[…] ces fonctions ont des <em>variables indépendantes</em> réelles, et elles-mêmes ne <em>sont</em> pas simplement, mais <em>se font</em>.</p><span class="dp-source">Formulaire du Traité de Psychologie rationnelle, 1864</span></div>
</div>

<div id="lg-d5">
<span class="dp-etiquette">⊢₅ — l'application de la règle de croyance</span>
<p>La règle : Croyable(p) := ¬Dém(p → ⊥). Puisque ◇Liberté, la liberté est croyable. Le pas est une déduction irréprochable — mais notez ce qu'il donne aussi : ¬Liberté n'étant pas davantage démontrée contradictoire, <strong>la règle arme les deux camps</strong>. C'est pourquoi le pas suivant ne pourra pas être une déduction.</p>
<p class="lg-etat">statut : déduction</p>
</div>

<div id="lg-croyable">
<span class="dp-etiquette">terme — Croyable(Liberté)</span>
<p>La croyance est libre partout où la raison n'a pas prononcé ⊥ — et là seulement.</p>
<div class="dp-cite"><p>[…] les croyances qui, sans prétendre dépasser ces bornes en s'obstinant dans l'affirmation d'objets que la raison a déclarés contradictoires, demeurent libres de s'étendre au delà […]</p><span class="dp-source">Formulaire du Traité de logique générale</span></div>
</div>

<div id="lg-d6">
<span class="dp-etiquette">⊢₆ — LE PARI</span>
<p>Le seul joint souligné double de la charpente. Ce n'est pas une déduction : le dilemme du chapitre XIII a établi qu'aucune preuve n'existe, d'aucun côté. C'est un <strong>acte</strong> — et si la liberté est réelle, cet acte est précisément ce qu'il affirme.</p>
<div class="dp-cite"><p>Alors c'est à la liberté qu'il appartient de déclarer si la liberté est ou non.</p><span class="dp-source">Deuxième Essai, ch. XIII</span></div>
<p class="lg-etat">statut : choix — signalé par l'auteur. voir « la liberté »</p>
</div>

<div id="lg-d7">
<span class="dp-etiquette">⊢₇ — de la liberté à la personne</span>
<p>La Personne := la conscience — σ(Soi, Non-Soi) — en tant que ses actes ont des variables indépendantes. La neuvième catégorie devient le nom du système entier ; l'étage tardif l'étendra vers le haut (conscience première, 1886) et vers le bas (monades, 1903).</p>
<p class="lg-etat">statut : définition — voir « l'étage tardif »</p>
</div>

<div id="lg-personne">
<span class="dp-etiquette">terme — Personne</span>
<div class="dp-cite"><p>9. Personnalité : <em>Liberté</em>. — La <em>Personnalité</em> réunit toutes les catégories, du point de vue de l'homme […]</p><span class="dp-source">Formulaire du Traité de Psychologie rationnelle</span></div>
<p>Le mot arrivera en 1903 — « le personnalisme est le vrai nom » — mais la place était réservée dès 1854 : la dernière case du tableau.</p>
</div>

</div>

<details class="dp-pli" data-rang="rouage 1">
<summary class="dp-titre"><span class="dp-rang">l'axiome</span><span class="dp-texte">Le pivot — ( Infini ∧ Nombre → ⊥ )</span></summary>
<div class="dp-corps">
<p>Tout le système sort de deux définitions et d'un choc. Les voici, mises à plat :</p>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="nombre">Nombre(x)</button>
<button class="lg-c lg-c--def" type="button" data-lg="defsym">:=</button>
<button class="lg-t" type="button" data-lg="acheve">Achevé(x)</button>
<span class="lg-x">&nbsp;&nbsp;·&nbsp;&nbsp;</span>
<button class="lg-t" type="button" data-lg="infini">Infini(x)</button>
<button class="lg-c lg-c--def" type="button" data-lg="defsym">:=</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="acheve">Achevable(x)</button>
<span class="lg-x">&nbsp;&nbsp;·&nbsp;&nbsp;</span>
<button class="lg-c lg-c--val" type="button" data-lg="pv1">⊢</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-c lg-c--op" type="button" data-lg="poss">◇</button><span class="lg-x">(</span>
<button class="lg-t" type="button" data-lg="nombre">Nombre(x)</button>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-t" type="button" data-lg="infini">Infini(x)</button>
<span class="lg-x">)</span>
</p>
<div class="lg-console" aria-live="polite"></div>
<p class="lg-invite">— touchez les deux := puis le ⊢ —</p>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Où la bataille a vraiment lieu</span>
<p>La déduction est inattaquable : <em>achevé et inachevable</em>, ensemble, c'est ⊥. Toute la charge repose donc sur les deux <strong>:=</strong> — et c'est exactement là que Cantor frappera. Sa définition : Nombre(x) := classe d'équivalence par bijection. <em>Achevé</em> n'y figure plus ; un ensemble est donné par sa condition d'appartenance, non par un comptage qui finit. Les deux camps sont logiquement irréprochables ; <strong>ils ne se battent pas sur un théorème, ils se battent sur un :=</strong>. La forme rend ce déplacement visible — c'est tout ce qu'elle peut faire, et ce n'est pas rien.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="rouage 2">
<summary class="dp-titre"><span class="dp-rang">⊢₁</span><span class="dp-texte">La serrure de l'en-soi — et sa prémisse à découvert</span></summary>
<div class="dp-corps">
<p>Voici le pas tel que le Formulaire l'écrit : « L'espace, le temps, la matière, le mouvement, s'ils étaient en soi, impliqueraient le continu en soi, et par suite un nombre infini de parties en soi de ce continu, ce qui est absurde ». Mis en forme, il manque un maillon — et la forme le montre :</p>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="ensoi">EnSoi(X)</button>
<button class="lg-c lg-c--cache" type="button" data-lg="e1">→</button>
<button class="lg-t" type="button" data-lg="actuel">ToutActuel(X)</button>
<span class="lg-x">&nbsp;·&nbsp;</span>
<span class="lg-x">(</span><button class="lg-t" type="button" data-lg="continu">Continu(X)</button>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-t" type="button" data-lg="actuel">ToutActuel(X)</button><span class="lg-x">)</span>
<button class="lg-c lg-c--op" type="button" data-lg="implique">→</button>
<button class="lg-t" type="button" data-lg="infparties">∞Parties(X)</button>
<button class="lg-c lg-c--op" type="button" data-lg="implique">→</button>
<button class="lg-t" type="button" data-lg="absurde">⊥</button>
<span class="lg-x">&nbsp;·&nbsp;</span>
<button class="lg-c lg-c--val" type="button" data-lg="e2">⊢</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="ensoi">EnSoi(X)</button>
</p>
<div class="lg-console" aria-live="polite"></div>
<p class="lg-invite">— touchez le → en tirets —</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">La prémisse n'est pas écrite dans la déduction — elle est écrite ailleurs</span>
<p>Pourquoi « divisible sans fin » (permis) devient-il, en soi, « divisé en une infinité » (⊥) ? Parce que le possible est une affaire de représentation : hors de tout esprit, rien n'est « en puissance », tout est ce qu'il est. Renouvier a posé ce principe noir sur blanc — du côté inverse :</p>
<div class="dp-cite">
<p>[…] on ne réfléchit pas que l'indéfinité de la représentation possible, ou universelle, ne saurait conférer l'existence à d'autres rapports particuliers que ceux qui sont effectivement compris dans les phénomènes donnés […]</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<p>Le possible ne confère pas l'existence ; l'existence en soi ne garde donc aucun possible. La prémisse est cohérente avec le système et défendable — mais elle porte tout le pas, et elle mérite d'être vue. C'est le seul → en tirets de la page.</p>
</div>
</div>
</details>

<div class="lg-lib" hidden>
<div id="lg-defsym">
<span class="dp-etiquette">connecteur — := (« est défini comme »)</span>
<p>Le := ne se démontre pas : il <strong>pose</strong>. On ne le réfute pas, on le conteste — en proposant un autre :=, et en comparant ce que chacun permet de faire. C'est le connecteur le plus puissant et le plus vulnérable de la page : trois des grandes querelles du système (Cantor, la force, la substance) sont des querelles de :=.</p>
</div>
<div id="lg-acheve">
<span class="dp-etiquette">terme — Achevé</span>
<p>Ce dont la synthèse est faite : un tout posé, un comptage fini. L'<em>achevable</em> est son ombre modale : ce qui pourrait l'être. Le pivot joue ces deux mots l'un contre l'autre.</p>
</div>
<div id="lg-pv1">
<span class="dp-etiquette">⊢ — la déduction du pivot</span>
<p>Des deux définitions, la conclusion suit en deux lignes : si Nombre(x), alors Achevé(x) ; si Infini(x), alors jamais achevable — donc pas achevé. Les deux ensemble : ⊥. Valide sans reste.</p>
<p class="lg-etat">statut : déduction — la charge est sur les deux :=</p>
</div>
<div id="lg-e1">
<span class="dp-etiquette">→ en tirets — la prémisse à découvert</span>
<p><strong>EnSoi ⇒ ToutActuel</strong> : hors de tout esprit, pas de « en puissance ». C'est le maillon que la déduction du Formulaire saute — non qu'il soit indéfendable : il est défendu ailleurs (voir l'encart), mais il n'est pas <em>dans</em> le pas. Un kantien qui garde la chose en soi avec des « parties potentielles » refuse exactement ceci.</p>
<p class="lg-etat">statut : prémisse à découvert</p>
</div>
<div id="lg-actuel">
<span class="dp-etiquette">terme — ToutActuel</span>
<p>État d'une chose dont rien n'est « en réserve » : toutes ses déterminations sont posées. Le contraire du potentiel — lequel, chez Renouvier, n'existe que relativement à une représentation.</p>
</div>
<div id="lg-continu">
<span class="dp-etiquette">terme — Continu</span>
<p>Ce qui n'a pas de dernières parties : entre deux points, toujours un troisième. Représenté, le continu est une règle de division toujours ouverte — inoffensif. En soi, il devrait être <em>fait</em> de ses parties — et elles seraient sans nombre.</p>
</div>
<div id="lg-infparties">
<span class="dp-etiquette">terme — ∞Parties</span>
<p>Une infinité <em>actuelle</em> de parties : un nombre infini — exactement ce que le pivot vient d'interdire.</p>
</div>
<div id="lg-e2">
<span class="dp-etiquette">⊢ — le rejet de l'antécédent</span>
<p>Puisque la conséquence est ⊥, l'antécédent tombe : pas de chose en soi — pour les quatre supports que sont l'espace, le temps, la matière, le mouvement. Le kantisme perd son arrière-monde par l'arithmétique.</p>
<p class="lg-etat">statut : déduction (une fois la prémisse accordée)</p>
</div>
</div>

<details class="dp-pli" data-rang="rouage 3">
<summary class="dp-titre"><span class="dp-rang">⊢₂</span><span class="dp-texte">σ — la seule opération du système</span></summary>
<div class="dp-corps">
<p>Neuf catégories, mais une seule machine. Chaque catégorie est la synthèse de deux contraires corrélatifs — nous noterons cette opération <strong>σ</strong> (le symbole est de nous ; l'opération est de lui, à chaque ligne du Formulaire) :</p>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="sigma">σ(a, b)</button>
<button class="lg-c lg-c--def" type="button" data-lg="defsym">:=</button>
<span class="lg-x">la synthèse qui pose ensemble deux contraires corrélatifs</span>
</p>
<div class="lg-console" aria-live="polite"></div>
</div>
<p>Les neuf instances, telles que la page des <a href="/recherche/complications/essais/">Essais</a> les déplie une à une :</p>
<p class="lg-formule" aria-label="Les neuf instances de sigma">
<span>Déterminé := σ(Distinct, Identique)</span><span class="lg-x">·</span>
<span>Tout := σ(Un, Multiple)</span><span class="lg-x">·</span>
<span>Étendue := σ(Point, Espace)</span><span class="lg-x">·</span>
<span>Durée := σ(Instant, Temps)</span><span class="lg-x">·</span>
<span>Espèce := σ(Différence, Genre)</span><span class="lg-x">·</span>
<span>Changement := σ(Rapport, Non-rapport)</span><span class="lg-x">·</span>
<span>Force := σ(Acte, Puissance)</span><span class="lg-x">·</span>
<span>Passion := σ(État, Tendance)</span><span class="lg-x">·</span>
<span><strong>Conscience := σ(Soi, Non-Soi)</strong></span>
</p>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La loi des corrélats — et le théorème d'innocuité</span>
<p>La règle de σ : ni a ni b n'est représentable seul. Renouvier la formule, et en tire d'un coup deux résultats :</p>
<div class="dp-cite">
<p>[…] ces termes contraires sont abstraits et corrélatifs, et ne s'appliquent séparément, dans la rigueur de leur signification pure, à aucune autre représentation que celle d'eux-mêmes. Par exemple, aucune chose n'est <em>une</em>, abstraction faite de toute multiplicité ; aucune n'est <em>multiple</em>, abstraction faite de toute unité ; mais toute chose est représentée comme un <em>tout</em>.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<p>Premier résultat : les prétendus absolus — l'Un seul, le Simple seul, l'Infini seul — sont des <strong>a sans b</strong> : ils ne dénotent rien. Second résultat, contre Kant : les catégories, bien employées, <strong>ne produisent aucune antinomie</strong> — les antinomies naissent toutes de l'usage d'un terme arraché à son corrélat. La machine est sûre ; seul son emploi hors règle casse.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Et les forces, au passage</span>
<p>La loi des corrélats désamorce d'avance la physique des causes-choses : « Il n'existe donc pas de <em>causes substantielles</em>, et les <em>forces</em> sont des rapports <em>sui generis</em> donnés entre des phénomènes. » Retenez cette ligne — c'est elle que 1903 rouvrira, par l'autre bout, dans <a href="/recherche/complications/physique-tardive/">La physique du personnalisme</a>.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="rouage 4">
<summary class="dp-titre"><span class="dp-rang">⊢₃</span><span class="dp-texte">Ω — un seul lemme, deux théorèmes positifs</span></summary>
<div class="dp-corps">
<p>La quatrième partie du Premier Essai fait échouer les neuf catégories sur le monde. Mis en forme, les neuf échecs se révèlent être <strong>un seul lemme</strong> :</p>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="omegadef">Ω</button>
<button class="lg-c lg-c--def" type="button" data-lg="defsym">:=</button>
<span class="lg-x">le tout des phénomènes</span>
<span class="lg-x">&nbsp;·&nbsp;</span>
<button class="lg-t" type="button" data-lg="correlat">σ exige deux places</button>
<span class="lg-x">&nbsp;·&nbsp;</span>
<button class="lg-c lg-c--val" type="button" data-lg="o1">⊢</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="omega">Savoir(Ω)</button>
</p>
<div class="lg-console" aria-live="polite"></div>
</div>
<p>Mais deux catégories, en échouant, <em>produisent</em>. La succession et la causalité, appliquées à Ω, ne rendent pas seulement l'ignorance — elles rendent deux théorèmes :</p>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="passe">PasséEffectif(Ω)</button>
<button class="lg-c lg-c--val" type="button" data-lg="o2">⊢</button>
<button class="lg-t" type="button" data-lg="commencement">Commencement</button>
<span class="lg-x">&nbsp;·&nbsp;</span>
<button class="lg-t" type="button" data-lg="commencement">Commencement</button>
<button class="lg-c lg-c--val" type="button" data-lg="o3">⊢</button>
<button class="lg-t" type="button" data-lg="premieres">CausesPremières</button>
</p>
<div class="lg-console" aria-live="polite"></div>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La neuvième instance, et son ombre portée</span>
<p>Appliquez maintenant le lemme à la dernière catégorie. Conscience := σ(Soi, Non-Soi) ; posez Soi := Ω ; alors Non-Soi := rien — et σ n'a plus sa seconde place :</p>
<div class="dp-cite">
<p>[…] une conscience enveloppant la totalité des phénomènes cesse de répondre à la notion de conscience […]</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<p>En 1854, Renouvier en tire la pluralité des consciences premières. Et notez que le texte code déjà, dans le théorème des causes premières, la question qui occupera sa vie : « une <strong>ou plusieurs</strong> causes premières » — le Formulaire laisse l'article indécis. L'histoire de cette indécision est la page <a href="/recherche/complications/evolution/">Comment je suis arrivé à cette conclusion</a>.</p>
</div>
</div>
</details>

<div class="lg-lib" hidden>
<div id="lg-sigma">
<span class="dp-etiquette">terme — σ (la synthèse)</span>
<p>L'opération native du système : prendre deux contraires qui ne valent rien l'un sans l'autre, et poser leur tenue ensemble. Neuf instances la déclinent, du Déterminé à la Conscience. Le symbole σ est notre notation — chaque formule de cette page est un commentaire, contestable comme tel.</p>
</div>
<div id="lg-omegadef">
<span class="dp-etiquette">terme — Ω</span>
<p>Le tout des phénomènes. Sa définition contient sa perte : « rien hors de lui » signifie « aucun vis-à-vis », donc aucune place dans une relation, donc aucune prise pour σ.</p>
</div>
<div id="lg-correlat">
<span class="dp-etiquette">lemme — σ exige deux places</span>
<p>Toute détermination est une synthèse ; toute synthèse a deux termes ; déterminer x, c'est lui donner un vis-à-vis. Le lemme vaut pour les neuf catégories d'un coup — c'est pourquoi la quatrième partie du Premier Essai, si longue en chapitres, est si courte en logique.</p>
</div>
<div id="lg-o1">
<span class="dp-etiquette">⊢ — la limite</span>
<p>Ω sans vis-à-vis, σ sans seconde place : ¬Savoir(Ω). La science est bornée non par faiblesse, mais par la grammaire de la relation.</p>
<p class="lg-etat">statut : déduction</p>
</div>
<div id="lg-passe">
<span class="dp-etiquette">terme — PasséEffectif</span>
<p>Le passé n'est pas un « possible » : il a eu lieu. Série effective, donc achevée de fait, donc nombrée — et le pivot s'applique : finie.</p>
</div>
<div id="lg-o2">
<span class="dp-etiquette">⊢ — le théorème du commencement</span>
<p>Série effective ⊢ finie ⊢ premier terme. C'est l'anti-Kant exact : là où la première antinomie laissait thèse et antithèse dos à dos, Renouvier tranche par l'arithmétique du pivot.</p>
<p class="lg-etat">statut : déduction</p>
</div>
<div id="lg-o3">
<span class="dp-etiquette">⊢ — le théorème des causes premières</span>
<div class="dp-cite"><p>[…] le principe de contradiction oblige à admettre une ou plusieurs causes premières qui terminent la suite ascendante des événements.</p><span class="dp-source">Formulaire du Traité de logique générale</span></div>
<p class="lg-etat">statut : déduction — l'article (« une ou plusieurs ») reste ouvert</p>
</div>
<div id="lg-premieres">
<span class="dp-etiquette">terme — CausesPremières</span>
<p>Des termes qui commencent des séries sans être eux-mêmes des conséquents. Leur existence est déduite ; leur <em>nombre</em> ne l'est pas — et cette case vide est celle où 1886 viendra écrire « une ».</p>
</div>
</div>

<details class="dp-pli" data-rang="rouages 5-6-7">
<summary class="dp-titre"><span class="dp-rang">⊢₄ ⊢₅ ⊢₆</span><span class="dp-texte">La liberté — le possible, le dilemme, la règle, le pari</span></summary>
<div class="dp-corps">
<p>Quatre pièces s'emboîtent ici, et une seule n'est pas une déduction. D'abord le possible, hérité du théorème des causes premières :</p>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="premieres">CausePremière(c)</button>
<button class="lg-c lg-c--op" type="button" data-lg="implique">→</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="cause">Causé(c)</button>
<span class="lg-x">&nbsp;·&nbsp;</span>
<button class="lg-c lg-c--val" type="button" data-lg="l1">⊢</button>
<button class="lg-c lg-c--op" type="button" data-lg="poss">◇</button><button class="lg-t" type="button" data-lg="liberte">Liberté</button>
</p>
<div class="lg-console" aria-live="polite"></div>
</div>
<p>Puis le dilemme du chapitre XIII — le plus beau morceau de logique du corpus, parce qu'il se retourne sur lui-même :</p>
<div class="lg-bloc">
<p class="lg-formule">
<span class="lg-x">(</span>
<button class="lg-t" type="button" data-lg="liberte">Liberté</button>
<button class="lg-c lg-c--op" type="button" data-lg="l2a">→</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="preuve">Preuve</button>
<span class="lg-x">)</span>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<span class="lg-x">(</span>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="liberte">Liberté</button>
<button class="lg-c lg-c--op" type="button" data-lg="l2b">→</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="preuve">Preuve</button>
<span class="lg-x">)</span>
<button class="lg-c lg-c--val" type="button" data-lg="l3">⊢</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="preuve">Preuve(Liberté)</button>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="preuve">Preuve(¬Liberté)</button>
</p>
<div class="lg-console" aria-live="polite"></div>
<p class="lg-invite">— touchez les deux → : ils n'échouent pas pour la même raison —</p>
</div>
<p>Puis la règle de croyance, et son application — irréprochable, et à double tranchant :</p>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="croyable">Croyable(p)</button>
<button class="lg-c lg-c--def" type="button" data-lg="defsym">:=</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="dem">Dém( p → ⊥ )</button>
<span class="lg-x">&nbsp;·&nbsp;</span>
<button class="lg-c lg-c--val" type="button" data-lg="l4">⊢</button>
<button class="lg-t" type="button" data-lg="croyable">Croyable(Liberté)</button>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-t" type="button" data-lg="croyable">Croyable(¬Liberté)</button>
</p>
<div class="lg-console" aria-live="polite"></div>
</div>
<p>Et enfin le pari — le joint double :</p>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="croyable">Croyable(Liberté)</button>
<button class="lg-c lg-c--choix" type="button" data-lg="d6">⊢₆</button>
<button class="lg-t" type="button" data-lg="liberte">Liberté</button>
<span class="lg-x">&nbsp;—&nbsp;par l'acte&nbsp;</span>
<button class="lg-t" type="button" data-lg="aff">Affirmer(Liberté)</button>
</p>
<div class="lg-console" aria-live="polite"></div>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">L'honnêteté du système est dans la symétrie</span>
<p>Voyez ce que la formule montre et que les résumés cachent : la règle rend croyables <strong>les deux</strong> thèses. Un déterministe est, à ce point exact du raisonnement, aussi en règle que Renouvier. Voilà pourquoi ⊢₆ ne peut pas être une déduction, et pourquoi Renouvier — c'est sa grandeur — l'a écrit lui-même au lieu de le maquiller. Le système contient l'aveu de son propre point de bascule.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Même les probabilités ne sauvent pas la mise — il le dit</span>
<p>Le chapitre XIII convoque le calcul des probabilités (la loi des grands nombres vérifiée par l'expérience est compatible avec des possibles réellement égaux). Verdict de l'auteur, dès 1864 : ce calcul « fournit ainsi, selon sa nature, une sorte de probabilité, plutôt qu'une démonstration de la liberté comme réelle ». Une <em>probabilité de la liberté</em> — pas une preuve. Le pari reste entier.</p>
<p class="lg-invite">source : Formulaire du Traité de Psychologie rationnelle : 1864 (1ère éd. du 2ème Essai), p. XXXVII ; 1875 (2ème éd. du 3ème Essai), p. 307.</p>
</div>
</div>
</details>

<div class="lg-lib" hidden>
<div id="lg-cause">
<span class="dp-etiquette">terme — Causé</span>
<p>Déterminé par des antécédents selon une loi. Une cause première ne l'est pas — par définition : la nier causée, c'est la poser « avant elle-même ».</p>
</div>
<div id="lg-l1">
<span class="dp-etiquette">⊢ — du théorème au possible</span>
<p>Le monde contient déjà des commencements non déterminés (les causes premières). Alors une conscience qui commencerait ses séries — la liberté — n'ajoute aucune contradiction à l'inventaire. ◇Liberté : le droit d'exister, pas encore l'existence.</p>
<p class="lg-etat">statut : déduction</p>
</div>
<div id="lg-l2a">
<span class="dp-etiquette">→ — la première branche du dilemme</span>
<p>Si je suis libre, c'est <em>librement</em> que je juge la question — mon jugement est un acte, pas un constat : il ne prouve rien. La liberté, vraie, détruit la preuve de la liberté.</p>
</div>
<div id="lg-l2b">
<span class="dp-etiquette">→ — la seconde branche</span>
<p>Si je suis déterminé, mon jugement — quel qu'il soit, vrai ou faux — était inévitable : il ne prouve rien non plus. « C'est une manière d'être dans le vrai, que de suivre une loi nécessaire en affirmant le faux » : la nécessité, vraie, avale toute preuve, y compris la sienne.</p>
</div>
<div id="lg-l3">
<span class="dp-etiquette">⊢ — l'impasse démontrée</span>
<p>Des deux branches ensemble : aucune preuve, d'aucun côté, n'est possible. Ce n'est pas un constat d'ignorance provisoire — c'est un théorème d'impossibilité. Le terrain est déblayé pour un acte.</p>
<p class="lg-etat">statut : déduction</p>
</div>
<div id="lg-preuve">
<span class="dp-etiquette">terme — Preuve</span>
<p>Une démonstration contraignante, valable pour tout esprit, indépendante de celui qui la donne. C'est exactement ce que le dilemme rend impossible ici : toute « preuve » de la liberté passe par un jugement dont le statut est la question même.</p>
</div>
<div id="lg-dem">
<span class="dp-etiquette">terme — Dém( p → ⊥ )</span>
<p>« Il est démontré que p implique contradiction. » La croyance n'est bornée que par cela — pas par l'invraisemblable, pas par l'inouï : par le seul ⊥ établi.</p>
</div>
<div id="lg-l4">
<span class="dp-etiquette">⊢ — l'application, à double tranchant</span>
<p>◇Liberté donne Croyable(Liberté). Mais rien n'a démontré ¬Liberté contradictoire : donc Croyable(¬Liberté) aussi. La déduction est parfaite — et elle laisse les deux portes ouvertes. C'est fait exprès.</p>
<p class="lg-etat">statut : déduction</p>
</div>
<div id="lg-aff">
<span class="dp-etiquette">terme — Affirmer(Liberté)</span>
<p>Non une proposition : un acte. Et l'acte a une propriété que nulle proposition n'a — si la liberté est réelle, <em>l'affirmer librement est un cas de ce qu'on affirme</em>. L'affirmation ne prouve pas la liberté ; elle l'exerce. En face, affirmer la nécessité, si la nécessité est vraie, n'est qu'un événement de plus.</p>
<div class="dp-cite"><p>Le principe de ces principes est la liberté.</p><span class="dp-source">Deuxième Essai — le second ordre de la certitude</span></div>
<p class="lg-etat">d'où le vertige : chaque ⊢ de cette page, une fois <em>affirmé</em>, repose sur ⊢₆</p>
</div>
</div>

<details class="dp-pli" data-rang="rouages 8-9">
<summary class="dp-titre"><span class="dp-rang">⊢₇ et après</span><span class="dp-texte">L'étage tardif — le raccord de 1886, le choix de 1903</span></summary>
<div class="dp-corps">
<p>Deux arguments s'ajoutent à la charpente après 1885, et ils introduisent les deux derniers types de joints : l'ondulé et le second double.</p>

<p class="dp-epigraphe">1886 — l'argument de l'unité</p>
<div class="lg-bloc">
<p class="lg-formule">
<span class="lg-x">(</span>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="loisansphi">Loi sans Phénomène</button>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="phisansc">Phénomène sans Conscience</button>
<span class="lg-x">)</span>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-t" type="button" data-lg="communaute">Communauté(Lois)</button>
<button class="lg-c lg-c--raccord" type="button" data-lg="t1">⊢</button>
<button class="lg-t" type="button" data-lg="c0">ConsciencePremière</button>
</p>
<div class="lg-console" aria-live="polite"></div>
<p class="lg-invite">— le seul ⊢ ondulé du corpus : touchez-le —</p>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Pourquoi ondulé — les deux forces qui tirent sur ce joint</span>
<p><strong>Ce qui pousse</strong> : le phénoménisme de 1854 lui-même. Une loi n'existe que représentée ; les lois sont les mêmes pour toutes les consciences ; une loi une exige « une conscience une et universelle donnée à cet objet ». Rien d'étranger n'entre — c'est la prémisse de jeunesse qui produit Dieu.</p>
<p><strong>Ce qui tire en face</strong> : le chapitre LIII, resté debout. Une conscience du Tout est ⊥ — elle n'aurait pas de non-soi. Le raccord de Renouvier passe au millimètre : C₀ n'enveloppe pas Ω ; son non-soi, ce sont ses créatures libres ; elle est « souverain Auteur et siège suprême de ces lois […] mais non un être existant en dehors de ces lois » — et finie, le pivot y veille. <strong>Reste l'objection qu'un kantien ferait</strong> : la communauté des catégories pourrait être un fait sans auteur. Renouvier répond par sa définition — une loi non représentée n'existe pas —, ce qui reconduit le débat à un :=. Le joint tient, mais il travaille. L'histoire de sa pose est sur la page <a href="/recherche/complications/evolution/">Comment je suis arrivé à cette conclusion</a>.</p>
</div>

<p class="dp-epigraphe">1903 — le choix sur la force</p>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="source">Source(idée de Force) = Volonté</button>
<span class="lg-x">&nbsp;·&nbsp;</span>
<span class="lg-x">(</span>
<button class="lg-t" type="button" data-lg="nominale">Force := ValeurNominale</button>
<button class="lg-c lg-c--op" type="button" data-lg="ou">∨</button>
<button class="lg-t" type="button" data-lg="forcevol">Force := Volonté</button>
<span class="lg-x">)</span>
<button class="lg-c lg-c--choix" type="button" data-lg="t2">⊢</button>
<button class="lg-t" type="button" data-lg="forcevol">Force := Volonté</button>
</p>
<div class="lg-console" aria-live="polite"></div>
</div>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="forcevol">Force := Volonté</button>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-t" type="button" data-lg="rienpasse">RienNePasse</button>
<button class="lg-c lg-c--val" type="button" data-lg="t3">⊢</button>
<button class="lg-t" type="button" data-lg="monades">Monades</button>
<button class="lg-c lg-c--val" type="button" data-lg="t4">⊢</button>
<button class="lg-t" type="button" data-lg="harmonie">Harmonie</button>
<span class="lg-x">&nbsp;—&nbsp;avec&nbsp;</span>
<button class="lg-t" type="button" data-lg="liberte">variables indépendantes</button>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="infini">Infini</button>
</p>
<div class="lg-console" aria-live="polite"></div>
</div>
<div class="dp-note">
<span class="dp-etiquette">Le second choix — argumenté, mais choix</span>
<p>La disjonction est réelle, et la première branche est respectable : c'est celle des « mathématiciens et physiciens » qui ont « dû l'abandonner, ou du moins la réduire à sa valeur nominale ». Renouvier prend l'autre, pour une raison qu'il donne : la branche nominale renonce à comprendre ; la sienne comprend — au prix de peupler la matière de volontés. La forme classe : ∨-élimination par décision motivée, pas par théorème. Le détail est sur <a href="/recherche/complications/physique-tardive/">La physique du personnalisme</a>.</p>
</div>
</div>
</details>

<div class="lg-lib" hidden>
<div id="lg-loisansphi">
<span class="dp-etiquette">terme — Loi sans Phénomène</span>
<p>Une loi qui régnerait sur rien. Exclue : une loi est un « phénomène complexe constamment impliqué dans d'autres phénomènes » — elle n'a pas d'autre lieu que ce qu'elle règle.</p>
</div>
<div id="lg-phisansc">
<span class="dp-etiquette">terme — Phénomène sans Conscience</span>
<p>Un donné sans témoin. Exclu par la définition initiale : les choses sont données « en qualité de représentations ». C'est la moitié la plus dure du phénoménisme — et c'est elle qui portera tout le poids de 1886.</p>
</div>
<div id="lg-communaute">
<span class="dp-etiquette">terme — Communauté(Lois)</span>
<p>Le fait : espace, temps, causalité sont les mêmes pour toutes les consciences — nous sommes « membres du même monde intelligible ». Ce fait-là, la pluralité de 1854 le laissait sans raison.</p>
</div>
<div id="lg-t1">
<span class="dp-etiquette">⊢ ondulé — le raccord de 1886</span>
<p>« Cette harmonie, en effet, implique l'unité d'une conscience qui la conçoit et la réalise. » Le pas est le sien, mot pour mot — et il doit passer entre deux murs qu'il a lui-même bâtis : le ch. LIII (pas de conscience du Tout) et le pivot (pas d'infini). D'où C₀ : une, libre, <em>finie</em>, avec un dehors. Ça passe — en travaillant.</p>
<p class="lg-etat">statut : raccord sous tension — Esquisse, t. II, 1886</p>
</div>
<div id="lg-c0">
<span class="dp-etiquette">terme — ConsciencePremière</span>
<div class="dp-cite"><p>[…] la conscience première et universelle, auteur du monde, libre créateur[s] d'êtres libres.</p><span class="dp-source">Esquisse, t. II, p. 348 — « créateur[s] » : coquille de numérisation, rétablie</span></div>
<p>Une — l'article que la case « une ou plusieurs » attendait depuis 1854. Finie, par le pivot. Libre, par le pur commencement.</p>
</div>
<div id="lg-ou">
<span class="dp-etiquette">connecteur — ∨ (« ou »)</span>
<p>La disjonction : au moins l'une des deux branches. En choisir une quand aucun théorème ne ferme l'autre, c'est une ∨-élimination par décision — le geste exact de 1903 sur la force.</p>
</div>
<div id="lg-source">
<span class="dp-etiquette">terme — Source(idée de Force)</span>
<div class="dp-cite"><p>[…] cette signification est premièrement donnée dans la conscience de l'effort volontaire, et de là secrètement empruntée pour l'usage universel qu'on en fait.</p><span class="dp-source">Étude sur la perception externe et sur la force</span></div>
<p>Un constat génétique : le mot vient du vouloir. De là ne suit pas encore que la force <em>soit</em> volonté — d'où la disjonction, et le choix.</p>
</div>
<div id="lg-nominale">
<span class="dp-etiquette">terme — Force := ValeurNominale</span>
<div class="dp-cite"><p>[…] les mathématiciens et les physiciens ont dû l'abandonner, ou du moins la réduire à sa valeur nominale, exprimant un rapport défini d'antécédent à conséquent […]</p><span class="dp-source">Le Personnalisme, préface</span></div>
<p>La branche positiviste : plus de force, des fonctions. Renouvier la juge tenable — et vide.</p>
</div>
<div id="lg-forcevol">
<span class="dp-etiquette">terme — Force := Volonté</span>
<p>La branche prise : garder au mot son seul contenu connu. Conséquence immédiate — les porteurs de force sont des vouloirs, donc des consciences. La physique change d'habitants.</p>
</div>
<div id="lg-t2">
<span class="dp-etiquette">⊢ double — le choix de 1903</span>
<p>Aucun théorème ne ferme la branche nominale. Renouvier élit l'autre, avec un motif (comprendre plutôt que renoncer) — mais un motif n'est pas une démonstration. Second joint double du corpus, et il est argumenté, non signé : la différence avec ⊢₆ est là.</p>
<p class="lg-etat">statut : choix motivé</p>
</div>
<div id="lg-rienpasse">
<span class="dp-etiquette">terme — RienNePasse</span>
<div class="dp-cite"><p>[…] aucun intermédiaire n'est perçu, aucun véhicule de l'action d'un phénomène sur l'autre […]</p><span class="dp-source">Étude sur la perception externe et sur la force</span></div>
</div>
<div id="lg-monades">
<span class="dp-etiquette">terme — Monades</span>
<div class="dp-cite"><p>[…] on peut les appeler des monades […]</p><span class="dp-source">Étude, ch. XLVI</span></div>
<p>Des agents mentaux sans fenêtres — Leibniz corrigé deux fois : des variables indépendantes en plus (la liberté), l'infini en moins. L'« automate incorporel » cesse d'être automate.</p>
</div>
<div id="lg-harmonie">
<span class="dp-etiquette">terme — Harmonie</span>
<p>Des séries qui s'accordent sans que rien ne passe : il faut un accordeur — C₀, posée en 1886, dix-sept ans avant que le dernier mot du dernier livre ne soit écrit : « et c'est l'harmonie préétablie ».</p>
</div>
<div id="lg-t3">
<span class="dp-etiquette">⊢ — des vouloirs sans fenêtres aux monades</span>
<p>Si les éléments sont des vouloirs et que rien ne transite entre eux, chacun se développe du dedans : la définition de la monade est atteinte par déduction — une fois le choix ⊢ fait en amont.</p>
<p class="lg-etat">statut : déduction (conditionnelle au choix)</p>
</div>
<div id="lg-t4">
<span class="dp-etiquette">⊢ — des monades à l'harmonie</span>
<p>Des séries closes qui pourtant se répondent : l'accord ne peut être que préréglé. La conclusion suit — et elle exigeait C₀ : sans le raccord de 1886, ce ⊢ n'aurait pas de quoi payer.</p>
<p class="lg-etat">statut : déduction (conditionnelle au raccord)</p>
</div>
</div>

<details class="dp-pli" data-rang="l'audit">
<summary class="dp-titre"><span class="dp-rang">bilan</span><span class="dp-texte">Le tableau de contrôle — chaque joint, son statut, sa source</span></summary>
<div class="dp-corps">
<p>Voici l'audit complet des articulations maîtresses. Les statuts sont nos jugements — c'est-à-dire des commentaires, contestables comme tels ; les sources sont les siennes.</p>
<div class="dp-escalier">
<div class="dp-marche"><span class="dp-marche-num">⊢₁</span><span><strong>prémisse à découvert</strong> — du pivot à ¬ChoseEnSoi ; le maillon tu : « en soi ⇒ tout actuel ». <em>Formulaire ; l'appui est p. 282 du même texte.</em></span></div>
<div class="dp-marche"><span class="dp-marche-num">⊢₂</span><span><strong>définition</strong> — Connaître := Relier ; le geste fondateur, assumé. <em>Formulaire.</em></span></div>
<div class="dp-marche"><span class="dp-marche-num">⊢₃</span><span><strong>déduction</strong> — le lemme d'Ω : pas de vis-à-vis, pas de savoir. <em>Premier Essai, quatrième partie.</em></span></div>
<div class="dp-marche"><span class="dp-marche-num">⊢₄</span><span><strong>déduction</strong> — commencement, causes premières, donc ◇Liberté. <em>Formulaire.</em></span></div>
<div class="dp-marche"><span class="dp-marche-num">⊢₅</span><span><strong>déduction</strong> — la règle de croyance, appliquée ; elle arme les deux camps. <em>Formulaire.</em></span></div>
<div class="dp-marche dp-marche--pli"><span class="dp-marche-num">⊢₆</span><span><strong>choix — signé.</strong> « C'est à la liberté qu'il appartient de déclarer si la liberté est ou non. » <em>Deuxième Essai, ch. XIII.</em></span></div>
<div class="dp-marche"><span class="dp-marche-num">⊢₇</span><span><strong>définition</strong> — Personne := la conscience à variables indépendantes. <em>Formulaire de 1864, inchangé.</em></span></div>
<div class="dp-marche"><span class="dp-marche-num">⊢ 1886</span><span><strong>raccord sous tension</strong> — de l'unité des lois à la conscience première, entre les deux murs de 1854. <em>Esquisse, t. II.</em></span></div>
<div class="dp-marche"><span class="dp-marche-num">⊢ 1903</span><span><strong>choix — motivé</strong> — Force := Volonté, contre la branche nominale laissée ouverte. <em>Le Personnalisme.</em></span></div>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le bilan tient en une phrase</span>
<p>Neuf articulations maîtresses pour cinquante ans de système : <strong>trois déductions, deux définitions, une prémisse à découvert, un raccord, deux choix</strong> — et des deux choix, l'un est signé par l'auteur, l'autre argumenté par lui. Un philosophe qu'on vérifie n'est pas diminué : celui-ci a construit de telle sorte qu'on <em>puisse</em> le vérifier, et il a souligné lui-même le joint principal. C'est rare.</p>
</div>
</div>
</details>

<div class="dp-legende">
<p><strong>Comment lire cette page.</strong> Le <span style="font-family: var(--dp-serif); font-style: italic;">sérif</span> cite Renouvier mot pour mot ; la linéale — y compris chaque formule — est notre commentaire. Le trait sous un joint dit sa nature : plein, déduit ; pointillé, défini ; tirets, supposé ; double, choisi ; ondulé, raccordé sous tension.</p>
<p><strong>Ce que la forme peut, et ce qu'elle ne peut pas.</strong> Une formalisation teste la <em>validité</em> : si les prémisses, alors la conclusion. Elle ne teste ni la vérité des prémisses, ni la justesse des définitions — elle les met à nu, c'est tout son office, et c'est déjà beaucoup : trois des grandes querelles autour de ce système (Cantor, la force, la substance) se révèlent être des querelles de :=, pas de théorèmes.</p>
<p><strong>Le vertige, pour finir.</strong> Dans ce système, la certitude est une clef de voûte, pas une première pierre — « le principe de ces principes est la liberté ». Chaque ⊢ de cette page, du moment qu'on l'<em>affirme</em>, repose donc sur ⊢₆. L'audit lui-même est un acte. Renouvier n'aurait pas voulu qu'il en fût autrement.</p>
<p><strong>Sources.</strong> Œuvres de Charles Renouvier, disponibles sur ce site. Les symboles (σ, Ω, ⊢ et le reste) sont de nous.</p>
<p><strong>Ce qui manque encore — et c'est une invitation.</strong> Descendre d'un étage : formaliser chaque catégorie avec ses Observations, mettre en forme le calcul des probabilités du chapitre XIII, et donner sa page à la contestation — chaque statut de l'audit est discutable, et la page est construite pour qu'on puisse la prendre en défaut. « Je les propose pour être vérifiées » : nous aussi.</p>
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

(function () {
  var racine = document.getElementById('dp');
  if (!racine) return;
  racine.addEventListener('click', function (e) {
    var jeton = e.target.closest('[data-lg]');
    if (!jeton || !racine.contains(jeton)) return;
    var source = document.getElementById('lg-' + jeton.getAttribute('data-lg'));
    var bloc = jeton.closest('.lg-bloc');
    var sortie = bloc ? bloc.querySelector('.lg-console') : null;
    if (!source || !sortie) return;
    sortie.innerHTML = source.innerHTML;
    sortie.classList.add('lg-ouverte');
    var actifs = bloc.querySelectorAll('.lg-actif');
    for (var i = 0; i < actifs.length; i++) actifs[i].classList.remove('lg-actif');
    jeton.classList.add('lg-actif');
  });
})();
</script>
</div>
