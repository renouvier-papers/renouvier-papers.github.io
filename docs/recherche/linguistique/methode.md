---
title: "Méthode et reproductibilité"
description: "Données, règles, dictionnaires complets et programme intégral du dépouillement — tout ce qu'il faut pour refaire les chiffres."
---

# Méthode et reproductibilité

Les deux pages voisines — [Lexicométrie](/recherche/linguistique/lexicometrie/) et [Étiquetage morpho-syntaxique](/recherche/linguistique/etiquetage-morphosyntaxique/) — avancent des nombres. Un nombre qu'on ne peut pas refaire n'est pas un résultat : c'est une anecdote. Cette page contient donc tout ce qu'il faut pour refaire ceux-là : les données identifiées, chaque règle de préparation et de calcul énoncée, les dictionnaires de décision au complet, **le programme intégral**, et un mode d'emploi de vérification avec valeurs-témoins.

Rien ici n'est aléatoire, rien n'est appris : la chaîne est déterministe de bout en bout. Deux exécutions sur les mêmes fichiers donnent les mêmes nombres, à la machine près. Si vous trouvez un écart, c'est que l'une de nos deux copies du texte diffère — et cela aussi, le programme sait le détecter. **Rien ne disparaît quand vous ouvrez.**

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

<details class="dp-pli" data-rang="principe">
<summary class="dp-titre"><span class="dp-rang">le contrat</span><span class="dp-texte">Ce que « reproductible » veut dire ici</span></summary>
<div class="dp-corps">
<p>Quatre conditions, toutes remplies ou la page ne vaut rien :</p>
<p><strong>1. Données publiques.</strong> Le corpus est fait des transcriptions intégrales publiées sur ce site — pas d'un état privé du texte. Quiconque lit les mêmes pages part des mêmes octets.</p>
<p><strong>2. Règles énoncées.</strong> Chaque transformation — ce qu'on retire, ce qu'on recolle, comment on découpe les mots et les phrases, comment on calcule — est écrite en toutes lettres au pli suivant, et une seconde fois, sous forme exécutable, dans le programme.</p>
<p><strong>3. Programme publié.</strong> Le pli « Le programme, intégral » contient le code complet du dépouillement, sans dépendance cachée : Python 3, les bibliothèques de calcul numpy et scipy, rien d'autre. Pas de modèle statistique appris, pas de tirage aléatoire : la chaîne est déterministe.</p>
<p><strong>4. Résultats confrontables.</strong> Le programme imprime, dans l'ordre, tous les tableaux des deux pages voisines. Le dernier pli donne des valeurs-témoins pour une vérification en cinq minutes.</p>
<p>Une conséquence assumée : quand la consolidation du programme a déplacé un chiffre d'un dixième par rapport à un premier dépouillement de travail, ce sont <em>les pages</em> qui ont été corrigées, jamais le programme qui a été ajusté pour retrouver un nombre. Le code fait foi.</p>
</div>
</details>

<details class="dp-pli" data-rang="données">
<summary class="dp-titre"><span class="dp-rang">les octets de départ</span><span class="dp-texte">Les données, identifiées et contrôlées</span></summary>
<div class="dp-corps">
<p>Huit fichiers, quatre strates. Les effectifs de la dernière colonne sont ceux que le programme attend : il compare son propre décompte à ces valeurs et avertit si l'écart dépasse 0,5 % — le garde-fou qui détecte une copie divergente du texte.</p>
<table class="dp-tab">
<thead><tr><th>strate</th><th>volumes (transcriptions du site)</th><th>mots attendus</th></tr></thead>
<tbody>
<tr><td>1875</td><td>Premier Essai t. II et t. III · Deuxième Essai t. II et t. III (2ᵉ éd.)</td><td>376 259</td></tr>
<tr><td>1885-1886</td><td>Esquisse, t. I et t. II</td><td>399 690</td></tr>
<tr><td>1903</td><td>Le Personnalisme (avec l'Étude)</td><td>174 042</td></tr>
<tr><td class="dp-t92"><em>1892</em></td><td class="dp-t92">Troisième Essai, t. I (2ᵉ éd.)</td><td class="dp-t92">88 913</td></tr>
</tbody>
</table>
<p><strong>Ce qui est retiré</strong> avant tout comptage : l'en-tête technique de chaque fichier, la notice d'édition, le balisage des titres de chapitres, les marqueurs de pagination, les appels de note, les marques typographiques d'italique. <strong>Ce qui est gardé</strong> : tout le texte de Renouvier, préfaces, formulaires et citations d'autrui compris.</p>
<p><strong>Ce qui est recollé.</strong> Les transcriptions coupent des mots en trois circonstances, toutes réparées avant comptage :</p>
<table class="dp-tab">
<thead><tr><th>règle</th><th>motif</th><th>exemple</th><th>cas</th></tr></thead>
<tbody>
<tr><td>a</td><td>tiret devant un marqueur de page</td><td>« probable- [p. 71] ment »</td><td>215</td></tr>
<tr><td>b</td><td>tiret en fin de ligne</td><td>« déduc-⏎tions »</td><td>108</td></tr>
<tr><td>c</td><td>marqueur de page enclavé dans le mot</td><td>« mouve[p. 218]ment »</td><td>506</td></tr>
</tbody>
</table>
<p>La règle c est de loin la plus fréquente — et la plus sournoise : sans elle, 506 mots deviendraient 1 012 fragments, dont des dizaines de faux « ment » isolés. C'est le genre de défaut qu'on ne soupçonne qu'en inspectant ses propres résidus : nous l'avons trouvé parce qu'un premier comptage donnait 49 occurrences du « mot » <em>ment</em>.</p>
</div>
</details>

<details class="dp-pli" data-rang="règles">
<summary class="dp-titre"><span class="dp-rang">la chaîne</span><span class="dp-texte">Les règles, une à une</span></summary>
<div class="dp-corps">
<p><strong>Découpage en mots.</strong> Un mot est une suite de lettres, traits d'union internes compris (<em>peut-être</em>, <em>c'est-à-dire</em> restent entiers), apostrophe finale comprise pour les élisions. Trois normalisations d'époque : les élisions sont détachées (<em>l'espace</em> → <em>l'</em> + <em>espace</em>) ; le trait d'union du XIXᵉ siècle après <em>très-</em> est dénoué (<em>très-grand</em> → <em>très grand</em>) ; les inversions verbe-pronom sont rendues à leurs mots (<em>est-il</em> → <em>est</em> + <em>il</em>, <em>a-t-on</em> → <em>a</em> + <em>on</em>) — sans quoi tout pronom inversé échapperait au comptage des personnes. Tous les comptages se font en minuscules.</p>
<p><strong>Découpage en phrases.</strong> Coupe après point, point d'interrogation, point d'exclamation ou points de suspension suivis d'une majuscule ou d'un guillemet ouvrant — après avoir protégé une liste close d'abréviations (M., MM., Mme, Mlle, St, etc., ch., liv., art., sect., vol., t., p., pp., fig., no, cf., ibid., op., cit., trad., éd., Voy., les initiales isolées et le signe §). Seules comptent les phrases d'au moins dix lettres. Les erreurs résiduelles de ce découpage pèsent également sur les quatre strates : elles n'affectent pas les écarts entre elles, qui seuls sont interprétés.</p>
<p><strong>Fréquences.</strong> Toujours rapportées pour 10 000 mots de la strate. Les regroupements (<em>force(s)</em>, <em>je, j'</em>) sont indiqués sur la ligne même du tableau qui les utilise — il n'y a pas de lemmatisation cachée.</p>
<p><strong>Richesse lexicale.</strong> Nombre de mots différents par tranches consécutives de 10 000 mots, moyenné sur les tranches — seule façon de comparer des livres de tailles différentes, la richesse brute croissant mécaniquement avec la taille.</p>
<p><strong>Spécificités.</strong> Méthode hypergéométrique de Lafon (1980). Pour un mot de fréquence totale K dans la réunion des trois strates (N mots), et de fréquence k dans une strate de taille n : si le mot y est sur-représenté, on calcule la probabilité d'observer <em>au moins</em> k occurrences en tirant n mots sans remise parmi N ; s'il y est sous-représenté, la probabilité d'en observer <em>au plus</em> k. L'indice publié est S = ±log₁₀ de cette probabilité (positif : sur-représentation). Seuil de calcul : K ≥ 20 ; seuil d'affichage : |S| ≥ 8 pour les palmarès. La strate de contrôle de 1892 n'entre ni dans N ni dans aucun calcul de spécificité.</p>
<p><strong>Étiquetage.</strong> Trois voies, dans cet ordre : classes fermées (listes exhaustives du pli suivant), désinences verbales sûres avec dictionnaires d'exceptions, formes en <em>-ment</em> par règles suffixales et listes. Toute forme non couverte reste sans étiquette ; le taux de couverture est publié (58-59 % selon la strate) ainsi que le résidu.</p>
<p><strong>Delta de Burrows.</strong> Chaque strate est découpée en segments consécutifs de 20 000 mots (18 segments pour 1875, 19 pour 1886, 8 pour 1903, 4 pour 1892). On mesure la fréquence, dans chaque segment, des 120 mots-outils les plus fréquents du corpus commun ; chaque mot-outil est centré-réduit sur l'ensemble des segments ; la distance entre deux segments est la moyenne des écarts absolus. La datation d'un segment de 1892 est la strate dont le profil moyen lui est le plus proche. La liste exacte des 120 mots-outils est imprimée par le programme à chaque exécution — elle est dérivée du corpus, pas choisie à la main.</p>
</div>
</details>

<details class="dp-pli" data-rang="dictionnaires">
<summary class="dp-titre"><span class="dp-rang">les décisions</span><span class="dp-texte">Les dictionnaires, complets par construction</span></summary>
<div class="dp-corps">
<p>Le principe : aucune décision de classement n'existe hors du programme. Les listes qu'on lit dans le code du pli suivant ne sont pas des extraits de quelque chose de plus grand — elles <em>sont</em> la totalité des décisions. En voici l'inventaire :</p>
<table class="dp-tab">
<thead><tr><th>ensemble</th><th>rôle</th><th>formes</th></tr></thead>
<tbody>
<tr><td>EXCL_AIT</td><td>faux imparfaits écartés (<em>fait, sait, parfait…</em>)</td><td>33</td></tr>
<tr><td>IMP_RAIT</td><td>imparfaits des verbes en <em>-rer</em> (<em>considérait, durait…</em>)</td><td>69</td></tr>
<tr><td>COND_X</td><td>conditionnels hors règle <em>-erait</em> (<em>serait, faudrait…</em>)</td><td>128</td></tr>
<tr><td>PS_OK</td><td>passés simples irréguliers (<em>furent, prirent…</em>)</td><td>51</td></tr>
<tr><td>PRES_ERENT</td><td>présents en <em>-èrent</em> et voisins écartés (<em>diffèrent…</em>)</td><td>41</td></tr>
<tr><td>EXCL_FUT / FUT_IRREG</td><td>faux futurs écartés / futurs irréguliers admis</td><td>24 / 84</td></tr>
<tr><td>NOM_MENT / V_MENT / ADV_X</td><td>noms, verbes, adverbes en <em>-ment</em> tranchés un à un</td><td>132 / 30 / 48</td></tr>
<tr><td>FERMEES</td><td>classes grammaticales fermées (couverture, mots-outils)</td><td>178</td></tr>
</tbody>
</table>
<p>Deux règles générales complètent ces listes, parce qu'elles sont sûres sans exception rencontrée dans ce corpus : une forme en <em>-erait</em> est un conditionnel, une forme en <em>-érait</em> un imparfait (<em>considérerait</em> / <em>considérait</em> : un seul <em>e</em> les sépare) ; et les terminaisons adverbiales productives (<em>-quement</em>, <em>-ellement</em>, <em>-amment</em>, <em>-ivement</em>…) classent d'office. Chaque forme qui échappe aux règles et aux listes reste sans étiquette et grossit le résidu publié — 918 occurrences en <em>-ment</em>, soit 0,088 % du corpus. Qui veut contester un classement n'a qu'un mot à chercher dans le code : la décision y est, nominative.</p>
</div>
</details>

<details class="dp-pli" data-rang="programme">
<summary class="dp-titre"><span class="dp-rang">le juge de paix</span><span class="dp-texte">Le programme, intégral</span></summary>
<div class="dp-corps">
<p>Voici le programme complet — celui-là même qui a produit chaque nombre des deux pages voisines. Dépendances : Python 3, numpy, scipy. Adapter la variable <code>DOSSIER</code> et, si besoin, les noms de fichiers du dictionnaire <code>FICHIERS</code> aux chemins locaux des transcriptions ; l'exécution prend quelques dizaines de secondes et imprime tous les tableaux, dans l'ordre des pages.</p>
<p class="dp-note"><strong>Télécharger le fichier :</strong> <a href="/recherche/linguistique/depouillement.py" download><code>depouillement.py</code></a> — servi tel quel, identique octet pour octet au code reproduit ci-dessous. Le télécharger plutôt que le copier évite toute altération à la transcription.</p>
<pre style="font-size:.72em; line-height:1.5; overflow-x:auto;"><code>#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Dépouillement lexicométrique et morpho-syntaxique du corpus Renouvier
# — programme source des pages « Lexicométrie » et « Étiquetage
#   morpho-syntaxique » de renouvier-papers.github.io.
#
# Dépendances : Python 3, numpy, scipy. Aucun aléa, aucun modèle appris :
# deux exécutions sur les mêmes fichiers donnent les mêmes nombres.
#
# Données : les transcriptions intégrales publiées sur le site. Adapter
# DOSSIER et FICHIERS aux chemins locaux ; les volumes s&#x27;identifient par
# leur notice de tête. Le programme vérifie les effectifs attendus et
# avertit si les fichiers diffèrent de ceux du dépouillement d&#x27;origine.
# ============================================================================
import re, math, statistics, itertools
from collections import Counter
import numpy as np
from scipy.stats import hypergeom

DOSSIER = &quot;/mnt/project&quot;
FICHIERS = {   # strate -&gt; liste de fichiers (transcriptions du site)
    &quot;1875&quot;: [&quot;essai-1-tome-2.md&quot;, &quot;essai-1-tome-3.md&quot;,
             &quot;essai-2-tome-2.md&quot;, &quot;essai-2-tome-3.md&quot;],
    &quot;1886&quot;: [&quot;esquisse-tome-1&quot;, &quot;esquisse-tome-2&quot;],
    &quot;1903&quot;: [&quot;personnalisme.md&quot;],
    &quot;1892&quot;: [&quot;essai-3-tome-1.md&quot;],          # point de contrôle
}
ORDRE = [&quot;1875&quot;, &quot;1886&quot;, &quot;1903&quot;, &quot;1892&quot;]
TOKENS_ATTENDUS = {&quot;1875&quot;: 376259, &quot;1886&quot;: 399690, &quot;1903&quot;: 174042, &quot;1892&quot;: 88913}

# ----------------------------------------------------------------------------
# 1. NETTOYAGE — ce qui est retiré, ce qui est recollé
# ----------------------------------------------------------------------------
def nettoie(t):
    t = re.sub(r&#x27;^---\n.*?\n---\n&#x27;, &#x27;&#x27;, t, flags=re.S)      # en-tête du fichier
    t = re.sub(r&#x27;^&gt;.*$&#x27;, &#x27;&#x27;, t, flags=re.M)                 # notice d&#x27;édition
    t = re.sub(r&#x27;^#{1,6} .*$&#x27;, &#x27;&#x27;, t, flags=re.M)           # balisage des titres
    # recollage des mots coupés :
    #   a) tiret + marqueur de page :   « probable- [p. 71] ment »
    t = re.sub(r&#x27;([A-Za-zà-ÿ])-\s*\[p\.\s*[^\]]{1,14}\]\s*([a-zà-ÿ])&#x27;, r&#x27;\1\2&#x27;, t)
    #   b) tiret + fin de ligne :       « déduc-\ntions »
    t = re.sub(r&#x27;([A-Za-zà-ÿ])-\n\s*([a-zà-ÿ])&#x27;, r&#x27;\1\2&#x27;, t)
    #   c) marqueur de page enclavé :   « mouve[p. 218]ment »
    t = re.sub(r&#x27;([a-zà-ÿ])\[p\.\s*[^\]]{1,14}\]([a-zà-ÿ])&#x27;, r&#x27;\1\2&#x27;, t)
    t = re.sub(r&#x27;\[p\.\s*[^\]]{1,14}\]&#x27;, &#x27; &#x27;, t)            # marqueurs de page
    t = re.sub(r&#x27;\[\^?[0-9]{1,3}\]&#x27;, &#x27; &#x27;, t)                # appels de note
    t = t.replace(&#x27;*&#x27;, &#x27;&#x27;).replace(&#x27;_&#x27;, &#x27;&#x27;)                 # marques d&#x27;italique
    t = re.sub(r&#x27;^\s*-{3,}\s*$&#x27;, &#x27; &#x27;, t, flags=re.M)        # filets
    return t

# ----------------------------------------------------------------------------
# 2. TOKENISATION — règles publiées telles quelles
# ----------------------------------------------------------------------------
ENCLITIQUES = r&quot;(?:je|tu|il|elle|on|nous|vous|ils|elles|ce|en|y|moi|toi|le|la|les|lui|leur)&quot;
def tokenise(t):
    t = t.replace(&#x27;\u2019&#x27;, &quot;&#x27;&quot;)                            # apostrophe courbe
    t = re.sub(r&#x27;\b([Tt]rès)-(?=[a-zà-ÿ])&#x27;, r&#x27;\1 &#x27;, t)      # très-grand -&gt; très grand
    t = re.sub(r&#x27;([a-zà-ÿ])-t-(&#x27; + ENCLITIQUES + r&#x27;)\b&#x27;, r&#x27;\1 \2&#x27;, t)  # a-t-on
    t = re.sub(r&#x27;([a-zà-ÿ])-(&#x27; + ENCLITIQUES + r&#x27;)\b&#x27;, r&#x27;\1 \2&#x27;, t)    # est-il
    # token = lettres, traits d&#x27;union internes, apostrophe finale d&#x27;élision
    return re.findall(r&quot;[A-Za-zÀ-ÿ]+(?:-[A-Za-zÀ-ÿ]+)*&#x27;?&quot;, t)

TXT, LOW = {}, {}
for s in ORDRE:
    brut = &quot;\n&quot;.join(open(f&quot;{DOSSIER}/{f}&quot;, encoding=&quot;utf-8&quot;, errors=&quot;replace&quot;).read()
                     for f in FICHIERS[s])
    TXT[s] = nettoie(brut)
    LOW[s] = [w.lower() for w in tokenise(TXT[s])]
C = {s: Counter(LOW[s]) for s in ORDRE}
N = {s: len(LOW[s]) for s in ORDRE}
for s in ORDRE:
    ecart = abs(N[s] - TOKENS_ATTENDUS[s]) / TOKENS_ATTENDUS[s]
    if ecart &gt; 0.005:
        print(f&quot;!! {s} : {N[s]} tokens, attendu ~{TOKENS_ATTENDUS[s]} — fichiers différents ?&quot;)

def f10k(s, *mots):
    return sum(C[s][m] for m in mots) / N[s] * 10000

def tab(titre, lignes, cols=ORDRE):
    print(&quot;\n== &quot; + titre + &quot; ==&quot;)
    for nom, vals in lignes:
        print(f&quot;  {nom:26s} &quot; + &quot; &quot;.join(f&quot;{v:8.1f}&quot; if isinstance(v, float) else f&quot;{v:&gt;8}&quot; for v in vals))

# ----------------------------------------------------------------------------
# 3. MESURES DE BASE (richesse par tranches de 10 000 mots)
# ----------------------------------------------------------------------------
print(&quot;== BASE ==&quot;)
for s in ORDRE:
    toks = LOW[s]
    tranches = [toks[i:i+10000] for i in range(0, N[s]-10000+1, 10000)]
    sttr = statistics.mean(len(set(tr))/10000 for tr in tranches)
    print(f&quot;  {s} : {N[s]:&gt;7} tokens · {len(set(toks)):&gt;6} types · STTR {sttr:.3f} · &quot;
          f&quot;lg. mot {sum(map(len,toks))/N[s]:.2f}&quot;)

# ----------------------------------------------------------------------------
# 4. PHRASES (abréviations protégées avant la coupe)
# ----------------------------------------------------------------------------
ABREV = (r&quot;(?:M|MM|Mme|Mlle|St|etc|ch|liv|art|sect|vol|t|p|pp|fig|no|n|cf|Ibid|ibid|&quot;
         r&quot;op|cit|trad|éd|Voy|V|C|J|A|B|D|E|F|G|H|I|K|L|N|O|P|Q|R|S|T|U|X|§)&quot;)
print(&quot;== PHRASES ==&quot;)
for s in ORDRE:
    t = re.sub(r&#x27;\b&#x27; + ABREV + r&#x27;\.&#x27;, lambda m: m.group(0).replace(&#x27;.&#x27;, &#x27;§&#x27;), TXT[s])
    t = re.sub(r&#x27;\s+&#x27;, &#x27; &#x27;, t)
    ph = [p for p in re.split(r&#x27;(?&lt;=[.!?…])\s+(?=[«&quot;A-ZÀ-Ý])&#x27;, t)
          if len(re.findall(r&quot;[A-Za-zÀ-ÿ]&quot;, p)) &gt;= 10]
    lg = [len(tokenise(p)) for p in ph]
    print(f&quot;  {s} : {len(ph):&gt;5} phrases · moyenne {statistics.mean(lg):.1f} · &quot;
          f&quot;médiane {statistics.median(lg):.0f}&quot;)

# ----------------------------------------------------------------------------
# 5. SPÉCIFICITÉS (Lafon ; hypergéométrique ; S = ±log10 p ; seuil K &gt;= 20)
#    Strates 1875, 1886, 1903 seulement — 1892 n&#x27;entre dans aucun calcul.
# ----------------------------------------------------------------------------
TROIS = [&quot;1875&quot;, &quot;1886&quot;, &quot;1903&quot;]
Ntot = sum(N[s] for s in TROIS)
Ftot = Counter()
for s in TROIS:
    Ftot.update(C[s])
SPEC = {}
for s in TROIS:
    d = {}
    for w, K in Ftot.items():
        if K &lt; 20:
            continue
        k = C[s][w]
        p_sur = hypergeom.sf(k-1, Ntot, K, N[s])
        p_sous = hypergeom.cdf(k, Ntot, K, N[s])
        d[w] = (-math.log10(max(p_sur, 1e-300)) if p_sur &lt; p_sous
                else math.log10(max(p_sous, 1e-300)))
    SPEC[s] = d
STOP = set((&quot;de la le les l&#x27; un une des du au aux et ou mais or ni car donc à en dans par &quot;
    &quot;pour sur avec sans sous chez entre vers contre selon que qu&#x27; qui quoi dont où si comme &quot;
    &quot;quand est sont était été être a ont avait avoir il elle on nous vous ils elles je tu ce &quot;
    &quot;cette ces cet se ne n&#x27; pas point plus moins très bien tout toute tous toutes d&#x27; s&#x27; c&#x27; j&#x27; &quot;
    &quot;m&#x27; t&#x27; y ainsi aussi même mêmes autre autres leur leurs son sa ses mon ma mes notre nos &quot;
    &quot;votre vos peut peuvent fait faire deux trois premier première second seconde là ici &quot;
    &quot;encore déjà toujours jamais rien quelque quelques chose choses celui celle ceux celles &quot;
    &quot;lui eux soi cela ça alors puis enfin cependant néanmoins toutefois pourtant après avant &quot;
    &quot;depuis pendant lorsque puisque quoique afin parce&quot;).split())
print(&quot;== SPÉCIFICITÉS (mots pleins, S &gt;= 8) ==&quot;)
for s in TROIS:
    sur = sorted(((v, w) for w, v in SPEC[s].items() if v &gt;= 8 and w not in STOP),
                 reverse=True)[:22]
    print(f&quot;  ++{s} : &quot; + &quot; · &quot;.join(f&quot;{w}({v:.0f})&quot; for v, w in sur))

# ----------------------------------------------------------------------------
# 6. TRAJECTOIRES /10 000 mots (regroupements indiqués sur la ligne)
# ----------------------------------------------------------------------------
GROUPES = {
  &quot;catégorie(s)&quot;: (&quot;catégorie&quot;, &quot;catégories&quot;), &quot;représentation(s)&quot;: (&quot;représentation&quot;, &quot;représentations&quot;),
  &quot;fonction(s)&quot;: (&quot;fonction&quot;, &quot;fonctions&quot;), &quot;science(s)&quot;: (&quot;science&quot;, &quot;sciences&quot;),
  &quot;vérité(s)&quot;: (&quot;vérité&quot;, &quot;vérités&quot;), &quot;certitude&quot;: (&quot;certitude&quot;,),
  &quot;dieu&quot;: (&quot;dieu&quot;,), &quot;création&quot;: (&quot;création&quot;,), &quot;créateur&quot;: (&quot;créateur&quot;,),
  &quot;péché&quot;: (&quot;péché&quot;,), &quot;mal&quot;: (&quot;mal&quot;,),
  &quot;corps&quot;: (&quot;corps&quot;,), &quot;force(s)&quot;: (&quot;force&quot;, &quot;forces&quot;), &quot;matière&quot;: (&quot;matière&quot;,),
  &quot;monade(s)&quot;: (&quot;monade&quot;, &quot;monades&quot;),
  &quot;liberté&quot;: (&quot;liberté&quot;,), &quot;volonté(s)&quot;: (&quot;volonté&quot;, &quot;volontés&quot;),
  &quot;croyance(s)&quot;: (&quot;croyance&quot;, &quot;croyances&quot;), &quot;infini*&quot;: (&quot;infini&quot;, &quot;infinie&quot;, &quot;infinis&quot;, &quot;infinies&quot;),
  &quot;nécessité&quot;: (&quot;nécessité&quot;,), &quot;conscience(s)&quot;: (&quot;conscience&quot;, &quot;consciences&quot;),
  &quot;personne(s)&quot;: (&quot;personne&quot;, &quot;personnes&quot;), &quot;personnalisme&quot;: (&quot;personnalisme&quot;,),
}
tab(&quot;TRAJECTOIRES /10k  (1875 1886 1903 1892)&quot;,
    [(nom, [f10k(s, *mots) for s in ORDRE]) for nom, mots in GROUPES.items()])

# ----------------------------------------------------------------------------
# 7. GRAMMAIRE : personnes, négation, connecteurs, ponctuation
# ----------------------------------------------------------------------------
tab(&quot;PERSONNES /10k&quot;, [
    (&quot;je, j&#x27;&quot;, [f10k(s, &quot;je&quot;, &quot;j&#x27;&quot;) for s in ORDRE]),
    (&quot;me, m&#x27;, moi&quot;, [f10k(s, &quot;me&quot;, &quot;m&#x27;&quot;, &quot;moi&quot;) for s in ORDRE]),
    (&quot;nous&quot;, [f10k(s, &quot;nous&quot;) for s in ORDRE]),
    (&quot;on&quot;, [f10k(s, &quot;on&quot;) for s in ORDRE]),
    (&quot;il, ils&quot;, [f10k(s, &quot;il&quot;, &quot;ils&quot;) for s in ORDRE]),
])
print(&quot;\n== NÉGATION (forme dans les 5 mots après ne/n&#x27;) ==&quot;)
for s in ORDRE:
    toks = LOW[s]; d = Counter()
    for i, w in enumerate(toks):
        if w in (&quot;ne&quot;, &quot;n&#x27;&quot;):
            for fme in (&quot;pas&quot;, &quot;point&quot;, &quot;plus&quot;, &quot;jamais&quot;, &quot;rien&quot;):
                if fme in toks[i+1:i+6]:
                    d[fme] += 1
                    break
    tot = d[&quot;pas&quot;] + d[&quot;point&quot;]
    print(f&quot;  {s} : pas {d[&#x27;pas&#x27;]} · point {d[&#x27;point&#x27;]} ({d[&#x27;point&#x27;]/tot*100:.1f} %) · &quot;
          f&quot;ne/10k {sum(1 for w in toks if w in (&#x27;ne&#x27;,chr(110)+chr(39)))/N[s]*10000:.0f}&quot;)
BIG = {s: Counter(zip(LOW[s], LOW[s][1:])) for s in ORDRE}
def conn(s, *unites):
    n = 0
    for u in unites:
        n += BIG[s][tuple(u.split())] if &quot; &quot; in u else C[s][u]
    return n / N[s] * 10000
CONNECTEURS = {&quot;donc&quot;: (&quot;donc&quot;,), &quot;or&quot;: (&quot;or&quot;,), &quot;car&quot;: (&quot;car&quot;,), &quot;mais&quot;: (&quot;mais&quot;,),
    &quot;si&quot;: (&quot;si&quot;,), &quot;ainsi&quot;: (&quot;ainsi&quot;,), &quot;cependant&quot;: (&quot;cependant&quot;,),
    &quot;pourtant&quot;: (&quot;pourtant&quot;,), &quot;parce que&quot;: (&quot;parce que&quot;,),
    &quot;en effet&quot;: (&quot;en effet&quot;,), &quot;au contraire&quot;: (&quot;au contraire&quot;,),
    &quot;lorsque&quot;: (&quot;lorsque&quot;, &quot;lorsqu&#x27;&quot;), &quot;c&#x27;est-à-dire&quot;: (&quot;c&#x27; est-à-dire&quot;,),
    &quot;d&#x27;ailleurs&quot;: (&quot;d&#x27; ailleurs&quot;,)}
tab(&quot;CONNECTEURS /10k&quot;, [(nom, [conn(s, *u) for s in ORDRE]) for nom, u in CONNECTEURS.items()])
print(&quot;\n== PONCTUATION /10k ==&quot;)
for s in ORDRE:
    print(f&quot;  {s} :  ? {TXT[s].count(&#x27;?&#x27;)/N[s]*10000:5.1f}   ! {TXT[s].count(&#x27;!&#x27;)/N[s]*10000:4.1f}   &quot;
          f&quot;; {TXT[s].count(&#x27;;&#x27;)/N[s]*10000:5.1f}   : {TXT[s].count(&#x27;:&#x27;)/N[s]*10000:5.1f}&quot;)

# ----------------------------------------------------------------------------
# 8. ÉTIQUETAGE — dictionnaires de décision COMPLETS
# ----------------------------------------------------------------------------
EXCL_AIT = set(&quot;&quot;&quot;fait ait sait aient parfait satisfait imparfait bienfait forfait méfait
  souhait souhaits lait attrait attraits trait traits portrait portraits extrait extraits
  abstrait abstraits soustrait retrait retraits distrait plait parait surfait refait
  contrefait stupéfait&quot;&quot;&quot;.split())
IMP_RAIT = set(&quot;&quot;&quot;considérait opérait espérait désespérait exagérait tolérait libérait
  générait conférait déférait préférait différait persévérait coopérait adhérait révérait
  vénérait altérait désirait admirait tirait attirait retirait inspirait respirait
  soupirait expirait aspirait empirait virait déchirait durait figurait mesurait assurait
  murmurait procurait jurait demeurait éclairait comparait déclarait ignorait séparait
  préparait montrait entrait rencontrait pénétrait montraient entraient considéraient
  duraient figuraient demeuraient déclaraient ignoraient tiraient attiraient désiraient
  admiraient offrait offraient découvrait démontrait souffrait ouvrait couvrait
  recouvrait&quot;&quot;&quot;.split())
COND_X = set(&quot;&quot;&quot;serait seraient aurait auraient pourrait pourraient saurait sauraient
  faudrait devrait devraient voudrait voudraient ferait feraient dirait diraient irait
  iraient verrait verraient viendrait viendraient tiendrait mettrait mettraient prendrait
  prendraient rendrait rendraient vaudrait vaudraient croirait croiraient suffirait
  suffiraient agirait finirait choisirait servirait sortirait partirait ouvrirait
  offrirait réussirait jouirait subirait unirait fournirait établirait établiraient
  conviendrait deviendrait deviendraient connaîtrait connaîtraient paraîtrait
  apparaîtrait disparaîtrait mourrait courrait sentirait consentirait appartiendrait
  obtiendrait soutiendrait contiendrait maintiendrait comprendrait apprendrait
  reprendrait entreprendrait attendrait entendrait perdrait répondrait correspondrait
  suivrait vivrait écrirait produirait conduirait réduirait introduirait construirait
  détruirait traduirait plairait déplairait permettrait concevrait reviendrait
  produiraient parviendrait évanouirait tendrait permettraient admettrait démentirait
  étendrait conduiraient tiendraient serviraient prétendrait conclurait paraîtraient
  appartiendraient suivraient soumettrait résoudrait déduirait dépendrait naîtraient
  obéirait reconnaîtraient reconnaîtrait aboutiraient introduiraient régirait ensuivrait
  correspondraient équivaudrait définirait découvrirait défendrait descendrait
  admettraient concluraient&quot;&quot;&quot;.split())
PS_OK = set(&quot;&quot;&quot;furent firent eurent purent durent vinrent tinrent prirent mirent virent
  dirent surent voulurent connurent parurent reçurent crurent devinrent obtinrent
  naquirent moururent vécurent suivirent servirent sentirent partirent sortirent
  ouvrirent offrirent réussirent choisirent finirent établirent réunirent définirent
  produisirent conduisirent introduisirent construisirent détruisirent écrivirent
  comprirent apprirent reprirent entreprirent attendirent entendirent répondirent
  perdirent rendirent descendirent&quot;&quot;&quot;.split())
PRES_ERENT = set(&quot;&quot;&quot;diffèrent demeurent tirent figurent suggèrent opèrent concourent
  altèrent meurent attirent acquièrent mesurent éclairent considèrent préfèrent espèrent
  tolèrent libèrent exagèrent digèrent insèrent coopèrent adhèrent révèrent vénèrent
  réfèrent confèrent transfèrent persévèrent désespèrent gèrent cèdent secourent courent
  parcourent discourent recourent conquièrent requièrent assurent réclament&quot;&quot;&quot;.split())
EXCL_FUT = set(&quot;&quot;&quot;vrai vrais barbara considérons ignorons comparons préparons désirons
  admirons honorons mesurons assurons demeurons figurons tirons montrons rencontrons
  entrons opérons espérons déclarons séparons adorons restaurons&quot;&quot;&quot;.split())
FUT_IRREG = set(&quot;&quot;&quot;sera seront serai serons serez aura auront aurai aurons aurez pourra
  pourront pourrai pourrons ira iront irai irons fera feront ferai ferons ferez devra
  devront devrai devrons dira diront dirai dirons direz faudra vaudra voudra voudront
  viendra viendront tiendra tiendront verra verront verrai verrons saura sauront saurai
  saurons mettra mettront prendra prendront rendra rendront comprendra apprendra
  deviendra deviendront conviendra connaîtra connaîtront paraîtra apparaîtra recevra
  recevront croira croiront vivra vivront suivra suivront écrira écriront répondra
  attendra entendra perdra perdront enverra enverrons offriront souffriront ouvriront
  découvriront&quot;&quot;&quot;.split())
def cl_verbe(w):
    &quot;&quot;&quot;Étiquette IMP / COND / FUT / PS, ou None (forme laissée sans étiquette).&quot;&quot;&quot;
    if w in EXCL_AIT or w in PRES_ERENT:
        return None
    if w.endswith((&quot;erait&quot;, &quot;eraient&quot;)):     # trouver+ait : conditionnel sûr
        return &quot;COND&quot;
    if w.endswith((&quot;érait&quot;, &quot;éraient&quot;)):     # considér+ait : imparfait sûr
        return &quot;IMP&quot;
    if w in COND_X:
        return &quot;COND&quot;
    if w in IMP_RAIT:
        return &quot;IMP&quot;
    if w.endswith((&quot;ait&quot;, &quot;aient&quot;)) and not w.endswith((&quot;rait&quot;, &quot;raient&quot;)):
        return &quot;IMP&quot;
    if w in PS_OK or w.endswith(&quot;èrent&quot;):
        return &quot;PS&quot;
    if w in FUT_IRREG:
        return &quot;FUT&quot;
    if w not in EXCL_FUT and re.search(r&quot;(erai|eras|era|erons|erez|eront)$&quot;, w):
        return &quot;FUT&quot;
    return None
NOM_MENT = set(&quot;&quot;&quot;mouvement sentiment comment développement moment jugement fondement
  entendement commencement changement raisonnement établissement argument élément
  enchaînement événement rapprochement consentement enseignement gouvernement
  département comportement instrument monument document testament tempérament firmament
  ornement fragment segment complément supplément appartement traitement vêtement
  châtiment compartiment aliment ciment sacrement serment ferment tourment régiment
  sédiment rudiment empêchement éclaircissement dévouement déroulement arrangement
  enveloppement perfectionnement affranchissement avancement détriment rayonnement
  recueillement accomplissement accroissement affaiblissement agrandissement amendement
  acharnement anéantissement apaisement assentiment assujettissement attachement
  balancement bouleversement classement commandement dédommagement dénombrement
  dénouement déplacement dérangement détachement discernement écartement écoulement
  effacement égarement élancement éloignement emportement encouragement engagement
  enlèvement entraînement envahissement épanouissement étonnement évanouissement
  excrément fonctionnement froissement gémissement groupement isolement jaillissement
  licenciement ligament mécontentement ménagement morcellement pansement parlement
  payement pressentiment prolongement raffinement ralentissement rassemblement
  rattachement redoublement refroidissement relâchement remaniement renoncement
  renouvellement renversement retentissement retranchement revirement roulement
  soulèvement tremblement tâtonnement vieillissement&quot;&quot;&quot;.split())
V_MENT = set(&quot;&quot;&quot;forment ment mentent aiment arment calment charment confirment déforment
  dorment enferment estiment expriment ferment germent impriment infirment informent
  priment réforment renferment réaffirment suppriment transforment affirment animent
  réclament proclament acclament déclament&quot;&quot;&quot;.split())
ADV_X = set(&quot;&quot;&quot;seulement autrement simplement proprement absolument vraiment
  immédiatement certainement indéfiniment nullement infiniment nettement réciproquement
  non-seulement justement complètement complétement librement fortement pratiquement
  facilement pleinement difficilement légitimement diversement manifestement vainement
  rarement extrêmement franchement uniquement hardiment indissolublement brièvement
  parallèlement naïvement longuement rapidement pareillement ouvertement secondement
  résolument grandement fermement premièrement deuxièmement troisièmement
  dernièrement&quot;&quot;&quot;.split())
def cl_ment(w):
    &quot;&quot;&quot;Étiquette ADV / NOM / V pour les formes en -ment, ou None (résidu compté).&quot;&quot;&quot;
    if not w.endswith(&quot;ment&quot;) or len(w) &lt; 5:
        return None
    if w in V_MENT:
        return &quot;V&quot;
    if w in NOM_MENT:
        return &quot;NOM&quot;
    if w in ADV_X or w.endswith((&quot;amment&quot;, &quot;emment&quot;, &quot;quement&quot;, &quot;ellement&quot;, &quot;alement&quot;,
        &quot;iblement&quot;, &quot;ablement&quot;, &quot;ivement&quot;, &quot;eusement&quot;, &quot;airement&quot;, &quot;èrement&quot;,
        &quot;ièrement&quot;, &quot;ûrement&quot;, &quot;itement&quot;, &quot;ctement&quot;, &quot;ément&quot;)):
        return &quot;ADV&quot;
    return &quot;RESIDU&quot;
print(&quot;\n== TEMPS/MODES /10k (IMP COND FUT PS) et -MENT /10k (ADV NOM) ==&quot;)
residu_ment = 0
for s in ORDRE:
    dv, dm = Counter(), Counter()
    for w in LOW[s]:
        e = cl_verbe(w)
        if e:
            dv[e] += 1
        m = cl_ment(w)
        if m == &quot;RESIDU&quot;:
            residu_ment += 1
        elif m:
            dm[m] += 1
    print(f&quot;  {s} : IMP {dv[&#x27;IMP&#x27;]/N[s]*1e4:5.1f}  COND {dv[&#x27;COND&#x27;]/N[s]*1e4:5.1f}  &quot;
          f&quot;FUT {dv[&#x27;FUT&#x27;]/N[s]*1e4:5.1f}  PS {dv[&#x27;PS&#x27;]/N[s]*1e4:4.1f}   |   &quot;
          f&quot;ADV {dm[&#x27;ADV&#x27;]/N[s]*1e4:6.1f}  NOM {dm[&#x27;NOM&#x27;]/N[s]*1e4:5.1f}&quot;)
print(f&quot;  résidu -ment non classé : {residu_ment} occ. &quot;
      f&quot;({residu_ment/sum(N.values())*100:.3f} % des tokens)&quot;)

# ----------------------------------------------------------------------------
# 9. COUVERTURE + DELTA DE BURROWS + DATATION DE 1892
# ----------------------------------------------------------------------------
FERMEES = set(&quot;&quot;&quot;le la les l&#x27; un une des du au aux ce cet cette ces mon ma mes ton ta tes
  son sa ses notre nos votre vos leur leurs quel quelle quels quelles chaque plusieurs
  quelques aucun aucune nul nulle tout toute tous toutes je tu il elle on nous vous ils
  elles me m&#x27; te t&#x27; se s&#x27; moi toi soi lui eux y en de d&#x27; à dans par pour sur avec sans
  sous chez entre vers contre selon malgré parmi envers hors dès depuis pendant durant
  devant derrière après avant jusque jusqu&#x27; outre et ou mais or ni car donc que qu&#x27; qui
  dont où si comme quand lorsque lorsqu&#x27; puisque puisqu&#x27; quoique quoiqu&#x27; ne n&#x27; pas point
  plus jamais rien guère est sont était étaient être été sera seront serait seraient
  soit soient fut furent a ont avait avaient avoir eu aura auront aurait auraient ait
  aient eut eurent c&#x27; j&#x27; très bien peu ainsi aussi encore déjà toujours alors puis enfin
  cependant néanmoins toutefois pourtant même mêmes autre autres tel telle tels
  telles&quot;&quot;&quot;.split())
print(&quot;\n== COUVERTURE (classes fermées + paradigmes + -ment classés) ==&quot;)
for s in ORDRE:
    n_ok = sum(1 for w in LOW[s]
               if w in FERMEES or cl_verbe(w) or cl_ment(w) in (&quot;ADV&quot;, &quot;NOM&quot;, &quot;V&quot;))
    print(f&quot;  {s} : {n_ok/N[s]*100:.1f} %&quot;)
Ctot = Counter()
for s in TROIS:
    Ctot.update(LOW[s])
MOTS_OUTILS = [w for w, _ in Ctot.most_common(400) if w in FERMEES][:120]
segments, etiquettes = [], []
for s in ORDRE:
    toks = LOW[s]
    for i in range(0, len(toks) - 20000 + 1, 20000):
        c = Counter(toks[i:i+20000])
        segments.append([c[w] / 20000 * 1000 for w in MOTS_OUTILS])
        etiquettes.append(s)
X = np.array(segments)
Z = (X - X.mean(0)) / (X.std(0) + 1e-9)
idx = {s: [i for i, l in enumerate(etiquettes) if l == s] for s in ORDRE}
def delta(a, b):
    return float(np.mean(np.abs(Z[a] - Z[b])))
print(&quot;\n== DELTA DE BURROWS (segments de 20 000 mots ; 120 mots-outils) ==&quot;)
print(&quot;  mots-outils :&quot;, &quot; &quot;.join(MOTS_OUTILS))
for s in TROIS:
    print(f&quot;  intra-{s} : &quot;
          f&quot;{statistics.mean(delta(a,b) for a,b in itertools.combinations(idx[s],2)):.3f}&quot;)
for s1, s2 in [(&quot;1875&quot;, &quot;1886&quot;), (&quot;1886&quot;, &quot;1903&quot;), (&quot;1875&quot;, &quot;1903&quot;)]:
    print(f&quot;  {s1} &lt;-&gt; {s2} : &quot;
          f&quot;{statistics.mean(delta(a,b) for a in idx[s1] for b in idx[s2]):.3f}&quot;)
centres = {s: Z[idx[s]].mean(0) for s in TROIS}
print(&quot;  -- datation des segments de 1892 --&quot;)
for k, i in enumerate(idx[&quot;1892&quot;]):
    d = {s: float(np.mean(np.abs(Z[i] - centres[s]))) for s in TROIS}
    print(f&quot;  1892-{k+1} : &quot; + &quot;  &quot;.join(f&quot;{s} {d[s]:.3f}&quot; for s in TROIS)
          + f&quot;  -&gt; {min(d, key=d.get)}&quot;)
</code></pre>
</div>
</details>

<details class="dp-pli" data-rang="vérifier">
<summary class="dp-titre"><span class="dp-rang">en cinq minutes</span><span class="dp-texte">Vérifier — mode d'emploi et valeurs-témoins</span></summary>
<div class="dp-corps">
<p><strong>1.</strong> Récupérer les huit transcriptions listées au pli « Les données » depuis ce site. <strong>2.</strong> Télécharger <a href="/recherche/linguistique/depouillement.py" download><code>depouillement.py</code></a> (ou copier le programme du pli précédent) ; régler <code>DOSSIER</code>. <strong>3.</strong> Exécuter : <code>python3 depouillement.py</code>. <strong>4.</strong> Confronter la sortie aux tableaux des deux pages — ou, plus vite, aux témoins ci-dessous, choisis pour couvrir toute la chaîne (préparation, lexique, grammaire, stylométrie) :</p>
<table class="dp-tab">
<thead><tr><th>témoin</th><th>valeur attendue</th></tr></thead>
<tbody>
<tr><td>mots de la strate 1875</td><td>376 259</td></tr>
<tr><td>longueur moyenne de phrase, 1885-1886</td><td>49,5 mots</td></tr>
<tr><td>spécificité de <em>corps</em> en 1903</td><td>S = 126</td></tr>
<tr><td><em>je, j'</em> pour 10 000 mots en 1903</td><td>5,4</td></tr>
<tr><td>part de <em>ne… point</em> en 1875</td><td>17,5 %</td></tr>
<tr><td>conditionnel pour 10 000 mots en 1875</td><td>50,5</td></tr>
<tr><td>Delta 1875 ↔ 1903</td><td>1,279</td></tr>
<tr><td>datation des 4 segments de 1892</td><td>1875 · 1875 · 1875 · 1886</td></tr>
</tbody>
</table>
<p>Un écart sur les mots de la strate signale des fichiers différents (le programme l'aura déjà dit) ; un écart ailleurs, à fichiers identiques, signale une erreur — la nôtre ou la vôtre — et mérite d'être signalé : c'est ainsi que ces pages s'amendent. Les limites de fond, elles, restent celles dites dans les deux pages : citations d'autrui comptées avec leur hôte, ambiguïtés assumées (<em>il</em> impersonnel, <em>que</em> non ventilé), couverture d'étiquetage de 59 % par choix de certitude. La reproductibilité ne rend pas ces choix indiscutables ; elle les rend discutables précisément — c'est toute la différence.</p>
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

**Sources.** Transcriptions intégrales de ce site (huit volumes, listés au pli « Les données »). Méthode des spécificités : P. Lafon, « Sur la variabilité de la fréquence des formes dans un corpus », *Mots*, 1, 1980. Delta : J. F. Burrows, « 'Delta' : a Measure of Stylistic Difference and a Guide to Likely Authorship », *Literary and Linguistic Computing*, 17, 2002.
