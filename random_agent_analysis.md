# Analyse de RandomAgent

## Partie 1 : RandomAgent contre RandomAgent


A l'issue de 10 000 parties jouées entre deux agents de la classe `RandomAgent` avec le réglage d'environnement `seed=42`, les données suivantes ont été réccoltées à l'aide de la fonction `connect4_game_with_stats` du module `game_loop.py` : 

- sur la durée d'une partie : <br>

| Nombre de tours moyen | Nombre de tours minimal | Nombre de tours maximal |
|     :---:             |      :---:              |     :---:               |
| 21.2806                | 7.0000                 | 42.0000                 |

- sur les fréquences des résultats des parties

| Agent | Fréquence de victoire | Fréquence d'égalité   | Fréquence de défaite | 
|     :---:    | :---:  | :---: | :---:  |
| RandomAgent0 | 0.5478 | 0.0021 |0.4501 |
| RandomAgent1 | 0.4501 | 0.0021 |0.5478 |

- sur le temps utilisé par chaque agent pour jouer son action :

| Agent | Temps moyen pour jouer | Temps maximal pour jouer | 
|    :---:     | :---:    | :---:    |
| RandomAgent0 | 0.000080 | 0.010167 |
| RandomAgent1 | 0.000083 | 0.008106 |

- sur la mémoire utilisé par chaque agent pour jouer son action :


| Agent | Pic moyen de mémoire utilisée pour jouer | Pic maximal de mémoire utilisée pour jouer | 
|    :---:     | :---:        | :---:    |
| RandomAgent0 | 1623.064751  | 1624     |
| RandomAgent1 |  1622.624966 | 0.008106 |


On constate donc les parties remplissent en moyenne la moitiée de la grille environ. La durée de jeu est donc moyenne et peut parfois aller jusu'à l'égalité (le nombre de tours maximal est 42) mais que cela est rare (seulement 0.21% des parties se terminent par une égalité).

Les agents semblent de forces équivalentes puisque les fréquences de victoire sont de l'ordre de 55% pour celui qui joue en premier, et 45% pour celui qui joue en second. En effet, la différence de 5% vient vraisemblablement de l'avantage d'initiative que possède l'agent jouant en premier. 

En ce qui concerne les performances requises par la compétition de ML-Arena (3s et un usage mémoire maximal de 384 Mi par coup), celles-ci sont sans surprise amplement respectées pour des agents aussi simples, que ce soit en moyenne ou en maximum. On constate cependant que l'agent jouant en premier semble avoir un maximum de temps et mémoire utilisés supérieur à l'agent jouant en second.

En conclusion, retenons en particulier de cette analyse que l'agent jouant en premier semble avoir un avantage d'initiative mais est plus à risque de ne pas respecter les performances requises par la compétition de ML-Arena.