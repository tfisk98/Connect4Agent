# Comprehension du jeu 
## Partie 1: Regles du jeu
### 1.1: Analyse des règles du jeu 

Le jeu de Puissance 4 se compose d'un plateau vertical de 42 cases : une grille de 6 lignes et 7 colonnes (fois deux pour représenter chaque joueur dans Pettingzoo). Un joueur joue avec les jetons jaunes et l'autre avec les rouges. Ils jouent tour à tour en déposant un jeton en haut d'une colonne (non pleine sinon le coup est illégal) et ce dernier tombe alors le long de celle-ci. Pour gagner, un joueur doit créer une chaine horizontale, verticale ou diagonale de 4 jetons de la couleur qui lui est attribué. Si le plateau est rempli sans que cette condition soit réalisée par l'un des deux joueurs, la partie est alors déclarée nulle.  Un coup illégal entraîne une défaite. Les résultats possibles pour un joueur sont donc victoire, match nul ou défaite.

 
### 1.2: Analyse des conditions de victoire

Voici les configurations victorieuses :

| Condition 1 | Condition 2       | Condition 3 | Condition 4 |
|     :---:   |      :---:        |      :--- |      :---  |
|  0 &ensp;0 &ensp;0 &ensp;0    | 0<br>0<br>0<br>0  | 0<br>&ensp;&ensp;0<br>&ensp;&ensp;&ensp;&ensp;0<br>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;0 | &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;0<br>&ensp;&ensp;&ensp;&ensp;0<br>&ensp;&ensp;0<br>0

Pour une position et une couleur de jeton données dans la grille, il est nécessaire de vérifier 4 directions (ou 8 demi-directions), ce qui donnerait en peudo-code :
- vérifier le nombre de jetons contigus de la même couleur vers le bas : si 3 -> victoire;
- vérifier le nombre de jetons contigus de la même couleur vers la gauche et la droite : si la somme des deux > 3 -> victoire;
- vérifier le nombre de jetons contigus de la même couleur sur la première diagonale dans la première demi-direction puis la seconde : si la somme des deux > 3 -> victoire;
- faire de même avec la deuxième diagonale : si la somme > 3 -> victoire;
- sinon, pas de victoire à cette position. 


## Partie 2: Comprendre PettingZoo
### 2.1 : Lire la documentation

Les noms des deux agents sont : `'player_0'` et `'player_1'`.

La variable `action` de type personnalisé `Discrete` modélise les entiers compris entre 0 et 6 et correspondant aux indices des colonnes de la grille, c'est-à-dire les lieux où un agent peut jouer. :

`env.agent_iter()` est une liste de la forme  <br><center>`['player_0', 'player_1', 'player_0', 'player_1', ... ]` </center><br>sur laquelle on itère au cours d'une partie afin de déterminer l'agent dont c'est le tour.

`env.step(action)` place un jeton dans la grille de l'agent en train de jouer et actualise également l'état global de l'environnement pour initialiser le tour suivant.

`env.last()` renvoie l'état global de l'environnement à l'instant où il est appelé, c'est-à-dire les objets `observation`, `reward`,  `termination`, `truncation` ainsi que `info`.

L'observation retournée est un dictionnaire possédant les clés `"observation"` et `"action_mask"`. La première a pour valeur l'espace d'observation, c'est-à-dire la grille de jeu. La deuxième clé `"action_mask"` est associée à un `mask` vecteur de taille 7 où un index représente une colonne, la valeur associée à cet index indiquant si le coup est légal (valeur 1) ou non (valeur 0). Notons que pour un agent dont ce n'est pas le tour, `mask` ne contiendra que des 0.

La clé `'action_mask'` est ainsi particulièrement importante car elle permet de déterminer les coups légaux possibles pour le prochain coup. 

### 2.2: Analyse de l'espace d'observation

Le tableau d'observation est un tenseur de dimension 3 de taille (6,7,2). 

Les deux premières dimensions représentent une position dans le plateau de jeu. La première correspond aux lignes (index 0 à 6) et la seconde aux colonnes (index 0 à 7). La dernière dimension représente la grille de l'agent en train de jouer (index 0) ou celle de son adversaire (index 1). A l'index 
`(i, j, k)` on a donc : 
- la position (i, j) de la grille de l'agent associé à k;
- la valeur 1 si un jeton de l'agent associé à k;
- la valeur 0 si il y a un jeton de l'adversaire ou une case vide.

## Partie 3 : Décomposition du problème
### 3.1 : Décomposer l'implémentation de l'agent

Au moment de jouer; l'agent reçoit les informations renvoyées par env.last() : 
- le dictionnaire `observation` donnant accès à l'état actuel des grilles de jeu ainsi que les actions légales possibles comme décrit dans les paragraphes précédents;
- le nombre `reward` indiquant le nombre de points gagnés par l'agent (1 pour une victoire, 0  pour une égalité et -1 pour une défaite);
- le booléen `termination` indiquant si le plateau de jeu est plein (égalité) ou non;
- le booléen `truncation` indiquant si un agent a gagné ou jouer un coup illégal; 
- le dictionnaire `info` dont les clés sont les agents et les valeurs des dictionnaires contenant les informations sur l'agent associé à la clé correspondante. 

Les coups valides sont déterminés à l'aide de la valeur `mask` de la clé `"action_mask"` de `observation`. D'après la structure de `mask` décrite au paragraphe 2.1, il suffit alors de parcourir le vecteur et de récupérer les index `i` tels que `mask[i]==1` pour déterminer les colonnes où le coup est légal.

Pour choisir un coup, l'agent sélectionnera alors une des colonnes légales selon une politique d'action définie par la classe associée à l'agent via la méthode `choose_action`. Une première approche naïve consisterait alors en un choix aléatoire équiprobable parmi les colonnes légales (pour des stratégies plus évoluées, se référer au paragraphe 3.2).

Une fois la colonne choisie l'agent n'aura alors plus qu'a retourner via `env.step` son action, ou autrement dit un entier compris entre 0 et 6 correspondant à la colonne dans laquelle le jeton sera joué. 


### 3.2 : Conception d'algorithme - Progression

- Niveau 0 : l'agent choisis une colonne aléatoirement sans tenir compte de l'action_mask et peut donc jouer des coups illégaux.

- Niveau 1 : l'agent joue des coups au hasard mais légaux c'est à dire dans les colonnes dont la valeur dans l'action mask vaut 1. 

Un motif de victoire sera détecté en simulant le dépots d'un jeton dans une colonne puis en observant si l'un des 4 motifs de victoires décris est vérifié, selon le pseudo-algorithme décris dans la section 1.2.

- Niveau 2 : l'agent observe sur sa grille, parmis les colonnes jouables, lesquelles peuvent mènent à une victoire immédiate en vérifiant les 8 motifs de victoires possibles. Si il en trouve une, il la sélectionne. Sinon il joue au hasard. 

- Niveau 3 : Une fois les motifs de victoires vérifiés et dans le cas où aucun d'entre eux n'est détecté par l'agent. Celui-ci vérifie les opportunités de victoires de son adversaire et le bloque si il repère un motif de victoire. Dans le cas, où il n'en trouve pas, il joue au hasard. 

- Niveau 4 : Dans le cas ou l'agent ne trouve aucune potentielle chaine de 4 pions pour lui ou son adversaire, des consignes lui seront données pour sélectionner la colonne dans laquelle jouer. Il pourra s'agir de privilégier des colonnes placées au centre, de chercher des chaines de 2 pions, ou enfin de bloquer les chaines de 2 pions adverses par exemple. 

- Niveau 5 : Pas d'algorithme de choix choisi pour le moment. 

### 3.3 : Définir l'interface de l'agent