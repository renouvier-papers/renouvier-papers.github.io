#!/usr/bin/env python3
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
# DOSSIER et FICHIERS aux chemins locaux ; les volumes s'identifient par
# leur notice de tête. Le programme vérifie les effectifs attendus et
# avertit si les fichiers diffèrent de ceux du dépouillement d'origine.
# ============================================================================
import re, math, statistics, itertools
from collections import Counter
import numpy as np
from scipy.stats import hypergeom

DOSSIER = "/mnt/project"
FICHIERS = {   # strate -> liste de fichiers (transcriptions du site)
    "1875": ["essai-1-tome-2.md", "essai-1-tome-3.md",
             "essai-2-tome-2.md", "essai-2-tome-3.md"],
    "1886": ["esquisse-tome-1", "esquisse-tome-2"],
    "1903": ["personnalisme.md"],
    "1892": ["essai-3-tome-1.md"],          # point de contrôle
}
ORDRE = ["1875", "1886", "1903", "1892"]
TOKENS_ATTENDUS = {"1875": 376259, "1886": 399690, "1903": 174042, "1892": 88913}

# ----------------------------------------------------------------------------
# 1. NETTOYAGE — ce qui est retiré, ce qui est recollé
# ----------------------------------------------------------------------------
def nettoie(t):
    t = re.sub(r'^---\n.*?\n---\n', '', t, flags=re.S)      # en-tête du fichier
    t = re.sub(r'^>.*$', '', t, flags=re.M)                 # notice d'édition
    t = re.sub(r'^#{1,6} .*$', '', t, flags=re.M)           # balisage des titres
    # recollage des mots coupés :
    #   a) tiret + marqueur de page :   « probable- [p. 71] ment »
    t = re.sub(r'([A-Za-zà-ÿ])-\s*\[p\.\s*[^\]]{1,14}\]\s*([a-zà-ÿ])', r'\1\2', t)
    #   b) tiret + fin de ligne :       « déduc-\ntions »
    t = re.sub(r'([A-Za-zà-ÿ])-\n\s*([a-zà-ÿ])', r'\1\2', t)
    #   c) marqueur de page enclavé :   « mouve[p. 218]ment »
    t = re.sub(r'([a-zà-ÿ])\[p\.\s*[^\]]{1,14}\]([a-zà-ÿ])', r'\1\2', t)
    t = re.sub(r'\[p\.\s*[^\]]{1,14}\]', ' ', t)            # marqueurs de page
    t = re.sub(r'\[\^?[0-9]{1,3}\]', ' ', t)                # appels de note
    t = t.replace('*', '').replace('_', '')                 # marques d'italique
    t = re.sub(r'^\s*-{3,}\s*$', ' ', t, flags=re.M)        # filets
    return t

# ----------------------------------------------------------------------------
# 2. TOKENISATION — règles publiées telles quelles
# ----------------------------------------------------------------------------
ENCLITIQUES = r"(?:je|tu|il|elle|on|nous|vous|ils|elles|ce|en|y|moi|toi|le|la|les|lui|leur)"
def tokenise(t):
    t = t.replace('\u2019', "'")                            # apostrophe courbe
    t = re.sub(r'\b([Tt]rès)-(?=[a-zà-ÿ])', r'\1 ', t)      # très-grand -> très grand
    t = re.sub(r'([a-zà-ÿ])-t-(' + ENCLITIQUES + r')\b', r'\1 \2', t)  # a-t-on
    t = re.sub(r'([a-zà-ÿ])-(' + ENCLITIQUES + r')\b', r'\1 \2', t)    # est-il
    # token = lettres, traits d'union internes, apostrophe finale d'élision
    return re.findall(r"[A-Za-zÀ-ÿ]+(?:-[A-Za-zÀ-ÿ]+)*'?", t)

TXT, LOW = {}, {}
for s in ORDRE:
    brut = "\n".join(open(f"{DOSSIER}/{f}", encoding="utf-8", errors="replace").read()
                     for f in FICHIERS[s])
    TXT[s] = nettoie(brut)
    LOW[s] = [w.lower() for w in tokenise(TXT[s])]
C = {s: Counter(LOW[s]) for s in ORDRE}
N = {s: len(LOW[s]) for s in ORDRE}
for s in ORDRE:
    ecart = abs(N[s] - TOKENS_ATTENDUS[s]) / TOKENS_ATTENDUS[s]
    if ecart > 0.005:
        print(f"!! {s} : {N[s]} tokens, attendu ~{TOKENS_ATTENDUS[s]} — fichiers différents ?")

def f10k(s, *mots):
    return sum(C[s][m] for m in mots) / N[s] * 10000

def tab(titre, lignes, cols=ORDRE):
    print("\n== " + titre + " ==")
    for nom, vals in lignes:
        print(f"  {nom:26s} " + " ".join(f"{v:8.1f}" if isinstance(v, float) else f"{v:>8}" for v in vals))

# ----------------------------------------------------------------------------
# 3. MESURES DE BASE (richesse par tranches de 10 000 mots)
# ----------------------------------------------------------------------------
print("== BASE ==")
for s in ORDRE:
    toks = LOW[s]
    tranches = [toks[i:i+10000] for i in range(0, N[s]-10000+1, 10000)]
    sttr = statistics.mean(len(set(tr))/10000 for tr in tranches)
    print(f"  {s} : {N[s]:>7} tokens · {len(set(toks)):>6} types · STTR {sttr:.3f} · "
          f"lg. mot {sum(map(len,toks))/N[s]:.2f}")

# ----------------------------------------------------------------------------
# 4. PHRASES (abréviations protégées avant la coupe)
# ----------------------------------------------------------------------------
ABREV = (r"(?:M|MM|Mme|Mlle|St|etc|ch|liv|art|sect|vol|t|p|pp|fig|no|n|cf|Ibid|ibid|"
         r"op|cit|trad|éd|Voy|V|C|J|A|B|D|E|F|G|H|I|K|L|N|O|P|Q|R|S|T|U|X|§)")
print("== PHRASES ==")
for s in ORDRE:
    t = re.sub(r'\b' + ABREV + r'\.', lambda m: m.group(0).replace('.', '§'), TXT[s])
    t = re.sub(r'\s+', ' ', t)
    ph = [p for p in re.split(r'(?<=[.!?…])\s+(?=[«"A-ZÀ-Ý])', t)
          if len(re.findall(r"[A-Za-zÀ-ÿ]", p)) >= 10]
    lg = [len(tokenise(p)) for p in ph]
    print(f"  {s} : {len(ph):>5} phrases · moyenne {statistics.mean(lg):.1f} · "
          f"médiane {statistics.median(lg):.0f}")

# ----------------------------------------------------------------------------
# 5. SPÉCIFICITÉS (Lafon ; hypergéométrique ; S = ±log10 p ; seuil K >= 20)
#    Strates 1875, 1886, 1903 seulement — 1892 n'entre dans aucun calcul.
# ----------------------------------------------------------------------------
TROIS = ["1875", "1886", "1903"]
Ntot = sum(N[s] for s in TROIS)
Ftot = Counter()
for s in TROIS:
    Ftot.update(C[s])
SPEC = {}
for s in TROIS:
    d = {}
    for w, K in Ftot.items():
        if K < 20:
            continue
        k = C[s][w]
        p_sur = hypergeom.sf(k-1, Ntot, K, N[s])
        p_sous = hypergeom.cdf(k, Ntot, K, N[s])
        d[w] = (-math.log10(max(p_sur, 1e-300)) if p_sur < p_sous
                else math.log10(max(p_sous, 1e-300)))
    SPEC[s] = d
STOP = set(("de la le les l' un une des du au aux et ou mais or ni car donc à en dans par "
    "pour sur avec sans sous chez entre vers contre selon que qu' qui quoi dont où si comme "
    "quand est sont était été être a ont avait avoir il elle on nous vous ils elles je tu ce "
    "cette ces cet se ne n' pas point plus moins très bien tout toute tous toutes d' s' c' j' "
    "m' t' y ainsi aussi même mêmes autre autres leur leurs son sa ses mon ma mes notre nos "
    "votre vos peut peuvent fait faire deux trois premier première second seconde là ici "
    "encore déjà toujours jamais rien quelque quelques chose choses celui celle ceux celles "
    "lui eux soi cela ça alors puis enfin cependant néanmoins toutefois pourtant après avant "
    "depuis pendant lorsque puisque quoique afin parce").split())
print("== SPÉCIFICITÉS (mots pleins, S >= 8) ==")
for s in TROIS:
    sur = sorted(((v, w) for w, v in SPEC[s].items() if v >= 8 and w not in STOP),
                 reverse=True)[:22]
    print(f"  ++{s} : " + " · ".join(f"{w}({v:.0f})" for v, w in sur))

# ----------------------------------------------------------------------------
# 6. TRAJECTOIRES /10 000 mots (regroupements indiqués sur la ligne)
# ----------------------------------------------------------------------------
GROUPES = {
  "catégorie(s)": ("catégorie", "catégories"), "représentation(s)": ("représentation", "représentations"),
  "fonction(s)": ("fonction", "fonctions"), "science(s)": ("science", "sciences"),
  "vérité(s)": ("vérité", "vérités"), "certitude": ("certitude",),
  "dieu": ("dieu",), "création": ("création",), "créateur": ("créateur",),
  "péché": ("péché",), "mal": ("mal",),
  "corps": ("corps",), "force(s)": ("force", "forces"), "matière": ("matière",),
  "monade(s)": ("monade", "monades"),
  "liberté": ("liberté",), "volonté(s)": ("volonté", "volontés"),
  "croyance(s)": ("croyance", "croyances"), "infini*": ("infini", "infinie", "infinis", "infinies"),
  "nécessité": ("nécessité",), "conscience(s)": ("conscience", "consciences"),
  "personne(s)": ("personne", "personnes"), "personnalisme": ("personnalisme",),
}
tab("TRAJECTOIRES /10k  (1875 1886 1903 1892)",
    [(nom, [f10k(s, *mots) for s in ORDRE]) for nom, mots in GROUPES.items()])

# ----------------------------------------------------------------------------
# 7. GRAMMAIRE : personnes, négation, connecteurs, ponctuation
# ----------------------------------------------------------------------------
tab("PERSONNES /10k", [
    ("je, j'", [f10k(s, "je", "j'") for s in ORDRE]),
    ("me, m', moi", [f10k(s, "me", "m'", "moi") for s in ORDRE]),
    ("nous", [f10k(s, "nous") for s in ORDRE]),
    ("on", [f10k(s, "on") for s in ORDRE]),
    ("il, ils", [f10k(s, "il", "ils") for s in ORDRE]),
])
print("\n== NÉGATION (forme dans les 5 mots après ne/n') ==")
for s in ORDRE:
    toks = LOW[s]; d = Counter()
    for i, w in enumerate(toks):
        if w in ("ne", "n'"):
            for fme in ("pas", "point", "plus", "jamais", "rien"):
                if fme in toks[i+1:i+6]:
                    d[fme] += 1
                    break
    tot = d["pas"] + d["point"]
    print(f"  {s} : pas {d['pas']} · point {d['point']} ({d['point']/tot*100:.1f} %) · "
          f"ne/10k {sum(1 for w in toks if w in ('ne',chr(110)+chr(39)))/N[s]*10000:.0f}")
BIG = {s: Counter(zip(LOW[s], LOW[s][1:])) for s in ORDRE}
def conn(s, *unites):
    n = 0
    for u in unites:
        n += BIG[s][tuple(u.split())] if " " in u else C[s][u]
    return n / N[s] * 10000
CONNECTEURS = {"donc": ("donc",), "or": ("or",), "car": ("car",), "mais": ("mais",),
    "si": ("si",), "ainsi": ("ainsi",), "cependant": ("cependant",),
    "pourtant": ("pourtant",), "parce que": ("parce que",),
    "en effet": ("en effet",), "au contraire": ("au contraire",),
    "lorsque": ("lorsque", "lorsqu'"), "c'est-à-dire": ("c' est-à-dire",),
    "d'ailleurs": ("d' ailleurs",)}
tab("CONNECTEURS /10k", [(nom, [conn(s, *u) for s in ORDRE]) for nom, u in CONNECTEURS.items()])
print("\n== PONCTUATION /10k ==")
for s in ORDRE:
    print(f"  {s} :  ? {TXT[s].count('?')/N[s]*10000:5.1f}   ! {TXT[s].count('!')/N[s]*10000:4.1f}   "
          f"; {TXT[s].count(';')/N[s]*10000:5.1f}   : {TXT[s].count(':')/N[s]*10000:5.1f}")

# ----------------------------------------------------------------------------
# 8. ÉTIQUETAGE — dictionnaires de décision COMPLETS
# ----------------------------------------------------------------------------
EXCL_AIT = set("""fait ait sait aient parfait satisfait imparfait bienfait forfait méfait
  souhait souhaits lait attrait attraits trait traits portrait portraits extrait extraits
  abstrait abstraits soustrait retrait retraits distrait plait parait surfait refait
  contrefait stupéfait""".split())
IMP_RAIT = set("""considérait opérait espérait désespérait exagérait tolérait libérait
  générait conférait déférait préférait différait persévérait coopérait adhérait révérait
  vénérait altérait désirait admirait tirait attirait retirait inspirait respirait
  soupirait expirait aspirait empirait virait déchirait durait figurait mesurait assurait
  murmurait procurait jurait demeurait éclairait comparait déclarait ignorait séparait
  préparait montrait entrait rencontrait pénétrait montraient entraient considéraient
  duraient figuraient demeuraient déclaraient ignoraient tiraient attiraient désiraient
  admiraient offrait offraient découvrait démontrait souffrait ouvrait couvrait
  recouvrait""".split())
COND_X = set("""serait seraient aurait auraient pourrait pourraient saurait sauraient
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
  admettraient concluraient""".split())
PS_OK = set("""furent firent eurent purent durent vinrent tinrent prirent mirent virent
  dirent surent voulurent connurent parurent reçurent crurent devinrent obtinrent
  naquirent moururent vécurent suivirent servirent sentirent partirent sortirent
  ouvrirent offrirent réussirent choisirent finirent établirent réunirent définirent
  produisirent conduisirent introduisirent construisirent détruisirent écrivirent
  comprirent apprirent reprirent entreprirent attendirent entendirent répondirent
  perdirent rendirent descendirent""".split())
PRES_ERENT = set("""diffèrent demeurent tirent figurent suggèrent opèrent concourent
  altèrent meurent attirent acquièrent mesurent éclairent considèrent préfèrent espèrent
  tolèrent libèrent exagèrent digèrent insèrent coopèrent adhèrent révèrent vénèrent
  réfèrent confèrent transfèrent persévèrent désespèrent gèrent cèdent secourent courent
  parcourent discourent recourent conquièrent requièrent assurent réclament""".split())
EXCL_FUT = set("""vrai vrais barbara considérons ignorons comparons préparons désirons
  admirons honorons mesurons assurons demeurons figurons tirons montrons rencontrons
  entrons opérons espérons déclarons séparons adorons restaurons""".split())
FUT_IRREG = set("""sera seront serai serons serez aura auront aurai aurons aurez pourra
  pourront pourrai pourrons ira iront irai irons fera feront ferai ferons ferez devra
  devront devrai devrons dira diront dirai dirons direz faudra vaudra voudra voudront
  viendra viendront tiendra tiendront verra verront verrai verrons saura sauront saurai
  saurons mettra mettront prendra prendront rendra rendront comprendra apprendra
  deviendra deviendront conviendra connaîtra connaîtront paraîtra apparaîtra recevra
  recevront croira croiront vivra vivront suivra suivront écrira écriront répondra
  attendra entendra perdra perdront enverra enverrons offriront souffriront ouvriront
  découvriront""".split())
def cl_verbe(w):
    """Étiquette IMP / COND / FUT / PS, ou None (forme laissée sans étiquette)."""
    if w in EXCL_AIT or w in PRES_ERENT:
        return None
    if w.endswith(("erait", "eraient")):     # trouver+ait : conditionnel sûr
        return "COND"
    if w.endswith(("érait", "éraient")):     # considér+ait : imparfait sûr
        return "IMP"
    if w in COND_X:
        return "COND"
    if w in IMP_RAIT:
        return "IMP"
    if w.endswith(("ait", "aient")) and not w.endswith(("rait", "raient")):
        return "IMP"
    if w in PS_OK or w.endswith("èrent"):
        return "PS"
    if w in FUT_IRREG:
        return "FUT"
    if w not in EXCL_FUT and re.search(r"(erai|eras|era|erons|erez|eront)$", w):
        return "FUT"
    return None
NOM_MENT = set("""mouvement sentiment comment développement moment jugement fondement
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
  soulèvement tremblement tâtonnement vieillissement""".split())
V_MENT = set("""forment ment mentent aiment arment calment charment confirment déforment
  dorment enferment estiment expriment ferment germent impriment infirment informent
  priment réforment renferment réaffirment suppriment transforment affirment animent
  réclament proclament acclament déclament""".split())
ADV_X = set("""seulement autrement simplement proprement absolument vraiment
  immédiatement certainement indéfiniment nullement infiniment nettement réciproquement
  non-seulement justement complètement complétement librement fortement pratiquement
  facilement pleinement difficilement légitimement diversement manifestement vainement
  rarement extrêmement franchement uniquement hardiment indissolublement brièvement
  parallèlement naïvement longuement rapidement pareillement ouvertement secondement
  résolument grandement fermement premièrement deuxièmement troisièmement
  dernièrement""".split())
def cl_ment(w):
    """Étiquette ADV / NOM / V pour les formes en -ment, ou None (résidu compté)."""
    if not w.endswith("ment") or len(w) < 5:
        return None
    if w in V_MENT:
        return "V"
    if w in NOM_MENT:
        return "NOM"
    if w in ADV_X or w.endswith(("amment", "emment", "quement", "ellement", "alement",
        "iblement", "ablement", "ivement", "eusement", "airement", "èrement",
        "ièrement", "ûrement", "itement", "ctement", "ément")):
        return "ADV"
    return "RESIDU"
print("\n== TEMPS/MODES /10k (IMP COND FUT PS) et -MENT /10k (ADV NOM) ==")
residu_ment = 0
for s in ORDRE:
    dv, dm = Counter(), Counter()
    for w in LOW[s]:
        e = cl_verbe(w)
        if e:
            dv[e] += 1
        m = cl_ment(w)
        if m == "RESIDU":
            residu_ment += 1
        elif m:
            dm[m] += 1
    print(f"  {s} : IMP {dv['IMP']/N[s]*1e4:5.1f}  COND {dv['COND']/N[s]*1e4:5.1f}  "
          f"FUT {dv['FUT']/N[s]*1e4:5.1f}  PS {dv['PS']/N[s]*1e4:4.1f}   |   "
          f"ADV {dm['ADV']/N[s]*1e4:6.1f}  NOM {dm['NOM']/N[s]*1e4:5.1f}")
print(f"  résidu -ment non classé : {residu_ment} occ. "
      f"({residu_ment/sum(N.values())*100:.3f} % des tokens)")

# ----------------------------------------------------------------------------
# 9. COUVERTURE + DELTA DE BURROWS + DATATION DE 1892
# ----------------------------------------------------------------------------
FERMEES = set("""le la les l' un une des du au aux ce cet cette ces mon ma mes ton ta tes
  son sa ses notre nos votre vos leur leurs quel quelle quels quelles chaque plusieurs
  quelques aucun aucune nul nulle tout toute tous toutes je tu il elle on nous vous ils
  elles me m' te t' se s' moi toi soi lui eux y en de d' à dans par pour sur avec sans
  sous chez entre vers contre selon malgré parmi envers hors dès depuis pendant durant
  devant derrière après avant jusque jusqu' outre et ou mais or ni car donc que qu' qui
  dont où si comme quand lorsque lorsqu' puisque puisqu' quoique quoiqu' ne n' pas point
  plus jamais rien guère est sont était étaient être été sera seront serait seraient
  soit soient fut furent a ont avait avaient avoir eu aura auront aurait auraient ait
  aient eut eurent c' j' très bien peu ainsi aussi encore déjà toujours alors puis enfin
  cependant néanmoins toutefois pourtant même mêmes autre autres tel telle tels
  telles""".split())
print("\n== COUVERTURE (classes fermées + paradigmes + -ment classés) ==")
for s in ORDRE:
    n_ok = sum(1 for w in LOW[s]
               if w in FERMEES or cl_verbe(w) or cl_ment(w) in ("ADV", "NOM", "V"))
    print(f"  {s} : {n_ok/N[s]*100:.1f} %")
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
print("\n== DELTA DE BURROWS (segments de 20 000 mots ; 120 mots-outils) ==")
print("  mots-outils :", " ".join(MOTS_OUTILS))
for s in TROIS:
    print(f"  intra-{s} : "
          f"{statistics.mean(delta(a,b) for a,b in itertools.combinations(idx[s],2)):.3f}")
for s1, s2 in [("1875", "1886"), ("1886", "1903"), ("1875", "1903")]:
    print(f"  {s1} <-> {s2} : "
          f"{statistics.mean(delta(a,b) for a in idx[s1] for b in idx[s2]):.3f}")
centres = {s: Z[idx[s]].mean(0) for s in TROIS}
print("  -- datation des segments de 1892 --")
for k, i in enumerate(idx["1892"]):
    d = {s: float(np.mean(np.abs(Z[i] - centres[s]))) for s in TROIS}
    print(f"  1892-{k+1} : " + "  ".join(f"{s} {d[s]:.3f}" for s in TROIS)
          + f"  -> {min(d, key=d.get)}")
