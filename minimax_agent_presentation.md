# Presentation de `Minimax_Agent`

## 1.Description 


La classe `Minimax_Agent` simule un agent, qui joue un coup selon l'algorithme d'évaluation Minimax, pour une profondeur donnée. La profondeur désigne ici le nombre de coups à simuler pour avant de passer à l'évaluation de la grille. Des profondeurs de 1 à 6 ont été considérer ici.

### L'algorithme Minimax

L'algorithme Minimax est un algorithme très connu en théorie des jeux et très utilisé dans des jeux à 2 joueurs, où le but est la victoire de l'un au dépends de l'autre, comme le morpion, le jeux d'échecs ou encore ici Puissance 4. L'hypothèse faites est que les agents sont deux joueurs qui cherchent à maximiser leur évaluation. Lors d'une recherche, le joueur zéro prends le rôle du max et va chercher à jouer le coup qui maximise son score et l'adversaire celui qui minimise l'évaluation du joueur zéro. 


A partir d'une mesure chargée de fournir une évaluation objective de la grille et de déterminer ainsi que de quantifier l'avantage ou non d'une position pour l'agent minimax. La mesure se veut donc positive si l'avantage est pour l'agent Minimax et son score d'autant plus élevé que la position lui est favorable.


L'algorithme prends un paramètre profondeur qui correspond au nombre de coups à simuler avant de procéder à l'évaluation de la grille. La complexité de la recherche Minimax est un facteur du produit du nombre de coups par branche et du paramètre de profondeur. Il y aura donc des contraintes sur le niveau de profondeur que l'on peut se permettre si l'on veut rester dans les critères ML Arena de 3 secondes par coup.


Lors d'une recherche MinMax l'agent parcours une branche jusqu'au bout puis par backtracking remonte la branche pour fournir un score temporaire à l'agent zéro. Puis il parcours la branche suivante jusqu'à avoir évaluer l'arbre entier. Cela peut prendre du temps et l'agent peut se retrouver à évaluer des positions absurdes, ou avec une évaluation très défavorable et inintéressante pour lui. On aimerait donc lui éviter des calculs inutiles. Un élagage alpha-beta est donc appliqué afin d'éviter de calculer des branches dont on sait qu'elles ne seront pas choisi par l'agent.


### Sur l'évaluation 

Le `MinimaxAgent` possède un module évaluation lui permettant de mesurer la qualité de sa position sur la grille. Celle-ci repose sur des critères simples et objectifs, classés par score du plus au moins favorable :

_ La création d'un puissance 4 (chaine de 4 pions)
_ La création de chaines de 3 pions 
_ Le nombre de jetons au centre 
_ La création de chaines de 2 pions

On attribue des coéfficients à ces critères,( respectivement 10000, 5,3,2) qui représentent les priortés de l'agent. La victoire doit avoir un score très supérieur aux autres pour être sur d'être priorisé par l'agent au moment de son choix. Créer une chaine de trois est plus important que les deux derniers critères car peut mener à une potentielle victoire et doit avoir une valeur supérieure à la création de deux chaines de deux pour éviter la création de triangle inutiles. Enfin jouer au centre est plus important que créer une chaine de deux afin que le joueur joue au centre plutôt que sur des lignes conjointes et ne concède pas d'avantage long terme à l'adversaire. L'évaluation d'une grille est prise en soustrayant l'évaluation de la grille de l'agent à celle de son adversaire. Elle varie donc entre -20 000 pour une défaite de l'agent à 20 000 pour une victoire.

La faiblesse d'une évaluation aussi simple est de ne pas différencier les chaines de trois créant des menaces de celles menant à rien. Une tentative d'implémentation a été éffectué par les auteurs sans succès.


### Implémentation 

La plupart des fonctions considérés ont été implémanter sans l'aide de Numpy, mais à l'aide de boucle for et while bien choisie. La prise en compte de la symétricité de la grille a permis de chercher des chaines de 2 et de 3 à partir d'un point seulement dans 4 directions au lieu de 8, générant un gain de temps visible. 
Des tests ont révélés que l'agent prenait moins de temps pour choisir un coup avec cela qu'avec Numpy, même un peu soigné. De même l'exclusion des chaines de 3 ne représentant pas de menaces a été tenté un peu hativement mais sans accroissement de performances. 

## 2.Analyse des performances 

Sans surprise le niveau de l'agent augmente avec la profondeur. Des tests ont été éffectués sur des positions forcés, gagnantes pour l'agent, sur des séquences allant jusqu'à 5 coups. Puis des parties ont été joué contre le SmartAgent, pour le valider dans des conditions réelles.

### Résolution de Problèmes 

Sans surprise, une victoire forcé en X coups est détecté systématiquement par un agent de porfondeur égales. Ceci valide en partie la démarche et l'implémentation de l'agent. Cependant, une observation de intéressante fut dégagé et constitue un axe d'amélioration du modèle. Lors d'un problème, où un agent de profondeur 5 possède un gain forcé en 3 coups, celui ne va pas joué la colonne menant à la victoire la plus rapide mais la colonne 0 car il a calculé que peut importe ce qu'il jouait à ce tour là il aurait la victoire en 3 coups au tour suivant. Ceci génère des calculs inutiles.

### `MinimaxAgent`contre `SmartAgent` 

Un test constitue à une série de 100 parties contre le SmartAgent en commençant, puis une seconde de 100 parties en second joueur.

Des faits surprenant ont cependant été observé. 

En commençant :

|.  Profondeur |. Victoires |. Défaites |
| 1 | 78 | 22 |
| 2 | 92 | 4 |
| 3 | 100 | 0 |
| 4 | 87 | 3 |
| 5 | 100 | 0 |


En jouant en second : 

|.  Profondeur |. Victoires |.  Défaites |
| 1 | 6 | 94 |
| 2 | 68 | 21 |
| 3 | 51 | 23 |
| 4 | 69 | 12 |
| 5 | 79 | 6 |

Les résultats ne sont pas linéaires. Il y a cependant des choses à dire. Premièrement on voit que tous les agents battent aissément le `SmartAgent` lorsqu'ils commencent la partie et obtiennent des taux de victoire autour de 90 % pour une profoncdeur supérieure ou égale à 2. Cela s'explique par le fait que le `SmartAgent` ne pouvant que blocker les menaces directes restent des agents aléatoires pas programmés pour  construire des chaines de 2 ou 3 jetons et surtout incapables de construire et parer les doubles menaces. Cela semble démontrer la capacité du `MinimaxAgent` a savoir créer des situations très difficile à parer même sans être explicitement programmé pour.  

Le second tableau donne les résultats des parties où le `SmartAgent`débute. Si les scores ne sont pas aussi écrasant en faveur du `MinimaxAgent`, il faut toutefois noté pour des profondeurs >=2 des scores systématiquement à son avantage. Plus important le `SmartAgent`ne semble pas être capable de dépasser le total de 25 victoires sur 100 parties alors qu'il possède l'avantage de commencer. Le privilège de débuter est d'ailleurs bien visible ici. A noter que l'impact de la profondeur est également visible avec un nombre de défaites qui globalement décroit à mesure que la profondeur augmente. La victoire au Puissance 4 n'étant pas toujours facile lorsque les joueurs sont au même niveau, la capacité à moins concéder des défaites lorsque l'on ne débute pas est un atout. 


### Le facteur temps 


Temps Maximum Par Coups en secondes : 


|.  Profondeur |. 1 Parties |. 100 Parties | 
| 1 | 0.005 | 0.01 |
| 2 | 0.04 | 0.2 |
| 3 | 0.1 | 4.1 |
| 4 | 0.9 | 247 |
| 5 | 2.3 | 901 |

Sans surprise, le temps maximum mis par le `MiniMaxAgent` est fonction croissante de la profondeur. On constate cependant que le `MinimaxAgent`peut prendre énormément de temps sur un coup ce qui est une grande déception. Le coup maximal pour 100 parties peut atteindre des proportions assez incroyables et sont très handicapante. Si des séries de 100 parties où l'agent ne conserve les mêmes temps maximaux de sélection de coups pour les agents de profondeur 3,4 et 5 sont possibles, il y a néanmoins une propention non-négligeable où cela n'est pas le cas. Ceci est un sérieux bémol pour le `Minimax` sans doute due à une érreur d'implémentation. Le modèle de profondeur 2 reste cependant dans les temps. 


## Bilan 

Le `MinimaxAgent` est un agent très performant, capable de battre un aisément un agent `SmartAgent` capable de détecter des opportunités et des menaces directes et jouant au centre, et ceci même implémenté assez simplement sans détection de menace ou base de données de parties. Cependant le facteur temps, si il n'est pas lié à une érreur d'implémentation constitue un frein à l'utilisation dans une compétition.   


