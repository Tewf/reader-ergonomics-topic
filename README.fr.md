# Topic

Un seul gabarit pour une unité d'écriture, appelée **topic**, dont les parties peuvent être des topics du même
gabarit. Tout ensemble d'informations s'écrit alors comme un arbre qui se lit de la même façon à chaque profondeur.

Le nom est celui du domaine. Un **topic** est l'unité de DITA et de la rédaction modulaire (topic-based authoring)
([information typing](evidence/information-typing/frame.md)). Les modèles de documents appellent la même unité un
objet de contenu ([document model](evidence/document-model/frame.md)), et les études des arbres à l'écran l'appellent
un nœud ([progressive disclosure](evidence/progressive-disclosure/frame.md)).

Cette page en anglais : [README.md](README.md). Les deux versions suivent le même état.

> **État :** la revue de littérature est faite (2026-10-29) : trois revues multivocales, 218 sources, dans
> [evidence](evidence/). Le gabarit du topic et sa vérification sont écrits ; aucune étude auprès de lecteurs ne les
> a testés. Ce n'est ni une norme officielle, ni une étude évaluée par des pairs, ni un résultat nouveau.
>
> **Comment il est fait :** avec Claude, un assistant IA d'Anthropic, sous la direction du mainteneur, comme
> reader-ergonomics. Les corrections sont bienvenues sous forme d'issues.

## Où il se place

```text
        utilise ──▶ (pointe vers ce dont il dépend)

 niveau 2   les extensions de genre : reader-ergonomics-academic,      autres projets
            reader-ergonomics-presentations, reader-ergonomics-software-design
                                 │                                        │
                                 ├────────────────────────────────────────┘
                                 ▼  peuvent prendre le topic pour squelette (une hypothèse)
 niveau 1   reader-ergonomics-topic    une forme de topic, imbriquée à toute profondeur, sa revue et sa vérification
                                 │
                                 ▼  obéit aux principes ; la CI exécute leurs vérifications ici
 niveau 0   reader-ergonomics          comment un texte sert son lecteur
```

- **Il obéit à [reader-ergonomics](https://github.com/Tewf/reader-ergonomics)**, donc il se place un niveau au-dessus,
  et un projet qui l'utilise se place au-dessus de lui. Aucun niveau ne dépend d'un niveau supérieur.
- **reader-ergonomics ne pointe jamais vers lui :** la norme ne pointe vers aucune extension. Ce dépôt pointe vers
  la norme, jamais vers les extensions.
- **Que les projets du dessus l'utilisent est une hypothèse.** Si aucun ne le fait, ce dépôt répond quand même à une
  question.

## Périmètre

| | Quoi | Pourquoi |
|---|---|---|
| dedans | les preuves sur les gabarits récursifs, du côté du lecteur | le lecteur est l'objet, comme dans reader-ergonomics |
| dedans | la forme du topic : les blocs de tout topic, et comment un topic contient d'autres topics ou pointe vers eux | un seul gabarit, gardé en un seul endroit |
| dedans | une vérification qu'un programme exécute sur un topic à toute profondeur | ce qu'un programme peut vérifier, un programme le vérifie |
| dehors | les genres : articles, preuves, exposés, documents de conception | ils restent dans leurs propres dépôts |
| dehors | ce qu'est une affirmation de recherche, comment on la prouve ou la vérifie | un autre problème, avec ses propres preuves |

## Ce que la revue a trouvé

Chaque réponse renvoie à la revue qui porte ses preuves ; un niveau dit la force de ces preuves.

| Question | Réponse | Niveau | Revue |
|---|---|---|---|
| **Profondeur.** Les lecteurs retiennent mieux les niveaux du haut, et reader-ergonomics limite un plan à trois niveaux. La récursion peut-elle être illimitée dans le stockage et plafonnée dans ce que voit le lecteur ? | Oui, comme conception, à trois conditions : le chemin vers la racine est montré, ce dont la plupart des lecteurs ont besoin se trouve avant le premier pli, et chaque topic replié montre un résumé. Les lecteurs ouvrent rarement une seconde couche, et pour des agents un second niveau de pliage n'a jamais aidé. | supporté avec réserve ; jamais testé directement | [progressive-disclosure](evidence/progressive-disclosure/) |
| **Autoréférence.** Un type de topic dont les enfants sont des topics donne un arbre ; un topic qui se contient lui-même est un cycle. Lequel faut-il au gabarit ? | Le type récursif seul. Chaque modèle de document lu garde chaque instance comme un arbre fini, et interdit, signale ou plafonne un cycle. | convention, sur 14 systèmes | [document-model](evidence/document-model/) |
| **Graphes.** Un topic utilisé par deux parents ne forme plus un arbre. L'arbre n'est-il que le stockage, et le graphe le sens ? | Les normes stockent un graphe d'arbres et donnent à chaque lecture un seul arbre : un parent qui contient, tout autre parent par référence. Aucune étude de la façon dont les lecteurs rencontrent une unité réutilisée n'a été trouvée. | convention ; le côté lecteur est une lacune | [document-model](evidence/document-model/) |
| **Genres.** Le topic est-il ce que partagent les formes de genre, ou leur rival ? | Ce qu'elles partagent, comme la pratique le fait déjà : DITA dérive concept, tâche et référence d'un même topic de base. Le typage seul n'a donné aucun gain d'apprentissage dans le propre test de Horn en 1969 (19,56 contre 17,65, 41 étudiants). Qu'un lecteur qui connaît la base lise mieux un type dérivé n'a pas été testé. | convention ; ce transfert est la question ouverte de ce dépôt | [information-typing](evidence/information-typing/) |

## La référence que le topic doit battre

| Lecteur | Référence | Contrôle |
|---|---|---|
| une personne, l'unité et ses types | le topic de base de DITA 1.3 avec ses types concept, tâche et référence, ses maps et sa réutilisation par référence, validé, cycles signalés | le même contenu en prose non typée |
| une personne, l'arbre sur une page | le même contenu en un seul document d'au plus trois niveaux de titres, sa table des matières toujours visible à côté | l'arbre entièrement déplié |
| un modèle | des passages retrouvés dans l'ordre du document, à budget de jetons égal | un arbre de résumés |

La comparaison mesure le repérage, l'idée générale contre le détail, le rappel après un délai, le transfert vers un
type dérivé jamais vu, et ce qu'une vérification par programme attrape. Le fichier `baseline.md` de chaque revue en
donne le plan.

## Le gabarit du topic

| Partie | Résumé |
|---|---|
| [shapes](shapes/) | le topic, la base dont dérive toute forme, et comment les quatre formes générales de reader-ergonomics s'y ajustent |
| [la vérification](checks/local/topic.py) | s'exécute sur chaque topic de ce dépôt, à toute profondeur : titre, résumé, listé par son parent avec ce résumé, aucun cycle d'inclusion |
| [decisions](decisions/) | un compte rendu par choix d'architecture, chacun ouvert par la décision en une phrase |
| [ai-augmented](ai-augmented/) | sur cette branche seulement : le topic comme format commun à une personne, un modèle et un assistant de preuve |

- Le topic a cinq blocs : titre, résumé, corps, contenu et voir aussi. Chacun est relié à un principe de
  reader-ergonomics et aux preuves d'ici ([topic](shapes/topic.md)).
- Les quatre formes générales s'ajustent toutes, avec deux renommages et une fusion : la ligne de sujet d'un commit
  est à la fois son titre et son résumé. Le topic a été tiré de ces quatre formes, donc le test le plus juste est le
  suivant ([le tableau](shapes/README.md)).
- Sur six formes des extensions de genre dont il n'a pas été tiré, cinq s'ajustent ; un compte rendu de décision
  sans résumé ne s'ajuste pas. Exécutée sur ces trois dépôts, 113 documents, la vérification trouve 7 défauts une
  fois leurs étapes de revue déclarées comme types.
- Ce dépôt est son propre premier arbre de topics : la vérification s'y exécute en CI, et ses tests sont dans
  [checks/test_topic.py](checks/test_topic.py).

## Suite

1. Comparer le topic à la référence ci-dessus, auprès de lecteurs : le plan est dans le `baseline.md` de chaque revue.
2. Les extensions de genre peuvent dériver leurs formes du topic ; chacune le dirait dans son propre dépôt.

## Le vérifier

```sh
git clone https://github.com/Tewf/reader-ergonomics
python3 reader-ergonomics/checks/run.py chemin/vers/ce/depot
```

La CI exécute les mêmes vérifications à chaque push, et une exécution échoue sur toute erreur
([checks.yml](https://github.com/Tewf/reader-ergonomics-topic/blob/master/.github/workflows/checks.yml)). Chaque
push sur master produit aussi le site, [tewf.github.io/reader-ergonomics-topic](https://tewf.github.io/reader-ergonomics-topic/)
([pages.yml](https://github.com/Tewf/reader-ergonomics-topic/blob/master/.github/workflows/pages.yml)).

## Licence

Code sous [Apache License 2.0](LICENSE) ; prose sous [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Réutilisez-le librement, en
citant ce dépôt ; [CITATION.cff](CITATION.cff) donne une citation si besoin.
