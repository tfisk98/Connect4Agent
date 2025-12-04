# Présentation de RandomAgent

## 1. Description

La classe `RandomAgent` simule un agent très simple qui joue uniformément au hasard parmi les coups légaux disponibles. Une classe fille `WeightedRandomAgent` existe également et ajoute une pondération faisant jouer l'agent dans la colonne centrale si cela est possible. L'agent joue de la même manière que `RandomAgent` sinon.

## 2. Analyse des performances

### 2.1. RandomAgent contre RandomAgent

#### 2.1.1. Données

A l'issue de 10 000 parties jouées entre deux agents de la classe `RandomAgent` avec le réglage d'environnement `seed=42`, les données suivantes ont été réccoltées à l'aide de la fonction `connect4_game_with_stats` du module `game_loop.py` : 

- sur la durée d'une partie : <br>

| Nombre de tours moyen | Nombre de tours minimal | Nombre de tours maximal |
|     :---:             |      :---:              |     :---:               |
| 21.2806                | 7              | 420000                 |

- sur les fréquences des résultats des parties

| Agent | Fréquence de victoire | Fréquence d'égalité   | Fréquence de défaite | 
|     :---:    | :---:  | :---: | :---:  |
| RandomAgent0 | 0.5478 | 0.0021 |0.4501 |
| RandomAgent1 | 0.4501 | 0.0021 |0.5478 |

- sur le temps utilisée par chaque agent pour jouer son action :

| Agent | Temps moyen pour jouer (en s) | Temps maximal pour jouer (en s) | 
|    :---:     | :---:    | :---:    |
| RandomAgent0 | 0.000080 | 0.010167 |
| RandomAgent1 | 0.000083 | 0.008106 |

- sur la mémoire utilisée par chaque agent pour jouer son action :


| Agent | Pic moyen de mémoire utilisée pour jouer (en B) | Pic maximal de mémoire utilisée pour jouer (en B) | 
|    :---:     | :---:        | :---:    |
| RandomAgent0 | 1623.064751  | 2836     |
| RandomAgent1 |  1622.624966 | 1624 |

#### 2.1.2. Analyse

On constate donc les parties remplissent en moyenne la moitiée de la grille environ. La durée de jeu est donc moyenne et peut parfois aller jusu'à l'égalité (le nombre de tours maximal est 42) mais que cela est rare (seulement 0.21% des parties se terminent par une égalité). Il arrive également qu'un agent gagne parfois avec le nombre de coup optimal (le nombre de tours minimal est 7).

Les agents semblent de forces équivalentes puisque les fréquences de victoire sont de l'ordre de 55% pour celui qui joue en premier, et 45% pour celui qui joue en second. En effet, la différence de 5% vient vraisemblablement de l'avantage d'initiative que possède l'agent jouant en premier. 

En ce qui concerne les performances requises par la compétition de ML-Arena (3s et un usage mémoire maximal de 384 Mi par coup), celles-ci sont sans surprise amplement respectées pour des agents aussi simples, que ce soit en moyenne ou en maximum. On constate cependant que l'agent jouant en premier semble avoir un maximum de temps et mémoire utilisés supérieur à l'agent jouant en second.

En conclusion, retenons en particulier de cette analyse que l'agent jouant en premier semble avoir un avantage d'initiative mais est potentiellement plus à risque de ne pas respecter les performances requises par la compétition de ML-Arena.

### 2.2. WeightedRandomAgent contre RandomAgent

#### 2.2.1. Données

##### 2.2.1.1. WeightedRandomAgent joue en premier

Avec la même configuration de test que pour le paragraphe 1.1, les données suivantes ont été obtenues : 

- sur la durée d'une partie : <br>

| Nombre de tours moyen | Nombre de tours minimal | Nombre de tours maximal |
|     :---:             |      :---:              |     :---:               |
| 11.8919               | 7               | 42             |

- sur les fréquences des résultats des parties

| Agent | Fréquence de victoire | Fréquence d'égalité   | Fréquence de défaite | 
|     :---:    | :---:  | :---: | :---:  |
| WeightedRandomAgent | 0.8721 | 0.0009 |0.1270 |
| RandomAgent         | 0.1270 | 0.0009 |0.8721 |

- sur le temps utilisé par chaque agent pour jouer son action :

| Agent | Temps moyen pour jouer (en s) | Temps maximal pour jouer (en s) | 
|    :---:     | :---:    | :---:    |
| WeightedRandomAgent | 0.000017 | 0.010167 |
| RandomAgent         | 0.000083 | 0.010751 |

- sur la mémoire utilisée par chaque agent pour jouer son action :


| Agent | Pic moyen de mémoire utilisée pour jouer (en B) | Pic maximal de mémoire utilisée pour jouer (en B) | 
|    :---:     | :---:        | :---:    |
| WeightedRandomAgent | 307.405193   | 1616 |
| RandomAgent         |  1635.817775 | 2700 |

##### 2.2.1.2 WeightedRandomAgent joue en second

Avec la même configuration de test que pour le paragraphe 1.1, les données suivantes ont été obtenues : 

- sur la durée d'une partie : <br>

| Nombre de tours moyen | Nombre de tours minimal | Nombre de tours maximal |
|     :---:             |      :---:              |     :---:               |
| 12.4429               | 7               | 42             |

- sur les fréquences des résultats des parties

| Agent | Fréquence de victoire | Fréquence d'égalité   | Fréquence de défaite | 
|     :---:    | :---:  | :---: | :---:  |
| RandomAgent         | 0.1799 | 0.0004 |0.8197 |
| WeightedRandomAgent | 0.8197 | 0.0004 |0.1799 |

- sur le temps utilisé par chaque agent pour jouer son action :

| Agent | Temps moyen pour jouer (en s) | Temps maximal pour jouer (en s) | 
|    :---:     | :---:    | :---:    |
| RandomAgent          | 0.000079 | 0.010315 |
| WeightedRandomAgent  | 0.000016 | 0.010263 |

- sur la mémoire utilisée par chaque agent pour jouer son action :


| Agent | Pic moyen de mémoire utilisée pour jouer (en B) | Pic maximal de mémoire utilisée pour jouer (en B) | 
|    :---:     | :---:        | :---:    |
| RandomAgent         | 1631.747264 | 2836 |
| WeightedRandomAgent |  299.159817 | 1616 |

#### 2.2.2. Analyse 

Les conclusions sont dénuées d'ambiguïté : 
- l'agent avec pondération gagne dans plus de 80% des cas et les parties sont en général très courtes (12 coups en moyenne) indépendamment de l'ordre de jeu;
- on retrouve la différence de 5% liée à l'initiative en début de partie : l'agent pondéré gagne environ 5% plus souvent quand il joue en premier;
- l'agent avec pondération vérifie facilement les exigences de performance de la compétition ML-Arena et mieux que l'agent simplement aléatoire.

Ainsi, nous pouvons aisément affirmer que l'agent avec pondération est bien meilleur que  celui simplement aléatoire tout en respectant les conditions de la compétition de ML-Arena. De plus, la présence d'un avantage pour l'agent jouant en premier est confirmée ici aussi