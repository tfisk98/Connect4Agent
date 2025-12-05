# Présentation de `SmartAgent`

## 1. Description 

La classe `SmartAgent` simule un agent plus évolué que les agents aléatoires et réalisant notamment des stratégies élémentaires. 

### 1.1. Hiérarchie des stratégies 

L'agent suit la hiérarchie stratégique suivante parmi les coups légaux autorisés (de la plus prioritaire à la moins) :
- si possible, jouer un coup menant à une victoire immédiate;
- si possible, bloquer une position menant à une victoire immédiate de l'aversaire lors de son prochain coup; 
- si possible, jouer dans la colonne centrale;
- en dernier recours, jouer uniformément au hasard. 

L'agent est donc capable d'avaluer simplement une position en détectant ses possibilités de victoire immédiates ainsi que celles de son adversaire au prochain tour. 

### 1.2. Proposition d'amélioration de l'agent

L'agent pourrait par exemple être amélioré pour suivre la hiérarchie stratégique suivante :
- si possible, jouer un coup menant à une victoire immédiate;
- si possible, bloquer une position menant à une victoire immédiate de l'aversaire lors de son prochain coup; 
- simuler l'état du jeu après ses possibilités d'action pour son coup et appliquer les deux étapes précédentes pour détecter les victoires ou blocages avec un niveau de profondeur supplémentaire; 
- si possible, jouer dans la colonne centrale;
- si possible, renforcer ses propre chaînes de pions ou couper celles de l'adversaire;
- en dernier recours, jouer uniformément au hasard. 

## 2. Analyse des performances 

L'agent a été systématiquement testé contre  lui-même, `RandomAgent` et `WeighterRandomAgent` au travers de duels composés de 10 000 parties avec le réglage d'environnement `seed=42` à l'aide la fonction `connect4_game_with_stats` du module `game_loop.py`.

### 2.1. Données

#### 2.1.1. `SmartAgent` contre `SmartAgent` 

| Nombre de tours moyen | Nombre de tours minimal | Nombre de tours maximal |
|     :---:             |      :---:              |     :---:               |
| 25.0755              | 11             | 42                |

- sur les fréquences des résultats des parties

| Agent | Fréquence de victoire | Fréquence d'égalité   | Fréquence de défaite | 
|     :---:    | :---:  | :---: | :---:  |
| `SmartAgent`   | 0.5531 | 0.0719 |0.3750 |
| `SmartAgent`  | 0.3750 | 0.0719 |0.5531 |

- sur le temps utilisée par chaque agent pour jouer son action :

| Agent | Temps moyen pour jouer (en s) | Temps maximal pour jouer (en s) | 
|    :---:     | :---:    | :---:    |
| `SmartAgent`   | 0.000460 | 0.011101 |
| `SmartAgent` | 0.000451 | 0.011302 |

- sur la mémoire utilisée par chaque agent pour jouer son action :


| Agent | Pic moyen de mémoire utilisée pour jouer (en B) | Pic maximal de mémoire utilisée pour jouer (en B) | 
|    :---:     | :---:        | :---:    |
| `SmartAgent`   | 1181.347385   | 3339     |
| `SmartAgent`  |  1086.979180 | 1736 |

#### 2.1.2. `SmartAgent` contre `WeightedRandomAgent`

##### 2.1.2.1. `SmartAgent` joue en premier 

| Nombre de tours moyen | Nombre de tours minimal | Nombre de tours maximal |
|     :---:              |      :---:           |     :---:              |
| 16.7734                | 11             | 42               |

- sur les fréquences des résultats des parties

| Agent | Fréquence de victoire | Fréquence d'égalité   | Fréquence de défaite | 
|     :---:           | :---:  | :---: | :---:  |
| `SmartAgent`          | 0.9748 | 0.0038 |0.0214 |
| `WeigthedRandomAgent` | 0.0214 | 0.0038 |0.9748 |

- sur le temps utilisée par chaque agent pour jouer son action :

| Agent | Temps moyen pour jouer (en s) | Temps maximal pour jouer (en s) | 
|    :---:            | :---:    | :---:    |
| `SmartAgent`          | 0.000175 | 0.012168 |
| `WeigthedRandomAgent` | 0.000029 | 0.000864 |

- sur la mémoire utilisée par chaque agent pour jouer son action :


| Agent | Pic moyen de mémoire utilisée pour jouer (en B) | Pic maximal de mémoire utilisée pour jouer (en B) | 
|    :---:           | :---:       | :---:|
| `SmartAgent`         | 3315.625409 | 4793 |
|`WeigthedRandomAgent` |  902.946523 | 3187 |

##### 2.1.2.2. `SmartAgent` joue en second

| Nombre de tours moyen | Nombre de tours minimal| Nombre de tours maximal |
|     :---:              |      :---:           |     :---:              |
| 22.0297                | 11            | 42          |

- sur les fréquences des résultats des parties

| Agent | Fréquence de victoire | Fréquence d'égalité   | Fréquence de défaite | 
|     :---:           | :---:  | :---: | :---:  |
| `WeigthedRandomAgent` | 0.0729 | 0.0006 | 0.9198 |
| `SmartAgent`          | 0.9198 | 0.0006 | 0.0729 |

- sur le temps utilisée par chaque agent pour jouer son action :

| Agent | Temps moyen pour jouer (en s) | Temps maximal pour jouer (en s) | 
|    :---:            | :---:    | :---:    |
| `WeigthedRandomAgent` | 0.000036 | 0.001220 |
| `SmartAgent`          | 0.000185 | 0.014552 |

- sur la mémoire utilisée par chaque agent pour jouer son action :


| Agent | Pic moyen de mémoire utilisée pour jouer (en B) | Pic maximal de mémoire utilisée pour jouer (en B) | 
|    :---:            | :---:        |:---: |
| `WeigthedRandomAgent` |  1127.830577 | 3187 |
| `SmartAgent`          |  3310.667627 | 4673 |


#### 2.1.3. `SmartAgent` contre `RandomAgent`

##### 2.1.3.1. `SmartAgent` joue en premier 

| Nombre de tours moyen | Nombre de tours minimal | Nombre de tours maximal |
|     :---:             |      :---:              |     :---:               |
| 11.2095                | 7              | 42                |

- sur les fréquences des résultats des parties

| Agent | Fréquence de victoire | Fréquence d'égalité   | Fréquence de défaite | 
|     :---:    | :---:  | :---: | :---:  |
| `SmartAgent`  | 0.9909 | 0.0004 |0.0087 |
|` RandomAgent`  | 0.0087 | 0.0004 |0.9909 |

- sur le temps utilisée par chaque agent pour jouer son action :

| Agent | Temps moyen pour jouer (en s) | Temps maximal pour jouer (en s) | 
|    :---:     | :---:    | :---:    |
| `SmartAgent`   | 0.000176 | 0.010628 |
| `RandomAgent`  | 0.000049 | 0.001434 |

- sur la mémoire utilisée par chaque agent pour jouer son action :


| Agent | Pic moyen de mémoire utilisée pour jouer (en B) | Pic maximal de mémoire utilisée pour jouer (en B) | 
|    :---:     | :---:        | :---:    |
| `SmartAgent`   | 3313.937366  | 4793     |
| `RandomAgent`  |  1596.188519 | 3195 |

##### 2.1.3.2. `SmartAgent` joue en second

| Nombre de tours moyen | Nombre de tours minimal | Nombre de tours maximal |
|     :---:             |      :---:              |     :---:               |
| 12.7302                | 7              | 42               |

- sur les fréquences des résultats des parties

| Agent | Fréquence de victoire | Fréquence d'égalité   | Fréquence de défaite | 
|     :---:    | :---:  | :---: | :---:  |
| `RandomAgent`  | 0.9794 | 0.0006 |0.0200 |
| `SmartAgent`   | 0.0200 | 0.0006 |0.9794 |

- sur le temps utilisée par chaque agent pour jouer son action :

| Agent | Temps moyen pour jouer (en s) | Temps maximal pour jouer (en s) | 
|    :---:     | :---:    | :---:    |
| `RandomAgent`  | 0.000048 | 0.001353 |
| `SmartAgent`   | 0.000180 | 0.010860 |

- sur la mémoire utilisée par chaque agent pour jouer son action :


| Agent | Pic moyen de mémoire utilisée pour jouer (en B) | Pic maximal de mémoire utilisée pour jouer (en B) | 
|    :---:     | :---:        | :---:|
| `RandomAgent`  | 1590.520168  | 4609 |
| `SmartAgent`   |  3312.556760 | 3195 |


### 2.2. Analyse

#### 2.2.1. Force globale de `SmartAgent`

`SmartAgent` contre lui-même obtient une fréquence de victoire d'environ 55% ainsi qu'une fréquence d'égalité de 7% avec des parties de longueur normale (un nombre de tours par partie moyen d'environ 22). L'avantage d'initiative de 5% sur les victoire est donc conservé ici aussi. Il semble même être plus fort que précédemment si l'on tient compte de l'augmentation de la fréquence de cas d'égalité au détriment de la fréquence de victoire de l'agent jouant en second. 

Le `WeightedRandomAgent` se fait très largement battre dans tous les cas par `SmartAgent`. La fréquence de victoire est d'environ 97% lorsque le SmartAgent commence, 92% lorsqu'il joue en second, avec une fréquence d'égalité négligeable dans les deux cas. Les parties sont là aussi de longueur normale (des nombres de tours par partie moyen d'environ 16 et 22). Nous retrouvons ici aussi l'avantage d'initiative de 5%.  

Finalement, le `RandomAgent` est encore plus faible que `WeightedRandomAgent` face au `SmartAgent`. `SmartAgent` gagne dans 99% des cas environ lorsqu'il joue en premier et 97% des cas environ lorsqu'il joue en second avec des parties courtes d'une dizaine de coups en moyenne. L'avantage d'initiative lorsque `RadomAgent` joue en premier est en outre réduit à 2%.

#### 2.2.2. Analyse des coups joués

Contre `RandomAgent`, le coup se déclanchant le plus souvent est la préférence au centre. Ce constat paraît normal face à un agent aléatoire qui ne privilégie aucune colonne. 

Contre `WeightedRandomAgent`, le coup aléatoire devient le coup le plus utilisé par le SmartAgent, suivi de la préférence au centre, de la victoire puis de la défaite. La pondération au centre de `WeightedRandomAgent` empêche sans surprise `SmartAgent` de gagner très rapidement en jouant au centre.

Pour les cas de défaite de `SmartAgent`, il semblerait qu'une situation récurrente soit celle d'une plateau de jeu où l'adversaire peut gagner au prochain tour en jouant à deux positions différentes. Cela confirme l'importance de l'amélioration de la stratégie (paragraphe 1.2.) avec l'implémentation de la  vérification des conditions de victoire et de défaite avec un niveau de profondeur supplémentaire. 

#### 2.2.3. Bilan

Le `SmartAgent` est ainsi sans aucun doute meilleur que les agents aléatoires malgré des possibilités d'améliorations réelles. De plus, il obtient pour chacun des duels de 10 000 parties un temps maximal pour jouer très inférieur à la seconde ainsi qu'une mémoire maximale utilisée de l'orde du kB. Il vérifie donc très largement les contraintes de performance de la compétition ML-Arena. 



