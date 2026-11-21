---
title: "Calcul des probabilités : sa portée objective et ses principes (1905)"
---

# Calcul des probabilités : sa portée objective et ses principes (1905)

> **Source** : Paul Mansion, *Calcul des probabilités, sa portée objective et ses principes*, Paris, Gauthier-Villars, 1905, IV-120 p. (réunion de cinq articles parus de 1902 à 1904). — Exemplaire numérisé par Google.

[p. III]

## PRÉFACE

Le présent opuscule est formé de la réunion de cinq articles que nous avons publiés sur le Calcul des Probabilités en 1902, 1903, 1904.

Dans le premier, le second, le quatrième et le cinquième, nous calculons, avec plus de précision qu'on ne l'a fait jusqu'à présent, les probabilités que l'on rencontre dans la démonstration du théorème de Bernoulli et de la loi des grands nombres, et aussi dans plusieurs questions de probabilités dites *à posteriori*. Nous ne nous contentons pas d'évaluer approximativement ces diverses probabilités d'une manière vague, au moyen de la célèbre intégrale de Laplace (gamma *incomplet* de un demi) ; nous indiquons pour toutes des limites bien nettes entre lesquelles elles sont renfermées.

Au point de vue des principes du Calcul des Probabilités, le résultat le plus important de notre analyse est celui-ci : la loi des grands nombres de Poisson peut être mise sous une forme aussi précise que le théorème de Bernoulli et a la même valeur objective, parce qu'elle peut s'en déduire logiquement (Page 28, ligne 17, au lieu de *plus grand que*. lisez *plus grand*).

[p. IV] Dans le Discours *sur la portée objective du Calcul des Probabilités*, nous exposons nos vues sur la solidité même des principes de cette science et sur la légitimité des applications que l'on en fait.

Notre première thèse est la suivante : Le Calcul des Probabilités a pour objet les événements qui sont soumis à une loi complexe, résultante d'une loi principale d'après laquelle certains rapports numériques sont constants, et de lois perturbatrices secondaires donnant naissance à de faibles variations de ces rapports. Dans l'étude de pareils événements, on peut regarder comme légitimes les résultats déduits de la loi des grands nombres. Nous concluons de ce principe que l'on peut appliquer le calcul des probabilités à la statistique morale, aux jeux de hasard, à l'évolutionisme, mais non aux jugements en matière civile ou criminelle, ni à la probabilité des causes.

Notre seconde thèse est le *principe de l'accumulation des probabilités indépendantes* de Newman. A proprement parler, il ne peut être traduit en formule, sauf sous une forme symbolique où entre une fonction inconnue. Nous montrons que ce principe, jusqu'ici trop ignoré des géomètres et des logiciens, est la source parfaitement légitime de nos certitudes pratiques, dans le domaine de toutes les sciences qui reposent en dernière analyse sur le témoignage, sciences de la nature, sciences historiques.

[p. 1]

## DÉMONSTRATION DU THÉORÈME DE JACQUES BERNOULLI

par P. Mansion

Professeur à l'Université de Gand

Théorème. *La somme* \(\mathrm{P}\) *des valeurs de* \(\mathrm{T}_{m} = \mathrm{C}_{\mu}^{m} p^{m} q^{m}\), *où* \(m\) *est compris entre* \(\mu p - \mu l\), \(\mu p + \mu l\), \(\mu\) *étant égal à* \(m + n\) *et au moins égal à dix*, \(p\) *et* \(q\) *des quantités positives telles que* \(p + q = 1\), \(p \mathrel{\overset{=}{>}} q\), *l'inférieur ou égal à* \(\frac{1}{2} q\), \(\mu \mathrel{\overset{=}{>}} \frac{1}{q^{2}}\), *est supérieure à*

\[ \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt - \frac{3}{\sqrt{2\pi\mu pq}}, \qquad \mathrm{T} = l\sqrt{\frac{\mu}{2pq}}, \]

*et a l'unité pour limite quand* \(\mu\) *croît indéfiniment*[^1-a].

[p. 2] **1.** *Formules analytiques employées dans la démonstration*. I. Si \(\alpha\) est une quantité positive inférieure à l'unité, on a

\[ \log(1 + \alpha) = \frac{\alpha}{1} - \frac{\alpha^{2}}{2} + \frac{\alpha^{3}}{3} - \frac{\alpha^{4}}{4} + \cdots, \tag{1} \]

\[ -\log(1 - \alpha) = \frac{\alpha}{1} + \frac{\alpha^{2}}{2} + \frac{\alpha^{3}}{3} + \frac{\alpha^{4}}{4} + \cdots, \tag{2} \]

On déduit de (1), (2),

\[ \log(1 + \alpha) > \alpha - \frac{\alpha^{2}}{2} = \frac{\alpha}{2} + \frac{\alpha}{2}(1 - \alpha) > \frac{\alpha}{2}, \tag{3} \]

\[ -\log(1 - \alpha) < \alpha + \frac{\alpha^{2}}{2}(1 + \alpha + \alpha^{2} + \cdots) = \alpha + \frac{\alpha^{2}}{2(1 - \alpha)}. \tag{4} \]

Enfin, quel que soit \(\alpha\), \(\theta\) étant compris entre 0 et 1,

\[ e^{-\alpha} = 1 - \alpha + \frac{\alpha^{2}}{2} e^{-\theta\alpha} > 1 - \alpha. \tag{5} \]

II. Si N est un nombre entier, on a, d'après la formule de Stirling, sous sa forme élémentaire,

\[ 1.2.3 \ldots \mathrm{N} > \sqrt{2\pi\mathrm{N}}\,\mathrm{N}^{\mathrm{N}} e^{-\mathrm{N}}, \tag{6} \]

\[ 1.2.3 \ldots \mathrm{N} < \sqrt{2\pi\mathrm{N}}\,\mathrm{N}^{\mathrm{N}} e^{-\mathrm{N} + \frac{1}{12\mathrm{N}}}. \tag{7} \]

III. En faisant \(t^{2} = z\), on trouve aisément que

\[ \int_{0}^{\infty} e^{-t^{2}} t^{4}\,dt = \frac{1}{2} \int_{0}^{\infty} e^{-z} z^{\frac{3}{2}}\,dz = \frac{1}{2} \Gamma\left(\frac{5}{2}\right) = \frac{3}{8} \sqrt{\pi}. \tag{8} \]

IV. Si \(z_{x}\) est une fonction de \(x\) décroissante depuis \(x = 0\) jusque \(x = \mathrm{N} + 1\), N étant entier, on a évidemment

\[ z_{0} + z_{1} + \cdots + z_{\mathrm{N}} > \int_{0}^{\mathrm{N}+1} z_{x}\,dx. \tag{9} \]

[p. 3] V. Enfin, puisque \(q \mathrel{\overset{=}{<}} \frac{1}{2}\), \(\mu \mathrel{\overset{=}{>}} \frac{1}{q^{2}}\), \(p \mathrel{\overset{=}{>}} q\), on a

\[ \mu q \mathrel{\overset{=}{>}} \frac{1}{q} \mathrel{\overset{=}{>}} 2, \qquad \mu p \mathrel{\overset{=}{>}} \mu q \mathrel{\overset{=}{>}} 2, \tag{10} \]

même sans supposer \(\mu\) au moins égal à 10.

**2:** *On a*

\[ \mathrm{T}_{m} > \frac{1}{\sqrt{2\pi\mu pq}}\left[1 - \frac{1}{6\mu pq}\right] t_{m}, \quad \text{si } t_{m} = \left(\frac{m}{\mu p}\right)^{-m-\frac{1}{2}} \left(\frac{n}{\mu q}\right)^{-n-\frac{1}{2}}. \]

En effet, d'après les inégalités (6) et (7),

\[ \mathrm{C}_{\mu}^{m} = \frac{1.2.\cdots\mu}{1.2.\ldots m.1.2.\ldots n} > \frac{\sqrt{2\pi\mu}\,\mu^{\mu} e^{-\mu}}{\sqrt{2\pi m}\,m^{m} e^{-m} \sqrt{2\pi n}\,n^{n} e^{-n} . e^{\frac{1}{12}\left(\frac{1}{m} + \frac{1}{n}\right)}}, \]

ou

\[ \mathrm{C}_{\mu}^{m} > \frac{1}{\sqrt{2\pi\mu}} \frac{1}{\left(\frac{m}{\mu}\right)^{m+\frac{1}{2}} \left(\frac{n}{\mu}\right)^{n+\frac{1}{2}} e^{\frac{\mu}{12mn}}}. \]

Par suite,

\[ \mathrm{T}_{m} = \mathrm{C}_{\mu}^{m} p^{m} q^{n} > \frac{1}{\sqrt{2\pi\mu pq}} \frac{1}{\left(\frac{m}{\mu p}\right)^{m+\frac{1}{2}} \left(\frac{n}{\mu q}\right)^{n+\frac{1}{2}}} e^{-\frac{\mu}{12mn}}. \]

Mais, d'après (5), on a

\[ e^{-\frac{\mu}{12mn}} > 1 - \frac{\mu}{12mn}. \]

Nous pouvons donc écrire

\[ \mathrm{T}_{m} > \frac{1}{\sqrt{2\pi\mu pq}}\left(1 - \frac{\mu}{12mn}\right) t_{m}. \]

[p. 4] Le produit \(mn\) des deux quantités \(m\) et \(n\), dont la somme est la constante \(\mu\), est d'autant plus petit que \(m - n\) ou \(n - m\) est plus grand. La valeur la plus petite de \(mn\) correspondra donc à l'une ou l'autre des valeurs extrêmes que peuvent prendre \(m\) et \(n\), savoir, au plus, \(\mu p + \mu l\), \(\mu p - \mu l\) pour \(m\), \(\mu q - \mu l\), \(\mu q + \mu l\) pour \(n\). Or

\[ (\mu p + \mu l)(\mu q - \mu l) = \mu^{2}[pq - (p - q)l - l^{2}], \]

\[ (\mu p - \mu l)(\mu q + \mu l) = \mu^{2}[pq + (p - q)l - l^{2}]. \]

Le produit \(12mn\) est donc égal ou supérieur à

\[ 12(\mu p + \mu l)(\mu q - \mu l) = 12\mu^{2}(p + l)(q - l). \]

Le produit \(12(p + l)(q - l)\) est aussi d'autant plus petit que la différence \(p - q + 2l\) entre les deux facteurs \(p + l\), \(q - l\) est plus grande. Or, la plus grande valeur que puisse prendre \(l\) est \(\frac{1}{2} q\). Par suite,

\[ 12(p + l)(q - l) \mathrel{\overset{=}{>}} 12\left(p + \frac{1}{2} q\right)\left(q - \frac{1}{2} q\right) \]

\[ = 3(1 + p)q > 3.2p.q = 6pq. \]

On a donc

\[ 1 - \frac{\mu}{12mn} > 1 - \frac{\mu}{12\mu^{2}(p + l)(q - l)} > 1 - \frac{1}{6\mu pq}, \]

et enfin

\[ \mathrm{T}_{m} > \frac{1}{\sqrt{2\pi\mu pq}}\left(1 - \frac{1}{6\mu pq}\right) t_{m}. \]

**3.** *On a* \(t_{\mu p+1} < t_{\mu p}\) *ou* 1. En effet, posons, en général,

\[ t_{m} = e^{-u}, \]

\[ u = \left(m + \frac{1}{2}\right)\log\left(\frac{m}{\mu p}\right) + \left(n + \frac{1}{2}\right)\log\left(\frac{n}{\mu q}\right). \]

[p. 5] Si l'on fait

\[ m = \mu p + x, \qquad n = \mu q - x, \]

on a

\[ u = \left(\mu p + x + \frac{1}{2}\right)\log\left(1 + \frac{x}{\mu p}\right) + \left(\mu q - x + \frac{1}{2}\right)\log\left(1 - \frac{x}{\mu q}\right). \]

Pour \(x = 1\), on trouve

\[ u_{1} = \left(\mu p + \frac{3}{2}\right)\log\left(1 + \frac{1}{\mu p}\right) + \left(\mu q - \frac{1}{2}\right)\log\left(1 - \frac{1}{\mu q}\right), \]

et, d'après les inégalités (3) et (4),

\[ u_{1} > \left(\mu p + \frac{3}{2}\right)\left(\frac{1}{\mu p} - \frac{1}{2\mu^{2}p^{2}}\right) - \left(\mu q - \frac{1}{2}\right)\left[\frac{1}{\mu q} + \frac{1}{2\mu^{2}q^{2}\left(1 - \frac{1}{\mu q}\right)}\right] \]

\[ = 1 + \frac{3}{2\mu p} - \frac{1}{2\mu p} - \frac{3}{4} \frac{1}{\mu^{2}p^{2}} - 1 + \frac{1}{2\mu q} - \frac{1}{2(\mu q - 1)} + \frac{1}{4\mu q(\mu q - 1)} \]

\[ = \frac{1}{\mu p} - \frac{3}{4} \frac{1}{\mu^{2}p^{2}} - \frac{1}{4\mu q(\mu q - 1)} \]

\[ = \frac{3}{4\mu p}\left(1 - \frac{1}{\mu p}\right) + \frac{1}{4\mu}\left[\frac{1}{p} - \frac{1}{q(\mu q - 1)}\right]. \]

D'après (10), \(\mu p\) est supérieur à 1, et \(1 - \frac{1}{\mu p}\) est positif. On a aussi

\[ \frac{1}{p} - \frac{1}{q(\mu q - 1)} \mathrel{\overset{=}{>}} 0. \]

En effet, d'après (10) encore, \(\mu q - 1\) est positif. La précédente inégalité peut donc s'écrire successivement

\[ q(\mu q - 1) - p \mathrel{\overset{=}{>}} 0, \qquad \mu q^{2} - p - q \mathrel{\overset{=}{>}} 0, \]

\[ \mu q^{2} \mathrel{\overset{=}{>}} 1, \]

[p. 6] ce qui est conforme à l'une des hypothèses de l'énoncé du théorème.

On a donc

\[ u_{1} > 0, \qquad e^{-u_{1}} < 1, \qquad \text{ou} \qquad t_{\mu p+1} < t_{\mu p}. \]

**4.** *La fonction* \(t_{\mu p+x}\) *a un seul maximum, soit pour* \(x = 0\), *soit pour une valeur comprise entre* \(x = 0\) *et* \(x = p\). De l'égalité

\[ u = \left(\mu p + x + \frac{1}{2}\right)\log\left(1 + \frac{x}{\mu p}\right) + \left(\mu q - x + \frac{1}{2}\right)\log\left(1 - \frac{x}{\mu q}\right), \]

on déduit, par dérivation,

\[ u' = \log\left(1 + \frac{x}{\mu p}\right) - \log\left(1 - \frac{x}{\mu q}\right) + \frac{1}{2}\left(\frac{1}{\mu p + x} - \frac{1}{\mu q - x}\right), \]

\[ u'' = \frac{1}{\mu p + x}\left(1 - \frac{1}{2} \frac{1}{\mu p + x}\right) + \frac{1}{\mu q - x}\left(1 - \frac{1}{2} \frac{1}{\mu q - x}\right). \]

Si \(x\) est positif, même pour \(x = \mu l\) et \(l = \frac{1}{2} q\), \(2(\mu q - x) = 2\mu q - \mu q = \mu q\) est égal ou supérieur à 2 ; donc \(u''\) est une quantité positive. Si \(x\) est négatif, même pour sa valeur extrême, \(x = -\mu l = -\frac{1}{2} \mu q\), \(2(\mu p + x) = 2\mu p - \mu q\) est égal ou supérieur à \(\mu p\), lui-même égal ou supérieur à 2 d'après (10) ; donc \(u''\) est encore une quantité positive. Par suite, \(u'\) est une fonction croissante.

Si \(p = q = 1\), pour \(x = 0\), \(u' = 0\) ; \(u'\), qui croît sans cesse, passe donc du négatif au positif pour \(x = 0\) ; \(u\) a son minimum en \(x = 0\), et \(t_{\mu p} = e^{-u}\) a sa valeur maxima, savoir 1, aussi pour \(x = 0\).

Si \(p\) est supérieur à \(q\), on a, pour \(x = 0\),

\[ u' = \frac{1}{2}\left(\frac{1}{\mu p} - \frac{1}{\mu q}\right) < 0. \]

[p. 7] Pour \(x = p\), on trouve après quelques transformations,

\[ u' = \log\left(1 + \frac{1}{\mu q - p}\right) + \frac{1}{2}\left(\frac{1}{\mu p + p} - \frac{1}{\mu q - p}\right). \]

Donc, d'après (3),

\[ u' > \frac{1}{2} \frac{1}{\mu q - p} + \frac{1}{2}\left(\frac{1}{\mu p + p} - \frac{1}{\mu q - p}\right) = \frac{1}{2} \frac{1}{\mu p + p} > 0. \]

Ainsi \(u'\) passe du négatif au positif, quand \(x\) varie de 0 à \(p\) ; \(u\) a donc un minimum et \(t_{\mu p+x} = e^{-u}\), un maximum pour une valeur X de \(x\) comprise entre 0 et \(p\).

Remarque[^7-a]. *La valeur maxima de* \(t_{\mu p+x}\) *est inférieure à* \(\sqrt{e}\), *supérieure à* 1, *quand* \(p\) *est* \(> q\). En effet, la valeur minima de \(u\), correspondant à \(x = \mathrm{X}\), s'obtiendrait en éliminant X entre les relations

\[ u_{minima} = \left(\mu p + \mathrm{X} + \frac{1}{2}\right)\log\left(1 + \frac{\mathrm{X}}{\mu p}\right) \]

\[ + \left(\mu q - \mathrm{X} + \frac{1}{2}\right)\log\left(1 - \frac{\mathrm{X}}{\mu q}\right), \]

\[ u'_{\mathrm{X}} = 0 = \log\left(1 + \frac{\mathrm{X}}{\mu p}\right) - \log\left(1 - \frac{\mathrm{X}}{\mu q}\right) \]

\[ + \frac{1}{2}\left(\frac{1}{\mu p + \mathrm{X}} - \frac{1}{\mu q - \mathrm{X}}\right). \]

L'élimination complète est impraticable, mais en éliminant \(\log\left(1 - \frac{\mathrm{X}}{\mu q}\right)\) entre les équations, il vient

\[ u_{minima} = (\mu p + 1)\log\left(1 + \frac{\mathrm{X}}{\mu p}\right) \]

\[ - \frac{1}{2}\left(\mu q - \mathrm{X} + \frac{1}{2}\right)\left(\frac{1}{\mu q - \mathrm{X}} - \frac{1}{\mu p + \mathrm{X}}\right) \]

\[ > - \frac{1}{2}\left(\mu q - \mathrm{X} + \frac{1}{2}\right)\left(\frac{1}{\mu q - \mathrm{X}} - \frac{1}{\mu p + \mathrm{X}}\right). \]

[p. 8] Je dis que l'on a

\[ \left(\mu q - \mathrm{X} + \frac{1}{2}\right)\left(\frac{1}{\mu q - \mathrm{X}} - \frac{1}{\mu p + \mathrm{X}}\right) < 1. \]

En effet, cette inégalité, après quelques transformations, devient

\[ \mu p + 4\mu q\mathrm{X} + 2\mathrm{X}(1 - \mathrm{X}) < 2\mu^{2}q^{2} + \mu q. \]

On a \(\mu q^{2} \mathrel{\overset{=}{>}} 1\), ou \(\mu q^{2} = 1 + \alpha\), \(\alpha\) étant positif ou nul ; \(\mathrm{X} < p\) a pour conséquence \(4\mu q\mathrm{X} < 4\mu pq < 4\mu . \frac{1}{4}\) ou \(\mu\), et, par suite, \(4\mu q\mathrm{X} = \mu - \beta\), \(\beta\) étant positif ; \(\mathrm{X}(1 - \mathrm{X})\) est inférieure à \(\frac{1}{4}\) ou de la forme \(\frac{1}{4} - \gamma\), \(\gamma\) étant positif. L'inégalité à vérifier peut s'écrire

\[ \mu p + \mu - \beta + \frac{1}{2} - 2\gamma < 2\mu(1 + \alpha) + \mu q, \]

c'est-à-dire

\[ \frac{1}{2} < 2\mu q + 2\mu\alpha + \beta + 2\gamma. \]

Mais on a, d'après la formule (10), \(\mu q \mathrel{\overset{=}{>}} 2\). Donc l'inégalité devient

\[ \frac{1}{2} < 4 + 2\mu\alpha + \beta + 2\gamma, \]

laquelle est évidente.

Il en résulte que la valeur minima de \(u\) surpasse \(-\frac{1}{2}\), la valeur maxima de \(-u\) est inférieure à \(\frac{1}{2}\), et, par suite, celle de \(t_{\mu p+x}\) est inférieure à \(\sqrt{e}\).

Dans le cas actuel où \(\mu\) est \(> q\), elle surpasse d'ailleurs \(t_{\mu p}\) ou 1, puisque X n'est pas nul.

[p. 9] **5.** *Transformation de la somme des* \(t_{m}\) *et des* \(\mathrm{T}_{m}\). Si \(\mu p\) est entier, les valeurs de \(m\) à considérer dans \(\mathrm{P} = \mathrm{S}\mathrm{T}_{m}\) sont, \(\mathrm{E}(x)\) désignant le plus grand entier contenu dans \(x\),

\[ \mu p \text{ et } \left\{ \begin{matrix} \mu p + 1, & \mu p + 2, & \cdots, & \mu p + \mathrm{E}(\mu l) \\ \mu p - 1, & \mu p - 2, & \cdots, & \mu p - \mathrm{E}(\mu l) \end{matrix} \right\}. \]

Dans ce cas,

\[ \mathrm{S}t_{m} = t_{\mu p} + \mathop{\mathrm{S}}\limits_{x=1}^{x=\mathrm{E}(\mu l)} [t_{\mu p+x} + t_{\mu p-x}] > \mathop{\mathrm{S}}\limits_{x=1}^{x=\mathrm{E}(\mu l)} [t_{\mu p+x} + t_{\mu p-x}]. \]

Si \(\mu p\) n'est pas entier, il y aura entre \(\mu p\) et \(\mu p + 1\) un seul entier \(r\). On aura

\[ t_{r} > t_{\mu p+1}, \]

puisque la fonction \(t_{\mu p+x}\) a sa valeur minima, pour \(x = 1\), dans l'intervalle de \(x = 0\), à \(x = 1\), d'après les n<sup>os</sup> 3 et 4.

On devra donc donner à \(m\) les valeurs

\[ r \text{ et } \left\{ \begin{matrix} r + 1, & r + 2, & r + 3, & \text{etc.} \\ r - 1, & r - 2, & r - 3, & \text{etc.} \end{matrix} \right\} \]

comprises entre \(\mu p - \mu l\), \(\mu p + \mu l\).

La fonction \(t_{m}\) décroît de part et d'autre à partir de sa valeur maxima comprise entre \(t_{\mu p}\) et \(t_{\mu p+p}\) ; donc

\[ \begin{array}{ll} t_{r-1} > t_{\mu p-1}, \qquad & t_{r} > t_{\mu p+1}, \\ t_{r-2} > t_{\mu p-2}, \qquad & t_{r+1} > t_{\mu p+2}, \\ t_{r-3} > t_{\mu p-3}, \text{ etc.} \qquad & t_{r+2} > t_{\mu p+3}, \text{ etc.} \end{array} \]

Par suite, la somme de tous les \(t_{m}\) à considérer sera supérieure à

\[ \mathop{\mathrm{S}}\limits_{x=1}^{x=\mathrm{E}(\mu l)} [t_{\mu p+x} + t_{\mu p-x}]. \]

On a donc aussi

\[ \begin{aligned} \mathrm{P} &> \left[1 - \frac{1}{6\mu pq}\right] \frac{1}{\sqrt{2\pi \mu pq}}\, \mathrm{S}t_{m} \\ &> \left[1 - \frac{1}{6\mu pq}\right] \frac{1}{\sqrt{2\pi \mu pq}} \mathop{\mathrm{S}}\limits_{x=1}^{x=\mathrm{E}(\mu l)} [t_{\mu p+x} + t_{\mu p-x}]. \end{aligned} \]

[p. 10] **6.** *Transformation de la dernière somme*. Posons

\[ y_{x}^{2} = t_{\mu p+x} \times t_{\mu p-x}. \]

La moyenne arithmétique de deux quantités est supérieure ou égale à leur moyenne géométrique[^10-a]. On a donc

\[ t_{\mu p+x} + t_{\mu p-x} \mathrel{\overset{=}{>}} 2y_{x}, \]

\[ \mathrm{P} > \left(1 - \frac{1}{6\mu pq}\right) \frac{2}{\sqrt{2\pi \mu pq}} \mathop{\mathrm{S}}\limits_{x=1}^{x=\mathrm{E}(\mu l)} y_{x}. \]

Soit

\[ y_{x}^{2} = e^{-v}, \]

de sorte que

\[ \begin{aligned} v = {} & \left(\mu p + x + \frac{1}{2}\right) \log\left(1 + \frac{x}{\mu p}\right) + \left(\mu p - x + \frac{1}{2}\right) \log\left(1 - \frac{x}{\mu p}\right) \\ & + \left(\mu q + x + \frac{1}{2}\right) \log\left(1 + \frac{x}{\mu q}\right) + \left(\mu q - x + \frac{1}{2}\right) \log\left(1 - \frac{x}{\mu q}\right). \end{aligned} \]

On trouve, en dérivant deux fois par rapport à \(x\),

\[ \begin{aligned} v' = {} & \log\left(1 + \frac{x}{\mu p}\right) - \log\left(1 - \frac{x}{\mu p}\right) + \frac{1}{2}\left(\frac{1}{\mu p + x} - \frac{1}{\mu p - x}\right) \\ & + \log\left(1 + \frac{x}{\mu q}\right) - \log\left(1 - \frac{x}{\mu q}\right) + \frac{1}{2}\left(\frac{1}{\mu q + x} - \frac{1}{\mu q - x}\right); \end{aligned} \]

\[ \begin{aligned} v'' = {} & \frac{1}{\mu p + x} + \frac{1}{\mu p - x} - \frac{1}{2} \frac{1}{(\mu p + x)^{2}} - \frac{1}{2} \frac{1}{(\mu p - x)^{2}} \\ & + \frac{1}{\mu q + x} + \frac{1}{\mu q - x} - \frac{1}{2} \frac{1}{(\mu q + x)^{2}} - \frac{1}{2} \frac{1}{(\mu q - x)^{2}}. \end{aligned} \]

[p. 11] La dérivée \(v''\) est inférieure au second membre où l'on ne laisse que les termes positifs. On a donc

\[ \begin{aligned} v'' &< \frac{1}{\mu p + x} + \frac{1}{\mu p - x} + \frac{1}{\mu q + x} + \frac{1}{\mu q - x} \\ &= \frac{2\mu p}{\mu^{2}p^{2} - x^{2}} + \frac{2\mu q}{\mu^{2}q^{2} - x^{2}}. \end{aligned} \]

Or

\[ \begin{aligned} \frac{2\mu p}{\mu^{2}p^{2} - x^{2}} &= \frac{2}{\mu p} \frac{1}{1 - \frac{x^{2}}{\mu^{2}p^{2}}} = \frac{2}{\mu p} \left[1 + \frac{x^{2}}{\mu^{2}p^{2}} + \frac{x^{4}}{\mu^{4}p^{4}} + \cdots\right] \\ &= \frac{2}{\mu p} + \frac{2x^{2}}{\mu^{3}p^{3}} \left[1 + \frac{x^{2}}{\mu^{2}p^{2}} + \frac{x^{4}}{\mu^{4}p^{4}} + \cdots\right]. \end{aligned} \]

Puisque \(x\) a tout au plus la valeur \(\mu l\) égale ou inférieure à \(\frac{1}{2}\mu p\), de sorte que \(\frac{x^{2}}{\mu^{2}p^{2}}\) est égale ou inférieure à \(\frac{1}{4}\), on a

\[ \frac{2\mu p}{\mu^{2}p^{2} - x^{2}} \mathrel{\overset{=}{<}} \frac{2}{\mu p} + \frac{2x^{2}}{\mu^{3}p^{3}} \left[1 + \frac{1}{4} + \frac{1}{16} + \cdots\right] = \frac{2}{\mu p} + \frac{8}{3} \frac{x^{2}}{\mu^{3}p^{3}}. \]

De même,

\[ \frac{2\mu q}{\mu^{2}q^{2} - x^{2}} \mathrel{\overset{=}{<}} \frac{2}{\mu q} + \frac{8}{3} \frac{x^{2}}{\mu^{3}q^{3}}. \]

Par suite,

\[ v'' > \frac{2}{\mu p} + \frac{2}{\mu q} + \frac{8}{3} \frac{x^{2}}{\mu^{3}p^{3}} + \frac{8}{3} \frac{x^{2}}{\mu^{3}q^{3}} = \frac{2}{\mu pq} + \frac{8}{3} \frac{x^{2}(p^{3} + q^{3})}{\mu^{3}p^{3}q^{3}}, \]

et, puisque \(p^{3} + q^{3}\) est inférieur à \((p + q)^{3} = 1\),

\[ v' < \frac{2}{\mu pq} + \frac{8}{3} \frac{x^{2}}{\mu^{3}p^{3}q^{3}}. \]

[p. 12] On déduit de là, en intégrant deux fois de 0 à \(x\),

\[ v' < \frac{2x}{\mu pq} + \frac{8}{9} \frac{x^{3}}{\mu^{3}p^{3}q^{3}}, \qquad v < \frac{x^{2}}{\mu pq} + \frac{2}{9} \frac{x^{4}}{\mu^{3}p^{3}q^{3}}, \]

puis,

\[ -\frac{v}{2} > -\frac{x^{2}}{2\mu pq} - \frac{1}{9} \frac{x^{4}}{\mu^{3}p^{3}q^{3}}, \]

\[ y_{x} = e^{-\frac{v}{2}} > e^{-\frac{x^{2}}{2\mu pq} - \frac{1}{9} \frac{x^{4}}{\mu^{3}p^{3}q^{3}}}, \]

et, d'après (5),

\[ y_{x} > z_{x}, \]

si l'on pose

\[ z_{x} = e^{-\frac{x^{2}}{2\mu pq}} \left(1 - \frac{1}{9} \frac{x^{4}}{\mu^{3}p^{3}q^{3}}\right). \]

Si l'on introduit \(z_{x}\) à la place de \(y_{x}\) dans l'inégalité relative à P donnée au début de ce numéro, elle devient

\[ \mathrm{P} > \left(1 - \frac{1}{6\mu pq}\right) \frac{2}{\sqrt{2\pi \mu pq}} \mathop{\mathrm{S}}\limits_{x=1}^{x=\mu l} z_{x}. \]

Pour \(x = 0\), \(z_{0} = 1\) ; pour \(x\) croissant, \(z_{x}\) décroît. On a donc, d'après la formule (9), en observant d'ailleurs que \(\mathrm{E}(\mu l) + 1\) surpasse \(\mu l\),

\[ z_{0} + \mathop{\mathrm{S}}\limits_{x=1}^{x=\mathrm{E}(\mu l)} z_{x} > \int_{0}^{\mathrm{E}(\mu l)+1} z_{x}\,dx > \int_{0}^{\mu l} z_{x}\,dx, \]

\[ \mathop{\mathrm{S}}\limits_{x=1}^{x=\mathrm{E}(\mu l)} z_{x} > \int_{0}^{\mu l} z_{x}\,dx - 1. \]

Donc enfin

\[ \mathrm{P} > \left[1 - \frac{1}{6\mu pq}\right] \frac{2}{\sqrt{2\pi \mu pq}} \left\{ \int_{0}^{\mu l} z_{x}\,dx - 1 \right\}. \]

[p. 13] **7.** *Première estimation de la limite inférieure de* P. On a

\[ \begin{aligned} \int_{0}^{\mu l} z_{x}\,dx &= \int_{0}^{\mu l} e^{-\frac{x^{2}}{2\mu pq}} \left(1 - \frac{1}{9} \frac{x^{4}}{\mu^{3}p^{3}q^{3}}\right) dx \\ &> \int_{0}^{\mu l} e^{-\frac{x^{2}}{2\mu pq}}\,dx - \frac{1}{9} \int_{0}^{\infty} e^{-\frac{x^{2}}{2\mu pq}} \frac{x^{4}}{\mu^{3}p^{3}q^{3}}\,dx. \end{aligned} \]

Posons

\[ \frac{x^{2}}{2\mu pq} = t^{2}, \qquad \frac{\mu^{2}l^{2}}{2\mu pq} = \mathrm{T} \quad \text{ ou } \quad \mathrm{T} = l\sqrt{\frac{\mu}{2pq}}. \]

La première intégrale du second membre de la dernière égalité deviendra

\[ \sqrt{2\mu pq} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt. \]

La seconde prendra la forme

\[ \frac{4}{9\mu pq} \sqrt{2\mu pq} \int_{0}^{\infty} e^{-t^{2}} t^{4}\,dt, \]

et est égale, d'après la formule (8), à

\[ \frac{4}{9\mu pq} \sqrt{2\mu pq} \cdot \frac{3}{8} \sqrt{\pi} = \frac{1}{6} \frac{\sqrt{2\pi \mu pq}}{\mu pq}. \]

Donc enfin

\[ \int_{0}^{\mu l} z_{x}\,dx > \sqrt{2\mu pq} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt - \frac{1}{6} \frac{\sqrt{2\pi \mu pq}}{\mu pq}. \]

Il en résulte, pour P, d'après la dernière formule du n<sup>o</sup> 6, la relation

\[ \mathrm{P} > \left[1 - \frac{1}{6\mu pq}\right] \left\{ \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt - \frac{1}{3\mu pq} - \frac{2}{\sqrt{2\pi \mu pq}} \right\} \]

[p. 14] et, *à fortiori*,

\[ \mathrm{P} > \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt - \frac{1}{6\mu pq} \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt - \frac{1}{3\mu pq} - \frac{2}{\sqrt{2\pi \mu pq}}. \]

Or, on a

\[ \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt < \frac{2}{\sqrt{\pi}} \int_{0}^{\infty} e^{-t^{2}}\,dt = 1. \]

Donc enfin,

\[ \mathrm{P} > \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt - \frac{1}{6\mu pq} - \frac{1}{3\mu pq} - \frac{2}{\sqrt{2\pi \mu pq}}, \]

ou

\[ \mathrm{P} > \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt - \frac{1}{2\mu pq} - \frac{2}{\sqrt{2\pi \mu pq}}. \]

**8.** *Seconde estimation de la limite inférieure de* P. Si \(\mu\) est au moins égal à 10, on a

\[ \frac{1}{2\mu pq} < \frac{1}{\sqrt{2\pi \mu pq}}. \]

En effet, cette inégalité équivaut à la suivante :

\[ \pi < 2\mu pq. \]

Or, d'après (10), \(\mu q = 2 + \delta\), \(\delta\) étant positif ou nul, \(p = 1 - q = 1 - \frac{2 + \delta}{\mu}\). Par suite, l'inégalité à vérifier devient

\[ \pi < 2(2 + \delta)\left(1 - \frac{2 + \delta}{\mu}\right) = 2\mu.\, \frac{2 + \delta}{\mu} \left(1 - \frac{2 + \delta}{\mu}\right). \]

Le produit du second membre est minimum quand les deux derniers facteurs diffèrent le plus possible. La différence entre ces [p. 15] deux facteurs est \(1 - 2\,\frac{2 + \delta}{\mu}\) dont la valeur maxima correspond à \(\delta = 0\). Alors \(q = \frac{2}{\mu}\), \(p = 1 - \frac{2}{\mu}\), et l'on a

\[ 2\mu pq = 4\left(1 - \frac{2}{\mu}\right). \]

Cette dernière expression, pour \(\mu \mathrel{\overset{=}{>}} 10\) (hypothèse dont nous ne nous servons qu'ici) a une valeur égale ou supérieure à \(4\left(1 - \frac{2}{10}\right)\) ou \(3\frac{1}{5}\), donc supérieure à \(\pi\). On a donc

\[ \frac{1}{2\mu pq} < \frac{1}{\sqrt{2\pi\mu pq}}, \]

et, par suite, la dernière inégalité du n<sup>o</sup> précédent donne

\[ \mathrm{P} > \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt - \frac{3}{\sqrt{2\mu pq}}. \]

**9.** *Théorème de Jacques Bernoulli*. On a évidemment

\[ \mathrm{P} < (p + q)^{\mu} = 1. \]

Pour \(\mu\) croissant indéfiniment, T croît aussi indéfiniment ; on déduit des inégalités

\[ 1 > \mathrm{P} > \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt - \frac{3}{\sqrt{2\mu pq}} \]

pour \(\mu = \infty\),

\[ \lim \mathrm{P} = \frac{2}{\sqrt{\pi}} \int_{0}^{\infty} e^{-t^{2}}\,dt = 1, \]

c'est-à-dire le théorème de Jacques Bernoulli.

[p. 16]

[^1-a]: Nous avons publié une esquisse de la présente démonstration dans les Akten des fünften internationalen Kongresses katholischer Gelehrten zu München von 24. bis 28. september 1900 (München, 1901, Herder und Co.) pp. 427 et 428. Laplace (*Théorie analytique des probabilités*, Livre II, n° 16, pp. 275-284 de la troisième édition) donne des limites plus rapprochées que les nôtres, mais il n'a pas vraiment évalué les termes qu'il néglige. Il se contente de dire (p. 279) : “ Il serait facile, par l'analyse précédente, d'avoir égard aux termes de l'ordre \(\frac{1}{n}\) et des ordres supérieurs „. En réalité, ce n'est pas du tout facile.

[^7-a]: La démonstration du théorème de Bernoulli ne repose nullement sur cette remarque curieuse, mais, comme on le voit, assez difficile à démontrer.

[^10-a]: Nous avons déjà fait connaître cette transformation dans les Annales de la Société scientifique de Bruxelles, 1892, t. XVI, 1<sup>re</sup> partie, pp. 85-87, ou dans nos *Mélanges mathématiques* (1883-1898), pp. 79-80.

### Note sur la valeur approchée de \(t_{\mu p \pm x}\)

Dans les traités de Calcul des probabilités, on admet que l'on a très approximativement, pour de grandes valeurs de \(\mu\),

\[ t_{\mu p+x} = t_{\mu p-x} = e^{-\frac{x^{2}}{2\mu pq}}. \]

Nous allons chercher une limite supérieure et une limite inférieure de ces expressions afin de voir jusqu'à quel point est justifiée l'approximation dont il vient d'être question.

I. *Limites de* \(\left(1 + \frac{x}{\mu p}\right)^{-\frac{1}{2}}\), \(\left(1 + \frac{x}{\mu q}\right)^{-\frac{1}{2}}\). Les valeurs extrêmes de \(\frac{x}{\mu p}\), \(\frac{x}{\mu q}\) sont 0 et \(\frac{1}{2}\), cette dernière valeur correspondant au cas où \(2x = p = q = 2l\). Cherchons quelle valeur on peut donner à \(j\) et \(k\) dans la double égalité

\[ 1 - j\epsilon \mathrel{\overset{=}{>}} (1 + \epsilon)^{-\frac{1}{2}} \mathrel{\overset{=}{>}} 1 - k\epsilon \]

\(\epsilon\), quantité inférieure ou égale à \(\frac{1}{2}\), représentant \(\frac{x}{\mu p}\) ou \(\frac{x}{\mu q}\).

La première inégalité devient successivement

\[ 1 \mathrel{\overset{=}{<}} (1 + \epsilon)(1 - 2j\epsilon + j^{2}\epsilon^{2}) = 1 + \epsilon(1 - 2j) + \epsilon^{2}(-2j + j^{2}) + j^{2}\epsilon^{3} \]

\[ 0 \mathrel{\overset{=}{<}} 1 - 2j + j\epsilon(-2 + j) + j^{2}\epsilon^{2} = 1 - 2j - j\epsilon(2 - j - j\epsilon). \]

On voit d'abord que \(j\) ne peut surpasser \(\frac{1}{2}\). La valeur minima du second membre, pour une valeur donnée de \(j\), correspond à la valeur maxima de \(j\epsilon(2 - j - j\epsilon)\), laquelle s'obtient en donnant à \(\epsilon\) sa valeur maxima \(\frac{1}{2}\). L'inégalité devient alors

\[ 0 \mathrel{\overset{=}{<}} 1 - 2j - \frac{1}{2}j\left(2 - j - \frac{1}{2}j\right) = 1 - 3j + \frac{3}{4}j^{2}. \]

On peut supposer \(j = \frac{1}{3}\), ou même un peu plus grand.

[p. 17] La seconde inégalité devient de même

\[ 1 \mathrel{\overset{=}{>}} (1 + \epsilon)(1 - k\epsilon)^{2} = 1 + \epsilon(1 - 2k) + \epsilon^{2}(-2k + k^{2}) + k^{2}\epsilon^{3}, \]

\[ 0 \mathrel{\overset{=}{>}} 1 - 2k - k\epsilon(2 - k - k\epsilon). \]

Si l'on fait \(k = \frac{1}{2}\), l'inégalité est vérifiée pour toutes les valeurs de \(\epsilon\) de 0 à \(\frac{1}{2}\) ; pour \(k < \frac{1}{2}\), l'inégalité n'est plus vérifiée quand \(\epsilon\) est très petit. La valeur \(k = \frac{1}{2}\) est donc la plus petite que l'on puisse donner à \(k\).

Nous écrirons donc

\[ 1 - \frac{1}{3}\epsilon \mathrel{\overset{=}{>}} (1 + \epsilon)^{-\frac{1}{2}} \mathrel{\overset{=}{>}} 1 - \frac{1}{2}\epsilon, \]

\[ 1 - \frac{1}{3}\frac{x}{\mu p} \mathrel{\overset{=}{>}} \left(1 + \frac{x}{\mu p}\right)^{-\frac{1}{2}} \mathrel{\overset{=}{>}} 1 - \frac{1}{2}\frac{x}{\mu p}, \]

\[ 1 - \frac{1}{3}\frac{x}{\mu q} \mathrel{\overset{=}{>}} \left(1 + \frac{x}{\mu q}\right)^{-\frac{1}{2}} \mathrel{\overset{=}{>}} 1 - \frac{1}{2}\frac{x}{\mu q}. \]

II. *Limites de* \(\left(1 - \frac{x}{\mu p}\right)^{-\frac{1}{2}}\), \(\left(1 - \frac{x}{\mu q}\right)^{-\frac{1}{2}}\). On trouve, de même, par les calculs élémentaires que nous supprimons. pour abréger,

\[ 1 + \frac{5}{6}\epsilon \mathrel{\overset{=}{>}} (1 - \epsilon)^{-\frac{1}{2}} \mathrel{\overset{=}{>}} 1 + \frac{1}{2}\epsilon, \]

\[ 1 + \frac{5}{6}\frac{x}{\mu p} \mathrel{\overset{=}{>}} \left(1 - \frac{x}{\mu p}\right)^{-\frac{1}{2}} \mathrel{\overset{=}{>}} 1 + \frac{1}{2}\frac{x}{\mu p}, \]

\[ 1 + \frac{5}{6}\frac{x}{\mu q} \mathrel{\overset{=}{>}} \left(1 - \frac{x}{\mu q}\right)^{-\frac{1}{2}} \mathrel{\overset{=}{>}} 1 + \frac{1}{2}\frac{x}{\mu q}. \]

III. *Limites de* \(w_{1} = (\mu p + x) \log\left(1 + \frac{x}{\mu q}\right) + (\mu p - x)\). [p. 18] \(\log\left(1 - \frac{x}{\mu q}\right)\), \(x\) *étant nul ou positif*. On trouve, pour les dérivées première et seconde de \(w_{1}\),

\[ w_{1}' = \log\left(1 + \frac{x}{\mu p}\right) - \log\left(1 - \frac{x}{\mu q}\right), \]

\[ w_{1}'' = \frac{1}{\mu p + x} + \frac{1}{\mu q - x}. \]

Or

\[ \begin{aligned} \frac{1}{\mu p + x} &= \frac{1}{\mu p} \frac{1}{1 + \frac{x}{\mu p}} = \frac{1}{\mu p} \left[1 - \frac{x}{\mu p} + \frac{x^{2}}{\mu p(\mu p + x)}\right] \\ &= \frac{1}{\mu p} - \frac{x}{\mu^{2}p^{2}} + \frac{x^{2}}{\mu^{2}p^{2}(\mu p + x)}. \end{aligned} \]

Mais \(\mu p + x\) est compris entre \(\mu p\) et \(\mu p + \frac{1}{2}\mu p\) ; donc

\[ \begin{aligned} \frac{1}{\mu p + x} &< \frac{1}{\mu p} - \frac{x}{\mu^{2}p^{2}} + \frac{x^{2}}{\mu^{3}p^{3}}, \\ \frac{1}{\mu p + x} &> \frac{1}{\mu p} - \frac{x}{\mu^{2}p^{2}} + \frac{2}{3} \frac{x^{2}}{\mu^{3}p^{3}}. \end{aligned} \]

De même,

\[ \frac{1}{\mu q - x} = \frac{1}{\mu q} + \frac{x}{\mu^{2}q^{2}} + \frac{x^{2}}{\mu^{2}q^{2}(\mu q - x)}. \]

L'expression \(\mu q - x\) est comprise entre \(\mu q - \frac{1}{2}\mu q\) et \(\mu q\) ; donc

\[ \begin{aligned} \frac{1}{\mu q - x} &< \frac{1}{\mu q} + \frac{x}{\mu^{2}q^{2}} + 2\frac{x^{2}}{\mu^{3}q^{3}}, \\ \frac{1}{\mu q - x} &> \frac{1}{\mu q} + \frac{x}{\mu^{2}q^{2}} + \frac{x^{2}}{\mu^{3}q^{3}}. \end{aligned} \]

De ces diverses inégalités, on tire

\[ \begin{aligned} w_{1}'' &< \frac{1}{\mu p} - \frac{x}{\mu^{2}p^{2}} + \frac{x^{2}}{\mu^{3}q^{3}} + \frac{1}{\mu q} + \frac{x}{\mu^{2}q^{2}} + 2\frac{x^{2}}{\mu^{3}q^{3}} \\ &= \frac{1}{\mu pq} + \frac{x^{2}}{\mu^{2}p^{2}q^{2}}(p - q) + \frac{x^{2}}{\mu^{3}p^{3}q^{3}}(2p^{3} + q^{3}); \end{aligned} \]

[p. 19]

\[ w_{1}'' > \frac{1}{\mu p} - \frac{x}{\mu^{2}p^{2}} + \frac{2}{3} \frac{x^{2}}{\mu^{3}p^{3}} + \frac{1}{\mu q} + \frac{x}{\mu^{2}q^{2}} + \frac{x^{2}}{\mu^{3}q^{3}} \]

\[ = \frac{1}{\mu pq} + \frac{x}{\mu^{2}p^{2}q^{2}} (p - q) + \frac{x^{2}}{\mu^{3}p^{3}q^{3}} \left(p^{3} + \frac{2}{3} q^{3}\right). \]

On déduit de là, en intégrant deux fois de 0 à \(x\), \(w_{1}'\) et \(w_{1}\) étant nuls pour \(x = 0\),

\[ w_{1} < \frac{x^{2}}{2\mu pq} + \frac{x^{3}}{6\mu^{2}p^{2}q^{2}} (p - q) + \frac{x^{4}}{12\mu^{3}p^{3}q^{3}} (2p^{3} + q^{3}); \]

\[ w_{1} > \frac{x^{2}}{2\mu pq} + \frac{x^{3}}{6\mu^{2}p^{2}q^{2}} (p - q) + \frac{x^{4}}{12\mu^{3}p^{3}q^{3}} \left(p^{3} + \frac{2}{3} q^{3}\right). \]

IV. *Limites* de \(w_{2} = (\mu p - x) \log\left(1 - \frac{x}{\mu p}\right) + (\mu q + x) \cdot \log\left(1 + \frac{x}{\mu q}\right)\), \(x\) *étant positif*. On trouve de même, en changeant \(p\) en \(q\) et \(q\) en \(p\), dans les calculs précédents,

\[ w_{2} < \frac{x^{2}}{2\mu pq} - \frac{x^{3}}{6\mu^{2}p^{2}q^{2}} (p - q) + \frac{x^{4}}{12\mu^{3}p^{3}q^{3}} (p^{3} + 2q^{3}); \]

\[ w_{2} > \frac{x^{2}}{2\mu pq} - \frac{x^{3}}{6\mu^{2}p^{2}q^{2}} (p - q) + \frac{x^{4}}{12\mu^{3}p^{3}q^{3}} \left(\frac{2}{3} p^{3} + q^{3}\right). \]

V. *Limites de* \(t_{\mu p+x}\), \(t_{\mu p-x}\). On a d'abord

\[ t_{\mu p+x} = \left(1 + \frac{x}{\mu p}\right)^{-\mu p + q - \frac{1}{2}} \left(1 - \frac{x}{\mu q}\right)^{-\mu p - q - \frac{1}{2}} \]

\[ = \left(1 + \frac{x}{\mu p}\right)^{-\frac{1}{2}} \left(1 - \frac{x}{\mu q}\right)^{-\frac{1}{2}} e^{-w_{1}}. \]

Par suite, d'après I, II, III,

\[ t_{\mu p-x} < \left(1 - \frac{1}{3} \frac{x}{\mu p}\right) \left(1 + \frac{5}{6} \frac{x}{\mu q}\right) \]

\[ \times e^{-\frac{x^{2}}{2\mu pq} - \frac{x^{3}}{6\mu^{2}p^{2}q^{2}} (p - q) - \frac{x^{4}}{12\mu^{3}p^{3}q^{3}} \left(p^{3} + \frac{2}{3} q^{3}\right)} \]

\[ > \left(1 - \frac{1}{2} \frac{x}{\mu p}\right) \left(1 + \frac{1}{2} \frac{x}{\mu q}\right) \]

\[ \times e^{-\frac{x^{2}}{2\mu pq} - \frac{x^{2}}{6\mu^{2}p^{2}q^{2}} (p - q) - \frac{x^{4}}{12\mu^{3}p^{3}q^{3}} (2p^{3} + q^{3})}. \]

[p. 20] De même,

\[ t_{\mu p-x} = \left(1 - \frac{x}{\mu p}\right)^{-\mu p + q - \frac{1}{2}} \left(1 + \frac{x}{\mu q}\right)^{-\mu p - q - \frac{1}{2}} \]

\[ = \left(1 - \frac{x}{\mu p}\right)^{-\frac{1}{2}} \left(1 + \frac{x}{\mu q}\right)^{-\frac{1}{2}} e^{-w_{2}}. \]

Par conséquent, d'après I, II, IV,

\[ t_{\mu p-x} < \left(1 + \frac{5}{6} \frac{x}{\mu p}\right) \left(1 - \frac{1}{3} \frac{x}{\mu q}\right) \]

\[ \times e^{-\frac{x^{2}}{2\mu pq} + \frac{x^{3}}{6\mu^{2}p^{2}q^{2}} (p - q) - \frac{x^{4}}{12\mu^{3}p^{3}q^{3}} \left(\frac{2}{3} p^{3} + q^{3}\right)} \]

\[ > \left(1 + \frac{1}{2} \frac{x}{\mu p}\right) \left(1 - \frac{1}{2} \frac{x}{\mu q}\right) \]

\[ \times e^{-\frac{x^{2}}{2\mu px} + \frac{x^{3}}{6\mu^{2}p^{2}q^{2}} (p - q) - \frac{x^{4}}{12\mu^{3}p^{3}q^{3}} (p^{3} + 2q^{3})}. \]

VI. *Conclusion*. On voit d'après ces calculs combien il est difficile de justifier la formule classique

\[ t_{\mu p\pm x} = e^{-\frac{x^{2}}{2\mu pq}}. \]

Pour qu'elle soit admissible, il faut supposer : 1° \(\frac{x}{\mu p}\), \(\frac{x}{\mu q}\) très petits comparés à l'unité, c'est-à-dire que \(\frac{l}{p}\), \(\frac{l}{q}\) soient des fractions très petites puisque \(x\) peut prendre la valeur extrême \(\mu l\) ; 2° \(\frac{x^{2}}{\mu^{2}p^{2}q^{2}}\) doit être très petit comparé à \(\frac{x^{2}}{\mu pq}\), ou \(\frac{x}{\mu pq}\) comparé à 1, c'est-à-dire que \(\frac{l}{pq}\) doit aussi être une fraction très petite.

En résumé, comme la seconde condition implique la première, on doit supposer \(l\) très petit par rapport à \(pq\).

[p. 21]

## Sur une intégrale considérée en calcul des probabilités

On peut trouver une valeur approchée de l'expression

\[ \mathrm{P} = \int_{\frac{m}{\mu} - l}^{\frac{m}{\mu} + l} z^{m} (1 - z)^{n} \, dz : \int_{0}^{1} z^{m} (1 - z)^{n} \, dz, \]

de la manière suivante. Posons pour abréger,

\[ p = \frac{m}{\mu}, \qquad q = 1 - p = \frac{n}{\mu}, \]

puis, faisons dans la première intégrale,

\[ z = p + x, \qquad 1 - z = q - x. \]

Cette intégrale deviendra

\[ \int_{-l}^{+l} (p + x)^{m} (q - x)^{n} \, dx = p^{m} q^{n} \int_{-l}^{+l} \left(1 + \frac{x}{p}\right)^{m} \left(1 - \frac{x}{q}\right)^{n} \, dx. \]

Pour fixer les idées, nous supposons \(l\) tout au plus égal à la moitié de \(q\) et \(p\) égal ou supérieur à \(q\).

On a, comme on sait,

\[ \left(1 + \frac{x}{p}\right)^{m} \left(1 - \frac{x}{q}\right)^{n} + \left(1 - \frac{x}{p}\right)^{m} \left(1 + \frac{x}{q}\right)^{n} \]

\[ \mathrel{\overset{=}{>}} 2 \sqrt{\left(1 - \frac{x^{2}}{p^{2}}\right)^{m} \left(1 - \frac{x^{2}}{q^{2}}\right)^{n}} \]

\[ = 2e^{\frac{1}{2} \mu p \log\left(1 - \frac{x^{2}}{p^{2}}\right) + \frac{1}{2} \mu q \log\left(1 - \frac{x^{2}}{q^{2}}\right)}. \]

Or, si \(\alpha\) est inférieur à l'unité,

\[ l(1 - \alpha) > -\alpha - \frac{\alpha^{2}}{2(1 - \alpha)}. \]

[p. 22] Donc

\[ \frac{1}{2} \mu p \log\left(1 - \frac{x^{2}}{p^{2}}\right) + \frac{1}{2} \mu q \log\left(1 - \frac{x^{2}}{q^{2}}\right) \]

surpasse

\[ \frac{1}{2} \mu p \left[-\frac{x^{2}}{p^{2}} - \frac{x^{4}}{2p^{4}\left(1 - \frac{x^{2}}{p^{2}}\right)}\right] + \frac{1}{2} \mu q \left[-\frac{x^{2}}{q^{2}} - \frac{x^{4}}{2q^{4}\left(1 - \frac{x^{2}}{q^{2}}\right)}\right] \]

\[ = -\frac{\mu x^{2}}{2p} - \frac{\mu x^{4}}{4p(p^{2} - x^{2})} - \frac{\mu x^{2}}{2q} - \frac{\mu x^{4}}{4q(q^{2} - x^{2})} \]

\[ = -\frac{\mu x^{2}}{2pq} - \frac{\mu x^{4}}{4} \left\{\frac{1}{p(p^{2} - x^{2})} + \frac{1}{q(q^{2} - x^{2})}\right\}. \]

On a

\[ \frac{1}{p(p^{2} - x^{2})} + \frac{1}{q(q^{2} - x^{2})} \]

\[ = \frac{p^{3} + q^{3} - x^{2}}{pq(p^{2} - x^{2})(q^{2} - x^{2})} < \frac{1}{pq(p^{2} - l^{2})(q^{2} - l^{2})}. \]

Par conséquent, on a

\[ \sqrt{\left(1 - \frac{x^{2}}{p^{2}}\right)^{m} \left(1 - \frac{x^{2}}{q^{2}}\right)^{n}} > e^{-\frac{\mu x^{2}}{2pq}} e^{-\frac{\mu x^{4}}{4pq(p^{2} - l^{2})(q^{2} - l^{2})}} \]

et, puisque \(e^{-\alpha}\) est \(> 1 - \alpha\),

\[ \sqrt{\left(1 - \frac{x^{2}}{p^{2}}\right)^{m} \left(1 - \frac{x^{2}}{q^{2}}\right)^{n}} > e^{-\frac{\mu x^{2}}{2pq}} \left(1 - \frac{\mu x^{4}}{4pq(p^{2} - l^{2})(q^{2} - l^{2})}\right). \]

Il en résulte que l'on a

\[ \mathrm{P} > \frac{p^{m} q^{n} \int_{-l}^{+l} e^{-\frac{\mu x^{2}}{2pq}} \left(1 - \frac{\mu x^{4}}{4pq(p^{2} - l^{2})(q^{2} - l^{2})}\right) dx}{\int_{0}^{1} z^{m} (1 - z)^{n} \, dz}. \]

L'intégrale eulérienne du dénominateur est égale à

\[ \frac{\Gamma(m + 1)\Gamma(n + 1)}{\Gamma(\mu + 2)} = \frac{1.\,2.\,3.\,\ldots\,m.\,1.\,2.\,\ldots\,n}{1.\,2.\,3.\,\ldots\,\mu} \cdot \frac{1}{\mu + 1}. \]

[p. 23] Posons dans l'intégrale du numérateur,

\[ \frac{\mu x^{2}}{2pq} = t^{2}, \qquad \mathrm{T} = l \sqrt{\frac{\mu}{2pq}}, \]

elle deviendra

\[ \sqrt{\frac{2pq}{\mu}} \int_{-\mathrm{T}}^{+\mathrm{T}} e^{-t^{4}} \, dt \left(1 - t^{2} \frac{pq}{\mu(p^{2} - l^{2})(q^{2} - l^{2})}\right) \]

supérieure à

\[ \sqrt{\frac{2pq}{\mu}} \int_{-\mathrm{T}}^{+\mathrm{T}} e^{-t^{2}} \, dt - \sqrt{\frac{2pq}{\mu}} \frac{pq}{\mu(p^{2} - l^{2})(q^{2} - l^{2})} \int_{-\infty}^{+\infty} e^{-t^{2}} t^{4} \, dt. \]

Or, en faisant \(t = \sqrt{u}\), on trouve

\[ \int_{-\infty}^{+\infty} e^{-t^{2}} t^{4} \, dt = \frac{1}{2} \int_{-\infty}^{+\infty} e^{-u} u^{\frac{3}{2}} \, du = \Gamma\left(\frac{5}{2}\right) = \frac{5}{2} \cdot \frac{3}{2} \Gamma\left(\frac{1}{2}\right) = \frac{15}{4} \sqrt{\pi}. \]

On a donc enfin

\[ \mathrm{P} > \frac{1.\,2.\,3.\,\ldots\,\mu}{1.\,2.\,3.\,\ldots\,m.\,1.\,2.\,\ldots\,n} p^{m} q^{n} \frac{\mu + 1}{\mu} \sqrt{2\mu pq} \]

\[ \times \left\{2 \int_{0}^{\mathrm{T}} e^{-t^{2}} \, dt - \frac{15}{4} \frac{\sqrt{\pi}\, pq}{\mu(p^{2} - l^{2})(q^{2} - l^{2})}\right\}. \]

Au moyen de la formule de Stirling, on prouve assez facilement l'inégalité suivante :

\[ \frac{1.\,2.\,3.\,\ldots\,\mu}{1.\,2.\,3.\,\ldots\,m.\,1.\,2.\,\ldots\,n.} p^{m} q^{n} > \frac{1}{\sqrt{2\pi\mu pq}} \left(1 - \frac{1}{12\mu(p + l)(q - l)}\right). \]

Le facteur qui précède la parenthèse dans l'inégalité relative à P, est donc supérieur à

\[ \frac{\mu + 1}{\mu} \frac{1}{\sqrt{\pi}} \left[1 - \frac{1}{12\mu(p + l)(q - l)}\right] \]

\[ > \frac{1}{\sqrt{\pi}} \left[1 - \frac{1}{12\mu(p + l)(q + l)}\right]. \]

[p. 24] On a donc

\[ \mathrm{P} > \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}} \, dt \]

\[ - \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}} \, dt.\, \frac{1}{12\mu(p + l)(q - l)} - \frac{15pq}{4\mu(p^{2} - l^{2})(q^{2} - l^{2})}. \]

Or

\[ \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}} \, dt < \frac{2}{\sqrt{\pi}} \int_{0}^{\infty} e^{-t^{2}} \, dt = 1, \]

\[ 12(p + l)(q - l) > 12\left(p + \frac{1}{2} q\right)\left(q - \frac{1}{2} q\right) = 3(1 + p) q > 6pq, \]

\[ (p^{2} - l^{2})(q^{2} - l^{2}) > \left(p^{2} - \frac{1}{4} p^{2}\right)\left(q^{2} - \frac{1}{4} q^{2}\right) = \frac{9}{16} p^{2} q^{2}. \]

Par suite,

\[ \mathrm{P} > \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}} \, dt - \frac{1}{6\mu pq} - \frac{15pq.\,16}{4\mu.\,9.\,p^{2}q^{2}} \]

\[ = \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}} \, dt - \frac{1}{6\mu pq} - \frac{20}{3\mu pq}. \]

Comme

\[ \frac{1}{6} + \frac{20}{3} = \frac{41}{6} \]

est inférieur à 7, on a enfin

\[ \mathrm{P} > \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}} \, dt - \frac{7}{\mu pq}. \]

[p. 25]

## SUR LA LOI DES GRANDS NOMBRES DE POISSON

par

Paul MANSION

Professeur à l'Université de Gand[^25-a]

**1.** *Bertrand, Bienaymé, Meyer* et *Czuber sur la* Loi des grands nombres *de Poisson*. La *loi des grands nombres* exposée par Poisson dans ses *Recherches sur la probabilité des jugements en matière civile et criminelle* (Paris, Bachelier, 1837)[^25-aa] a été vivement critiquée par Bertrand et Bienaymé.

“ Lorsque la probabilité d'un événement est variable d'une épreuve à l'autre, dit Bertrand (*Calcul des probabilités*, Paris, Gauthier-Villars et fils, 1889, p. 94), le théorème de Bernoulli n'est plus applicable. La généralisation proposée par Poisson sous le nom de *loi des grands nombres* manque non seulement de rigueur, mais de précision. Les conditions supposées dans l'énoncé échappent par le vague à toute appréciation mathématique. „ Poisson, dit-il ailleurs (p. XXXII), “ a, à peu près seul, je crois, attaché une grande importance „ à sa découverte “ qui se distingue bien peu des lois connues du hasard „.

Bienaymé a lu à l'Académie des Sciences morales et politiques le 10 février 1855, et publié en 1870 (Paris, Anger) une note pédantesque de 12 pages in-8°, intitulée : *Sur un principe que M. Poisson avait cru découvrir et qu'il avait appelé* Loi des grands nombres. Poisson, suivant Bienaymé, “ a simplement démontré le théorème de Jacques Bernoulli dans l'hypothèse où la probabilité constante est la valeur moyenne d'un ensemble de probabilités variables qui peuvent s'offrir toutes à toutes les épreuves : hypothèse si évidente qu'il n'est pas nécessaire de la démontrer. „ (p. 9).

[p. 26] “ L'identité d'une probabilité constante et de la probabilité moyenne d'un certain nombre de probabilités qui peuvent régir une épreuve quelconque, avait paru jusqu'à ces derniers temps d'une évidence complète. C'est même ainsi que Jacques Bernoulli a entendu sa probabilité unique. On peut s'en assurer en lisant ce qu'il en a dit dans le préambule de son théorème „ (p. 6-7).

Les deux géomètres qui, dans le dernier demi-siècle, ont étudié le plus minutieusement, dans toute son étendue, le calcul des probabilités, A. Meyer et Czuber, ne jugent pas aussi durement les recherches de Poisson.

A. Meyer (*Cours de calcul des probabilités publié par Folie*, Bruxelles, Hayez, 1874 ; ou 2<sup>e</sup> série, t. IV des *Mémoires de la Société royale des Sciences de Liége* ; voir pp. 95-115) reproduit sans la critiquer la démonstration de Poisson.

Czuber analyse les recherches de Poisson dans son savant ouvrage : *Die Entwicklung der Wahrscheinlichkeitstheorie und ihrer Anwendungen* (Leipzig, Teubner, 1899, dans le 7<sup>e</sup> *Jahresbericht der Deutschen Mathematiker-Vereinigung* ; voir §§ 34-36, pp. 78-87) et en reproduit la partie essentielle dans son traité didactique récent (*Wahrscheinligkeitsrechnung*, Leipzig, Teubner, 1903 ; voir §§ 82-88, pp. 120-138). Tout en reconnaissant avec Bienaymé et Bertrand que souvent la *loi des grands nombres* se confond avec le théorème de Bernoulli, il fait observer qu'elle ne conduit pas à la même valeur pour les écarts maxima qui peuvent se produire dans le cas d'un grand nombre d'épreuves (voir § 87, pp. 133-136).

**2.** *Objet de la présente note*. Dans les applications du calcul des probabilités aux sciences d'observation, on ne peut presque jamais appliquer directement le théorème de Bernoulli, même en y regardant la probabilité constante de l'événement simple considéré, comme une probabilité moyenne déduite d'épreuves antérieures. On sait, en effet, que cette probabilité moyenne est elle-même variable dans des limites plus ou moins étendues suivant le genre d'événements considéré et c'est à cause de cette circonstance que les limites des écarts sont parfois très différentes pour un même nombre d'épreuves et pour une même probabilité moyenne absolue de l'événement simple étudié.

Nous avons essayé de tenir compte de la variabilité de la probabilité moyenne et d'établir rigoureusement *la loi des grands nombres*, dans une note publiée dans les Bulletins de l'Académie royale de Belgique (janvier 1893, 3<sup>e</sup> série, t. XXV, pp. 11-13) ; malheureusement, dans nos formules finales, entre un nombre \(k\) qui ne peut être déterminé avec précision et nous nous appuyons [p. 27] sur une formule relative au théorème de Bernoulli qui est insuffisamment démontrée.

Dans la présente note, nous évitons la considération de ce nombre \(k\) et nous nous appuyons sur une démonstration complète du théorème de Bernoulli que nous avons publiée dans les Annales de la Société scientifique de Bruxelles (1902, t. XXVI, 2<sup>e</sup> partie, pp. 191-205).

**3.** Lemme. Posons

\[ p + q = 1, \qquad p_{1} + q_{1} = 1, \qquad p_{2} + q_{2} = 1, \]

\[ 0 < p_{1} \mathrel{\overset{=}{<}} p \leqq p_{2} < 1 \]

\[ \mathrm{T} = l \sqrt{\frac{\mu}{2pq}} = l_{1} \sqrt{\frac{\mu}{2p_{1}q_{1}}} = l_{2} \sqrt{\frac{\mu}{2p_{2}q_{2}}} \]

\(\mu\) et T étant constants, \(l\), \(l_{1}\), \(l_{2}\) des fractions inférieures respectivement à \(p\) et \(q\), \(p_{1}\) et \(q_{1}\), \(p_{2}\) et \(q_{2}\).

L'expression \(p - l\) croît ou décroît en même temps que \(p\), comme on le voit, en écrivant

\[ p - l = p - \frac{\mathrm{T}\sqrt{2pq}}{\sqrt{\mu}} = \sqrt{p}\left(\sqrt{p} - \frac{\mathrm{T}\sqrt{2}}{\sqrt{\mu}} \sqrt{1 - p}\right). \]

L'expression \(p + l\) croît aussi avec \(p\). Car

\[ p + l = 1 - (q - l). \]

Or, si \(p\) croît, \(q = 1 - p\) et, par suite, \(q - l\) décroît ; donc \(p + l\) croît.

Il résulte de là que l'on a

\[ p_{1} - l_{1} \mathrel{\overset{=}{<}} p - l \leqq p_{2} - l_{2}; \qquad p_{1} + l_{1} \mathrel{\overset{=}{<}} p + l \leqq p_{2} + l_{2} \]

et aussi

\[ \mu(p_{1} - l_{1}) \mathrel{\overset{=}{<}} \mu(p - l) \leqq \mu(p_{2} - l_{2}), \]

\[ \mu(p_{1} + l_{1}) \mathrel{\overset{=}{<}} \mu(p + l) \leqq \mu(p_{2} + l_{2}). \]

Par suite, *lorsque* \(p\) *varie de* \(p_{1}\) *à* \(p_{2}\), *l'intervalle*

\[ [\mu(p - l), \mu(p + l)] \]

*est toujours compris dans l'intervalle* I *plus grand*

\[ [\mu(p_{1} - l_{1}), \mu(p_{2} + l_{2})]. \]

[p. 28] **4.** *Rappel du théorème de Bernoulli*. Nous avons démontré le théorème de Bernoulli sous la forme suivante : La probabilité que le nombre \(m\) de répétitions d'un événement A de probabilité constante \(p\), sur \(\mu\) épreuves, est compris dans l'intervalle \([\mu(p - l), \mu(p + l)]\) surpasse la quantité

\[ \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}} \, dt - \frac{3}{\sqrt{2\mu pq}}, \]

moyennant ces conditions : 1° \(p \mathrel{\overset{=}{>}} q\) ; 2° \(l \mathrel{\overset{=}{<}} \frac{1}{2} q\) ; 3° \(\mu\) est au moins égal à 10 et à \(\frac{1}{q^{2}}\) ; 4° \(\mathrm{T} \sqrt{2pq} = l \sqrt{\mu}\).

La probabilité dont il est question surpassera *à fortiori*

\[ \mathrm{P} = \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}} \, dt - \frac{3}{\sqrt{2\mu p_{3}q_{3}}}, \]

si \(p_{3}q_{3}\) est le plus petit des produits \(p_{1}q_{1}\), \(p_{2}q_{2}\) définis au n° 3, si \(l\) est inférieur à la plus petite des quantités \(\frac{1}{2} p_{1}\), \(\frac{1}{2} q_{1}\), \(\frac{1}{2} p_{2}\), \(\frac{1}{2} q_{2}\) ; enfin, si \(\mu\) est au moins égal à 10 et à la plus grande des quantités \((1 : p_{1}^{2})\), \((1 : q_{1}^{2})\), \((1 : p_{2}^{2})\), \((1 : q_{2}^{2})\).

La probabilité que le nombre des répétitions \(m\) de l'événement A, sur \(\mu\) épreuves, sera compris dans l'intervalle I, plus grand que \([\mu(p_{1} - l_{1}), \mu(p_{2} + l_{2})]\) surpassera évidemment P, ou sera de la forme \(\mathrm{P} + \alpha\), \(\alpha\) étant une quantité positive.

**5.** *Loi des grands nombres*. Supposons qu'un certain événement A soit soumis ainsi que son contraire, à \(\mu\) épreuves répétées, \(k\) fois dans des circonstances qui font prendre successivement à sa probabilité \(p\), \(k\) valeurs différentes, dont chacune est au moins égale à \(p_{1}\), au plus égale à \(p_{2}\).

D'après ce qui précède, dans **chacune** de ces séries de \(\mu\) épreuves, *la probabilité que le nombre* \(m\) *de répétitions de l'événement sera compris dans l'intervalle I* est de la forme \(\mathrm{P} + \alpha\), \(\alpha\) étant positif, et, par suite, *surpasse P*.

C'est, au fond, dans ce théorème que consiste la *loi des grands nombres*.

Il diffère du théorème de Bernoulli en ce que l'intervalle I est plus grand et l'expression P est plus petite que si \(p\) était constant, mais il est démontré avec la même rigueur et a la même valeur objective.

BRUXELLES. — IMPRIMERIE POLLEUNIS ET CEUTERICK.

[p. 29]

[^25-a]: Extrait des Annales de la Société scientifique de Bruxelles. t. XXVIII, première partie, p. 72-77.

[^25-aa]: Voir surtout le *Préambule* de l'ouvrage, pp. 7 à 29, 29, ch. II, n<sup>os</sup> 52 à 62, pp. 138-161 et le ch. IV tout entier, pp. 246-317. L'ouvrage de Poisson a été traduit en allemand par C. H. Schnuse sous le titre : *Lehrbuch der Wahrscheinlichkeitsrechnung und deren wichstigsten Anwendungen*, Braunschweig, Meyer, 1841. Le traducteur a ajouté à l'original la traduction d'un mémoire de Poisson sur la probabilité des résultats des observations, puis d'autres suppléments sur l'espérance morale ; le calcul des rentes viagères et des assurances sur la vie.

## SUR LA PORTÉE OBJECTIVE DU CALCUL DES PROBABILITÉS

par

P. MANSION

Professeur à l'Université de Gand

Directeur de la Classe des sciences et président de l'Académie en 1903

*Discours prononcé dans la séance publique de la Classe des sciences*

*le 16 décembre 1903*

BRUXELLES

HAYEZ, IMPRIMEUR DE L'ACADÉMIE ROYALE DE BELGIQUE

Rue de Louvain, 112

1903

[p. 30]

[p. 31]

## Sur la portée objective du calcul des probabilités.

### I. Doutes sur la portée objective du calcul des probabilités.

Il est peu de pays, croyons-nous, où le calcul des probabilités tienne une place aussi considérable dans l'enseignement supérieur qu'en Belgique. Depuis 1835, il fait partie intégrante du programme du doctorat en sciences physiques et mathématiques ; depuis 1838, de celui de nos hautes écoles techniques.

En France, au contraire, il n'est enseigné qu'accidentellement, comme accessoire du cours de physique mathématique à la Sorbonne ; à l'École Polytechnique, on ne lui consacre que quelques leçons des cours d'analyse et d'astronomie. En Allemagne, l'une des plus célèbres applications du calcul des probabilités, la théorie de la compensation des erreurs d'observation, fait souvent l'objet d'une *Vorlesung* spéciale, mais rarement le calcul des probabilités y est exposé dans toute son étendue. Aussi, de 1837, date du grand ouvrage de Poisson sur la *Probabilité des jugements en matière civile et criminelle*, à 1889, année où Bertrand publia son *Calcul des probabilités*[^31-a], il n'a paru sur la matière qu'un seul vrai traité [p. 32] écrit dans l'une des grandes langues européennes. C'est le cours fait par A. Meyer, à l'Université de Liège, de 1849 à 1857, publié par M. Folie en 1874, et traduit en allemand par M. E. Czuber en 1879[^32-a].

D'où vient cette haute fortune du calcul des probabilités dans notre pays ? Selon toute apparence, de la grande influence dont a joui dans les conseils du gouvernement et dans le monde scientifique belge, l'homme éminent qui, pendant un demi-siècle, a été la personnification de notre Académie, je veux dire Adolphe Quetelet, son secrétaire perpétuel de 1835 à 1874.

L'œuvre capitale de Quetelet, la *Physique sociale* (1836), où il a jeté les bases de la statistique morale ou, comme on dit maintenant en langage barbare, de la sociologie positive, est fondée sur le calcul des probabilités, sur la loi des grands nombres.

Quetelet y prouve par des chiffres que l'homme, quand il obéit à sa raison, agit comme d'après une loi ; qu'il en est de même quand il se laisse aller à ses instincts ; ou, plus exactement, il en est ainsi quand il se trouve dans le voisinage de l'un ou l'autre de ces deux cas limites : alors, la force d'en haut ou la force d'en bas, le libre arbitre ou la passion laisse sa trace dans les moyennes comme une force perturbatrice qui les altère quelque peu ; mais dans l'ordre des faits moraux, comme [p. 33] dans celui des faits physiques, apparaît toujours la loi des grands nombres, qui les résume approximativement au point de vue quantitatif.

Quetelet, comme Meyer, comme Poisson, comme Laplace, croit à la valeur objective du calcul des probabilités. Comme eux, en théorie, il fait çà et là des réserves sur la portée de tel ou tel principe ; mais, en général, il applique hardiment ces principes jusque dans les cas les plus extrêmes.

Cependant, même du vivant de Quetelet, on avait déjà battu en brèche la confiance accordée à ces principes. Gauss, au début de son exposition de la méthode des moindres carrés, a signalé ce qu'il y a de purement subjectif dans la définition des erreurs accidentelles[^33-a]. On sait maintenant que dans ses cours sur la compensation des erreurs, il prenait nettement le même point de départ que Legendre, c'est-à-dire qu'il ne la faisait nullement reposer sur le calcul des probabilités[^33-aa].

Bienaymé a défendu la théorie des erreurs de Laplace, mais en déclarant qu'il y a lieu d'y introduire de sérieuses corrections. En outre, trente ans après la mort de Poisson, il a publié une note excellente, quoique pédantesque d'allure et de style, sous le titre peu respectueux : *Sur un principe que M. Poisson avait cru découvrir et qu'il avait appelé Loi des grands nombres*[^33-aaa].

Cournot, non sans pédantisme aussi, a justement critiqué des applications de la règle de probabilité des causes [p. 34] où elle n'a qu'une portée subjective, et cela dans son *Exposition de la théorie des chances et des probabilités*[^34-a], où, après Condorcet, Laplace et Poisson, il a tenté, lui aussi, de soumettre au calcul des probabilités les jugements en matière civile et criminelle.

A une époque plus rapprochée de nous, le livre de Bertrand et celui de M. Poincaré[^34-aa] accusent des tendances encore plus sceptiques. Bertrand signale, comme ses devanciers, les points faibles de la théorie de la probabilité des causes (pp. 157 et sqq.) et par suite de celle de la compensation des erreurs accidentelles ; la loi des grands nombres, de Poisson, lui semble identique au théorème de Jacques Bernoulli (pp. XXXI-XXXII) ; il accable de ses sarcasmes spirituels les recherches de Quetelet sur l'homme moyen (pp. XLI-XLIII) et surtout les travaux des géomètres français sur la probabilité des jugements (pp. XLIII-XLIX, 319-327). La conclusion du *Calcul des probabilités* de Poincaré est aussi très peu rassurante : « On ne peut dépouiller complètement de ces hypothèses arbitraires, dit-il, les questions de probabilités ; aussi le mot de calcul semble-t-il ambitieux, et il ne sert qu'à dissimuler l'ignorance absolue... On ne doit pas s'attendre à rencontrer quelque résultat pleinement satisfaisant. Le calcul des probabilités offre une contradiction dans les termes mêmes qui servent à le désigner, et si je ne craignais de rappeler ici un mot trop souvent répété, je dirais qu'il nous enseigne surtout une chose : c'est de savoir que nous ne savons rien (pp. 273-274). »

[p. 35] Que penser de ces opinions, en apparence au moins si profondément divergentes ? Laplace est-il trop crédule ou M. Poincaré trop sceptique ? Faut-il renoncer au calcul des probabilités ? La chose semble impossible. Dans son récent ouvrage sur *La science et l'hypothèse*[^35-a], où il consacre un chapitre au calcul des probabilités, M. Poincaré lui-même, un peu moins pessimiste que dans son cours de la Sorbonne, dit expressément : « Toutes les fois que le physicien raisonne par induction, il fait plus ou moins consciemment du calcul des probabilités (p. 214). »

D'autre part, dans les fines analyses psychologiques de sa *Grammar of Assent*, Newman remarque que nous donnons continuellement un assentiment complet à des propositions invérifiables pour nous, et cet assentiment n'est basé que sur des probabilités accumulées. M. Ernest Naville fait des remarques analogues dans un mémoire sur *L'importance logique du témoignage*[^35-aa].

Il semble donc que l'homme, aussi bien dans ses théories scientifiques que dans cet ensemble d'opinions, de croyances ou de convictions qui le guident dans sa vie affective, morale ou religieuse, s'appuie sans cesse, qu'il le sache ou non, sur les principes du calcul des probabilités, et pourtant ceux-ci semblent peu sûrs à d'excellents esprits.

Cette antinomie apparente m'a frappé depuis longtemps ; j'ai indiqué partiellement dans mes cours et dans diverses notes publiées çà et là, comment, selon moi, on pouvait la résoudre. Mais je n'ai jamais eu l'occasion [p. 36] d'exposer l'ensemble de mes vues sur ce sujet. Cette occasion m'est offerte aujourd'hui et je vais tâcher de préciser devant vous les conditions suffisantes sinon nécessaires pour que le calcul des probabilités ait une portée objective.

Pour diminuer l'aridité inévitable d'un pareil sujet, — car, vous le savez, *si les nombres régissent le monde*, *ils le régissent sans l'amuser*, comme l'a fait remarquer M. De Tilly, — pour diminuer l'aridité inévitable d'un pareil sujet, au lieu de suivre l'ordre logique, je suivrai l'ordre historique. Cela me donnera l'occasion de faire parler à ma place Pascal, Laplace, Quetelet, Newman, Naville, Bertrand, Poincaré, Boutroux, et ce sera tout gain pour mes auditeurs comme pour moi.

[^31-a]: Paris, Gauthier-Villars et fils.

[^32-a]: Pour ne pas encombrer cette lecture de renseignements bibliographiques, nous renvoyons le lecteur curieux de connaitre l'histoire détaillée du calcul des probabilités aux ouvrages suivants : Gouraud, *Histoire du Calcul des probabilités*, Paris, Durand, 1848 ; Todhunter, *A History of the Mathematical Theory of probability*, Cambridge, Macmillan and C<sup>o</sup>, 1865 ; Czuber, *Die Entwicklung der Wahrscheinlichkeitstheorie*, Leipzig, Teubner, 1899.

[^33-a]: Gauss, *Werke*, IV, p. 7.

[^33-aa]: Gauss, *Werke*, VIII, pp. 147-148.

[^33-aaa]: Paris, Anger, 1870.

[^34-a]: Paris, Hachette, 1843.

[^34-aa]: *Calcul des probabilités*. Paris, Naud, 1896.

[^35-a]: Paris, Flammarion, s. d.

[^35-aa]: *Compte rendu de l'Académie des sciences morales et politiques*, 1887, 2<sup>e</sup> semestre, t. CXXVIII, pp. 269-281.

### II. Pascal et Fermat. La théorie des jeux.

Vers 1649, Blaise Pascal, dont la santé était ébranlée depuis longtemps déjà, dut renoncer à tout travail scientifique sur l'ordre des médecins. « Ils lui prescrivirent de quitter toute application d'esprit et de chercher les occasions de se divertir... Blaise chercha une occupation dans le commerce du monde et ne tarda pas à goûter cette vie nouvelle. Il se mit à jouer et à se divertir pour passer le temps. Il se livra, sans dérèglement toutefois, aux amusements de la société... A Paris, il se lia avec plusieurs personnes imbues de l'esprit du monde », et entre autres avec « le chevalier de Méré, Poitevin, honnête homme avec entêtement, puriste et précieux, affectant la simplicité, le naturel et le bon sens, voyant dans [p. 37] les choses de l'esprit et du sentiment un monde spécial, qu'il mettait très au-dessus du monde naturel[^37-a] ». Méré, dont Leibniz a dit qu'il avait un esprit pénétrant, même pour les mathématiques, et qui était joueur et philosophe[^37-aa], eut une grande influence sur le jeune Pascal ; il lui fit connaître, sans le lui donner, cet *esprit de finesse* dont l'auteur des *Pensées* devait plus tard marquer si fortement la différence avec l'*esprit de géométrie*.

En 1654, Méré souleva deux questions relatives au jeu de dés, qui ramenèrent brusquement Pascal à ces recherches scientifiques qu'il semblait avoir abandonnées pour toujours. Nous ne dirons rien de la première, que Roberval et Méré lui-même parvinrent à résoudre, mais la seconde a donné naissance au calcul des probabilités et vaut la peine d'être exposée. « Le problème était le suivant. Deux joueurs considérés comme également habiles rompent le jeu avant la fin. En ce cas, le règlement de tout ce qui doit leur appartenir doit être tellement proportionné à ce qu'ils avaient droit d'espérer de la fortune, que chacun d'eux trouve entièrement égal de prendre ce qu'on lui assigne, ou de continuer l'aventure du jeu : et cette juste distribution s'appelle le parti[^37-aaa]. » A Paris, Pascal seul parvint à résoudre la question, Roberval n'y réussit pas.

La méthode de Pascal est admirable de simplicité et, suivant un mot célèbre, elle peut être exposée à un passant dans la rue. « Voici, dit-il, à peu près comme je fais pour savoir la valeur de chacune des parties, quand deux [p. 38] joueurs jouent, par exemple, en trois parties et que chacun a mis 32 pistoles au jeu. Posons que le premier en ait deux et l'autre une : ils jouent maintenant une partie dont le sort est tel, que si le premier la gagne, il gagne tout l'argent qui est au jeu, savoir 64 pistoles ; si l'autre la gagne, ils sont deux parties à deux parties, et, par conséquent, s'ils veulent se séparer, il faut qu'ils retirent chacun leur mise, savoir chacun 32 pistoles. Considérez donc que, si le premier gagne, il lui appartient 64 ; s'il perd, il lui appartient 32. Donc s'ils ne veulent pas hasarder cette partie et se séparer sans jouer, le premier doit dire : « Je suis sûr d'avoir 32 pistoles ; car la perte » même me les donne ; mais pour les 32 autres, peut-être » je les aurai, peut-être vous les aurez ; le hasard est égal ; » partageons donc ces 32 pistoles par la moitié, et donnez- » moi outre cela mes 32 qui me sont sûres. » Il aura donc 48 pistoles, et l'autre 16[^38-a]. » Pascal indique comment sa méthode s'étend à des questions plus compliquées entre deux joueurs ; il l'a appliquée plus tard au cas de trois joueurs (II, p. 403), et il est évident qu'elle est générale, quoi qu'en ait dit Laplace à la première page de sa *Notice historique sur le calcul des probabilités*[^38-aa]. Au fond, Pascal résout de proche en proche une équation linéaire aux différences partielles et invente ainsi l'une des deux méthodes analytiques du calcul des probabilités.

Fermat, conseiller au parlement de Toulouse, le plus grand géomètre de la première moitié du XVII<sup>e</sup> siècle, le plus modeste aussi, pour ne pas dire le seul modeste, a [p. 39] créé la seconde de ces méthodes, celle qui repose sur la théorie des combinaisons. Pascal lui communique ses résultats ; Fermat les approuve et lui fait connaître sa propre méthode sous une première forme. Pascal en méconnaît d'abord la portée. Fermat la met sous une seconde forme et dissipe tous les nuages comme en se jouant. Non seulement il se sert de l'idée simple de probabilité comme Pascal, mais il introduit dans ses calculs le principe des probabilités composées et celui de la probabilité totale. Fermat envoya en même temps à Pascal quelques-uns de ses énigmatiques théorèmes sur les nombres, entre autres celui qui est relatif à la décomposition de tout nombre en nombres polygonaux. Pascal en fut épouvanté. « Cherchez ailleurs, dit-il, qui vous suive en vos inventions numériques[^39-a]. » Pascal eut raison, car ce n'est que cent cinquante ans plus tard que Cauchy est parvenu à démontrer le théorème sur les nombres polygonaux communiqué par Fermat à Pascal. Aujourd'hui encore, comme on le sait, un dernier théorème de Fermat reste indémontré, malgré les efforts des plus grands géomètres du XVIII<sup>e</sup> et du XIX<sup>e</sup> siècle pour retrouver la mystérieuse démonstration de l'illustre géomètre toulousain.

Dès 1654, Pascal et Fermat ont donc posé les principes et inventé les deux méthodes analytiques du calcul des probabilités. Leur correspondance, qui ne fut imprimée que beaucoup plus tard, circula dans le monde scientifique d'alors et provoqua de nouvelles recherches. Pendant [p. 40] plus d'un demi-siècle, divers géomètres, dont quelques-uns des plus illustres, Huygens, Leibniz, Montmort, Jacques, Jean et Nicolas Bernoulli, Moivre, Jean De Wit, le célèbre pensionnaire de Hollande, développent et appliquent les principes de Pascal et de Fermat, mais sans y rien ajouter d'essentiel. Ce n'est qu'à la fin de sa vie que Jacques Bernoulli découvrit le célèbre théorème qui porte son nom et que Poisson a généralisé un siècle plus tard en l'appelant *Loi des grands nombres*.

Mais afin de mieux faire saisir la portée de cette belle découverte, nous devons d'abord parler d'un cas de probabilité simple, où les plus ignorants comme les plus savants en analyse mathématique peuvent faire presque infailliblement des prédictions justes.

[^37-a]: Boutroux, *Pascal*. Paris, Hachette, 1900, p. 49.

[^37-aa]: Todhunter, p. 12.

[^37-aaa]: Boutroux, *Pascal*, p. 66.

[^38-a]: *Œuvres de Pascal*. Paris, Hachette, 1858, t. II. p. 393.

[^38-aa]: Laplace, *Théorie analytique des probabilités*, 3<sup>e</sup> édition. Paris, V<sup>e</sup> Courcier, 1820, pp. CXXXIV-CXXXV.

[^39-a]: Voir la correspondance échangée entre Pascal et Fermat (*Œuvres de Pascal*, II, pp. 392-407) pour les diverses assertions contenues dans le texte.

### III. Un cas où la probabilité devient presque une certitude.

Prédire presque infailliblement ! la chose paraît étrange au premier abord. Quand on agite un dé dans un cornet et qu'on le jette au hasard sur une table, peut-on prédire qu'il va nous donner un six ou un cinq ? Quand on tire une carte d'un jeu de whist, peut-on prévoir que l'on tournera la dame de trèfle ou le sept de cœur ?

Évidemment non. Mais *on peut prédire, presque à coup sûr, le contraire d'un événement très improbable*. Jetez six dés homogènes en l'air. Quelle est la probabilité d'amener une double rafle de cinq, d'amener six fois le chiffre cinq. Elle est très petite. Les six dés peuvent sortir de plus de 45 000 manières, exactement 46 656 ; il n'y en a qu'une favorable à l'arrivée des six cinq.

[p. 41] On peut donc hardiment parier 45 000 francs et plus contre un que le jeu amènera une autre combinaison que la double rafle des cinq.

Pour avoir une idée plus nette de la probabilité dont il s'agit ici, transformons-la, suivant un procédé familier à Quetelet[^41-a], en une autre équivalente. D'après les tables de survie pour la Belgique, publiées, il y a dix ans, par M. J. Leclerc, sur 46 656 jeunes hommes de 20 ans, 324 n'arrivent pas à l'âge de 21 ans, de sorte qu'il en mourra en moyenne 27 par mois, c'est-à-dire à peu près un par jour. La probabilité de l'arrivée d'une double rafle de cinq est donc à peu près la même que celle qu'un jeune homme de 20 ans, pris au hasard parmi plus de 45 000 hommes de même âge, mourra dans les vingt-quatre heures. La probabilité contraire, celle de la non-arrivée de la double rafle des cinq, est donc celle que le jeune homme dont nous parlions tantôt vivra encore au moins un jour.

N'est-il pas vrai que dans les deux cas équivalents que nous venons de citer, tout le monde est pratiquement certain, ou prédit à coup sûr, que la double rafle des cinq n'arrivera pas, que le jeune homme choisi au hasard vivra encore un jour ?

Si quelqu'un en doute, il est facile d'imaginer d'autres cas plus concluants. Le mot *absolument* contient dix lettres toutes différentes. On peut les permuter de plus de 3 1/2 millions de manières, exactement 3 628 800. La probabilité de former le mot *absolument* en tirant successivement d'une urne dix jetons sur lesquels sont inscrites les dix lettres est soixante-dix-sept fois moindre que celle [p. 42] de tantôt. L'arrivée d'une autre combinaison des dix lettres que celle qui donne le mot *absolument* est donc pratiquement certaine. C'est un événement aussi sûr que celui-ci : le jeune homme de tantôt, pris au hasard parmi les 46 656 de son âge, vivra encore au moins dix-sept minutes.

Bertrand a très bien expliqué pourquoi certains événements doivent se produire presque fatalement : « Tous les arrangements sont également possibles ; que les plus nombreux se présentent, il n'y a pas de sujets d'étonnement. Si toutes les combinaisons dont le nombre est immense étaient présentes matériellement », l'une d'elles, désignée d'avance, « deviendrait introuvable. Le hasard reste libre, mais la carte est forcée » (p. XXIII).

Si chacune des combinaisons des six dés était préparée dans une boîte de 1 décimètre carré de base et de 2 centimètres de hauteur, sans que, dans aucune boîte, les mêmes dés présentassent les mêmes faces, les 46 656 boîtes formeraient un monceau de plus de 9 mètres cubes, où il serait bien difficile de retrouver la double rafle des cinq. Si l'on met dans des boîtes semblables les jetons sur lesquels se trouvent les lettres du mot *absolument*, elles rempliront une salle de 15 mètres de long, de 8 de large et de 6 de haut. Qui pourrait espérer de retrouver le mot dans un dictionnaire de cette dimension et dont toutes les pages seraient brouillées au hasard.

Une dernière comparaison : le texte grec du Nouveau Testament contient de 8 à 900 000 lettres. La probabilité dont il vient d'être question est cinq fois plus petite que celle de rencontrer le δ du mot Κέδρον — qui n'y est qu'une fois, d'après Leusden — en ouvrant le livre et piquant une lettre au hasard avec une épingle.

[p. 43]

[^41-a]: *Théorie des probabilités*. Bruxelles, Jamar, 1853, pp. 16-17.

### IV. Le théorème de Bernoulli et la loi des grands nombres.

Nous pouvons maintenant donner une idée du théorème de Bernoulli et de la loi des grands nombres de Poisson. Ces géomètres ont trouvé, dans beaucoup de questions de probabilités, des cas où l'on peut prédire aussi sûrement que dans les exemples simples indiqués plus haut.

Jacques Bernoulli est l'aîné d'une famille, j'ai failli dire d'une dynastie de mathématiciens, originaire de Bâle, et si l'on remonte plus haut, d'Anvers. On y distingue Jacques I<sup>er</sup>, — c'est l'auteur du théorème, — Jacques II, Jean I<sup>er</sup>, Jean II, Jean III, Nicolas I<sup>er</sup>, Nicolas II, Daniel I<sup>er</sup>, Daniel II. Un fils de ce dernier, Christophe Bernoulli, qui a écrit sur la *Populationistik* en 1840, est mort à Bâle en 1863[^43-a].

NICOLAS

(1623-1708)

Jacques I<sup>er</sup> Nicolas Jean I<sup>er</sup>

(1654-1705). (1667-1748)

Nicolas I<sup>er</sup>

(1687-1759).

Nicolas II Daniel I<sup>er</sup> Jean II

(1695-1726). (1700-1782). (1710-1790)

Jean III Daniel II Jacques II

(1744-1807). (1751-1834) (1759-1789).

Christophe

(1782-1863).

[p. 44] Nicolas I<sup>er</sup>, neveu de Jacques I<sup>er</sup> et de Jean I<sup>er</sup>, publia, en 1713, l'*Ars conjectandi* de son oncle Jacques I<sup>er</sup>, mort huit ans auparavant, et fit connaître ainsi la proposition célèbre qui a donné une portée inattendue au calcul des probabilités.

Je ne puis évidemment vous exposer ce théorème au moyen des hiéroglyphes de l'algèbre ; quinze pages suffisent à peine pour en donner une démonstration complète. Mais on peut aisément le faire connaître sur des exemples.

Considérons une urne où il y a 300 boules identiques à la couleur près, 100 blanches, 200 noires. Par convention, la *probabilité a priori* de tirer une boule blanche de cette urne est 1/3, celle de tirer une boule noire 2/3.

On extrait une boule de l'urne au hasard, on en note la couleur, on la remet dans l'urne et l'on répète cette opération quatre-vingt-dix mille fois, en ayant soin, après chaque tirage, de bien mélanger les boules.

Calculons, au moyen des principes élémentaires trouvés par Fermat et des formules peu élémentaires de Stirling, de Moivre et de Laplace, la probabilité que le nombre des boules blanches sorties de l'urne sur les 90 000 tirages, est 30 000 à 600 près ; nous trouverons qu'elle est la même que celle de la non-arrivée d'une double rafle de cinq quand on jette six dés. Autrement dit, nous sommes pratiquement certains qu'il est sorti entre 29 400 et 30 600 boules blanches. Nous prédisons à 1/50 près.

Si nous avions fait cent fois plus de tirages, donc 9 000 000, nous pourrions parier avec la même certitude qu'il y a eu sortie de 3 000 000 de boules blanches à 6 000 près. Le nombre des tirages est cent fois plus [p. 45] grand, 9 000 000 au lieu de 90 000 ; l'écart absolu n'est que dix fois plus grand, 6 000 au lieu de 600. Cette fois, nous prédisons à 1/500 près.

Si nous nous étions assigné un écart absolu de 800 sur 90 000 tirages ou de 8 000 sur 9 000 000 de tirages, la probabilité que le nombre de boules blanches aurait été 30 000 à 800 près, ou 3 000 000 à 8 000 près, eût été la même que celle de la non-arrivée du mot *absolument* dans l'exemple cité antérieurement. Autrement dit, on peut prédire avec une quasi-certitude qu'il sortira 30,000 boules blanches à 800 près (ou 3 000 000 à 8 000 près) sur 90 000 (ou 9 000 000 de) tirages[^45-a].

\[ P = \frac{2}{\sqrt{\pi}} \int_{0}^{T} e^{-t^{2}}\,dt, \qquad T = l\sqrt{\frac{\mu}{2pq}} \]

\[ \text{si } = \mu\ 90\,000, \qquad l = \frac{1}{150}, \qquad \mu l = 600 ; \]

\[ \text{si } \mu = 9\,000\,000, \qquad l = \frac{1}{1500}, \qquad \mu l = 6\,000. \]

\[ \text{si } \mu = 90\,000, \qquad l = \frac{1}{225}, \qquad \mu l = 800 ; \]

\[ \text{si } \mu = 9000\,000, \qquad l = \frac{1}{1125}, \qquad \mu l = 8\,000. \]

[p. 46] En langage mathématique, on énoncera le théorème de Bernoulli, dans le cas actuel, comme il suit : L'écart relatif, c'est-à-dire la différence entre la probabilité *a priori*, 1/3, de l'arrivée d'une blanche, et le rapport du nombre de boules blanches au nombre total des tirages, diffère de moins en moins de zéro à mesure que l'on fait plus d'épreuves ; et l'on est pratiquement certain qu'il en est ainsi.

Si, sur les 90 000 ou sur les 9 000 000 de tirages, on avait oublié parfois de remettre une boule tirée dans l'urne, de manière que la composition de celle-ci eût varié tantôt dans un sens, tantôt dans un autre, le théorème de Bernoulli se transforme légèrement et devient la loi des grands nombres de Poisson ; les écarts possibles deviennent un peu plus grands, mais on peut assigner ceux qui ne seront pas dépassés avec une quasi-certitude comme dans le cas précédent.

Le théorème de Bernoulli et la loi des grands nombres permettent donc de prédire les écarts dans le sens indiqué plus haut, quand on connaît la *probabilité a priori* de l'événement dont on provoque la répétition un grand nombre de fois.

Mais inversement, si l'on a observé dans une série nombreuse d'épreuves relatives à un événement et à son contraire, le nombre de fois que cet événement est arrivé, le rapport de ce nombre au nombre total d'épreuves, la *probabilité a posteriori*, comme on l'appelle, sera très peu différente de la *probabilité a priori* de l'événement observé et, par suite, peut servir à la trouver.

Ainsi, dans les exemples cités plus haut, le rapport du nombre des boules blanches au nombre des tirages [p. 47] tendra fatalement vers un tiers et peut servir à faire connaître la composition relative de l'urne.

On peut traduire cette conséquence de la loi des grands nombres sous cette forme familière : On connaît d'autant mieux ce qu'il y a dans un sac que l'on y met plus souvent la main, et si on le fait assez souvent, on le connaîtra presque infailliblement. Plus solennellement, plus académiquement si l'on veut, la loi des grands nombres nous permet dans certains cas d'interroger la nature et de la forcer à répondre à nos questions.

[^43-a]: Voici un aperçu généalogique de cette intéressante famille :

    (D'après M. Cantor, dans l'*Allgemeine deutsche Biographie*, II. pp. 470-483.)

[^45-a]: Nous nous servons des formules classiques : où \(p = \frac{1}{3}\), \(q = \frac{2}{3}\) ; \(\mu\) est le nombre de tirages, \(l\) l'écart relatif, \(\mu l\) l'écart absolu. Quand \(T = 3\), on trouve \(P =\) à peu près \(1 - \frac{1}{46656}\), puis

    Quand \(T = 4\), \(P =\) à peu près \(1 - \frac{1}{3628800}\), puis

### V. La ruine du joueur. La guerre.

Moivre, Lagrange, Laplace et Ampère ont appliqué le théorème de Bernoulli au problème dit de la ruine du joueur, du joueur qui joue indéfiniment à un jeu équitable ou non.

Un jeu est dit équitable quand la mise du joueur est proportionnelle à sa probabilité de gagner.

Il résulte immédiatement du théorème de Bernoulli que chaque joueur gagnera à un jeu équitable à peu près un nombre de parties proportionnel à sa probabilité de gagner ; plus il jouera, plus la proportionnalité sera exacte et, par suite, il gagnera ou perdra une fraction toujours décroissante de sa mise totale. Rien de plus consolant en apparence pour les joueurs obstinés.

Malheureusement, la mise totale croît sans cesse, et l'on prouve aisément qu'il est pratiquement sûr que la perte totale de l'un des deux joueurs dépassera sa fortune, [p. 48] qu'il se ruinera si le temps ne lui manque pas. « La ruine tôt ou tard est certaine, dit Bertrand. La proposition semble contradictoire. En ruinant l'un des joueurs, le jeu enrichit l'autre ; en s'exposant à perdre une fortune, on a l'espoir de la doubler. Cela n'est pas douteux ; mais quand la fortune est doublée, le théorème s'y applique avec la même certitude (p. 105). » Par suite, « si deux joueurs jouent sans cesse, jusqu'à la ruine de l'un d'eux, le moins riche sera probablement vaincu ». En particulier, il en sera ainsi de « l'homme qui joue sans limite et sans cesse accepte tous les adversaires, dont l'ensemble, sans changer son sort, peut recevoir un nom collectif, *le public* ; le public, qui n'est jamais ruiné, ruine les imprudents qui l'attaquent » (p. XVI).

« Tout change quand les conditions du jeu sont inégales », autrement dit quand le jeu n'est pas équitable. A fortune égale, c'est le joueur favorisé qui l'emportera presque infailliblement, si les enjeux ne sont pas trop élevés, de manière qu'il puisse jouer, en tout cas, un grand nombre de parties. Dans ces jeux, dit Buffon, le joueur favorisé, « le banquier n'est qu'un fripon avoué et le ponte », son adversaire, « une dupe dont on est convenu de ne pas se moquer »[^48-a].

Mais il y a un cas où même le joueur favorisé se ruinera presque infailliblement, c'est celui où son avantage est petit et où il est forcé de jouer indéfiniment contre un adversaire très riche, et de jouer gros jeu ; dans ce cas, il n'est plus protégé par le théorème de Bernoulli. [p. 49] Ainsi, dans le cas où le *total* des enjeux n'est pas limité, un milliardaire peut ruiner à coup sûr le banquier du jeu de trente et quarante, si ce banquier n'est que millionnaire. L'avantage de ce *fripon avoué*, dans ce cas, n'est que de 6 ‰, et il est insuffisant pour le défendre contre la stratégie d'un milliardaire, qui peut doubler un grand nombre de fois sa mise par personnes interposées.

Me permettrez-vous, à l'imitation de Quetelet, une application, peut-être un peu naïve, de ce qui précède à la guerre. Annibal, dans sa lutte contre Rome, avait pour lui son génie militaire, l'indomptable valeur de ses auxiliaires gaulois, les richesses de Carthage, et pourtant il a perdu la partie : Rome avait une réserve indéfinie de patriotisme, elle pouvait être vaincue sur dix champs de bataille sans que rien fût compromis. Annibal était condamné à la victoire perpétuelle : il luttait pour la vie. En 1812, 1813 et 1814, une partie sanglante analogue s'est jouée en Espagne, en Russie, en Allemagne, entre Napoléon et les nations, et malgré son génie aussi, c'est Napoléon qui a été vaincu. Dans la guerre des Boers contre l'Angleterre, le même phénomène s'est reproduit : la petite nation africaine avait pour elle le droit, le patriotisme, la connaissance du théâtre de la lutte, l'endurance au climat ; elle a été vaincue par une armée de mercenaires indéfiniment renouvelable et disposant de vivres et de munitions en quantité illimitée. Tristes parties, disait Quetelet, il y a un demi-siècle, « que celles qui exigent pour enjeu la prospérité des nations et le sang des hommes ; où le gagnant est celui qui réussit à détériorer le mieux la part qu'il convoite, sans qu'il puisse prévoir l'étendue des sacrifices qu'il devra s'imposer pour l'obtenir » (p. 39).

[p. 50]

[^48-a]: Quetelet, p. 34.

### VI. Application au transformisme.

C'est sans doute aller à l'extrême des spéculations permises et peut-être même au delà, que d'appliquer les formules des géomètres sur la ruine du joueur aux hasards de la guerre. Mais assurément, comme l'a cru Delbœuf, on peut s'en servir pour porter quelque lumière dans une question de biologie, toujours actuelle, depuis qu'elle a été posée par Darwin, en 1859, dans l'*Origin of species*. Peut-on expliquer la formation de nouvelles espèces, ou au moins de nouvelles variétés, de nouvelles races — les géomètres ne peuvent les distinguer — par la survivance d'*un petit nombre* d'individus, devenus, dans la lutte pour la vie, *légèrement* plus aptes que la masse de leurs congénères ; ou, comme disait Delbœuf, un principe interne de variation, si *faible* soit-il, doit-il à la fin introduire des changements toujours plus prononcés chez presque tous les individus appartenant à une même espèce ? J'appuie sur les mots *petit nombre*, *légèrement plus apte*, *variation faible*, parce que la réponse à la question en dépend.

L'individu faiblement avantagé par la nature a un peu plus de chance de vivre et de perpétuer son avantage chez ses descendants qu'un autre quelconque des individus de la même espèce ; c'est ce que tout le monde voit et dit. Mais ce que l'on oublie souvent, c'est qu'il en a infiniment moins que l'ensemble de ces individus, surtout s'il joue gros jeu, s'il joue souvent son existence. Il est dans le cas du banquier millionnaire qui est aux [p. 51] prises avec un milliardaire au jeu de la roulette, et qui risque chaque fois une forte partie de sa fortune. Le milliardaire — ici l'ensemble des individus qui ne sont pas avantagés — perdra peut-être d'abord neuf ou dix millions, mais à la fin, il ruinera, presque infailliblement, le banquier qui n'est que millionnaire. Pour que celui-ci l'emportât, il faudrait que l'avantage qu'il a au jeu fût assez considérable et qu'ainsi il pût continuer indéfiniment la lutte. La loi des grands nombres est donc défavorable à l'évolutionnisme par transformation faible et lente, tandis qu'elle est favorable à l'évolutionnisme par transformation brusque et forte.

Darwin, à l'endroit où il combat le transformisme par saut brusque de Mivart et défend le transformisme par variations insensibles (*Origin of species*, 6<sup>e</sup> édition stéréotype, tirage de 1882, p. 202), a bien vu que celui-ci présuppose que les petites variations favorables portent sur un grand nombre d'individus et que les variations défavorables en atteignent et en détruisent un grand nombre d'autres. Malheureusement, cela revient à dire qu'*il y a évolution quand il y a évolution*, et si Darwin n'avait pas d'autre argument, il n'aurait rien expliqué du tout.

Mais que penser de la démonstration si séduisante de Delbœuf[^51-a] en faveur du transformisme par variation très faible d'un petit nombre d'individus ? D'abord qu'elle est très fine et très ingénieuse, parce que l'auteur, comme [p. 52] Pascal dans le problème des partis, ne manie que des nombres entiers, il évite toute formule empruntée au calcul des probabilités, et c'est sagesse, car les biologistes et les philosophes se défient toujours des géomètres qui semblent mesurer la certitude, le doute, la probabilité, la possibilité. On ne songe pas à se défier de Delbœuf, qui ne fait que d'innocentes additions, soustractions et multiplications. Mais hélas, la démonstration ne prouve rien, à cause d'une singulière inadvertance de l'auteur : il a oublié de réduire au nombre primitif de représentants d'une espèce, le nombre total de ceux qui les remplacent après chaque génération, bien qu'il ait averti qu'il faut le faire. Il a oublié de faire une division ou de tenir compte du *struggle for life*. Or, quand on veut effectuer cette division, cette réduction nécessaire, on doit fatalement faire l'une de ces deux hypothèses : ou bien admettre, avec Delbœuf, que *tous les individus, transformés ou non, sont égaux au point de vue des chances de vie*, ou que les individus transformés sont les uns notablement plus aptes, les autres notablement moins aptes à l'emporter dans la lutte pour la vie. Dans le premier cas, le groupe non transformé, favorisé par sa supériorité numérique, l'emportera sur le groupe transformé, qui disparaîtra, contrairement à ce qu'a pensé Delbœuf[^52-a]. Dans l'autre cas, sa démonstration redevient valable tout en gardant sa belle simplicité, et ainsi complétée et corrigée, constitue un argument en faveur de l'évolutionnisme par saut brusque de Mivart.

[p. 53]

[^51-a]: *Revue scientifique* du 13 janvier 1877, pp. 669-679. C'est à la p. 673, col. 2, qu'il parle de la réduction à faire et qu'il suppose tous les individus égaux au point de vue des chances de vie.

[^52-a]: Il avait cependant remarqué, p. 673, col. 1, que *la rareté d'une espèce est un désavantage pour elle*.

### VII. La vraie nature du calcul des probabilités et du hasard.

La ruine du joueur, le jeu sanglant des armes comme on disait autrefois, le transformisme nous ont écarté de notre route. Revenons aux principes du calcul des probabilités et aux conséquences philosophiques de la loi des grands nombres.

Nous avons parlé de *probabilités a priori* et de probabilités *a posteriori* à propos de cette loi. Mais quand on y regarde de près, on s'aperçoit qu'en pratique, toutes les probabilités sont *a posteriori*. Nous disons que la probabilité d'amener un chiffre déterminé avec un dé, 5 par exemple, est 1/6, parce que nous supposons le dé bien homogène et que nous jugeons qu'il est également facile d'amener chacune des six faces. Mais si le dé était pipé, s'il ne pouvait amener que les faces 4 et 5, d'ailleurs avec la même facilité, la probabilité d'amener 5 serait 1/2.

En réalité, il n'y a qu'un moyen de savoir si le dé est pipé ou non, de connaître la probabilité objective de l'arrivée de chacune des faces, c'est de soumettre le dé à des épreuves répétées. On trouvera, par exemple, qu'en 600 épreuves, le 5 se présente 97 fois, en 6 000, 1 003 fois, en 12 000, 2 002 fois et ainsi de suite. On en conclura que la probabilité *a posteriori*, la probabilité objective de l'arrivée de 5 est environ 1/6 ou, plus exactement, qu'elle est comprise entre 97/600 et 1003/6000. On se servira de la première valeur dans les calculs relatifs au théorème de Bernoulli, des autres, dans les [p. 54] formules plus exactes relatives à la loi des grands nombres de Poisson.

Cela prouve que, bien loin qu'on puisse se passer de celle-ci en la remplaçant toujours par le théorème de Bernoulli, comme le veulent Bienaymé et Bertrand, l'emploi de cette loi est au contraire indispensable, puisque l'on ne peut jamais, en pratique, connaître une probabilité objective avec une exactitude absolue.

Il y a plus : quelque étrange que cela paraisse, le calcul des probabilités n'existerait plus, n'aurait plus aucune raison d'être, si la probabilité objective d'un événement était une fraction bien déterminée.

Quel sens, en effet, pourrait-on donner à cette phrase : La probabilité de l'arrivée d'un 5 quand on jette un certain dé sur une table est constamment égale à 1/6 ? Pas d'autre que celui-ci : En 6 coups, 5 se présente une fois ; en 12, deux fois, en 600, cent fois et ainsi de suite. Ce n'est pas tout, il faut évidemment que le 5 se présente toujours au même rang dans chaque série de six coups depuis le début du jeu ; sans cela, en subdivisant les 600 coups en groupes convenables, il y aurait des *sixaines* sans 5. Mais si 5 se présente avec cette régularité absolue, il n'y a plus rien de probable ou d'improbable dans son arrivée ; on est certain qu'il se présentera ou non quand on jouera tel ou tel coup dans la série des 600 ; ce sera une loi de la nature.

Ce que nous disons à propos de ce dé peut se répéter à propos de toutes les questions de probabilités. *Le calcul des probabilités ne s'applique pas à des phénomènes dont on connaît les lois d'une manière absolue* ; car dans l'ordre de ces phénomènes, on prédit à coup sûr si l'on en connaît les lois. « Une intelligence qui, pour un instant donné, [p. 55] dit Laplace, connaîtrait toutes les forces dont la nature est animée, et la situation respective des êtres qui la composent, si, d'ailleurs, elle était assez vaste pour soumettre ces données à l'analyse, embrasserait dans la même formule les mouvements des plus grands corps de l'univers et ceux du plus léger atome : *rien ne serait incertain pour elle, et l'avenir comme le passé serait présent à ses yeux* (pp. II-III). »

Avant Laplace, Schiller avait dit par la bouche de Wallenstein[^55-a] :

*Es giebt keinen Zufall*,<br>
*Und was uns blindes Ohngefähr nur dünkt*,<br>
*Gerade das steigt aus dem tiefsten Quellen*.

Oui, à part le domaine des actions libres dont Laplace ne s'occupe pas, tout est soumis à des lois dans la nature ; il n'y a pas de hasard dans le sens strict du mot, et ce que nous appelons cas fortuit a son origine dans quelque relation nécessaire, mystérieuse et cachée.

Malheureusement ces lois, auxquelles nous croyons avec une foi si profonde et d'ailleurs si bien justifiée, comme nous le dirons plus loin, nous ne les connaissons pas toutes ; nous n'en connaissons même que très peu ; en outre, nous sommes loin d'avoir cette intelligence sublime qui permettrait d'embrasser dans une même formule tous les mouvements de l'univers physique.

Mais nous ne sommes pas complètement ignorants non plus. Il arrive que nous parvenions à trouver des rapports à peu près constants dans l'apparition de certains phénomènes. C'est alors que le calcul des probabi[p. 56]lités intervient au moyen de la loi des grands nombres et permet de prédire presque à coup sûr, comme nous l'avons dit, les écarts maxima entre lesquels varieront ultérieurement ces rapports sous une ou plusieurs influences perturbatrices.

Le calcul des probabilités a donc pour objet les événements que nous sommes fondés à considérer comme soumis à une loi partiellement inconnue, loi complexe d'ailleurs, résultante d'une loi principale, d'après laquelle des rapports numériques sont constants, et de lois perturbatrices secondaires donnant naissance à de faibles variations de ces rapports, variations dites *fortuites* par définition[^56-a].

Quand donc, en calcul des probabilités, on parle des *lois du hasard*, comme on l'a fait plus d'une fois, il faut bien l'avouer, pour éblouir les profanes[^56-aa], c'est par une hardie figure de langage, une catachrèse, je crois. La loi se rencontre dans la loi principale qui affirme la constance absolue de certains rapports, le hasard dans la perturbation qui les fait un peu varier, soit par l'intervention de causes volontaires, — c'est, ce semble, le hasard, dans le sens propre du mot[^56-aaa], — soit par l'intervention d'autres lois naturelles. Dans ce dernier cas, comme l'a dit Laplace, le hasard n'est que l'ignorance où nous nous trouvons de la nature de ces lois.

[p. 57]

[^55-a]: *Mort de Wallenstein*, acte II, scène 3, vers la fin.

[^56-a]: Bien entendu, ces lois perturbatrices secondaires n'entrent pas en action dans les mêmes circonstances que la loi principale, sans quoi la loi complexe, résultante de la loi principale et des lois perturbatrices, serait une loi absolue pour le phénomène considéré.

[^56-aa]: Bertrand, *Les lois du hasard*, introduction à son cours, pp. VI-L. M. Cantor, *Das Gesetz im Zufall*. Berlin, Habel, 1877.

[^56-aaa]: « La liberté du choix produit, à parler rigoureusement, les seuls cas fortuits. » (Bertrand, p. XLIX.)

### VIII. Application aux jeux.

Les remarques précédentes nous permettent d'indiquer un certain nombre de cas où le calcul des probabilités a une portée objective.

Il y a d'abord les jeux de hasard non équitables, loteries d'État, jeux de trente et quarante, etc., au moyen desquels les *fripons avoués* dont parle Buffon détroussent à coup sûr les contribuables ou les dupes qu'attire l'espérance fallacieuse de gains fabuleux. Le produit annuel de l'ancienne loterie de France pouvait être porté au budget comme un revenu de l'État à peu près certain.

Dans les jeux de hasard équitables, on est étonné du petit nombre de coups nécessaires pour qu'apparaissent les rapports presque constants qui caractérisent la loi des grands nombres. Ainsi, par exemple, dans les jeux où l'on emploie les dés, on remarque bien vite qu'il est facile de s'en procurer d'homogènes, c'est-à-dire tels que chaque face se présente approximativement une fois sur six.

Il en est de même pour les cartes. Gauss jouait tous les soirs au whist avec trois amis. Il a noté, pendant plusieurs années, pour chacun des quatre joueurs, le nombre de fois où ils ont eu dans leur jeu, 1, 2, 3, 4 ou aucun as : il a trouvé que ces nombres étaient à peu près ceux que donnerait le calcul des probabilités.

Ce résultat est d'autant plus curieux qu'il n'y a pas à espérer que les hommes réalisent jamais toutes les combinaisons possibles que peuvent présenter les cinquante-deux cartes d'un jeu de whist : deux cent millions [p. 58] de joueurs devraient pour cela jouer jour et nuit, à deux minutes par jeu, pendant plus de dix mille milliards de siècles, en supposant bien entendu qu'aucune combinaison déjà obtenue ne se reproduise jamais. Dans les observations de Gauss, la constance approximative des rapports exigée par la loi des grands nombres a apparu après un nombre d'épreuves relativement faible[^58-a].

Cette même constance apparaît plus curieuse encore dans un autre jeu, purement mathématique d'ailleurs, où le nombre des cas possibles ne se compte pas par milliards, mais où il est triplement infini, comme le nombre des points d'un volume. Je veux parler du jeu ou problème de l'aiguille. On jette une aiguille, parfaitement cylindrique et homogène, sur un parquet où sont tracées des parallèles équidistantes : leur distance est précisément la longueur de l'aiguille. La probabilité *a priori* que l'aiguille rencontre les parallèles est \((2 : \pi)\), \(\pi\) étant le rapport de la circonférence au diamètre. M. J. Richard, en mille épreuves seulement, a trouvé pour la probabilité *a posteriori* (20 : 31), valeur qui diffère bien peu de la probabilité calculée *a priori*[^58-aa]. Des expériences antérieures avaient donné des résultats analogues.

Dans son *Calcul des probabilités* (pp. 4-5), Bertrand s'est amusé à traiter une question où il y a ainsi un nombre infini de cas possibles, mais de propos délibéré sans doute, il l'a fait de manière à dérouter le lecteur. Il s'agit du problème suivant : *Quelle est la probabilité qu'une corde tracée au hasard dans un cercle est plus petite que le côté* [p. 59] *du triangle équilatéral*. Bertrand donne trois solutions et trois réponses absolument divergentes : 1/2, 1/3, 1/4. Un des plus fins géomètres contemporains, notre associé, M. Ernest Cesàro, a montré depuis longtemps qu'il n'y avait rien d'extraordinaire dans les résultats de Bertrand. Au fond, celui-ci a traité trois problèmes distincts, et si l'on voulait faire des essais expérimentaux y relatifs, il faudrait, pour réaliser les conditions admises implicitement dans les trois solutions, trois dispositifs mécaniques différents[^59-a].

[^58-a]: Voir Cantor, pp. 24-25.

[^58-aa]: *Sur la philosophie des mathématiques*. Paris, Gauthier-Villars, 1903, p. 161.

### IX. Application à la statistique.

La plus belle et la plus utile application de la loi des grands nombres est incontestablement celle qu'on en a faite à la statistique entendue dans le sens le plus large de ce mot. L'importance de la statistique grandit tous les jours à notre époque, parce qu'elle permet de saisir les phénomènes actuels de l'évolution sociale par une sorte d'enregistrement presque continu.

Dans les pays civilisés, le dénombrement exact des naissances, des décès, des mariages, des délits, des crimes et d'une foule d'autres faits sociaux a permis de démêler certaines lois et d'en tirer des conséquences théoriques et pratiques.

[p. 60] Les données relatives aux naissances et aux décès ont permis de calculer des tables dites de mortalité ou mieux de survie. La décroissance régulière des nombres qui y sont inscrits a permis de résumer ces tables dans des formules mathématiques dues à Gompertz et à Makeham. Les tables de survie ou les formules équivalentes sont la base des calculs des innombrables sociétés d'assurances sur la vie qui ont surgi partout et dont les plus anciennes datent de trois siècles. Les nombres inscrits dans ces tables ne sont qu'à peu près constants, ils varient sous mille influences diverses, et les calculateurs de ces sociétés, les actuaires, ont soin de *réajuster* sans cesse leurs tables pour les remettre d'accord avec la réalité. Mais ce sont là précisément les conditions d'application à coup sûr du calcul des probabilités : une loi principale, d'après laquelle certains rapports sont constants, des lois secondaires qui les font varier légèrement, souvent sans qu'on puisse s'en apercevoir qu'après des calculs laborieux. Quelles données historiques hautement intéressantes ne sont pas contenues implicitement dans ces tables de survie, en apparence si arides et si stériles ! Donnons-en un exemple : En 1829, la vie moyenne en Belgique était de 31 ans et 5 mois ; en 1856, de 38 ans et 1 mois ; en 1890, de 45 ans et 1 mois. Mais le changement n'a pas été brusque ; personne ne s'est douté que, d'année en année, chaque Belge, en moyenne, vivait quatre-vingts jours de plus ; personne, sauf toutefois les actuaires, dont plusieurs, dit-on, se servent, dans leurs contrats avec les assurés, des tables de 1856, quand elles sont plus avantageuses pour les assureurs que celles de 1890.

Quetelet a remarqué que les nombres relatifs à l'âge où [p. 61] l'on se marie procèdent avec plus de régularité que ceux qui se rapportent à l'âge où l'on meurt. On en a été étonné, presque scandalisé. Le mariage n'est-il pas un acte plus libre que la mort ? On meurt malgré soi ; on se marie, en général, parce qu'on le veut bien. Cela est vrai. Mais pourquoi les actes libres n'obéiraient-ils à aucune loi ? En réalité, la raison agit chez l'homme comme une règle. Nous sommes réunis aujourd'hui dans cette salle du Palais des Académies pour la séance annuelle de la Classe des sciences. Nous sommes venus les uns de Bruxelles, les autres de Gand, Liége, Louvain, Anvers, Malines, Gembloux, etc. On sait que les membres de l'Académie et leurs auditeurs sont gens raisonnables. On prédira donc hardiment qu'aucun des assistants à cette réunion, étranger à Bruxelles, ne retournera chez lui à pied ; et qu'aucun des Bruxellois, avant de rentrer à son *home*, n'ira faire une promenade à Waterloo. Et pourtant ne sommes-nous pas libres d'agir autrement, ne pourrions-nous pas retourner à pied ou aller relire l'*Expiation* de Victor Hugo dans la *morne plaine* où sombra la fortune de Napoléon ? Mais ce serait trop absurde.

Quand les hommes agissent raisonnablement, ils se conduisent à peu près tous de même dans les mêmes circonstances. C'est pour cela que la loi des grands nombres est applicable à une foule de phénomènes sociaux où la liberté humaine intervient comme facteur principal.

Mais la constance, ou la quasi-constance du nombre des vols à main armée et des crimes, nous dira-t-on, comment allez-vous l'expliquer ? Car cette constance est aussi un fait : *il est un budget*, dit Quetelet, *qu'on paie avec une régularité effrayante, c'est celui des prisons, des* [p. 62] *bagnes et des échafauds* (p. 96). Est-ce qu'on tue, est-ce qu'on vole fatalement ? Les passions sont-elles irrésistibles ?

Non évidemment ; mais dans de telles ou telles circonstances, tel ou tel criminel vole ou tue presque fatalement, comme l'observation le prouve ; dans certains cas, il est presque impossible de résister à la tentation pour ceux qui ont l'habitude du vol et du meurtre, car, suivant le vieux dicton : *l'habitude est une seconde nature*. Les voleurs et les assassins, qui ont depuis longtemps étouffé presque complètement la voix de leur conscience, voleront et tueront probablement en 1904, comme ils ont volé et tué en 1903. Quelques-uns, il est vrai, s'amenderont à cause de leur âge ou de leur vigueur disparue, quelques-uns mourront ou seront emprisonnés et mis dans l'impossibilité de nuire. Mais d'autres sortiront de prison pour recommencer une vie criminelle ; il y en a aussi qui entreront dans la carrière du vol et du meurtre après s'être fait la main en commettant avec une facilité toujours plus grande des délits de plus en plus graves.

Ainsi se recrute l'armée de ces malheureux livrés à leurs plus mauvais instincts. Ce sont ces mauvais instincts, fortifiés par des habitudes invétérées, qui agissent comme une loi, et c'est pour cela que, hélas, on peut prédire quel sera à peu près le terrible *budget du crime* dont a parlé Quetelet. Nous ajoutons avec lui que *c'est celui-là surtout qu'il faut s'attacher à réduire*, parce qu'on le doit et que l'expérience a prouvé qu'on le peut.

En résumé, l'homme qui s'abandonne à ses instincts pervers agit comme d'après une loi ; l'homme qui suit les lumières de sa raison et suivant la belle pensée antique s'efforce d'être le plus homme possible, agit aussi comme [p. 63] d'après une loi. Des rapports numériques à peu près constants s'observent dans certains phénomènes sociaux qui dépendent de ces deux forces adverses, l'une agissant comme force principale, l'autre comme force perturbatrice. La statistique morale, cette création originale de Quetelet, permet de constater, dans les deux cas, jusqu'à quel point l'homme a écouté la voix de sa conscience : *In der Moralstatistik*, dit M. Cantor, *ist dem Gewissen der Menschheit Gelegenheit gegeben sich zu äusseren* (p. 43).

[^59-a]: Le travail de M. Cesàro, malheureusement enfoui dans un recueil élémentaire trop peu connu, le *Periodico di matematica* (1891, janvier et février), contient d'ailleurs les vrais principes relatifs aux probabilités continues et beaucoup d'autres idées justes sur l'objet même de la présente lecture.

### X. Fausses applications mathématiques du calcul des probabilités.

J'aborde maintenant l'examen critique de quelques applications illégitimes du calcul des probabilités et d'abord d'applications mathématiques.

Bienaymé a énoncé et a cru démontrer en 1875[^63-a] le théorème suivant : « Dans une série de nombres pris au hasard, il y en a à peu près un tiers plus grands que celui qui précède et que celui qui suit, un tiers plus petits, un tiers qui sont compris entre le précédent et le suivant » ; autrement dit, à peu près un tiers de maxima, un tiers de minima, un tiers de séquences. Bertrand a essayé de donner une démonstration élémentaire de ce théorème. On l'a en outre vérifié au moyen des tables de logarithmes, en ne considérant que les derniers chiffres des logarithmes des nombres ou des fonctions circulaires.

[p. 64] La démonstration du théorème est inutile, parce qu'il est évident d'après le sens même attaché naturellement aux mots : *nombres choisis au hasard*. Si le théorème énoncé ne se vérifiait pas pour une série de nombres suffisamment étendue, on ne dirait pas de ces nombres qu'ils sont pris au hasard. On ne le dirait pas, par exemple, si les maxima, minima et séquences se succédaient *avec une régularité absolue* comme dans la suite

\[ 1, 5, 2;\ 4, 6, 5;\ 7, 9, 8;\ \text{etc.}, \]

parce que la notion du hasard, en calcul des probabilités, implique qu'il y a une loi, mais une loi *légèrement* troublée par des perturbations. Or, dans la suite indiquée, il y a une loi, mais il n'y a pas de perturbations.

Si, dans une suite de nombres, il y avait continuellement deux séquences après un maximum et un minimum, comme dans celle-ci,

\[ 1, 2, 3, 2;\ 4, 5, 6, 5;\ 7, 8, 9, 8;\ \text{etc.}, \]

on aurait une autre loi que celle de Bienaymé et l'on ne pourrait pas dire non plus que les nombres se suivent au hasard.

La vérification que l'on a faite au moyen des tables de logarithmes ne confirme en rien l'exactitude de la proposition de Bienaymé ; on a simplement constaté que les derniers chiffres des tables se succèdent au hasard dans le sens de son théorème, disons mieux, dans le sens de sa définition du hasard.

Dans son livre : *La science et l'hypothèse* (pp. 224-226), M. Poincaré a montré, à propos d'un autre exemple mathématique, comment, en apparence, on semble appli[p. 65]quer le calcul des probabilités, tandis qu'au fond on démontre, d'abord par à-peu-près, puis rigoureusement, un théorème d'analyse. Parmi les dix mille logarithmes d'une table, dit-il en substance, j'en prends un au hasard. Quelle est la probabilité que sa troisième décimale est un nombre pair. Je n'hésite pas à répondre 1/2, et, en effet, en relevant dans une table les troisièmes décimales de ces dix mille nombres, je trouve à peu près autant de chiffres pairs que de chiffres impairs ; la probabilité objective est donc d'accord avec la probabilité subjective. Mais, en réalité, comme le remarque immédiatement le savant géomètre, la vérification était inutile, parce qu'on peut démontrer rigoureusement qu'il y a à peu près autant de troisièmes décimales paires que d'impaires dans les tables des valeurs de toutes les fonctions continues à dérivées premières et secondes limitées. En répondant 1/2 à la question posée, il faisait, dit-il, dans son for intérieur, d'une façon plus ou moins inconsciente et imparfaite, le raisonnement qui l'a conduit à la démonstration complète du théorème, « comme un calculateur exercé qui avant d'avoir achevé une multiplication se rend compte que *cela va faire à peu près tant* ». Le théorème d'ailleurs est un théorème d'analyse, une loi absolue sans aucune perturbation à laquelle on puisse appliquer le mot de hasard.

Cournot, qui pourtant se piquait d'être philosophe, n'a pas eu autant de perspicacité que M. Poincaré, en traitant une question analogue à la précédente. Il a cru pouvoir appliquer la loi des grands nombres entendue d'une manière très particulière, à la récurrence des dix chiffres 0, 1, 2, ..., 9, dans la valeur de \(\pi\) exprimée au [p. 66] moyen du nombre 3, suivi d'une suite illimitée de décimales[^66-a].

Pour Cournot, les événements fortuits ou les résultats du hasard sont ceux qui sont amenés par l'action simultanée d'autres événements appartenant à des séries indépendantes. C'est une bonne définition du hasard, mais trop large pour les applications du calcul des probabilités, parce que, dans celui-ci, on est toujours forcé de supposer l'une des séries fortement *prédominante et ordonnée*, les autres ne jouant que le rôle de séries *légèrement* perturbatrices.

Cournot, en partant de cette notion du hasard, affirme *a priori* que la suite indéfinie des chiffres du nombre \(\pi\) doit présenter *tous les caractères d'une succession fortuite*, bien que chaque chiffre ait une valeur rigoureusement déterminée ; autrement dit, il doit y avoir, dans la valeur de \(\pi\), à peu près autant de 0, que de 1, 2, 3, ..., 9. Cette assertion repose sur ce qu'il n'y a nulle solidarité, nulle dépendance entre \(\pi\) et la base 10 de la numération décimale.

Observons tout d'abord que l'on ignore s'il n'y a aucune solidarité entre \(\pi\) et 10. Il y en a bien une entre \(\pi\), 5 et 239, comme le prouve la célèbre formule de Machin :

\[ \frac{\pi}{4} = 4\left[\frac{1}{5} - \frac{1}{3}\left(\frac{1}{5}\right)^{3} + \frac{1}{5}\left(\frac{1}{5}\right)^{5} - \frac{1}{7}\left(\frac{1}{5}\right)^{7} + \cdots\right] - \left[\frac{1}{239} - \frac{1}{3}\left(\frac{1}{239}\right)^{3} + \frac{1}{5}\left(\frac{1}{239}\right)^{5} - \frac{1}{7}\left(\frac{1}{239}\right)^{7} + \cdots\right]. \]

[p. 67] Ensuite, n'y eût-il aucune solidarité entre \(\pi\) et 10, comment pourrait-on déduire de là que, dans l'expression de \(\pi\), le nombre des 3 et celui des 4 est à peu près le même ? Sur un nombre donné de décimales, un million par exemple, il y a un nombre déterminé de 3, un nombre déterminé de 4 ; personne n'a prouvé que le rapport de ces deux nombres tende vers l'unité ou vers une autre limite quelconque quand le nombre des décimales croît. Mais eût-on prouvé complètement l'assertion de Cournot, on ne pourrait nullement dire qu'elle est une conséquence de la loi des grands nombres ou d'aucun théorème du calcul des probabilités. C'est une proposition d'analyse, vraie ou fausse, comme la remarque de M. Poincaré sur la troisième décimale des logarithmes. Au fond, Cournot attribue au hasard un rôle régulateur, tandis qu'*en calcul des probabilités, le hasard est, par définition, un perturbateur des lois et des règles*.

[^63-a]: *Comptes rendus de l'Académie des sciences de Paris*, t. LXXXI, pp. 417-423.

[^66-a]: Voir Lechalas, *Le hasard*. (Revue néoscolastique, 1903, pp. 148-164.)

### XI. L'argument épicurien contre les causes finales.

L'erreur la plus ancienne relative au calcul des probabilités est sans doute celle qui est contenue dans l'argument épicurien contre les causes finales. On trouve cet argument dans le *De natura rerum*, ce poème étrange où Lucrèce, le poète pessimiste de la fin de la république, a exposé avec une si naïve ignorance la science arriérée d'Épicure, sans se douter et sans se soucier des immortelles découvertes faites dans l'intervalle par Aristarque de Samos, Archimède, Ératosthènes, Hipparque.

*Nam certe neque consilio primordia rerum*<br>
*Ordine se suo quaeque sagaci menti locarunt*<br>
[p. 68] *Nec quos quaeque darent motus pepigere profecto*,<br>
*Sed quia multa modis multis mutata per omne*<br>
*Ex infinito vexantur percita plagis*,<br>
*Omne genus motus et coetus experiundo*,<br>
*Tandem deveniunt in talis disposituras*,<br>
*Qualibus haec rerum constitit summa creata*.

« Assurément ce n'est pas à dessein ni par une pensée intelligente que les éléments des choses se sont arrangés chacun à leur place ; ils n'ont pas concerté d'avance les mouvements de chacun d'eux. Mais nombreux, changeant de mille manières, partout et toujours, frappés et détournés par des chocs, essayant toute sorte de mouvements et d'assemblages, ils arrivent enfin à cet arrangement des choses qui constitue notre univers[^68-a]. »

C'est dans les mots *omne genus motus et coetus experiundo*, « en essayant toute sorte de mouvements et d'assemblages », que se trouve le postulat de Lucrèce, postulat qu'ont admis d'ailleurs, consciemment ou non, beaucoup de ceux qui ont écrit contre l'argument épicurien ; tous, sans s'en douter, ont en réalité confondu probabilité subjective et probabilité objective. Comme c'est une erreur très commune, expliquons de nouveau la différence entre les deux espèces de probabilités en l'appliquant à la question de l'argument épicurien.

La probabilité objective d'amener un 4 ou un 5 avec un dé est 1/6, si sur 600, 6 000 coups, 4 ou 5 arrive à peu près 100 fois, 1 000 fois, etc. ; elle est 1/2, au contraire, si le dé est pipé et n'amène que 4 ou 5, d'ailleurs avec une égale facilité. Mais dans les deux cas, pour qui a [p. 69] vu simplement le dé, s'il le croit homogène, ou pour qui ne l'a jeté qu'une seule fois, la probabilité subjective est 1/6.

Si les lettres du premier vers de l'Iliade ou, si vous le voulez, de l'Iliade entière peuvent former \(n\) arrangements différents, — mettons un trillion, mais c'est beaucoup trop peu, — l'un d'eux sera, par hypothèse, le poème attribué à Homère. On pourra dire que la probabilité de l'arrivée du poème, quand on arrange toutes les lettres à la suite les unes des autres sans les voir, est un trillionième dans deux sens encore. Dans le sens subjectif, cela signifie simplement que l'Iliade est l'un des arrangements que l'on peut imaginer fait avec ces lettres. Dans le sens objectif, cela veut dire que *les arrangements de ces lettres se font d'après des lois* telles que sur \(p\) fois \(n\) arrangements (mettons sur un dodécillion) l'Iliade se présente environ \(p\) fois (soit un octillion de fois) ; \(p\) est supposé un nombre très grand par rapport à \(n\), comme ici un octillion par rapport à un trillion.

Regardons maintenant le monde actuel depuis que l'on a cru y voir des marques de dessein comme une Iliade immense dont les derniers éléments peuvent former N arrangements. La probabilité subjective de l'arrivée du monde actuel sera \(\frac{1}{\mathrm{N}}\), car cet arrangement existant est un des N possibles. Mais il serait absurde d'admettre que la probabilité objective est aussi \(\frac{1}{\mathrm{N}}\), car ce serait supposer les derniers éléments des corps soumis à des lois telles que, sur PN arrangements, elles forcent ces éléments à passer à peu près P fois par chacun des N arrangements imaginables, P étant très grand par rapport à N. Dans [p. 70] cette hypothèse et dans cette hypothèse seulement, on pourrait admettre le postulat puéril de Lucrèce et d'Épicure : *en essayant toute sorte de mouvements et d'assemblages, les éléments arrivent enfin à cet arrangement des choses qui constitue notre univers*.

Mais qui pourrait établir l'existence des lois dont il vient d'être question ? La loi de la dissémination de l'énergie tend au contraire à prouver que l'univers, loin de repasser périodiquement par les mêmes états, marche vers un état final définitif.

L'argument épicurien est donc sans aucune valeur.

[^68-a]: Texte de la petite édition de Bernays (Leipzig, Teubner, 1874), I, v. 1021-1028 ; ancienne traduction un peu retouchée.

### XII. De la probabilité des causes et des événements futurs tirée des événements observés.

« Bayes, dans les *Transactions philosophiques* de 1765, dit Laplace, a cherché directement la probabilité que les possibilités indiquées par des expériences déjà faites sont comprises entre des limites données ; il y est parvenu d'une manière très fine et très ingénieuse, quoiqu'un peu embarrassée. Cet objet se rattache à la théorie de la probabilité des causes et des événements futurs, conclue des événements observés ; théorie dont j'exposai quelques années après les principes, avec la remarque de l'influence des inégalités qui peuvent exister entre les chances que l'on suppose égales (p. CXXXVII). »

Laplace, contre son habitude, est ici trop modeste ; car les mémoires posthumes de Bayes, publiés en 1764 [p. 71] et 1765, ne contiennent les principes relatifs à la matière que sous forme très imparfaite. C'est Laplace lui-même qui a établi, au moyen des principes antérieurement connus, les deux théorèmes fondamentaux sur la probabilité des causes et des événements futurs, tirée des événements observés.

Au premier abord, ces deux théorèmes semblent pleins de promesses ; ne contiennent-ils pas toute la méthode de la philosophie naturelle : trouver les causes probables des événements observés, prédire les événements futurs, que veut-on de plus ? Il faut bien en rabattre, hélas, parce que les théorèmes de Laplace présupposent la connaissance *a priori* de toutes les causes qui ont pu donner naissance aux événements observés, et de la probabilité, *a priori* aussi, de l'arrivée de ces événements dans l'hypothèse de l'action de chacune de ces causes. Peut-on trouver un seul cas pratique où ces hypothèses soient vérifiées ? Nous en doutons fort.

Aussi toutes les applications connues des principes de Bayes et Laplace à l'étude de la nature n'ont-elles qu'une valeur subjective, comme Bertrand et M. Poincaré l'ont fait remarquer avec beaucoup de force dans leurs ouvrages sur le *Calcul des probabilités*. Ceux qui ont calculé la probabilité de certaines causes en oubliant les conditions d'existence des théorèmes fondamentaux sont arrivés à des résultats démentis par les faits. Laplace, par exemple, à une époque où l'on avait constaté quarante-trois mouvements directs dans les révolutions et les rotations des corps du système solaire, disait que l'on peut parier plus de quatre milliards contre un, qu'une cause générale a déterminé le sens de tous ces mouvements (pp. LX-LXI). [p. 72] On pouvait donc prédire à coup sûr qu'il n'y a pas de mouvements rétrogrades dans le système solaire, et cependant il y en a.

Veut-on une application plus familière qui montre le caractère subjectif de cette théorie ? Je l'emprunte à M. Poincaré[^72-a]. A l'écarté, votre adversaire donne et tourne le roi ; quelle est la probabilité que ce soit un grec ? Dans l'ignorance où l'on est de l'honnêteté de son adversaire, on suppose que cette probabilité *a priori* est 1/2. Alors la probabilité *a posteriori*, déduite de l'arrivée du roi, serait 8/9. Elle serait donc énorme. Si l'on suppose que la probabilité *a priori* est 1/9, la probabilité *a posteriori* est 1/2. Avant l'arrivée du roi, on pouvait donc parier 8 contre 1 que l'adversaire n'était pas un tricheur ; après, seulement 1 contre 1. Évidemment, des conclusions aussi étranges sont purement subjectives.

La conséquence la plus grave en apparence de ce qui précède est la suivante. On expose d'ordinaire la méthode des moindres carrés, en la fondant sur la loi des erreurs accidentelles de Gauss et sur la règle de Bayes ou sur la considération équivalente des probabilités relatives. Il semble donc au premier abord que la méthode des moindres carrés elle-même n'ait plus de portée objective.

Heureusement, il n'en est rien. On n'est pas forcé de baser la méthode des moindres carrés, ni la théorie des moyennes, qui en est un cas particulier, sur la théorie de [p. 73] la probabilité des causes. Comme l'a montré Quetelet, le groupement, suivant la loi exponentielle ou binomiale de Laplace et de Gauss, des valeurs dont on cherche la moyenne est, dans un grand nombre de recherches de physique sociale, un fait contre lequel les critiques subjectives ne peuvent rien. La méthode des moindres carrés peut s'exposer d'une manière purement algébrique, en utilisant les beaux travaux analytiques de MM. Glaisher et Van Geer. On est ainsi d'ailleurs dans la tradition de Legendre, et même de Gauss dans ses leçons, c'est-à-dire des inventeurs de la méthode.

De même, si la règle de Bayes ne peut rien apprendre de sérieux, d'objectif sur l'existence d'une cause du mouvement des planètes dans le sens direct, ou sur d'autres lois naturelles, cela ne prouve pas la non-existence de cette cause ou de ces lois ; cela ne prouve pas qu'un autre principe du calcul des probabilités ne puisse nous donner des lumières sur des questions de ce genre, comme nous le dirons tantôt.

[^72-a]: *Calcul des Probabilités*, p. 134.

### XIII. Application du calcul des probabilités aux décisions judiciaires.

« L'application du calcul des probabilités aux décisions judiciaires est, dit Stuart Mill, le scandale des mathématiques. L'accusation est injuste. On peut peser du cuivre et le donner pour or, la balance est sans reproche. Dans leurs travaux sur la théorie des jugements, [p. 74] Condorcet, Laplace, Poisson » et Cournot « n'ont pesé que du cuivre[^74-a]. »

Ces paroles de Bertrand excusent les mathématiques, mais elles n'excusent pas les mathématiciens — dont deux illustres et même l'un, Laplace, très illustre — d'avoir tenté de soumettre au calcul des probabilités des événements qu'il est évidemment impossible de ranger sous une loi, si peu strictement approximative qu'on la suppose. Au moins avons-nous cette consolation que c'est un mathématicien aussi, Bertrand lui-même, qui a définitivement banni des traités ce chapitre humiliant sur la probabilité des jugements.

L'erreur fondamentale de Condorcet, de Laplace, de Poisson et de Cournot, c'est d'assimiler un jugement au tirage de boules d'une urne qui en contient des blanches et des noires ; l'un suppose que la composition de l'urne est constante pour tous les procès et qu'elle est la même pour tous les juges ; un autre fait varier la composition de l'urne d'un procès à l'autre ; un troisième donne une urne plus riche en boules blanches au juge plus intègre ou plus perspicace.

Mais à tous leurs systèmes, on peut faire une objection sans réplique possible. « L'indépendance des tirages est supposée ; les urnes, dans les calculs, échappent à toute influence commune. Les juges, au contraire, s'éclairent les uns les autres, les mêmes faits les instruisent, les mêmes témoignages les troublent, la même éloquence les égare, c'est sur les mêmes considérants qu'ils font reposer [p. 75] la vérité ou l'erreur. L'assimilation est impossible[^75-a]. »

Frappons-nous donc la poitrine, nous autres mathématiciens, et pour ne plus retomber dans de pareilles aberrations, relisons la page où Pascal a indiqué si bien, quoique avec quelque exagération, selon son habitude, « la différence entre l'esprit de géométrie et l'esprit de finesse ». On peut d'autant plus le croire qu'il a été, lui aussi, une victime de l'esprit mathématique appliqué à la psychologie et à l'apologétique.

« En l'un, dit Pascal, les principes sont palpables, mais éloignés de l'usage commun ; de sorte qu'on a peine à tourner la tête de ce côté-là, manque d'habitude. »

« Mais dans l'esprit de finesse, les principes sont dans l'usage commun et devant les yeux de tout le monde. On n'a que faire de tourner la tête ni de se faire violence. Il n'est question que d'avoir bonne vue, mais il faut l'avoir bonne ; car les principes sont si déliés et en si grand nombre, qu'il est presque impossible qu'il n'en échappe. Or l'omission d'un seul principe mène à l'erreur. »

« Ce qui fait donc que de certains esprits fins ne sont pas géomètres, c'est qu'ils ne peuvent du tout se tourner vers les principes de géométrie ; mais ce qui fait que des géomètres ne sont pas fins, c'est qu'ils ne voient pas ce qui est devant eux et qu'étant accoutumés aux principes nets et grossiers de géométrie, et à ne raisonner qu'après avoir bien vu et manié leurs principes, ils se perdent dans les choses de finesse, où les principes ne se laissent pas ainsi manier. On les voit à peine, on les sent plutôt [p. 76] qu'on ne les voit ; on a des peines infinies à les faire sentir à ceux qui ne les sentent pas d'eux-mêmes ; ce sont choses tellement délicates et si nombreuses, qu'il faut un sens bien délicat et bien net pour les sentir, et juger droit et juste selon ce sentiment, sans pouvoir le plus souvent les démontrer, parce qu'on n'en possède pas ainsi les principes, et que ce serait une chose infinie de l'entreprendre. Il faut tout d'un coup voir la chose d'un seul regard, et non par progrès de raisonnement, au moins jusqu'à un certain degré. Et ainsi il est rare que les géomètres soient fins, et que les fins soient géomètres, à cause que les géomètres veulent traiter géométriquement ces choses fines, et se rendent ridicules, voulant commencer par les définitions, et ensuite par les principes, ce qui n'est pas la manière d'agir en cette sorte de raisonnement. Ce n'est pas que l'esprit ne le fasse ; mais il le fait tacitement, naturellement et sans art, car l'expression en passe tous les hommes et le sentiment n'en appartient qu'à peu d'hommes[^76-a]. »

[^74-a]: Bertrand, p. XLIII.

[^75-a]: Bertrand, p. XLV.

### XIV. Le principe de l'accumulation des probabilités indépendantes de Newman.

Les principes fondamentaux du calcul des probabilités sont peu nombreux : celui des probabilités totales et des probabilités composées, dus à Fermat (1654) ; le théo[p. 77]rème de Bernoulli (1715) et la loi des grands nombres de Poisson (1837) ; les règles de Bayes et de Laplace (1764, 1774) sur les probabilités des causes et des événements futurs. Un dernier *principe* est celui *de l'accumulation des probabilités indépendantes*, entrevu maintes fois dans le passé, mais qui n'a été mis en pleine lumière qu'en 1858, dans la *Grammar of Assent*[^77-a] par J.-H. Newman, plus tard le cardinal Newman, l'un des plus subtils et des plus profonds penseurs de l'Angleterre au XIX<sup>e</sup> siècle.

Pour exposer ce principe, je prends comme guide Newman lui-même, en m'aidant çà et là des spéculations semblables aux siennes, dues à M. Ernest Naville, le savant auteur de la *Logique de l'hypothèse*.

La déduction logique explicite, dit Newman (pp. 288-301, *passim*), n'est pas ce qui nous donne la certitude *dans le domaine des faits concrets*. Nous y arrivons, au contraire, par une accumulation de probabilités, indépendantes entre elles[^77-aa], surgissant de la nature et des circonstances du fait examiné ; probabilités trop faibles pour agir chacune isolément sur notre esprit, trop fines, trop détournées pour être mises explicitement en syllogismes ; trop nombreuses et trop variées d'ailleurs pour être ainsi transformées. Ces probabilités ne s'additionnent [p. 78] pas brutalement, elles agissent et réagissent les unes sur les autres, se corrigent ou se confirment de manière à conduire l'esprit à l'assentiment complet, sans qu'il soit pleinement conscient du chemin suivi. Cet assentiment est personnel, même lorsqu'il existe pour un même fait concret chez un grand nombre de personnes, parce que les probabilités accumulées ne sont pas vues par tous distinctement chacune à part, et qu'elles varient en nombre et en poids suivant les divers intellects : *Omne quod recipitur in aliquo, recipitur ad modum recipientis*. Ce qui est une preuve pour un esprit ne l'est pas pour un autre, qui ne parvient pas à l'examiner sous le même angle. Comme l'a dit Pascal, « dans les choses de finesse, on a des peines infinies à les faire sentir (les principes) à ceux qui ne les sentent pas par eux-mêmes ».

Prenons maintenant, avec Newman, des exemples de preuve implicite basée sur une accumulation de probabilités indépendantes.

« Nous sommes tous certains, dit-il, sans aucune possibilité de doute, que l'Angleterre est une île. C'est là une proposition à laquelle nous donnons un assentiment complet ! Il n'existe rien qui soit plus sûr et nous ferions volontiers dépendre nos plus chers intérêts de la vérité de ce fait que nous vivons dans une île. Nous ne craignons pas qu'aucune découverte vienne jamais ébranler notre croyance, et il nous serait impossible de regarder comme sérieuse l'assertion de celui qui nous dirait que l'Angleterre est rattachée au continent du côté de la Norvège ou de la France. Et cependant les arguments que nous pou[p. 79]vons faire valoir pour expliquer notre conviction sur ce point sont-ils en rapport avec l'extrême certitude que nous en avons ? On nous a dit dans notre enfance que l'Angleterre est une île ; elle est entourée par la mer sur toutes les cartes ; jamais la chose n'a été mise en question devant nous ; au contraire, nous avons toujours entendu dire, tous les livres que nous avons lus admettent que l'Angleterre est une île ; toute notre histoire nationale, toute notre vie commerciale, sociale et politique le suppose. Mais nous n'en avons pas de preuve directe comme celui qui aurait fait le tour de l'Angleterre ; et nous n'avons peut-être même jamais rencontré quelqu'un qui l'ait fait. Est-ce à dire que notre conviction n'est pas raisonnable ? Nullement. Mais il est certain que nous ne pouvons que difficilement analyser d'une manière complète les raisons de notre assentiment. »

Ce que Newman dit ici à propos de l'Angleterre s'étend à la science géographique tout entière : « Que peut-on connaître par soi-même, dit M. Naville ? Les chemins que l'on a parcourus et les horizons que l'on a embrassés du regard : cela est toujours bien peu. Ce que les plus grands voyageurs ont pu percevoir directement ne formerait qu'une ligne peu visible sur un globe de très grande dimension[^79-a]. » Et cependant tout le monde [p. 80] croit à la géographie, non seulement les savants chez qui existe le sens critique, mais les jeunes gens de nos collèges chez qui il n'est pas éveillé encore. Tous, consciemment ou non, admettent et appliquent le principe de l'accumulation des probabilités indépendantes, agissant et réagissant les unes sur les autres, de manière à produire la plus complète certitude.

Ce que nous venons de dire pour le présent, pour la géographie, nous pouvons le dire pour le passé, pour l'histoire. Toute l'histoire repose sur les témoignages de nos devanciers. A la rigueur, je puis aller voir si l'Angleterre est vraiment une île, mais il m'est impossible d'assister à la bataille de Salamine ; je ne puis pas entendre, comme Eschyle, *la clameur immense*, — *modulée comme un chant sacré*, — *qui s'élève dans les rangs des Grecs*, — ni *l'écho des rochers de l'île* près de laquelle se livrait en ce moment une des batailles [p. 81] décisives de la civilisation contre la barbarie. Ce que je dis de Salamine, je le dis aussi de la victoire de Scipion à Zama, de celle de Charles Martel à Poitiers, de la défaite de Napoléon à Waterloo. Nous ne doutons de la réalité d'aucun de ces grands faits de l'histoire ; leur retentissement dans la vie de l'humanité a été si profond qu'en supprimer un seul ce serait rendre incompréhensible l'ensemble de ses annales et le présent lui-même. Mais quel tissu subtil de probabilités ne faudrait-il pas exposer à quelque habitant d'une autre planète tombé soudain parmi nous pour lui transmettre nos convictions ! S'il avait lu Laplace quelque part là-haut, dans la planète Mars ou dans Jupiter, ne nous opposerait-il pas ce célèbre passage : « L'action du temps affaiblit sans cesse la probabilité des faits historiques, comme elle altère les monuments les plus durables. On peut, à la vérité, la ralentir en multipliant et conservant les témoignages et les monuments qui les étayent. Malgré les avantages infinis que procure l'imprimerie, les révolutions physiques et morales dont la surface de ce globe sera toujours agitée finiront, en se joignant à l'effet inévitable du temps, par rendre douteux, après des milliers d'années, les faits historiques les plus certains (p. LXXXII). » Que pourrions-nous répondre à ce Martien ou Jovien qui applique ici de travers, avec Laplace, le principe des probabilités composées ? Nous ne pourrions lui donner évidemment notre connaissance actuelle de la solidarité, des connexions nécessaires de toutes les périodes de l'histoire. Nous serions réduits à lui dire avec Pascal que « les géomètres qui ne sont que géomètres ont l'esprit droit, mais pourvu qu'on leur explique bien toutes choses par [p. 82] définitions et par principes » ; qu' « autrement ils sont faux et insupportables, car ils ne sont droits que sur les principes éclaircis » (*Pensées*, éd. Didiot, p. 60) ; puis nous devrions attendre patiemment qu'il apprenne à connaître le principe de l'accumulation des probabilités indépendantes, ou plutôt qu'il apprenne à s'en servir.

Mais d'où vient la force probante de ce principe ? comment peut-il engendrer la certitude, même si chacune des probabilités considérées est très petite, pourvu qu'elles soient nombreuses ? Au fond, comme Newman le dit plusieurs fois, et comme nous l'insinuons déjà plus haut, c'est la *méthode de réduction à l'absurde*, si puissante en métaphysique et dans les hautes mathématiques, qui, appliquée ici à l'ordre concret, constitue la partie principale, l'essence de ces raisonnements implicites, de ces rapides intuitions de l'esprit. Supposez que l'Angleterre ne soit pas une île, que Napoléon ait été vainqueur à Waterloo, et vous ne comprenez plus rien à l'histoire ni à la géographie contemporaines : vous êtes acculés à l'absurde ou au moins à l'inexplicable[^82-a]. En réalité, l'axiome rationnel qui est à la base de la démonstration de la loi des grands nombres est donc aussi le fondement du principe de l'accumulation des probabilités indépendantes : *le contraire d'un événement très improbable, est extrêmement probable* ou *pratiquement certain*.

[p. 83] Analytiquement, le principe de Newman peut se traduire à peu près par la formule

\[ \mathrm{P} = 1 - \varphi(n)(1 - p_{1})(1 - p_{2}) \ldots (1 - p_{n}), \]

où \(p_{1}, p_{2}, \ldots, p_{n}\) sont les probabilités accumulées ; \(\varphi(n)\) une fonction de \(n\), décroissante de 1 à 0, quand \(n\) croît de 1 à \(\infty\), et exprimant l'interdépendance subjective des probabilités \(p_{1}, \ldots, p_{n}\) ; pour \(n\) croissant, la probabilité cherchée P tend vers l'unité[^83-a].

[^76-a]: *Pensées*, édition Didiot (Lille, Desclée, 1896), pp. 59-60. Cette édition, selon nous, est la seule bonne au point de vue philosophique et théologique.

[^77-a]: Nous nous servons de la cinquième édition : London, Long-mans, Green and Co, 1885 ; mais nous ne la citons pas textuellement, la perfection de la prose de Newman la rendant souvent intraduisible.

[^77-aa]: Elles sont *objectivement indépendantes*, hétérogènes, si j'ose ainsi dire (voir l'exemple du juge au paragraphe suivant) ; subjectivement, on pourrait, au contraire, les dire *interdépendantes*, puisqu'elles réagissent les unes sur les autres dans notre esprit.

[^79-a]: *L'importance logique du témoignage*, p. 5 du tirage à part. Voici une autre remarque très juste du même (pp. 4-5) : « Les choses que nous percevons nous-mêmes n'ont leur sens et leur portée que par l'adjonction d'idées empruntées au témoignage. Un jour, à Paris, j'ai vu sur le quai qui longe les Tuileries l'empereur Napoléon III passer dans un cabriolet qu'il conduisait lui-même. Voilà un fait que j'ai constaté par moi-même ; nous réduisons ce fait aux éléments des perceptions personnelles séparées des idées qui proviennent d'une autre source. J'ai vu un grand bâtiment ; comment savais-je que ce bâtiment se nommait les Tuileries et qu'il était la résidence du souverain de la France ? Par le témoignage des autres. J'ai vu un homme passer ; comment savais-je que cet homme s'appelait Napoléon III et qu'il était l'empereur des Français ? Par le témoignage. Si je réduis le fait aux données de mes perceptions personnelles, voici ce qui reste : J'ai vu, près d'un grand bâtiment, un homme qui conduisait un cabriolet, rien de plus. *Les faits qui se passent sous nos yeux n'ont leur sens et leur valeur que par l'intervention d'idées que nous devons aux affirmations de nos semblables*. »

[^82-a]: Notez que c'est le grand nombre de probabilités militant en faveur de la proposition à établir et non l'*autorité* des témoignages, qui permet d'employer la méthode de réduction à l'absurde. C'est d'ailleurs aussi au moyen de l'accumulation des probabilités que l'on parvient à établir l'autorité des témoignages et des témoins.

### XV. Applications diverses du principe de Newman.

Les applications du principe de Newman sont infinies dans le domaine de la vie pratique comme dans celui des sciences historiques et naturelles.

Un juge instruit un procès criminel où il y a eu vol avec effraction et meurtre ; il se forme peu à peu une conviction de plus en plus nette de la culpabilité du [p. 84] prévenu par accumulation de probabilités déduites d'indices souvent bien faibles, quand on les considère isolément : traces de pas, blessures récentes constatées chez le prévenu, trouble à sa première rencontre avec la justice, explications embarrassées, contradictions, impossibilité pour lui de prouver son alibi, ou alibi trop visiblement préparé d'avance, dépositions variées de témoins à charge et à décharge, antécédents de l'accusé, dépenses inusitées après le crime, etc., etc.

Un clinicien expérimenté procède de même avant de donner son diagnostic dans un cas difficile.

Il en est ainsi encore dans les sciences de la nature en général. Nous avons parlé plus haut de l'application illégitime que Laplace a faite de la théorie de la probabilité des causes à la question du mouvement direct des corps du système solaire. Mais si son raisonnement est sans force probante, cela n'entraîne pas la fausseté de sa conclusion ; il y a très probablement une cause unique du sens direct de presque tous ces mouvements. Quand on lit la suite de son texte, on voit que la conviction de Laplace ne provient pas de la règle dite de Bayes, mais de la connexion de la question agitée par lui avec sa célèbre hypothèse de la nébuleuse primitive. Or, cette hypothèse, il l'appuie, comme on le sait, sur presque tous les faits de la mécanique et de la physique du ciel ; chacun d'eux ne donne qu'une probabilité très faible à l'hypothèse ; mais leur ensemble a un grand poids, et il n'a fait qu'augmenter depuis la découverte de plus de cinq cents petites planètes et depuis que l'analyse spectrale nous a révélé la composition chimique des soleils et des nébuleuses.

Tous les savants, astronomes, physiciens, chimistes, [p. 85] géologues, biologistes, botanistes, zoologistes, font nécessairement usage du principe de l'accumulation des probabilités indépendantes, chaque fois qu'ils s'appuient sur le témoignage ou la science d'autrui. Or, qui n'est forcé de le faire, même les mathématiciens ? « Toute la suite des hommes, dit Pascal, doit être considérée comme un même homme, qui subsiste toujours et qui apprend continuellement[^85-a]. »

Un biologiste emploie le microscope et recourt à des réactifs divers pour étudier les mystères de l'organisation et du développement des cellules ; il croit forcément à la théorie des lentilles et, par suite, à l'optique et à la physique tout entière ; il admet la pureté de ses réactifs, ce qui implique de proche en proche toute la chimie. Il en est de même de l'astronome qui observe le spectre du soleil. Au fond, l'un et l'autre croient à la physique et à la chimie comme nous autres profanes, nous croyons que l'Angleterre est une île. Cette croyance, légitime d'ailleurs, bien que difficile à justifier en détail, repose sur des témoignages, c'est-à-dire sur des probabilités accumulées. Mais il y a plus, il en est de même de chaque savant dans sa propre science ; le physicien, par exemple, ne peut faire une recherche originale sans accepter préalablement les résultats établis par ses prédécesseurs, car il ne peut refaire à lui seul des expériences qui ont coûté des siècles. En mathématiques, les analystes purs admettent sur le témoignage des géomètres, dans le sens strict du mot, les propriétés des surfaces du troisième ordre ou les résultats de la théorie générale des surfaces ; inversement, les géomètres s'en rapportent aux analystes [p. 86] touchant la vérité de théories difficiles comme celle des nombres algébriques, des substitutions ou des fonctions abéliennes : ils pourraient aller voir dans les terribles in-quarto de Kronecker, de Jordan et de Weierstrass si les démonstrations des analystes sont bonnes, comme nous pourrions, en cas de nécessité absolue, aller voir si l'Angleterre est une île ; mais chacun a autre chose à faire dans son propre domaine et préfère se fier au témoignage des gens dont il a reconnu la compétence.

L'histoire de la science, l'histoire de la naissance, du progrès et de la décadence des systèmes scientifiques s'explique et s'éclaire souvent à la lumière du principe de l'accumulation des probabilités indépendantes. Il y a vingt-trois siècles, le génie peut-être le plus systématique et le plus réaliste qui fut jamais, Aristote, fait une synthèse de toutes les connaissances de son temps, sur Dieu, l'homme, la nature vivante, le ciel et la terre, en ne laissant de côté que les mathématiques pures. Il relie des milliers de faits au moyen de quelques idées fondamentales, matière, forme, forme substantielle, puissance, acte, finalité, accident, substance ; il les enchaîne, ou les explique, comme on dit, au moyen de quelques principes, point d'arrivée ou point de départ : Dieu est acte pur ; ce qui passe de la puissance à l'acte, le fait sous l'influence de ce qui est en acte ; le mouvement centripète ou centrifuge caractérise les quatre éléments de la physique terrestre, le mouvement circulaire, le cinquième élément et la physique céleste, etc. Le tissu des faits réels et des hypothèses qui les relie est si serré, le système total repose sur un nombre si grand de probabilités accumulées que, pendant plus de deux mille ans, il est considéré comme la vérité même, à l'égal des *Éléments* [p. 87] d'Euclide, pour l'arithmétique et la géométrie. Aussi, quand Galilée renverse la barrière qui sépare la physique céleste[^87-a] de la physique terrestre et transforme celle-ci en y introduisant le principe de l'inertie, avec quelle peine ne triomphe-t-il pas de l'amas des probabilités anciennes qui plaidaient en faveur de celle d'Aristote ! Il ne réussit que peu à peu, en accumulant à son tour des faits et des probabilités en faveur des vues nouvelles. Il en est de même quand Lavoisier fait la révolution chimique, quand Ampère, Faraday, Fresnel, Carnot, Mayer, Clausius, Helmholtz, Plateau, lord Kelvin, Maxwell, Hertz, tous les voyants de la physique au XIX<sup>e</sup> siècle, remplacent les vérités incomplètes de leurs devanciers par des lumières plus vives. Les nouveaux systèmes ne parviennent pas tout de suite à s'annexer et à s'approprier toutes les probabilités accumulées qui semblent militer exclusivement en faveur des anciens systèmes. Il en est ainsi pour toutes les sciences de la nature.

Dans l'histoire de la pensée humaine, il y a des livres immortels qui ont une influence finalement prépondérante, la *Métaphysique* d'Aristote, les *Éléments* d'Euclide, la *Somme* de S. Thomas d'Aquin, les *Principes* de Newton. Mais d'autres écrits d'une forme dialectique [p. 88] moins dominatrice, mais pleins de faits accumulés d'observation interne ou externe, sans rigueur de déduction apparente, ont eu de tout temps une influence plus immédiate, plus étendue, sinon plus profonde. J'en citerai trois, bien différents sous tous les rapports : l'*Imitation de Jésus-Christ*, cette fleur suprême du moyen âge ; les *Pensées* de Pascal, ce singulier mélange d'apologétique vraiment chrétienne, de jansénisme impitoyable et de psychologie outrancière ; enfin l'*Origin of species* de Darwin, où sous mille formes se retrouvent des vues contraires au principe aristotélicien sur le passage de la puissance à l'acte. Ouvrez-les au hasard, vous y rencontrerez à toutes les pages des pensées, des remarques, des inductions, des faits qui vous paraîtront plus ou moins vraisemblables suivant votre degré de culture et de réceptivité, mais dont l'ensemble exercera sur vous, si vous les fréquentez beaucoup, une action singulièrement pénétrante. C'est qu'au fond, Thomas a Kempis, Pascal et Darwin y répètent sans cesse chacun une seule et même pensée, sans se lasser jamais, parce qu'ils sont convaincus : *le joug du Seigneur est doux et léger* — *le christianisme est transcendant, mais* (c'est ici la note janséniste) *il est dur* — *le monde organique est dans un perpétuel devenir* ; ils conquièrent ou essaient de conquérir l'esprit, le cœur, l'âme entière du lecteur par une accumulation de probabilités convergeant toutes vers un même but[^88-a].

[p. 89]

[^83-a]: Philosophiquement parlant, il faut évidemment distinguer la certitude pratique de la certitude logique que nous avons de certaines propositions : *la suite des nombres premiers est illimitée, aucun polyèdre n'a sept arêtes*, etc. Mais en fait, nous donnons souvent un assentiment aussi complet à des propositions de l'ordre concret pratiquement certaines (*l'Angleterre est une île, Napoléon a été vaincu à Waterloo*) qu'aux propositions mathématiques que nous venons de citer. *Correlation between certitude and implicit proof seems to me a law of our minds*, dit Newman (p. 301). Comparez De Smedt, S. J., *Principes de la critique historique*, Paris, 1883, chap. IV (surtout pp. 63, 68-69, 71), où l'auteur expose et défend très bien le principe de l'accumulation des probabilités indépendantes appliqué à l'histoire.

[^85-a]: Pascal, éd. Didiot, p. 291.

[^87-a]: Nous faisons allusion à ses découvertes des taches du Soleil, des montagnes de la Lune, qui prouvaient que les astres, comme la terre, étaient soumis au changement ; non à sa querelle philosophico-théologique avec les congrégations romaines où ni lui, ni ses adversaires n'avaient de preuves en faveur de leurs vues subjectives contraires. Le système astronomique d'Aristote avait d'ailleurs été abandonné dès l'antiquité.

[^88-a]: N'est-ce pas d'une manière analogue, n'est-ce pas à cause de leur profond réalisme, dans le sens plein du mot, que, dans le domaine de la fiction, ces livres immortels aussi, l'*Iliade*, la *Divine Comédie*, les drames de Shakespeare, le *Faust* de Goethe ont une influence si durable et si profonde sur l'humanité cultivée ?

### XVI. Conclusion.

Mais il est temps de conclure cette étude, où nous nous sommes peut-être laissé trop entraîner dans des chemins de traverse, et de résumer en quelques lignes nos conclusions sur la portée objective du calcul des probabilités.

Le principe fondamental est celui-ci : Entre deux propositions contraires, l'une peu probable, l'autre très probable, l'esprit humain choisit la seconde, *librement*, *mais presque invinciblement*, et la déclare pratiquement certaine.

On déduit de là la légitimité logique de la loi des grands nombres et du principe de l'accumulation des probabilités indépendantes.

La loi des grands nombres s'applique d'abord à la question de la ruine du joueur et à ses conséquences, ensuite à la statistique chaque fois qu'elle rencontre des rapports à peu près constants dans les nombres qu'elle rassemble.

Le principe de l'accumulation des probabilités indépendantes est *pratiquement, sinon métaphysiquement*, la source de nos certitudes dans les sciences naturelles et historiques qui reposent en dernière analyse sur le témoignage, chaque fois que nous ne sommes pas personnellement inventeur ou témoin.

La loi des grands nombres et le principe de l'accumulation des probabilités indépendantes impriment fortement dans nos esprits la croyance à l'existence des lois naturelles, et ne laissent à ce que l'on appelle le [p. 90] hasard que le rôle d'une cause inconnue légèrement perturbatrice.

Notre conclusion suprême, où nous laissons presque complètement la parole à Quetelet (p. 102), est donc celle-ci :

« Le hasard, ce mot mystérieux dont on a tant abusé, ne doit être regardé que comme servant à couvrir notre ignorance ; c'est un fantôme qui exerce l'empire le plus absolu sur le vulgaire habitué à ne considérer les faits qu'isolément, mais qui s'évanouit devant le philosophe dont l'œil embrasse une longue suite d'événements et dont la pénétration ne saurait être mise en défaut par des écarts qui disparaissent à ses yeux quand il sait se placer assez haut pour saisir les lois de la nature ; il n'est pas en notre pouvoir de les changer ; mais il est de notre dignité de chercher à les saisir au milieu des anomalies sans nombre qu'elles semblent présenter », car « ces lois sont éternelles[^90-a] comme l'intelligence dont elles découlent », Dieu. Pour lui, *rien n'est incertain et l'avenir comme le passé est présent à ses yeux*, suivant la belle parole de Laplace.

[p. 91]

[^90-a]: Un métaphysicien aurait dit, je crois, *au moins dans l'intelligence dont elles découlent*.

## TABLE DES MATIÈRES

| | |
|:---|---:|
| I. Doutes sur la portée objective du calcul des probabilités | 31 |
| II. Pascal et Fermat. La théorie des jeux | 36 |
| III. Un cas où la probabilité devient presque une certitude | 40 |
| IV. Le théorème de Bernoulli et la loi des grands nombres | 43 |
| V. La ruine du joueur. La guerre | 47 |
| VI. Application au transformisme | 50 |
| VII. La vraie nature du calcul des probabilités et du hasard | 53 |
| VIII. Application aux jeux | 57 |
| IX. Application à la statistique | 59 |
| X. Fausses applications mathématiques du calcul des probabilités | 63 |
| XI. L'argument épicurien contre les causes finales | 67 |
| XII. De la probabilité des causes et des événements futurs tirée des événements observés | 70 |
| XIII. Application du calcul des probabilités aux décisions judiciaires | 73 |
| XIV. Le principe de l'accumulation des probabilités indépendantes de Newman | 76 |
| XV. Applications diverses du principe de Newman | 83 |
| XVI. Conclusion | 89 |

[p. 92] Extrait des *Bull. de l'Acad. roy. de Belgique* (Classe des sciences), n° 12 [décembre], 1903, pp. 1235-1294.

[p. 93]

## Sur une intégrale considérée en calcul des probabilités.

**1.** *Objet de la présente note*. Nous nous proposons de calculer d'une manière approximative les rapports \([(\mathrm{A} + \mathrm{Q}) : \mathrm{E}]\), \([(\mathrm{A} - \mathrm{P}) : \mathrm{E}]\), \([(\mathrm{B} + \mathrm{P}) : \mathrm{E}]\), \([(\mathrm{B} - \mathrm{Q}) : \mathrm{E}]\) considérés autrefois par Poisson[^93-a], A, B, P, Q, E, ayant les valeurs suivantes :

\[ \mathrm{A} = \int_{0}^{p} z^{m}(1 - z)^{n}\,dz, \qquad \mathrm{B} = \int_{p}^{1} z^{m}(1 - z)^{n}\,dz, \]

\[ \mathrm{P} = \int_{p-l}^{p} z^{m}(1 - z)^{n}\,dz, \qquad \mathrm{Q} = \int_{p}^{p+l} z^{m}(1 - z)^{n}\,dz, \]

\[ \mathrm{E} = \int_{0}^{1} z^{m}(1 - z)^{n}\,dz. \]

On suppose \(m\) et \(n\) entiers ; \(m + n = \mu\) ; \(m = \mu p\), \(n = \mu q\) ; \(l\) est tout au plus égal à la moitié de la plus [p. 94] petite des fractions \(p\), \(q\). Pour fixer les idées, nous supposerons \(p\) égal ou supérieur à \(q\), ou \(m\) égal ou supérieur à \(n\). D'après les hypothèses, \(p + q = 1\).

**2.** *Valeurs approximatives préliminaires*. Nous avons démontré[^94-a] que

\[ \sqrt{1 - e^{-\frac{4}{3}\mathrm{T}^{2}}} > \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt > \sqrt{1 - e^{-\mathrm{T}^{2}}}, \]

\[ \mathrm{T} = l\sqrt{\frac{\mu}{2pq}}. \]

Mais pour \(\alpha < 1\),

\[ 1 - \frac{1}{2}\alpha > \sqrt{1 - \alpha} > 1 - \alpha. \]

Donc

\[ 1 - \frac{1}{2} e^{-\frac{4}{3}\mathrm{T}^{2}} > \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt > 1 - e^{-\mathrm{T}^{2}}, \]

ou encore

\[ e^{-\mathrm{T}^{2}} > 1 - \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt > \frac{1}{2} e^{-\frac{4}{3}\mathrm{T}^{2}}. \]

Pour abréger les écritures, nous poserons, dans la suite,

\[ \mathrm{J} = \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt \text{ ou } \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt = \frac{1}{2}\sqrt{\pi}\,\mathrm{J}. \]

[p. 95] **3.** *Limites de* E. On a, comme l'on sait,

\[ \mathrm{E} = \frac{\Gamma(m + 1)\Gamma(n + 1)}{\Gamma(m + n + 2)} = \frac{m!\,n!}{\mu!} \cdot \frac{1}{\mu + 1}. \]

D'après la formule de Stirling,

\[ \sqrt{2\pi m}\, m^{m} e^{-m} < m! < \sqrt{2\pi m}\, m^{m} e^{-m + \frac{1}{12m}}, \]

\[ \sqrt{2\pi n}\, n^{n} e^{-n} < n! < \sqrt{2\pi n}\, n^{n} e^{-n + \frac{1}{12n}}, \]

\[ \sqrt{2\pi\mu}\, \mu^{\mu} e^{-\mu} < \mu! < \sqrt{2\pi\mu}\, \mu^{\mu} e^{-\mu + \frac{1}{12\mu}}. \]

On tire aisément de là

\[ \frac{\sqrt{2\pi mn}}{\sqrt{\mu}(\mu + 1)} \left(\frac{m}{\mu}\right)^{m} \left(\frac{n}{\mu}\right)^{n} e^{-\frac{1}{12\mu}} < \mathrm{E}, \]

\[ \mathrm{E} < \frac{\sqrt{2\pi mn}}{\sqrt{\mu}(\mu + 1)} \left(\frac{m}{\mu}\right)^{m} \left(\frac{n}{\mu}\right)^{n} e^{\frac{1}{12m} + \frac{1}{12n}}, \]

ou encore, en introduisant \(\mu p\), \(\mu q\) au lieu de \(m\), \(n\),

\[ \sqrt{2\pi\mu pq}\, p^{\mu p} q^{\mu q} \frac{1}{(\mu + 1)\, e^{\frac{1}{12\mu}}} < \mathrm{E}, \]

\[ \mathrm{E} < \sqrt{2\pi\mu pq}\, p^{\mu p} q^{\mu q} \frac{1}{(\mu + 1)\, e^{-\frac{1}{12\mu pq}}}. \]

[p. 96] Or, on a d'abord

\[ (\mu + 1)\, e^{\frac{1}{12\mu}} < \mu + 2, \text{ ou } \frac{1}{12\mu} < \log\left(1 + \frac{1}{\mu + 1}\right). \]

En effet,

\[ \log\left(1 + \frac{1}{\mu + 1}\right) > \frac{1}{\mu + 1} - \frac{1}{2}\,\frac{1}{(\mu + 1)^{2}} > \frac{1}{\mu + 1}\left(1 - \frac{1}{2\mu}\right) \]

et, évidemment,

\[ \frac{1}{\mu + 1}\left(1 - \frac{1}{2\mu}\right) > \frac{1}{12\mu} \]

ou

\[ 6(2\mu - 1) > \mu + 1, \]

c'est-à-dire \(11\mu > 7\). — Ensuite

\[ (\mu + 1)\, e^{-\frac{1}{12\mu pq}} > \mu\left(1 - \frac{1}{12\mu pq}\right). \]

Donc enfin

\[ \frac{1}{\mu + 2}\sqrt{2\pi\mu pq}\, p^{m} q^{n} < \mathrm{E} < \frac{1}{\mu - \frac{1}{12pq}}\sqrt{2\pi\mu pq}\, p^{m} q^{m}. \]

**4.** *Limites de* A *et* B. 1° \(\mathrm{A} > \frac{1}{2}\mathrm{E}\), \(\mathrm{B} < \frac{1}{2}\mathrm{E}\). En effet, on a d'abord \(\mathrm{A} + \mathrm{B} = \mathrm{E}\), ensuite, comme nous allons le prouver, \(\mathrm{A} \mathrel{\overset{=}{>}} \mathrm{B}\). [p. 97] On trouve, en faisant

\[ z = p - x, \qquad 1 - z = q + x, \]

\[ \mathrm{A} = \int_{0}^{p} z^{m}(1 - z)^{n}\,dz \mathrel{\overset{=}{>}} \int_{p-q}^{p} z^{m}(1 - z)^{n}\,dz = \int_{0}^{q} (p - x)^{m}(q + x)^{n}\,dx. \]

De même, en faisant

\[ z = p + x, \qquad 1 - z = q - x, \]

\[ \mathrm{B} = \int_{p}^{1} z^{m}(1 - z)^{n}\,dz = \int_{0}^{q} (p + x)^{m}(q - x)^{n}\,dx. \]

Or, on a

\[ (p - x)^{m}(q + x)^{n} \mathrel{\overset{=}{>}} (p + x)^{m}(q - x)^{n}; \]

car cela revient à

\[ \left(\frac{q + x}{q - x}\right)^{n} \eqslantgtr \left(\frac{p + x}{p - x}\right)^{m}, \]

ou à

\[ n \log\frac{q + x}{q - x} \mathrel{\overset{=}{>}} m \log\frac{p + x}{p - x}, \]

ou, en dérivant, à

\[ n\left(\frac{1}{q + x} + \frac{1}{q - x}\right) \mathrel{\overset{=}{>}} m\left(\frac{1}{p + x} + \frac{1}{p - x}\right), \]

c'est-à-dire, successivement,

\[ \frac{2\mu q^{2}}{q^{2} - x^{2}} \mathrel{\overset{=}{>}} \frac{2\mu p^{2}}{p^{2} - x^{2}}, \qquad q^{2}(p^{2} - x^{2}) \mathrel{\overset{=}{>}} p^{2}({}^{2} - x^{2}), \qquad p^{2} \mathrel{\overset{=}{>}} q^{2}. \]

[p. 98] De proche en proche, de la dernière relation, on remonte à \(\mathrm{A} > \mathrm{B}\), sauf dans le cas où \(p = q\), \(m = n\) ; alors évidemment, \(\mathrm{A} = \mathrm{B} = \frac{1}{2}\mathrm{E}\).

**2°** *Limite inférieure de* B. On peut écrire

\[ \mathrm{B} = p^{m}q^{n} \int_{0}^{q} \left(1 + \frac{x}{p}\right)^{m} \left(1 - \frac{x}{q}\right)^{n} dx > p^{m}q^{n}\,\mathrm{B}_{1}, \]

si l'on pose

\[ \mathrm{B}_{1} = \int_{0}^{q-\alpha} \left(1 + \frac{x}{p}\right)^{m} \left(1 - \frac{x}{q}\right)^{n} dx, \]

\(\alpha\) étant indéterminé. Faisons

\[ \left(1 + \frac{x}{p}\right)^{m} \left(1 - \frac{x}{q}\right)^{n} = e^{u}, \]

ou

\[ u = m \log\left(1 + \frac{x}{p}\right) + n \log\left(1 - \frac{x}{q}\right). \]

On aura

\[ u' = \mu\left[\frac{1}{1 + \frac{x}{p}} - \frac{1}{1 - \frac{x}{q}}\right] \]

\[ = \mu\left[1 - \frac{x}{p} + \frac{x^{2}}{p(p + x)} - 1 - \frac{x}{q} - \frac{x^{2}}{q(q - x)}\right] \]

\[ = -\frac{\mu x}{pq} - \mu x^{2}\left[\frac{1}{q(q - x)} - \frac{1}{p(p + x)}\right] > -\frac{\mu x}{pq} - \frac{\mu x^{2}}{q\alpha}. \]

[p. 99] Donc

\[ u > -\frac{\mu x^{2}}{2pq} - \frac{\mu x^{3}}{3q\alpha}, \qquad e^{u} > c^{-\frac{\mu x^{2}}{2pq}} \cdot e^{-\frac{\mu x^{3}}{3q\alpha}} > e^{-\frac{\mu x^{2}}{2pq}}\left(1 - \frac{\mu x^{3}}{3q\alpha}\right). \]

On déduit de là

\[ \left(1 + \frac{x}{p}\right)^{m} \left(1 - \frac{x}{q}\right)^{n} = e^{u} > e^{-\frac{\mu x^{2}}{2pq}}\left(1 - \frac{\mu x^{3}}{3q\alpha}\right), \]

\[ \mathrm{B}_{1} = \int_{0}^{q-\alpha} e^{u}\,dx > \int_{0}^{q-\alpha} e^{-\frac{\mu x^{2}}{2pq}}\,dx - \frac{\mu}{3q\alpha} \int_{0}^{q-\alpha} e^{-\frac{\mu x^{2}}{2pq}} x^{3}\,dx, \]

et, *a fortiori*,

\[ \mathrm{B}_{1} > \int_{0}^{q-\alpha} e^{-\frac{\mu x^{2}}{2pq}}\,dx - \frac{\mu}{5q\alpha} \int_{0}^{\infty} e^{-\frac{\mu x^{2}}{2pq}} x^{3}\,dx. \]

Posons, dans la première intégrale du second membre

\[ \frac{\mu x^{2}}{2pq} = t^{2}, \qquad \mathrm{T}_{1} = (q - \alpha)\sqrt{\frac{\mu}{2pq}}; \]

il viendra

\[ \int_{0}^{q-\alpha} e^{-\frac{\mu x^{2}}{2pq}}\,dx = \sqrt{\frac{2pq}{\mu}} \int_{0}^{\mathrm{T}_{1}} e^{-t^{2}}\,dt. \]

La substitution

\[ \frac{\mu x^{2}}{2pq} = s \text{ ou } x^{2} = \frac{2pq}{\mu}\,s, \qquad x^{3}\,dx = \frac{2p^{2}q^{2}}{\mu^{2}}\,s\,ds \]

[p. 100] donne ensuite

\[ \int^{\infty} e^{-\frac{\mu x^{2}}{2pq}} x^{3}\,dx = \frac{2p^{2}q^{2}}{\mu^{2}} \int_{0}^{\infty} e^{-s}\,s\,ds = \frac{2p^{2}q^{2}}{\mu^{2}}\,\Gamma(2) = \frac{2p^{2}q^{2}}{\mu^{2}}. \]

On a donc

\[ \mathrm{B}_{1} > \sqrt{\frac{2pq}{\mu}} \int_{0}^{\mathrm{T}_{1}} e^{-t^{2}}\,dt - \frac{2p^{2}q}{3\alpha\mu}. \]

Comme on dispose de \(\alpha\), on peut choisir, dans chaque cas, cette fraction de manière que la limite inférieure de \(\mathrm{B}_{1}\) soit la plus grande possible. Pour simplifier, nous ferons

\[ 3\alpha = 2p^{2}q \text{ ou } \alpha = \frac{2}{3}p^{3}q. \]

Dans cette hypothèse, on aura

\[ \mathrm{B}_{1} > \sqrt{\frac{2pq}{\mu}} \int_{0}^{\mathrm{T}_{1}} e^{-t^{2}}\,dt - \frac{1}{\mu}, \]

\[ \mathrm{T}_{1} = q\left(1 - \frac{2}{3}p^{2}\right)\sqrt{\frac{\mu}{2pq}}. \]

On aura donc enfin

\[ \mathrm{B} > p^{m}q^{n} \left\{ \sqrt{\frac{2pq}{\mu}} \int_{0}^{\mathrm{T}_{1}} e^{-t^{2}}\,dt - \frac{1}{\mu} \right\} \]

[p. 101] et, en observant, d'après le n° 2, que

\[ \int_{0}^{\mathrm{T}_{1}} e^{-t^{2}}\,dt > \frac{\sqrt{\pi}}{2}\left(1 - e^{-\mathrm{T}_{1}^{2}}\right), \]

\[ \mathrm{B} > p^{m}q^{n} \left\{ \frac{\sqrt{2\pi\mu pq}}{\mu}\left(\frac{1}{2} - \frac{1}{2}e^{-\mathrm{T}_{1}^{2}}\right) - \frac{1}{\mu} \right\}. \]

**3°** *Limite supérieure de* B, *limites de* A. On a, comme on l'a vu,

\[ \mathrm{B} < \frac{1}{2}\mathrm{E} < \frac{1}{2} \cdot (\text{limite supérieure de E}), \]

\[ \mathrm{A} > \frac{1}{2}\mathrm{E} > \frac{1}{2} \cdot (\text{limite inférieure de E}), \]

\[ \mathrm{A} = \mathrm{E} - \mathrm{B} < \text{lim. sup. de E} - \text{lim. inf. de B}. \]

**5.** *Limites de* \((\mathrm{B} : \mathrm{E})\), \((\mathrm{A} : \mathrm{E})\). On a d'abord, sauf si \(p = q\),

\[ \mathrm{B} : \mathrm{E} < \frac{1}{2}, \qquad \mathrm{A} : \mathrm{E} > \frac{1}{2}. \]

Ensuite

\[ \frac{\mathrm{B}}{\mathrm{E}} > \frac{\text{limite inférieure de B}}{\text{limite supérieure de E}}, \]

c'est-à-dire

\[ \frac{\mathrm{B}}{\mathrm{E}} > \frac{p^{m}q^{n} \left\{ \frac{\sqrt{2\pi\mu pq}}{\mu}\left(\frac{1}{2} - \frac{1}{2}e^{-\mathrm{T}_{1}^{2}}\right) - \frac{1}{\mu} \right\}}{\sqrt{2\pi\mu pq}\, p^{m}q^{n}\, \frac{1}{\mu - \frac{1}{12pq}}} \]

\[ = \left(\frac{1}{2} - \frac{1}{2}e^{-\mathrm{T}_{1}^{2}}\right)\left(1 - \frac{1}{12\mu pq}\right) \]

\[ -\left(1 - \frac{1}{12\mu pq}\right)\frac{1}{\sqrt{2\pi\mu pq}}. \]

[p. 102] On déduit de là sans peine

\[ \frac{\mathrm{B}}{\mathrm{E}} > \frac{1}{2} - \frac{1}{2}e^{-\mathrm{T}_{1}^{2}} - \frac{1}{24\mu pq} - \frac{1}{\sqrt{2\pi\mu pq}}. \]

Enfin

\[ \frac{\mathrm{A}}{\mathrm{E}} = 1 - \frac{\mathrm{B}}{\mathrm{E}} < \frac{1}{2} + \frac{1}{2}e^{-\mathrm{T}_{1}^{2}} + \frac{1}{24\mu pq} + \frac{1}{\sqrt{2\pi\mu pq}}. \]

**6.** *Limites de* Q *et* \((\mathrm{Q} : \mathrm{E})\). 1° *Limites de* Q. Posons dans Q, comme dans B,

\[ z = p + x, \qquad 1 - z = q - x, \]

de manière que \(x\) varie seulement de 0 à \(l\), \(l\) étant au plus égal à \(\frac{1}{2}q\). On aura

\[ \mathrm{Q} = p^{m}q^{n} \int_{0}^{l} \left(1 + \frac{x}{p}\right)^{m} \left(1 - \frac{x}{q}\right)^{n} dx = p^{m}q^{n} \int_{0}^{l} e^{u}\,dx. \]

La quantité

\[ u' = -\frac{\mu x}{pq} - \mu x^{2}\left[\frac{1}{q(q - x)} - \frac{1}{p(p + x)}\right], \]

où

\[ q - x \mathrel{\overset{=}{>}} \frac{1}{2}q, \]

est évidemment telle que

\[ -\frac{\mu x}{pq} > u' > -\frac{\mu x}{pq} - \frac{2\mu x^{2}}{q^{2}}. \]

[p. 103] Par suite,

\[ -\frac{\mu x^{2}}{2pq} > u > -\frac{\mu x^{2}}{2pq} - \frac{2\mu x^{3}}{3q^{2}} \]

\[ e^{-\frac{\mu x^{2}}{2pq}} > e^{u} > e^{-\frac{\mu x^{2}}{2pq}} e^{-\frac{2\mu x^{3}}{3q^{2}}} > e^{-\frac{\mu x^{2}}{2pq}} \left(1 - \frac{2\mu x^{3}}{3q^{2}}\right) \]

Il en résulte d'abord l'inégalité

\[ \mathrm{Q} = p^{m} q^{n} \int_{0}^{l} e^{u}\,du < p^{m} q^{n} \int_{0} e^{-\frac{\mu x^{2}}{2pq}}\,dx \]

\[ = p^{m} q^{n} \sqrt{\frac{2pq}{\mu}} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt, \]

ou

\[ \mathrm{Q} < \frac{1}{2\mu} p^{m} q^{n} \sqrt{2\pi\mu pq}\,\mathrm{J} \]

On a ensuite

\[ \int_{0}^{l} e^{u}\,du > \int_{0}^{l} e^{-\frac{\mu x^{2}}{2pq}}\,dx - \int_{0}^{l} e^{-\frac{\mu x^{2}}{2pq}} \frac{2\mu}{3q^{2}} x^{3}\,dx \]

\[ > \int_{0}^{l} e^{-\frac{\mu x^{2}}{2pq}}\,dx - \frac{2\mu}{3q^{2}} \int_{0}^{\infty} e^{-\frac{\mu x^{2}}{2pq}} x^{3}\,dx, \]

ou encore,

\[ \int_{0}^{l} e^{u}\,du > \sqrt{\frac{2pq}{\mu}} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt - \frac{2\mu}{3q^{2}} \cdot \frac{2p^{2}q^{2}}{\mu^{2}} \]

\[ = \frac{1}{2\mu} \sqrt{2\pi\mu pq}\,\mathrm{J} - \frac{4p^{2}}{3\mu}. \]

[p. 104] Donc enfin

\[ \mathrm{Q} > p^{m} q^{n} \left[\frac{1}{2\mu} \sqrt{2\pi\mu pq}\,\mathrm{J} - \frac{4p^{2}}{3\mu}\right]. \]

2° *Limite supérieure de* \((\mathrm{Q} : \mathrm{E})\). On a

\[ \frac{\mathrm{Q}}{\mathrm{E}} < \frac{\text{limite supérieure de Q}}{\text{limite inférieure de E}}, \]

ou

\[ \frac{\mathrm{Q}}{\mathrm{E}} < \frac{\frac{1}{2\mu} p^{m} q^{n} \sqrt{2\pi\mu pq}\,\mathrm{J}}{\frac{1}{\mu + 2} p^{m} q^{n} \sqrt{2\pi\mu pq}} = \frac{1}{2}\mathrm{J} \left(1 + \frac{2}{\mu}\right). \]

Mais on sait que \(\frac{1}{2}\mathrm{J} < \frac{1}{2}\). Par suite,

\[ \frac{\mathrm{Q}}{\mathrm{E}} < \frac{1}{2}\mathrm{J} + \frac{1}{\mu}. \]

3° *Limite inférieure de* \((\mathrm{Q} : \mathrm{E})\). On a

\[ \frac{\mathrm{Q}}{\mathrm{E}} > \frac{\text{limite inférieure de Q}}{\text{limite supérieure de E}} = \frac{p^{m} q^{n} \left[\frac{1}{2\mu} \sqrt{2\pi\mu pq}\,\mathrm{J} - \frac{4p^{2}}{3\mu}\right]}{\frac{1}{\mu - \frac{1}{12pq}} \sqrt{2\pi\mu pq}\, p^{m} q^{m}} \]

\[ = \frac{1}{2}\mathrm{J} \left(1 - \frac{1}{12\mu pq}\right) - \frac{4}{3} \frac{p^{2}}{\sqrt{2\pi\mu pq}} \left(1 - \frac{1}{12\mu pq}\right) \]

et, *a fortiori*,

\[ \frac{\mathrm{Q}}{\mathrm{E}} > \frac{1}{2}\mathrm{J} - \frac{1}{24\mu pq} - \frac{4}{3} \frac{p^{2}}{\sqrt{2\pi\mu pq}}. \]

[p. 105] **7.** *Limites de* P *et de* \((\mathrm{P} : \mathrm{E})\). On prouve d'abord que P surpasse Q comme on a prouvé que A surpasse B, sauf, bien entendu, si \(m = n\), \(p = q\), ce qui entraîne \(\mathrm{P} = \mathrm{Q}\). On a donc

\[ \frac{\mathrm{P}}{\mathrm{E}} > \frac{\mathrm{Q}}{\mathrm{E}} > \frac{1}{2}\mathrm{J} - \frac{1}{24\mu pq} - \frac{4}{3} \frac{p^{2}}{\sqrt{2\pi\mu pq}}. \]

Ensuite, évidemment, \(\mathrm{P} + \mathrm{Q} < \mathrm{E}\), et, par suite,

\[ \frac{\mathrm{P}}{\mathrm{E}} < 1 - \frac{\mathrm{Q}}{\mathrm{E}} < 1 - \text{limite inférieure de } \frac{\mathrm{Q}}{\mathrm{E}}. \]

Donc

\[ \frac{\mathrm{P}}{\mathrm{E}} < 1 - \frac{1}{2}\mathrm{J} + \frac{1}{24\mu pq} + \frac{4}{3} \frac{p^{2}}{\sqrt{2\pi\mu pq}}. \]

Mais, d'après une inégalité du n° 2, on a

\[ 1 - \tfrac{1}{2}\mathrm{J} = 1 - \mathrm{J} + \tfrac{1}{2}\mathrm{J} < \tfrac{1}{2}\mathrm{J} + e^{-\mathrm{T}^{2}}. \]

Par conséquent,

\[ \frac{\mathrm{P}}{\mathrm{E}} < \frac{1}{2}\mathrm{J} + e^{-\mathrm{T}^{2}} + \frac{1}{24\mu pq} + \frac{4}{3} \frac{p^{2}}{\sqrt{2\pi\mu pq}}. \]

**8.** *Limites de* \([(\mathrm{P} + \mathrm{Q}) : \mathrm{E}]\). En rapprochant les résultats obtenus dans les deux derniers numéros, on trouve

\[ \frac{\mathrm{P} + \mathrm{Q}}{\mathrm{E}} < \mathrm{J} + \frac{1}{\mu} + e^{-\mathrm{T}^{2}} + \frac{1}{24\mu pq} + \frac{4}{3} \frac{p^{2}}{\sqrt{2\pi\mu pq}}, \]

\[ \frac{\mathrm{P} + \mathrm{Q}}{\mathrm{E}} > \mathrm{J} - \frac{1}{12\mu pq} - \frac{8}{3} \frac{p^{2}}{\sqrt{2\pi\mu pq}}. \]

[p. 106] Nous avons trouvé antérieurement, par une autre méthode[^106-a],

\[ 1 > \frac{\mathrm{P} + \mathrm{Q}}{\mathrm{E}} > \mathrm{J} - \frac{7}{\mu pq}. \]

**9.** *Limites de l'intégrale de Poisson*. Posons, pour simplifier les écritures,

\[ \varepsilon = \frac{1}{2} e^{-\mathrm{T}_{1}^{2}} + \frac{1}{24\mu pq} + \frac{1}{\sqrt{2\pi\mu pq}}, \qquad \eta = \frac{1}{24\mu pq} + \frac{4}{3} \frac{p^{2}}{\sqrt{2\pi\mu pq}}. \]

On aura

\[ \frac{1}{2} < \frac{\mathrm{A}}{\mathrm{E}} < \frac{1}{2} + \varepsilon, \qquad \frac{1}{2} - \varepsilon < \frac{\mathrm{B}}{\mathrm{E}} < \frac{1}{2}, \]

\[ \frac{1}{2}\mathrm{J} - \eta < \frac{\mathrm{P}}{\mathrm{E}} < \frac{1}{2}\mathrm{J} + \eta + e^{-\mathrm{T}^{2}}, \qquad \frac{1}{2}\mathrm{J} - \eta < \frac{\mathrm{Q}}{\mathrm{E}} < \frac{1}{2}\mathrm{J} + \frac{1}{\mu}. \]

On déduit de là

\[ \frac{1}{2} + \frac{1}{2}\mathrm{J} - \eta < \frac{\mathrm{A} + \mathrm{Q}}{\mathrm{E}} < \frac{1}{2} + \frac{1}{2}\mathrm{J} + \varepsilon + \frac{1}{\mu}, \tag{1} \]

\[ \frac{1}{2} - \frac{1}{2}\mathrm{J} - \eta - e^{-\mathrm{T}^{2}} < \frac{\mathrm{A} - \mathrm{P}}{\mathrm{E}} < \frac{1}{2} - \frac{1}{2}\mathrm{J} + \varepsilon + \eta, \tag{2} \]

\[ \frac{1}{2} + \frac{1}{2}\mathrm{J} - \varepsilon - \eta < \frac{\mathrm{B} + \mathrm{P}}{\mathrm{E}} < \frac{1}{2} + \frac{1}{2}\mathrm{J} + \eta + e^{-\mathrm{T}^{2}}, \tag{3} \]

\[ \frac{1}{2} - \frac{1}{2}\mathrm{J} - \varepsilon - \frac{1}{\mu} < \frac{\mathrm{B} - \mathrm{Q}}{\mathrm{E}} < \frac{1}{2} - \frac{1}{2}\mathrm{J} + \eta. \tag{4} \]

[p. 107] Observons que

\[ \mathrm{A} + \mathrm{Q} = \int_{0}^{p+l} z^{m} (1 - z)^{n}\,dz, \]

\[ \mathrm{A} - \mathrm{P} = \int_{0}^{p-l} z^{m} (1 - z)^{n}\,dz, \]

\[ \mathrm{B} + \mathrm{P} = \int_{p-l}^{1} z^{m} (1 - z)^{n}\,dz, \]

\[ \mathrm{B} - \mathrm{Q} = \int_{p+l}^{1} z^{m} (1 - z)^{n}\,dz. \]

Les relations (1), (2), (3), (4) donnent sous une forme précise, dans tous les cas, la limite supérieure et la limite inférieure du rapport d'une intégrale eulérienne de première espèce *incomplète* à l'intégrale *complète* correspondante. Poisson, à l'endroit cité, donne simplement la formule approximative, sans aucune indication de limites,

\[ \int_{0}^{\theta} z^{m} (1 - z)^{n}\,dz = (\tfrac{1}{2} \pm \tfrac{1}{2}\mathrm{J})\mathrm{E}, \]

le signe \(+\) correspondant au cas où \(\theta(m + n)\) surpasse \(m\), le signe \(-\) à celui où \(\theta(m + n)\) est inférieur à \(m\).

**10.** *Démonstration des inégalités du n°* 2. Considérons les volumes \(\mathrm{V}_{1}\), \(\mathrm{V}_{2}\), \(\mathrm{V}_{3}\), situés entre trois plans rectangulaires OXY, OYZ, OZX, sous la surface ayant pour équation \(\pi z = 4e^{-x^{2}-y^{2}}\), et projetés, \(\mathrm{V}_{1}\) suivant le carré OXPY de côté \(\mathrm{OX} = \mathrm{OY} = \mathrm{T}\), \(\mathrm{V}_{2}\) suivant le quart de cercle OXY de centre O et de rayon [p. 108] \(\mathrm{OX} = \mathrm{OY} = \mathrm{T}\), \(\mathrm{V}_{3}\) suivant le quart de cercle \(\mathrm{O}xy\) de rayon \(\mathrm{O}x = \mathrm{O}y = (2\mathrm{T} : \sqrt{\pi})\), et équivalent au carré OXPY.

Le volume \(\mathrm{V}_{1}\) est évidemment supérieur à \(\mathrm{V}_{2}\) qui en est une partie. Les volumes \(\mathrm{V}_{1}\) et \(\mathrm{V}_{3}\) ont une partie commune ; les parties non communes ont des bases équivalentes, mais dans ces parties non communes, les \(z\) de \(\mathrm{V}_{3}\) sont plus grands que ceux de \(\mathrm{V}_{1}\), parce que \(z\) est d'autant plus grand que \(x^{2} + y^{2}\) est plus petit. On a donc \(\mathrm{V}_{1} < \mathrm{V}_{3}\).

On trouve aisément, d'après les formules générales de cubature,

\[ \mathrm{V}_{1} = \mathrm{J}^{2}, \qquad \mathrm{V}_{2} = 1 - e^{-\mathrm{T}^{2}}, \qquad \mathrm{V}_{3} = 1 - e^{-\frac{4\mathrm{T}^{2}}{\pi}} < 1 - e^{-\frac{4}{3}\mathrm{T}^{2}} \]

et, par suite,

\[ 1 - e^{-\mathrm{T}^{2}} < \mathrm{J}^{2} < 1 - e^{-\frac{4}{3}\mathrm{T}^{2}}. \]

comme nous l'avons dit au n° 2[^108-a].

[p. 109]

[^93-a]: Poisson, *Probabilité des jugements*, § 88, pp. 224-228 ; traduction allemande de Schnuse, pp. 189-193.

[^94-a]: *Annales de la Société scientifique de Bruxelles*, 1888, t. XII, 1<sup>re</sup> partie, pp. 63-65. Pour la facilité du lecteur, nous reproduisons la partie essentielle de la démonstration au n° 10.

[^106-a]: *Annales de la Société scientifique de Bruxelles*, 1902, t. XXVI, 2<sup>e</sup> partie, pp. 211-214.

[^108-a]: Extrait des *Bull. de l'Acad. roy. de Belgique* (Classe des sciences), n° 3, pp. 239-254, 1904.

## Sur une sommation d'intégrales considérées en calcul des probabilités

**1.** *Objet de la présente note*. Soient \(m\), \(n\), \(\mu\), \(m'\), \(n'\), \(\mu'\), M des nombres entiers tels que

\[ m + n = \mu, \qquad m' + n' = \mu', \qquad \mu + \mu' = \mathrm{M}; \]

\(p\) et \(q\) des fractions définies par les égalités \(\mu p = m\), \(\mu q = n\). Soient ensuite

\[ m' = \mu' p + x, \qquad n' = \mu' q - x, \]

\(x\) variant par unités de 0 à \(\pm \mu' l\), \(l\) étant une fraction tout au plus égale à la plus petite des quantités \(\frac{1}{2} p\), \(\frac{1}{2} q\), \(\frac{1}{2} q\), par exemple.

Posons ensuite

\[ \mathrm{C}_{\mu'}^{m'} = \frac{1.2\ldots\mu'}{1.2\ldots m'.1.2\ldots n'}, \]

\[ \mathrm{B} = \int_{0}^{1} z^{m} (1 - z)^{n}\,dz = \frac{1.2\ldots m.1.2\ldots n}{1.2\ldots\mu.\mu + 1}, \]

\[ \mathrm{B}' = \int_{0}^{1} z^{m+m'} (1 - z)^{n+n'} = \frac{1.2\ldots m + m'.1.2\ldots n + n'}{1.2\ldots\mathrm{M}.\mathrm{M} + 1}, \]

\[ \mathrm{T}_{\mu' p + x} = \mathrm{T}_{m'} = \mathrm{C}_{\mu'}^{m'} \mathrm{B}' : \mathrm{B}. \]

La somme

\[ \mathrm{P} = \mathop{\mathrm{S}}\limits_{x=-\mu l}^{x=\mu l} \mathrm{T}_{\mu' p + x} \]

[p. 110] exprime la probabilité *a posteriori* qu'un événement, dont la probabilité *a priori* peut varier de zéro à l'unité et qui est arrivé \(m\) fois en \(\mu\) épreuves, se présentera à l'avenir \(m'\) fois sur \(\mu'\) épreuves, la différence entre \((m : \mu)\) et \((m' : \mu')\) étant tout au plus égale à \(l\).

Nous nous proposons de calculer une limite supérieure et une limite inférieure de \(\mathrm{B}' : \mathrm{B}\) et de \(\mathrm{T}_{m'}\), une limite inférieure de P. On sait d'ailleurs que la somme P est inférieure à l'unité.

Laplace, dans la *Théorie analytique des probabilités* (n° 30, 3<sup>e</sup> édition, 1820, pp. 385-387), calcule une valeur approchée du \(\mathrm{T}_{m'}\) ; Poisson, dans la *Probabilité des jugements* (n° 87, p. 223, ou p. 188 de la traduction allemande), une valeur approchée de P. Mais, suivant l'usage de leur temps, ni l'un ni l'autre ne s'inquiètent d'enfermer ces expressions entre deux limites, l'une supérieure, l'autre inférieure ; autrement dit, ils n'évaluent pas l'erreur commise dans l'évaluation de \(\mathrm{T}_{m'}\) et de P. L'évaluation précise de cette erreur est l'objet propre de la présente note.

**2.** *Limites de* \((\mathrm{B}' : \mathrm{B})\). On a, comme l'on sait, d'après la formule de Stirling,

\[ \sqrt{2\pi}\, r^{r+\frac{1}{2}} e^{-r} < 1.2\ldots r < \sqrt{2\pi}\, r^{r+\frac{1}{2}} e^{-r+\frac{1}{12r}}. \]

On déduit de là

\[ \mathrm{B} > \frac{\sqrt{2\pi}}{\mu + 1} \frac{m^{m+\frac{1}{2}} n^{n+\frac{1}{2}}}{\mu^{\mu+\frac{1}{2}}} e^{-\frac{1}{12\mu}}, \]

\[ \mathrm{B} < \frac{\sqrt{2\pi}}{\mu + 1} \frac{m^{m+\frac{1}{2}} n^{n+\frac{1}{2}}}{\mu^{\mu+\frac{1}{2}}} e^{\frac{1}{12m} + \frac{1}{12n}}. \]

[p. 111] De même,

\[ \mathrm{B}' > \frac{\sqrt{2\pi}}{\mathrm{M} + 1} \frac{(m + m')^{m+m'+\frac{1}{2}} (n + n')^{n+n'+\frac{1}{2}}}{\mathrm{M}^{\mathrm{M}+\frac{1}{2}}} e^{-\frac{1}{12\mathrm{M}}}, \]

\[ \mathrm{B}' < \frac{\sqrt{2\pi}}{\mathrm{M} + 1} \frac{(m + m')^{m+m'+\frac{1}{2}} (n + n')^{n+n'+\frac{1}{2}}}{\mathrm{M}^{\mathrm{M}+\frac{1}{2}}} e^{\frac{1}{12(m+m')} + \frac{1}{12(n+n')}}. \]

Par suite,

\[ \frac{\mathrm{B}'}{\mathrm{B}} > \frac{\mu + 1}{\mathrm{M} + 1} \frac{(m + m')^{m+m'+\frac{1}{2}} (n + n')^{n+n'+\frac{1}{2}} \mu^{\mu+\frac{1}{2}}}{\mathrm{M}^{\mathrm{M}+\frac{1}{2}} m^{m+\frac{1}{2}} n^{n+\frac{1}{2}}} \cdot a, \]

\[ a = e^{-\frac{1}{12\mathrm{M}} - \frac{1}{12m} - \frac{1}{12n}}; \]

\[ \frac{\mathrm{B}'}{\mathrm{B}} < \frac{\mu + 1}{\mathrm{M} + 1} \frac{(m + m')^{m+m'+\frac{1}{2}} (n + n')^{n+n'+\frac{1}{2}} \mu^{\mu+\frac{1}{2}}}{\mathrm{M}^{\mathrm{M}+\frac{1}{2}} m^{m+\frac{1}{2}} n^{n+\frac{1}{2}}} \cdot b, \]

\[ b = e^{\frac{1}{12(m+m')} + \frac{1}{12(n+n')} + \frac{1}{12\mu}}. \]

On démontre aisément les inégalités suivantes :

\[ \frac{\mu + 1}{\mathrm{M} + 1} > \frac{\mu}{\mathrm{M}}, \qquad \frac{\mu + 1}{\mathrm{M} + 1} < \frac{\mu^{\frac{1}{2}}}{\mathrm{M}^{\frac{1}{2}}}, \]

\[ \frac{1}{\mathrm{M}} = \frac{1}{\mu + \mu'} < \frac{1}{\mu} = \frac{1}{m + n} < \frac{1}{2m} + \frac{1}{2n}, \]

\[ \frac{1}{m + m'} + \frac{1}{n + n'} < \frac{1}{m} + \frac{1}{n}. \]

[p. 112] Il en résulte

\[ \frac{1}{12(m + m')} + \frac{1}{12(n + n')} + \frac{1}{12\mu} \]

\[ < \frac{1}{12m} + \frac{1}{12n} + \frac{1}{24m} + \frac{1}{24n} = \frac{1}{8m} + \frac{1}{8n}. \]

\[ \frac{1}{12\mathrm{M}} + \frac{1}{12m} + \frac{1}{12n} < \frac{1}{24m} + \frac{1}{24n} + \frac{1}{12m} + \frac{1}{12n} = \frac{1}{8m} + \frac{1}{8n}, \]

\[ -\frac{1}{12\mathrm{M}} - \frac{1}{12m} - \frac{1}{12n} > -\frac{1}{8m} - \frac{1}{8n}. \]

On a donc

\[ a > e^{-\frac{1}{8m} - \frac{1}{8n}}, \qquad b < e^{\frac{1}{8m} + \frac{1}{8n}}, \]

Par suite,

\[ \frac{\mathrm{B}'}{\mathrm{B}} > \sqrt{\frac{\mu}{\mathrm{M}}} \frac{(m + m')^{m+m'+\frac{1}{2}} (n + n')^{n+n'+\frac{1}{2}} \mu^{\mu+1}}{\mathrm{M}^{\mathrm{M}+1} m^{m+\frac{1}{2}} n^{n+\frac{1}{2}}} e^{-\frac{1}{8m} - \frac{1}{8n}}, \]

\[ \frac{\mathrm{B}'}{\mathrm{B}} < \frac{(m + m')^{m+m'+\frac{1}{2}} (n + n')^{n+n'+\frac{1}{2}} \mu^{\mu+1}}{\mathrm{M}^{\mathrm{M}+1} m^{m+\frac{1}{2}} n^{n+\frac{1}{2}}} e^{\frac{1}{8m} + \frac{1}{8n}}. \]

En observant que

\[ (m + m')^{m+m'+\frac{1}{2}} = m^{m+m'+\frac{1}{2}} \left(1 + \frac{m'}{m}\right)^{m+m'+\frac{1}{2}}, \]

\[ (n + n')^{n+n'+\frac{1}{2}} = n^{n+n'+\frac{1}{2}} \left(1 + \frac{n'}{n}\right)^{n+n'+\frac{1}{2}}, \]

\[ \mathrm{M}^{\mathrm{M}+1} = (\mu + \mu')^{\mathrm{M}+1} = \mu^{\mathrm{M}+1} \left(1 + \frac{\mu'}{\mu}\right)^{\mathrm{M}+1}, \]

[p. 113] puis que \(p = \frac{m}{\mu}\), \(q = \frac{n}{\mu}\), on trouve

\[ \frac{\mathrm{B}'}{\mathrm{B}} > \sqrt{\frac{m}{\mathrm{M}}} p^{m'} q^{n'} \frac{\left(1 + \frac{m'}{m}\right)^{m+m'+\frac{1}{2}} \left(1 + \frac{n'}{n}\right)^{n+n'+\frac{1}{2}}}{\left(1 + \frac{\mu'}{\mu}\right)^{\mu+\mu'+1}} e^{-\frac{1}{8m} - \frac{1}{8n}}, \]

\[ \frac{\mathrm{B}'}{\mathrm{B}} < p^{m'} q^{n'} \frac{\left(1 + \frac{m'}{m}\right)^{m+m'+\frac{1}{2}} \left(1 + \frac{n'}{n}\right)^{n+n'+\frac{1}{2}}}{\left(1 + \frac{\mu'}{\mu}\right)^{\mu+\mu'+1}} e^{\frac{1}{8m} + \frac{1}{8n}}. \]

Ces valeurs sont évidemment très voisines de \(p^{m'}q^{n'}\) si \(m\), \(n\) sont de grands nombres comparativement à \(m'\), \(n'\).

**3.** *Limites de* \(\mathrm{T}_{\mu'p+x}\). Au moyen de la formule de Stirling, on établit sans peine les inégalités

\[ \mathrm{C}_{\mu'}^{m'} > \frac{1}{\sqrt{2\pi\mu'}} \frac{\mu'^{\mu'+1}}{m'^{m'+\frac{1}{2}} n'^{n'+\frac{1}{2}}} e^{-\frac{1}{12m'} - \frac{1}{12n'}} \]

\[ \mathrm{C}_{\mu'}^{m'} < \frac{1}{\sqrt{2\pi\mu'}} \frac{\mu'^{\mu'+1}}{m'^{m'+\frac{1}{2}} n'^{n'+\frac{1}{2}}} e^{\frac{1}{12\mu'}}. \]

Posons

\[ \mathrm{C} = \frac{\mu'^{\mu'+1}}{m'^{m'+\frac{1}{2}} n'^{n'+\frac{1}{2}}} \frac{(m + m')^{m+m'+\frac{1}{2}} (n + n')^{n+n'+\frac{1}{2}}}{\mathrm{M}^{\mathrm{M}+1}} \frac{\mu^{\mu+1}}{m^{m+\frac{1}{2}} n^{n+\frac{1}{2}}}. \]

Puisque

\[ \mathrm{T}_{\mu'p+x} = \mathrm{C}_{\mu'}^{m'} \frac{\mathrm{B}'}{\mathrm{B}}, \]

[p. 114] on aura évidemment

\[ \mathrm{T}_{\mu'p+x} > \frac{1}{\sqrt{2\pi\mu'}} \sqrt{\frac{\mu}{\mathrm{M}}} \mathrm{C} e^{-\frac{1}{8m} - \frac{1}{8n} - \frac{1}{12m'} - \frac{1}{12n'}}, \]

\[ \mathrm{T}_{\mu'p+x} < \frac{1}{\sqrt{2\pi\mu'}} \mathrm{C} e^{\frac{1}{8m} + \frac{1}{8n} + \frac{1}{12\mu'}}. \]

On a

\[ \frac{1}{8m} + \frac{1}{8n} = \frac{1}{8\mu p} + \frac{1}{8\mu q} = \frac{1}{8\mu pq}, \]

\[ \frac{1}{12m'} + \frac{1}{12n'} = \frac{\mu'}{12m'n'} = \frac{\mu'}{12(\mu'p + x)(\mu'q - x)}. \]

Puisque \(x\) est tout au plus égal à \(\mu'l\), et \(l\) au plus égal à \(\frac{1}{2} q\) supposé inférieur ou égal à \(\frac{1}{2} p\), on a

\[ m'n' \mathrel{\overset{=}{>}} (\mu'p + \mu'l)(\mu'q - \mu'l) \mathrel{\overset{=}{>}} \mu'^{2}(p + \tfrac{1}{2} q)(q - \tfrac{1}{2} q) \]

\[ = \tfrac{1}{4} \mu'^{2}(1 + p) q > \tfrac{1}{2} \mu'^{2} pq. \]

Donc

\[ \frac{\mu'}{12m'n'} < \frac{\mu'}{6\mu'^{2}pq} = \frac{1}{6\mu'pq}, \qquad -\frac{\mu'}{12m'n'} > -\frac{1}{6\mu'pq}. \]

Par conséquent,

\[ \mathrm{T}_{\mu'p+x} > \frac{1}{\sqrt{2\pi\mu'}} \sqrt{\frac{\mu}{\mathrm{M}}} \mathrm{C} e^{-\frac{1}{8\mu pq} - \frac{1}{6\mu'pq}}. \]

Mais on sait que \(e^{-\alpha}\) surpasse \(1 - \alpha\), si \(\alpha\) est positif. Donc

\[ e^{-\frac{1}{8\mu pq} - \frac{1}{6\mu'pq}} > 1 - \frac{1}{8\mu pq} - \frac{1}{6\mu'pq}. \]

[p. 115] De même, si \(\alpha\) est égal ou inférieur à ½, on a

\[ e^{\alpha} = \frac{1}{e^{-\alpha}} < \frac{1}{1 - \alpha} \mathrel{\overset{=}{<}} 1 + 2\alpha. \]

Par suite,

\[ e^{\frac{1}{8m} + \frac{1}{8n} + \frac{1}{12\mu'}} = e^{\frac{1}{8\mu pq} + \frac{1}{12\mu'}} < 1 + \frac{1}{4\mu pq} + \frac{1}{6\mu'}. \]

On a donc enfin

\[ \mathrm{T}_{\mu'p+x} > \frac{1}{\sqrt{2\pi\mu'}} \sqrt{\frac{\mu}{\mathrm{M}}} \mathrm{C} \left(1 - \frac{1}{8\mu pq} - \frac{1}{6\mu'pq}\right), \]

\[ \mathrm{T}_{\mu'p+x} > \frac{1}{\sqrt{2\pi\mu'}} \mathrm{C} \left(1 + \frac{1}{4\mu pq} + \frac{1}{6\mu'}\right) \]

Ce sont les deux limites cherchées de \(\mathrm{T}_{\mu'p+x}\).

On peut mettre

\[ \frac{1}{\sqrt{2\pi\mu'}} \mathrm{C} \]

sous une autre forme, en se servant des relations

\[ m = \mu p. \qquad n = \mu q, \qquad m' = \mu'p + x, \qquad n' = \mu'q - x. \]

On trouve ainsi

\[ \frac{\mu'^{\mu'+1}}{m'^{m'+\frac{1}{2}} n'^{n'+\frac{1}{2}}} = \frac{1}{p^{\mu'p+x+\frac{1}{2}} q^{\mu'q-x+\frac{1}{2}} \left(1 + \frac{x}{\mu'p}\right)^{\mu'p+x+\frac{1}{2}} \left(1 - \frac{x}{\mu'q}\right)^{\mu'q-x+\frac{1}{2}}} \]

\[ \frac{(m + m')^{m+m'+\frac{1}{2}} (n + n')^{n+n'+\frac{1}{2}}}{\mathrm{M}^{\mathrm{M}+1}} \]

\[ = p^{\mathrm{M}p+x+\frac{1}{2}} q^{\mathrm{M}q-x+\frac{1}{2}} \left(1 + \frac{x}{\mathrm{M}p}\right)^{\mathrm{M}p+x+\frac{1}{2}} \left(1 - \frac{x}{\mathrm{M}q}\right)^{\mathrm{M}q-x+\frac{1}{2}}; \]

[p. 116]

\[ \frac{\mu^{\mu+1}}{m^{m+\frac{1}{2}} n^{n+\frac{1}{2}}} = \frac{1}{p^{\mu p+\frac{1}{2}} q^{\mu q+\frac{1}{2}}}, \]

puis

\[ \frac{1}{\sqrt{2\pi\mu}} \mathrm{C} = \frac{1}{\sqrt{2\pi\mu'pq}} \frac{\left(1 + \frac{x}{\mathrm{M}p}\right)^{\mathrm{M}p+x+\frac{1}{2}} \left(1 - \frac{x}{\mathrm{M}q}\right)^{\mathrm{M}q-x+\frac{1}{2}}}{\left(1 + \frac{x}{\mu'p}\right)^{\mu'p+x+\frac{1}{2}} \left(1 - \frac{x}{\mu'q}\right)^{\mu'q-x+\frac{1}{2}}}. \]

Pour abréger, nous écrirons

\[ t_{\mu'p+x} = \frac{\left(1 + \frac{x}{\mathrm{M}p}\right)^{\mathrm{M}p+x+\frac{1}{2}} \left(1 - \frac{x}{\mathrm{M}q}\right)^{\mathrm{M}q-x+\frac{1}{2}}}{\left(1 + \frac{x}{\mu'p}\right)^{\mu'p+x+\frac{1}{2}} \left(1 - \frac{x}{\mu'q}\right)^{\mu'-qx+\frac{1}{2}}}. \]

Alors on aura

\[ \mathrm{T}_{\mu'p+x} > \frac{1}{\sqrt{2\pi\mu'pq}} \sqrt{\frac{\mu}{\mathrm{M}}} \left(1 - \frac{1}{8\mu pq} - \frac{1}{6\mu'pq}\right) t_{\mu'p+x}, \]

\[ \mathrm{T}_{\mu'p+x} < \frac{1}{\sqrt{2\pi\mu'pq}} \left(1 + \frac{1}{4\mu pq} + \frac{1}{6\mu'}\right) t_{\mu'p+x}. \]

La première inégalité seule nous servira dans la suite. Pour simplifier les écritures, nous écrirons

\[ c = 1 - \frac{1}{8\mu pq} - \frac{1}{6\mu'pq}. \]

[p. 117] **4.** *Limite inférieure de* \(t_{\mu'p+x} + t_{\mu'p-x}\). On a

\[ t_{\mu'p+x} + t_{\mu'p-x} > 2\sqrt{t_{\mu'p+x} . t_{\mu'p-x}}. \]

Posons

\[ t_{\mu'p+x} . t_{\mu'p-x} = e^{v}, \qquad \sqrt{t_{\mu'p+x} . t_{\mu'p-x}} = e^{\frac{1}{2}v} \]

\[ v = \left(\mathrm{M}p + x + \frac{1}{2}\right) \log\left(1 + \frac{x}{\mathrm{M}p}\right) + \left(\mathrm{M}p - x + \frac{1}{2}\right) \log\left(1 + \frac{x}{\mathrm{M}p}\right) \]

\[ -\left(\mu'p + x + \frac{1}{2}\right) \log\left(1 + \frac{1}{\mu'p}\right) - \left(\mu'p - x + \frac{1}{2}\right) \log\left(1 - \frac{x}{\mu'p}\right) + \text{etc.}, \]

*etc*. désignant ici et plus bas des termes en \(q\) analogues aux termes en \(p\).

On trouve, en dérivant \(v\) par rapport à \(x\),

\[ v' = \log\left(1 + \frac{x}{\mathrm{M}p}\right) + \frac{1}{2} \frac{1}{\mathrm{M}p + x} - \log\left(1 - \frac{x}{\mathrm{M}p}\right) - \frac{1}{2} \frac{1}{\mathrm{M}p - x} \]

\[ -\log\left(1 + \frac{x}{\mu'p}\right) - \frac{1}{2} \frac{1}{\mu'p + x} + \log\left(1 - \frac{x}{\mu'p}\right) + \frac{1}{2} \frac{1}{\mu'p - x} + \text{etc.}; \]

\[ v'' = \frac{1}{\mathrm{M}p + x} - \frac{1}{2} \frac{1}{(\mathrm{M}p + x)^{2}} + \frac{1}{\mathrm{M}p - x} - \frac{1}{2} \frac{1}{(\mathrm{M}p - x)^{2}} \]

\[ -\frac{1}{\mu'p + x} + \frac{1}{2} \frac{1}{(\mu'p + x)^{2}} - \frac{1}{\mu'p - x} + \frac{1}{2} \frac{1}{(\mu'p - x)^{2}} + \text{etc.} \]

On a évidemment, puisque \(\mu'\) est inférieur à M,

\[ v'' > \frac{1}{\mathrm{M}p + x} + \frac{1}{\mathrm{M}p - x} - \frac{1}{\mu'p + x} - \frac{1}{\mu'p - x} + \text{etc.} \]

\[ = \frac{2\mathrm{M}p}{\mathrm{M}^{2}p^{2} - x^{2}} - \frac{2\mu'p}{\mu'^{2}p^{2} - x^{2}} + \text{etc.} \]

[p. 118]

\[ v'' > \frac{2}{\mathrm{M}p}\left[1 + \frac{x^{2}}{\mathrm{M}^{2}p^{2}} + \cdots\right] - \frac{2}{\mu'p}\left[1 + \frac{x^{2}}{\mu'^{2}p^{2}} + \cdots\right] + \text{etc.} \]

\[ > \frac{2}{\mathrm{M}p} - \frac{2}{\mu'p}\left[1 + \frac{4}{3}\frac{x^{2}}{\mu'^{2}p^{2}}\right] + \frac{2}{\mathrm{M}q} - \frac{2}{\mu'q}\left[1 + \frac{4}{3}\frac{x^{2}}{\mu'^{2}q^{2}}\right] \]

\[ = \frac{2}{\mathrm{M}pq} - \frac{2}{\mu'pq} - \frac{8}{3}\frac{x^{2}(p^{3} + q^{3})}{\mu'^{3}p^{3}q^{3}} \]

\[ > \frac{2}{\mathrm{M}pq} - \frac{2}{\mu'pq} - \frac{8}{3}\frac{x^{2}}{\mu'^{3}p^{3}q^{3}} = -\frac{2}{\mu'pq}\frac{\mu}{\mathrm{M}} - \frac{8}{3}\frac{x^{2}}{\mu'^{3}p^{3}q^{3}}. \]

Comme \(v\) et \(v'\) s'annulent, pour \(x = 0\), on trouve, en intégrant de 0 à \(x\),

\[ v' > -\frac{2x}{\mu'pq}\frac{\mu}{\mathrm{M}} - \frac{8}{9}\frac{x^{3}}{\mu'^{3}p^{3}q^{3}}, \]

\[ v > -\frac{x^{2}}{\mu'pq}\frac{\mu}{\mathrm{M}} - \frac{2}{9}\frac{x^{4}}{\mu^{3}p^{3}q^{3}}. \]

On a donc

\[ t_{\mu'p+x} + t_{\mu'p-x} > 2e^{\frac{1}{2}v} = 2e^{-\frac{x^{2}}{2\mu'pq}\frac{\mu}{\mathrm{M}} - \frac{1}{9}\frac{x^{4}}{\mu'^{3}p^{3}q^{3}}}, \]

et, par suite,

\[ t_{\mu'p+x} + t_{\mu'p-x} > 2e^{-\frac{x^{2}}{2\mu'pq}\frac{\mu}{\mathrm{M}}} \left(1 - \frac{1}{9}\frac{x^{4}}{\mu'^{3}p^{3}q^{3}}\right). \]

**5.** *Limite inférieure de* P. On a, puisque \(t_{\mu p} = 1\),

\[ \mathrm{P} = \mathop{\mathrm{S}}\limits_{x=-\mu l}^{x=+\mu l} \mathrm{T}_{\mu'p+x} > \frac{c}{\sqrt{2\pi\mu'pq}} \sqrt{\frac{\mu}{\mathrm{M}}} \mathop{\mathrm{S}}\limits_{x=-\mu'l}^{x=+\mu'l} t_{\mu'p+x} \]

\[ = \frac{2c}{\sqrt{2\pi\mu'pq}} \sqrt{\frac{\mu}{\mathrm{M}}} \left[\mathop{\mathrm{S}}\limits_{x=0}^{x=\mu'l} (t_{\mu p+x} + t_{\mu p-x}) - \frac{1}{2}\right], \]

[p. 119]

\[ \mathrm{P} > \frac{2c}{\sqrt{2\pi\mu'pq}} \sqrt{\frac{\mu}{\mathrm{M}}} \left[\mathop{\mathrm{S}}\limits_{x=0}^{x=\mu'l} e^{-\frac{x^{2}}{2\mu'pq}\frac{\mu}{\mathrm{M}}} \left(1 - \frac{1}{9}\frac{x^{4}}{\mu^{3}p^{3}q^{3}}\right) - \frac{1}{2}\right], \]

et, *a fortiori*, comme on le voit, en recourant à une représentation géométrique,

\[ \mathrm{P} > \frac{2c}{\sqrt{2\pi\mu'pq}} \sqrt{\frac{\mu}{\mathrm{M}}} \left[\int_{0}^{\mu'l} e^{-\frac{x^{2}}{2\mu'pq}\frac{\mu}{\mathrm{M}}} \left(1 - \frac{1}{9}\frac{x^{4}}{\mu'^{3}p^{3}q^{3}}\right)\,dx - \frac{1}{2}\right]. \]

Posons

\[ t^{2} = \frac{\mu x^{2}}{2\mu'pq\mathrm{M}}, \qquad \mathrm{T} = l\sqrt{\frac{\mu'}{2pq}}\sqrt{\frac{\mu}{\mathrm{M}}} = l\sqrt{\frac{\mu\mu'}{2pq(\mu + \mu')}}, \]

il viendra

\[ \mathrm{P} > \frac{2c}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt - \frac{8c}{9\sqrt{\pi}} \frac{\mathrm{M}^{2}}{\mu^{2}\mu'pq} \int_{0}^{\mathrm{T}} e^{-t^{2}} t^{4}\,dt - \frac{c}{\sqrt{2\pi\mu'pq}} \sqrt{\frac{\mu}{\mathrm{M}}}. \]

La seconde intégrale peut être remplacée par l'intégrale plus grande

\[ \frac{8c}{9\sqrt{\pi}} \frac{\mathrm{M}^{2}}{\mu^{2}\mu'pq} \int_{0}^{\infty} e^{-t^{2}} t^{4}\,dt, \]

sans que l'inégalité cesse d'exister. Or, si l'on pose \(t^{2} = u\),

\[ \int_{0}^{\infty} e^{-t^{2}} t^{4}\,dt = \frac{1}{2} \int_{0}^{\infty} e^{-u} u^{\frac{3}{2}}\,du = \frac{1}{2} \Gamma\left(\frac{5}{2}\right) = \frac{1}{2} \cdot \frac{3}{2} \cdot \frac{1}{2} \sqrt{\pi} = \frac{3}{8} \sqrt{\pi}. \]

[p. 120] Il résulte de là que

\[ \mathrm{P} > \frac{2c}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt - \frac{1}{3} \frac{\mathrm{M}^{2}}{\mu^{2}\mu'pq} - \frac{c}{\sqrt{2\pi\mu'pq}} \sqrt{\frac{\mu}{\mathrm{M}}}. \]

On a

\[ \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt < 1, \qquad c = 1 - \frac{1}{8\mu pq} - \frac{1}{6\mu'pq} < 1. \]

Par conséquent,

\[ \mathrm{P} > \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt - \frac{1}{8\mu pq} - \frac{1}{6\mu'pq} - \frac{1}{3} \frac{\mathrm{M}^{2}}{\mu^{2}\mu'qq} - \frac{1}{\sqrt{2\pi\mu'pq}} \sqrt{\frac{\mu}{\mathrm{M}}}. \]

On a ensuite

\[ \frac{1}{3} \frac{\mathrm{M}^{2}}{\mu^{2}\mu'pq} = \frac{1}{3pq} \frac{\mu^{2} + 2\mu\mu' + \mu'^{2}}{\mu^{2}\mu'} = \frac{1}{3\mu'pq} + \frac{2}{3\mu pq} + \frac{\mu'}{3\mu pq}. \]

Donc, enfin, en introduisant cette valeur dans l'inégalité précédente,

\[ \mathrm{P} > \frac{2}{\sqrt{\pi}} \int_{0}^{\mathrm{T}} e^{-t^{2}}\,dt - \frac{19}{24\mu pq} - \frac{1}{2\mu'pq} - \frac{1}{3} \frac{\mu'}{\mu pq} - \frac{1}{\sqrt{2\pi\mu'pq}} \sqrt{\frac{\mu}{\mathrm{M}}}. \]

Si \(\mu\) et \(\mu'\) sont de grands nombres, P est très voisin de l'unité[^120-a].

[p. 121]

[^120-a]: Extrait des *Bull. de l'Acad. roy. de Belgique* (Classe des sciences), n° 5, pp. 538-549, 1904.
