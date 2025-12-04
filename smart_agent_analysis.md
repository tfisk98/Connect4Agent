#Comparaison des performances

Les tableaux détaillés des 

##Taux de victoires

Le test à pris la forme d'un lancement de 10 000 parties entre deux agents qui est équivalent à lancer 100 séries de 100 parties entre agents.

  Sur 10 000 parties entre le SmartAgent, qui joue de manière guidée, et le RandomAgent qui joue de manière aléatoire, le taux de victoires se situe à 99,09% en faveur du SmartAgent et 4 parties nulles ont été observé. La victoire est donc quasi-systématique pour le SmartAgent.

Lorsque le RandomAgent commence, le pourcentage de victoire pour le SmartAgent tombe à 97.9% ce qui pourrait être expliqué par des fois où le RandomAgent arrive à créer et exploiter des doubles voies de victoires sur la première ligne. 

Contre un WeightedRandomAgent qui a pour consigne de privilégier le centre, le pourcentage de victoire est à 97.5% lorsque le SmartAgent commence. Le nombre de tour moyens par partie augmente pour passer à 16. Lorsque l'autre agent commence le SmartAgent enregistre 92% de victoires et 7.3% de défaites.  


##Efficacité de la stratégie 

Contre le RandomAgent, le coup se déclanchant le plus souvent est la préférence au centre. Ce constat est sans surpise face à un agent aléatoire qui ne détecte pas les 'puissance 4' et n'a pas pour consigne de privilégier une colonne en particulier. Une partie dure en moyenne 11,2 coups et les victoires sont souvent acquises en 7 coups par le SmartAgent. Les coups se déclanchant les plus fréquemment sont dans l'ordre d'apparition : les coups gagnants, les coups aléatoires, et les coups bloquants.

Contre le WeightedRandomAgent, le coup aléatoire devient le coup le plus utilisé par le SmartAgent, suivi de la préférence au centre, de la victoire puis de la défaite. Les parties deviennent plus longues et durent en moyenne 16,7 tours, et la victoire minimale se fait en 11 tours. Le SmartAgent mets donc en moyenne à peu près 5 tours de plus pour créer des chaines de 3 jetons ce qui n'est pas énorme en jouant de manière aléatoire. 

Le temps moyen pour jouer un coup par le SmartAgent est de l'ordre du centième de seconde et son pic de consommation de mémoire se situe autour de 4.7 kilobits. 


## Cas d'échecs

Le modèle ne parvient pas à gérer le cas où 2 colonnes offrent la possibilité d'un puissance 4 à l'adversaire, comme par exemple lorsque trois jetons sont positionnés sur la ligne du bas (5) de manière contigue, car il le détecte trop tard. Le cas où une colonne présente un cas de doubles menace sur 2 lignes successives ne peut également être paré par le modèle actuel.

## Améliorations 

Un axe d'amélioration pourrait donc être de pouvoir détecter les menaces ci-dessus suffisament tôt grâce à une fonction de calcul. Il serait également intéressant de pouvoir les créer. 
Pour faire suite à l'axe précédent, le véritable axe d'amélioration serait donc de diminuer l'aléatoire. Une fois la colonne du centre(3) remplie, l'agent redevient un agent aléatoire jusqu'à l'apparition de potentiels puissance 4, ce qui est une limite de l'agent actuel. 


## Annexe


#### SmartAgent vs RandomAgent : <br>

| Nombre de tours moyen | Nombre de tours minimal | Nombre de tours maximal |
|     :---:             |      :---:              |     :---:               |
| 11.2095                | 7              | 420000                 |

- sur les fréquences des résultats des parties

| Agent | Fréquence de victoire | Fréquence d'égalité   | Fréquence de défaite | 
|     :---:    | :---:  | :---: | :---:  |
| SmartAgent   | 0.9909 | 0.0004 |0.0087 |
| RandomAgent  | 0.0087 | 0.0004 |0.9909 |

- sur le temps utilisée par chaque agent pour jouer son action :

| Agent | Temps moyen pour jouer (en s) | Temps maximal pour jouer (en s) | 
|    :---:     | :---:    | :---:    |
| SmartAgent   | 0.000176 | 0.010628 |
| RandomAgent  | 0.000049 | 0.001434 |

- sur la mémoire utilisée par chaque agent pour jouer son action :


| Agent | Pic moyen de mémoire utilisée pour jouer (en B) | Pic maximal de mémoire utilisée pour jouer (en B) | 
|    :---:     | :---:        | :---:    |
| SmartAgent   | 3313.937366  | 4793     |
| RandomAgent  |  1596.188519 | 3195 |



#### RandomAgent vs SmartAgent : <br>

| Nombre de tours moyen | Nombre de tours minimal | Nombre de tours maximal |
|     :---:             |      :---:              |     :---:               |
| 12.7302                | 7              | 420000                 |

- sur les fréquences des résultats des parties

| Agent | Fréquence de victoire | Fréquence d'égalité   | Fréquence de défaite | 
|     :---:    | :---:  | :---: | :---:  |
| RandomAgent  | 0.9794 | 0.0006 |0.0200 |
| SmartAgent   | 0.0200 | 0.0006 |0.9794 |

- sur le temps utilisée par chaque agent pour jouer son action :

| Agent | Temps moyen pour jouer (en s) | Temps maximal pour jouer (en s) | 
|    :---:     | :---:    | :---:    |
| RandomAgent  | 0.000048 | 0.001353 |
| SmartAgent   | 0.000180 | 0.010860 |

- sur la mémoire utilisée par chaque agent pour jouer son action :


| Agent | Pic moyen de mémoire utilisée pour jouer (en B) | Pic maximal de mémoire utilisée pour jouer (en B) | 
|    :---:     | :---:        | :---:|
| RandomAgent  | 1590.520168  | 4609 |
| SmartAgent   |  3312.556760 | 3195 |



#### SmartAgent vs WeigthedRandomAgent : <br>

| Nombre de tours moyen | Nombre de tours minimal | Nombre de tours maximal |
|     :---:              |      :---:           |     :---:              |
| 16.7734                | 11.0000              | 420000                 |

- sur les fréquences des résultats des parties

| Agent | Fréquence de victoire | Fréquence d'égalité   | Fréquence de défaite | 
|     :---:           | :---:  | :---: | :---:  |
| SmartAgent          | 0.9748 | 0.0038 |0.0214 |
| WeigthedRandomAgent | 0.0214 | 0.0038 |0.9748 |

- sur le temps utilisée par chaque agent pour jouer son action :

| Agent | Temps moyen pour jouer (en s) | Temps maximal pour jouer (en s) | 
|    :---:            | :---:    | :---:    |
| SmartAgent          | 0.000175 | 0.012168 |
| WeigthedRandomAgent | 0.000029 | 0.000864 |

- sur la mémoire utilisée par chaque agent pour jouer son action :


| Agent | Pic moyen de mémoire utilisée pour jouer (en B) | Pic maximal de mémoire utilisée pour jouer (en B) | 
|    :---:           | :---:       | :---:|
| SmartAgent         | 3315.625409 | 4793 |
|WeigthedRandomAgent |  902.946523 | 3187 |



#### WeigthedRandomAgent vs SmartAgent  : <br>

| Nombre de tours moyen | Nombre de tours minimal| Nombre de tours maximal |
|     :---:              |      :---:           |     :---:              |
| 22.0297                | 11.0000              | 420000                 |

- sur les fréquences des résultats des parties

| Agent | Fréquence de victoire | Fréquence d'égalité   | Fréquence de défaite | 
|     :---:           | :---:  | :---: | :---:  |
| WeigthedRandomAgent | 0.0729 | 0.0006 | 0.9198 |
| SmartAgent          | 0.9198 | 0.0006 | 0.0729 |

- sur le temps utilisée par chaque agent pour jouer son action :

| Agent | Temps moyen pour jouer (en s) | Temps maximal pour jouer (en s) | 
|    :---:            | :---:    | :---:    |
| WeigthedRandomAgent | 0.000036 | 0.001220 |
| SmartAgent          | 0.000185 | 0.014552 |

- sur la mémoire utilisée par chaque agent pour jouer son action :


| Agent | Pic moyen de mémoire utilisée pour jouer (en B) | Pic maximal de mémoire utilisée pour jouer (en B) | 
|    :---:            | :---:        |:---: |
| WeigthedRandomAgent |  1127.830577 | 3187 |
| SmartAgent          |  3310.667627 | 4673 |
