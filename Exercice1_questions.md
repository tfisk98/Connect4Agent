# Compréhension du jeu 
## Partie 1: Règles du jeu
### 1.1: Analyse des règles du jeu 

Le jeu de Puissance 4 se compose d'un plateau vertical de 42 cases : une grille de 6 lignes et 7 colonnes (fois deux pour représenter chaque joueur dans Pettingzoo). Un joueur joue avec les jetons jaunes et l'autre avec les rouges. Ils jouent tour à tour en déposant un jeton en haut d'une colonne (non pleine sinon le coup est illégal) et ce dernier tombe alors le long de celle-ci. Pour gagner, un joueur doit créer une chaine horizontale, verticale ou diagonale de 4 jetons de la couleur qui lui est attribué. Si le plateau est rempli sans que cette condition soit réalisée par l'un des deux joueurs, la partie est alors déclarée nulle.  Un coup illégal entraîne une défaite. Les résultats possibles pour un joueur sont donc victoire, match nul ou défaite.

 
### 1.2: Analyse des conditions de victoire

Voici les configurations victorieuses :

| Condition 1 | Condition 2       | Condition 3 | Condition 4 |
|     :---:   |      :---:        |      :--- |      :---  |
|  0 &ensp;0 &ensp;0 &ensp;0    | 0<br>0<br>0<br>0  | 0<br>&ensp;&ensp;0<br>&ensp;&ensp;&ensp;&ensp;0<br>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;0 | &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;0<br>&ensp;&ensp;&ensp;&ensp;0<br>&ensp;&ensp;0<br>0

Pour une position et une couleur de jeton données dans la grille, il est nécessaire de vérifier 4 directions (ou 8 demi-directions) pour déterminer si la position est gagnante, ce qui donnerait en peudo-code :
- vérifier le nombre de jetons contigus du même joueur vers le bas : si 3 -> victoire;
- vérifier le nombre de jetons contigus du même joueur vers la gauche et la droite : si la somme des deux > 3 -> victoire;
- vérifier le nombre de jetons contigus du même joueur sur la première diagonale dans la première demi-direction puis la seconde : si la somme des deux > 3 -> victoire;
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

La clé `'action_mask'` est ainsi particulièrement importante car elle permet de déterminer les coups légaux possibles pour le prochain tour. 

### 2.2: Analyse de l'espace d'observation

Le tableau d'observation est un tableau `ndarray` de dimension 3 et de taille `(6,7,2)` de la bibliothèque `numpy`.

Les deux premières dimensions représentent une position dans le plateau de jeu cohérent avec l'affichage des matrices `ndarray`. La première correspond ainsi aux lignes (l'index 5 étant la ligne la plus basse de la grille de jeu réelle) et la seconde aux colonnes ( l'index 7 étant la colonne la plus à droite de la grille de jeu réelle). La dernière dimension représente la grille de l'agent en train de jouer (index 0) ou celle de son adversaire (index 1). A l'index 
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

- Niveau 0 : l'agent choisit une colonne aléatoirement sans contrainte.

- Niveau 1 : l'agent choisit une colonne aléatoirement parmi celles associées à un coup légal. 

- Niveau 2 : l'agent vérifie s'il a une opportunité de victoire et la saisit si possible, sinon, il fait la même chose qu'au niveau précédent. 

- Niveau 3 : l'agent vérifie s'il a une opportunité de victoire et la saisit si possible, sinon il vérifie les possibilités de victoire de l'adversaire au prochain tour et joue pour de façon à la bloquer. En dernier recours, il réalise le niveau 1. 

- Niveau 4 : Si l'agent n'a pas de possibilité de vitcoire et son adversaire non plus, il vérifie s'il peut réaliser des placements stratégiques (jouer au centre, renforcer ses chaînes de pions ou bloquer celles de l'adversaire). En dernier recours, il réalise le niveau 1. 

- Niveau 5 : Implémentation d'algorithmes de décision plus évolués, par apprentissage par exemple.

### 3.3 : Définir l'interface de l'agent

Une classe `MyAgent` contiendrait les méthodes :
- `__init__` prenant pour arguments `self`, l'environnement `env` ainsi qu'un argument optionnel `name` et les construits en tant qu'attributs de classe, construit également à partir de `self.env` l'attribut `action_space`; 
-  `choose_action` prenant pour arguments `self`, `observation` (obligatoire) et les autres objets renvoyés par `env.last()` (optionnels) et retourne la prochaine `action` à réaliser selon les stratégies implémentées par la fonction;
- `check_winning_move` permettant de déterminer si il y a un coup gagnant pour l'agent;
- `check_blocking_move` permettant de déterminer si l'adversaire a un coup gagnant au prochain tour;
- `check_center` permettant de déterminer si l'agent peut jouer au centre;
- éventuellement des méthodes plus évoluées d'analyse de la grille de jeu;
- éventuellement des méthodes auxiliaires pour fluidifier l'implémentation des précédentes.

Les méthodes d'analyse de l'état du jeu comme `check_winning_move` devraient retourner, soit le prochain coup à jouer, soit un raffinnement de `action_mask` prenant en compte les heuristiques stratégiques sur la qualité des coups. Les méthodes auxiliaires seront déterminées au fur et à mesure du développement.