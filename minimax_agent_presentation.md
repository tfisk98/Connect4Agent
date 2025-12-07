# Presentation de `MinimaxAgent`

## 1. Description 


La classe `MinimaxAgent` simule un agent, qui joue un coup selon l'algorithme d'évaluation `Minimax`, pour une profondeur donnée. La profondeur désigne ici le nombre de coups à simuler avant de passer à l'évaluation de la situation dejeu. Des profondeurs de 1 à 6 ont été considérées ici. L'agent qui a été utilisé par les auteurs du package sur la compétition ML-Arena a utilisé une profondeur de 2.

### 1.1. L'algorithme `Minimax`

L'algorithme `Minimax` est un algorithme très connu en théorie des jeux et vastement employé dans les jeux où 2 joueurs s'affrontent comme le morpion, le jeux d'échecs ou encore ici Puissance 4. L'hypothèse faite est que les agents sont deux joueurs qui cherchent à maximiser leur évaluation. Lors d'une recherche, l'agent va chercher à jouer le coup qui maximise son score si c'est lui qui joue et à minimiser celui de l'adversaire sinon. 

L'évaluation de la grille repose sur des critères déterminés préalablement. Elle est positive si elle avantage l'agent réalisant l'évaluation et négative sinon. L'algorithme prend également en compte un paramètre de profondeur qui correspond au nombre de coups à simuler avant de procéder à l'évaluation de la grille. 

Lors d'une recherche `MiniMax`, l'agent parcourt une branche jusqu'au bout, réalise l'évaluation de la position puis revient en arrière pour fournir un score temporaire à l'agent zéro. Il parcourt alors la branche suivante et ainsi de suite jusqu'à avoir évalué l'arbre entier. Toutefois, notons que l'agent peut se retrouver à évaluer des positions absurdes, ou avec une évaluation très défavorable et inintéressante pour lui. Une recherche moins naïve prenant en compte ce type de critères est donc réalisée : l'élagage `alpha-beta`.

Quoi qu'il en soit, l'évolution de la complexité avec la profondeur est non linéaire. Le niveau de profondeur ne peut dont pas être trop élevé si l'on souhaite satisfaire les critères de performances (notamment en temps) de la compétition ML-Arena.


### 1.2. L'évaluation d'une grille 

Le module `evaluate_pose.py` permet à l'agent `MinimaxAgent` de mesurer la qualité d'une état du jeu donné. Cette évaluation repose sur des critères simples. les voici classés par score du plus au moins favorable :
- la création d'un puissance 4 (chaine de 4 pions) ;
- La création de chaines de 3 pions ;
- le nombre de jetons au centre ;
- la création de chaines de 2 pions ;

Des coefficients sont attribués à ces critères (respectivement 10000, 5,3,2). ils représentent les priortés de l'agent. La victoire doit avoir un score très supérieur aux autres pour être garantie d'être priorisé. Créer une chaine de trois est plus important que les deux derniers critères car peut mener à une victoire. Enfin, jouer au centre est plus important que créer une chaine de deux car cela facilite la création de chaîne de jetons à long terme. 

L'agent `MinimaxAgent` réalise ensuite l'évaluation complète de la position de son point de vue puis de celui de son adversaire. L'évaluation d'une grille est alors obtenue en soustrayant au score de la position de l'agent à celui de son adversaire. Elle varie donc entre -20 000 (défaite de l'agent) et 20 000 (victoire de l'agent).

Il s'agit ici de critère simples. Ils ne sont donc pas exhaustifs et possèdent donc des faiblesses. En particulier, l'évaluation ne différencie pas les chaines de trois créant des menaces réelles des autres. Une tentative d'implémentation d'un système d'évaluation plus évolué a été éffectuée par les auteurs mais n'a pour le moment pas été couronnée de succès.

Une amélioration a néanmoins été effectuée grâce à la prise en compte de la symétricité de la grille. Cela a permis de rechercher des chaines de 2 ou 3 pions seulement dans 4 directions au lieu de 8. Cela a permis d'accélérer la prise de décision de l'agent.

## 2. Analyse des performances 

Sans surprise le niveau de l'agent augmente avec la profondeur. Des tests ont été éffectués sur des positions forcés, gagnantes pour l'agent, sur des séquences allant jusqu'à 5 coups. Puis des parties ont été joué contre les agents `RandomAgent` et `SmartAgent`.

### 2.1. Données pour une profondeur de 2

Les données présentées ici sont on été obtenues à l'issue de duels de 100 parties entre `MinimaxAgent` avec une profondeur de 2 et les autres agents du package.

#### 2.1.1. `MinimaxAgent` contre `RandomAgent`

##### 2.1.1.1. `MinimaxAgent` joue en premier 

| Nombre de tours moyen | Nombre de tours minimal | Nombre de tours maximal |
|     :---:              |      :---:           |     :---:              |
| 9.18             | 7            | 21              |

- sur les fréquences des résultats des parties

| Agent | Fréquence de victoire | Fréquence d'égalité   | Fréquence de défaite | 
|     :---:           | :---:  | :---: | :---:  |
| `MinimaxAgent`          | 1 | 0 |0 |
| `RandomAgent` | 0 | 0 |1 |

- sur le temps utilisée par chaque agent pour jouer son action :

| Agent | Temps moyen pour jouer (en s) | Temps maximal pour jouer (en s) | 
|    :---:            | :---:    | :---:    |
| `MinimaxAgent`          | 0.069456 | 0.143119 |
| `RandomAgent` |  0.000192 | 0.009874 |

- sur la mémoire utilisée par chaque agent pour jouer son action :


| Agent | Pic moyen de mémoire utilisée pour jouer (en B) | Pic maximal de mémoire utilisée pour jouer (en B) | 
|    :---:           | :---:       | :---:|
| `MinimaxAgent`         | 955.090078 | 1024 |
|`RandomAgent` |  1617.669159 | 3203 |

##### 2.1.1.2. `MinimaxAgent` joue en second

| Nombre de tours moyen | Nombre de tours minimal| Nombre de tours maximal |
|     :---:              |      :---:           |     :---:              |
| 10.35               | 8            | 20          |

- sur les fréquences des résultats des parties

| Agent | Fréquence de victoire | Fréquence d'égalité   | Fréquence de défaite | 
|     :---:           | :---:  | :---: | :---:  |
| `RandomAgent` | 0.03 | 0 | 0.97 |
| `MinimaxAgent`          | 0.97 | 0 | 0.03 |

- sur le temps utilisée par chaque agent pour jouer son action :

| Agent | Temps moyen pour jouer (en s) | Temps maximal pour jouer (en s) | 
|    :---:            | :---:    | :---:    |
| `RandomAgent` | 0.000264 | 0.008939 |
| `MinimaxAgent`          | 0.074011 |  0.147711 |

- sur la mémoire utilisée par chaque agent pour jouer son action :


| Agent | Pic moyen de mémoire utilisée pour jouer (en B) | Pic maximal de mémoire utilisée pour jouer (en B) | 
|    :---:            | :---:        |:---: |
| `RandomAgent` | 1609.820698 | 3339 |
| `MinimaxAgent`          | 977.687238 | 1088 |

#### 2.1.2. `MinimaxAgent` contre `SmartAgent`

##### 2.1.2.1. `MinimaxAgent` joue en premier 

| Nombre de tours moyen | Nombre de tours minimal | Nombre de tours maximal |
|     :---:              |      :---:           |     :---:              |
| 17.27            | 11           | 42             |

- sur les fréquences des résultats des parties

| Agent | Fréquence de victoire | Fréquence d'égalité   | Fréquence de défaite | 
|     :---:           | :---:  | :---: | :---:  |
| `MinimaxAgent`          | 0.93 | 0.01 |0.06 |
| `SmartAgent` | 0.06 | 0.01 |0.93 |

- sur le temps utilisée par chaque agent pour jouer son action :

| Agent | Temps moyen pour jouer (en s) | Temps maximal pour jouer (en s) | 
|    :---:            | :---:    | :---:    |
| `MinimaxAgent`          |0.076772 | 0.218365 |
| `SmartAgent` |  0.000440   | 0.010223 |

- sur la mémoire utilisée par chaque agent pour jouer son action :


| Agent | Pic moyen de mémoire utilisée pour jouer (en B) | Pic maximal de mémoire utilisée pour jouer (en B) | 
|    :---:           | :---:       | :---:|
| `MinimaxAgent`         | 957.894173 | 1024 |
|`SmartAgent` |  758.441723 | 3315 |

##### 2.1.2.2. `MinimaxAgent` joue en second

| Nombre de tours moyen | Nombre de tours minimal| Nombre de tours maximal |
|     :---:              |      :---:           |     :---:              |
| 25.59               | 11           | 42          |

- sur les fréquences des résultats des parties

| Agent | Fréquence de victoire | Fréquence d'égalité   | Fréquence de défaite | 
|     :---:           | :---:  | :---: | :---:  |
| `SmartAgent` | 0.25 | 0.15 | 0.6 |
| `MinimaxAgent`          | 0.6 | 0.15 | 0.25 |

- sur le temps utilisée par chaque agent pour jouer son action :

| Agent | Temps moyen pour jouer (en s) | Temps maximal pour jouer (en s) | 
|    :---:            | :---:    | :---:    |
| `SmartAgent` | 0.000433 |  0.010278 |
| `MinimaxAgent`          | 0.080153 |  0.184945 |

- sur la mémoire utilisée par chaque agent pour jouer son action :


| Agent | Pic moyen de mémoire utilisée pour jouer (en B) | Pic maximal de mémoire utilisée pour jouer (en B) | 
|    :---:            | :---:        |:---: |
| `SmartAgent` | 1084.348056 |  3315 |
| `MinimaxAgent`          | 1016.634300 | 1088 |


### 2.2. Autres données

Davantages de données sur des duels de 100 parties ont été récoltées en faisant jouer `MinimaxAgent` en contre `SmartAgent`en faisant varier la profondeurs. Des évaluations sur le temps maximal mis par l'agent pour jouer ont été égalements relevées pendant ce temps.

#### 2.2.1. `MinimaxAgent` joue en premier

|  Profondeur | Victoires | Défaites |
|     :---:           | :---:  | :---: |
| 1 | 78 | 22 |
| 2 | 92 | 4 |
| 3 | 100 | 0 |
| 4 | 87 | 3 |
| 5 | 100 | 0 |

#### 2.2.2. `MinimaxAgent` joue en second


| Profondeur | Victoires | Défaites |
|     :---:           | :---:  | :---: |
| 1 | 6 | 94 |
| 2 | 68 | 21 |
| 3 | 51 | 23 |
| 4 | 69 | 12 |
| 5 | 79 | 6 |

#### 2.2.3. Temps maximal pour jouer

|Profondeur | Temps maximal pour jouer (en s) | 
|     :---:           | :---:  |
| 1 | 0.01 | 
| 2 | 0.2 |
| 3 | 3.2 |
| 4 | 4.5 |
| 5 | 6.8 |

### 2.3. Analyse

#### 2.3.1 Force globale de `MinimaxAgent` avec profondeur 2

`MinimaxAgent` écrase complétement `RandomAgent` puisque les fréquences de victoire selon qu'il jouer premier ou second sont respectivement de 100% et 97%. Un score de 93% de victoires est également constaté lorsqu'il joue en premier contre `SmartAgent`. Lorsqu'il joue en second contre `SmartAgent`, le nombre de victoires est plus faible (60%) mais avec de nombreuses égalités (15%). Le `MinimaxAgent` ne perd donc que dans 25% des cas.

Les parties sont très courtes `RandomAgent` (une dizaine de coups en moyenne) et de longueur moyenne contre `SmartAgent` (une vingtaines de coups environ).

Finalement, l'avantage d'initiative semble considérablement réduit pour les deux autres agents lorsque `MinimaxAgent` commence en second

#### 2.3.2. Analyse des coups joués

Un examen de différentes situations de jeu montrent qu'une victoire forcé en X coups est détecté systématiquement par un agent de profondeur supérieure ou égale à X. Ceci valide en partie l'implémentation de l'agent. Cependant, une observation intéressante se dégage également et démontre une possibilité d'amélioration du modèle. En ezffet, en cas de détection d'une victoire forcée, l'agent continue d'évaluer l'ensemble des positions de jeux pour son réglage de profondeur. Il perd donc du temps avec des calculs inutiles alors qu'il pourrait simplement jouer la ligne forcée. 

Il est également visible que `MinimaxAgent` essaie de former des chaînes de pions comme attendu par l'implémentation de `Minimax` réalisée. Sex taux de victoires contre `RandomAgent` et `SmartAgent` ne sont donc pas surprenantes puisque ces deux agents ne détectent au mieux que les menaces directes. Cela semble démontrer la capacité du `MinimaxAgent` a créer des stratégies plus complexes que ces agents.  

#### 2.3.3. Effet de la profondeur sur les performances

D'après les données, augmenter la profondeur semble améliorer les 
chances de victoire de l'agent même si cela n'est pas aussi drastique que ce que l'on pourrait penser. A profondeur 5, l'effet est toute de même notable, notamment lorsque `MiniMaxAgent` joue en second. 

Pour ce qui est du temps maximal pour jouer, celui augmente sans surprise avec la profondeur. On constate notamment qu'à partir de la profondeur 3, l'agent dépasse les 3 secondes maximales imposées par ML-Arena. Sans amélioration supplémentaire de la vitesse de choix de l'agent, la profondeur 2 est donc imposée. Notons qu'elle vérifie également sans mal les contraintes d'utilisation mémoire.


#### 2.3.4. Bilan 

Le `MinimaxAgent` est un agent efficace qui bat voire écrase complétement les agents précédents si sa profondeur est au moins égale à 2. Il semble développer comme prévu des stratégies plus complexes que le `SmartAgent` et qui lui permettent de détecter des menaces ou possibilités de victoire plusieurs coups à l'avance. En outre, les conditions de performances de la compétition de ML-Arena sont bien respectées si la profondeur est égale à 2.


