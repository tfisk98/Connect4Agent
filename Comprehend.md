# Comprehension du jeu 
## Partie 1: Regles du jeu
### 1.1: Analyse des règles du jeu 

Le jeu de Puissance 4 se compose d'un plateau vertical de 42 cases : une grille de 6 lignes et 7 colonnes (fois deux pour représenter chaque joueur dans Pettingzoo). Un joueur joue avec les jetons jaunes et l'autre avec les rouges. Ils jouent tour à tour en déposant un jeton en haut d'une colonne (non pleine sinon le coup est illégal) et ce dernier tombe alors le long de celle-ci. Pour gagner, un joueur doit créer une chaine horizontale, verticale ou diagonale de 4 jetons de la couleur qui lui est attribué. Si le plateau est rempli sans que cette condition soit réalisée par l'un des deux joueurs, la partie est alors déclarée nulle.  Un coup illégal entraîne une défaite. Les résultats possibles pour un joueur sont donc victoire, match nul ou défaite.

 
### 1.2: Analyse des conditions de victoire

On représentera les jetons par des 0. Voici les conditions de victoires :

1.:        2.:  3.:      4.: 
0          0    0   
  0        0      0      0 0 0 0
    0      0        0
      0    0          0

Pour une position possible du prochain jeton à jouer, il est nécessaire de vérifier 4 directions (ou 8 demi-directions). En pseudo-code :
- vérifier le nombre de jetons contigus de la même couleur vers le bas : si 3 -> victoire;
- vérifier le nombre de jetons contigus de la même couleur vers la gauche et la droite : si la somme des deux > 3 -> victoire;
- vérifier le nombre de jetons contigus de la même couleur sur la première diagonale dans la première demi-direction puis la seconde : si la somme des deux > 3 -> victoire;
- faire de même avec la deuxième diagonale : si la somme > 3 -> victoire;
- sinon, pas de victoire possible à cette position. 


## Partie 2: Comprendre PettingZoo
### 2.1 : Lire la documentation

Les noms des deux agents sont : 'player_0' et'player_1'.

La variable 'action' correspond à un entier compris entre 0 et 6, correspondant à l'indice de la colonne dans lequel un joueur désire déposer son jeton :
- 'env.agent_iter()' est une liste de la forme ['player_0', 'player_1', 'player_0', 'player_1', ... ] sur laquelle on itère au cours d'une partie afin de connaitre le joueur/l'agent dont c'est le tour.
- 'env.step(action)' place un jeton dans la grille de l'agent en train de jouer (indice 0 de la troisième dimension de la grille de jeu pour 'agent_0', indice 1 pour l'autre 'agent_1' ), en placant un 1 aux indices correspondants (premère dimension de la grille de jeu pour le premier index, deuxième dimension pour le second ). 
- 'env.last()' renvoie l'état du jeu une fois le dernier coup joué : le dictionnaire (observation) contenant la grille de jeu (clé 'observation') de taille 6*7*2 ainsi que les coups légaux possibles pour le prochain coup (clé 'action_mask'), un score indiquant la qualité de la position de l'agent (reward), si la grille de jeu a été remplie (booléen termination), si la partie a été remportée ou un coup illégal joué (booléen truncation) ainsi que des informations complémentaires. 

La clé 'action_mask' est ainsi particulièrement importante car elle donne accès au vecteur d'entiers des coups légaux (représentés par 1, les coups illégaux étant eux réprésentés par 0) possibles pour le prochain coup. 

### 2.2: Analyse de l'espace d'observation

Le tableau d'observation est un tenseur de dimension 3 de taille (6,7,2). La première dimension représente les lignes de la grille, la seconde les colonnes et la 3e le nombre de joueurs. Les joueurs n'ont pas accès au même tableau, ou plutôt à la même information. On peut y déposer des 1 (pour un jeton déposé par le joueur), des 0 pour des jetons adverses ou un espace vide. Les jetons du joueurs seront affichés 'X', les jetons adverses 'O' et les espaces vides '.'.'

## Partie 3 : Décomposition du problème
### 3.1 : Décomposer l'implémentation de l'agent

En entrée l'agent reçoit les informations renvoyés par l'environnement : l'état des grilles au moment de choisir son action dans observation['observation'] et ses actions possibles dans observation['action_mask']. Un nombre reward (compris entre -1 et 1 où : -1 correspond à une défaite et 1 correspond à une victoire) indiquant l'état de la partie pourrait guider le choix de l'agent en l'orientant vers des choix défensifs si celui ci est négatif ou dans le cas contraire vers des choix offensifs si celui ci est proche de 1. 

Au début de la partie, toutes les colonnes sont jouables. On initialise observation['action_mask'] à [1,1,1,1,1,1,1]. Lorsqu'un jeton sera déposée sur la ligne 6 d'une colonne, il suffira d'écrire 'observation['action_mask'][col_index] = 0' pour signifier que cette colonne n'est plus jouable. Ainsi, la commande 'if observation['action_mask'][col_index]' sera suffisante pour vérifier la validité d'un coup proposé par un agent.

Pour choisir un coup il faudra choisir une colonne dans action mask qui a pour valeur 1, au hasard ou selon une politique choisie (cf Partie 3.2 de l'exercice 1). Lors du niveau 0 on pourra autoriser les colonnes ayant pour valeur 0 dans observation['action_mask']. Celles-ci donneront lieux à des coups illégaux et eventuellement à des disqualifications.

L'agent retournera un indice compris entre 0 et 6, inclus, qui correspondra à la colonne dans laquelle jouer son jeton. 


### 3.2 : 

- Niveau 0 : l'agent choisis une colonne aléatoirement sans tenir compte de l'action_mask et peut donc jouer des coups illégaux.

- Niveau 1 : l'agent joue des coups au hasard mais légaux c'est à dire dans les colonnes dont la valeur dans l'action mask vaut 1. 

Un motif de victoire sera détecté en simulant le dépots d'un jeton dans une colonne puis en observant si l'un des 4 motifs de victoires décris est vérifié, selon le pseudo-algorithme décris dans la section 1.2.

- Niveau 2 : l'agent observe sur sa grille, parmis les colonnes jouables, lesquelles peuvent mènent à une victoire immédiate en vérifiant les 8 motifs de victoires possibles. Si il en trouve une, il la sélectionne. Sinon il joue au hasard. 

- Niveau 3 : Une fois les motifs de victoires vérifiés et dans le cas où aucun d'entre eux n'est détecté par l'agent. Celui-ci vérifie les opportunités de victoires de son adversaire et le bloque si il repère un motif de victoire. Dans le cas, où il n'en trouve pas, il joue au hasard. 

- Niveau 4 : Dans le cas ou l'agent ne trouve aucune potentielle chaine de 4 pions pour lui ou son adversaire, des consignes lui seront données pour sélectionner la colonne dans laquelle jouer. Il pourra s'agir de privilégier des colonnes placées au centre, de chercher des chaines de 2 pions, ou enfin de bloquer les chaines de 2 pions adverses par exemple. 

- Niveau 5 : Pas d'algorithme de choix choisi pour le moment. 

