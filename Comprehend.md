###### Comprehension du jeu 
### Partie 1: Regles du jeu
## 1.1: Analyse des règles du jeu 

Le jeu de Puissance 4 se compose d'un plateau de 42 cases, une grille de 7 lignes par 6 colonnes où tour à tour deux joueurs y déposent un jeton rouge ou jaune. Le jeton est soit déposé au fond d'une colonne soit au-dessus du jeton le plus haut placé dans la colonne. Le but du jeu est de créer une chaine de 4 jetons de la même couleur. Dans le cas où le plateau est rempli sans possibilté de déclarer un vainqueur, la partie est alors déclaré nulle. Un joueur ne peut déposer un jeton dans une colonne pleine. Les résultats possibles pour un joueur sont donc victoire, match nul ou défaite. Une disqualafication suite à un coup illégal pourra aboutir à une défaite. 

 
## 1.1: Analyse des conditions de victoire

On représentera les jetons par des 0. Voici les conditions de victoires :
1.:0    2.:   0 3.: 0  4.: 
    0        0      0     0 0 0 0
     0      0       0
      0    0        0

Pour vérifier une victoire lorsqu'un joueur pose un jeton, il est nécessaire de vérifier 8 directions. Par exemple, on peut initialiser un compteur à 1 au dépot d'un jeton. Puis on commence à regarder les jetons à sa gauche. On s'arrête lorsque l'on tombe sur un jeton adverse ou lorsque le compteur de jetons atteint la valeur 4.Si il s'atteint la valeur 4 on déclare le joueur vainqueur et la partie se termine. Sinon on fait de même dans la direction opposée, ici la droite. Si le compteur atteint 4 avant de tomber sur un jeton de l'autre joueur on le déclare vainqueur, sinon on commence à regarder dans une autre direction: haut-gauche, haut, haut-droite, bas-droite, bas, bas-gauche (angliscismes). 



### Partie 2: Comprendre PettingZoo

Les noms des deux agents sont : 'player_0' et'player_1'.
La variable 'action' correspond à un entier compris entre 0 et 6, correspondant à l'indice de la colonne dans lequel un joueur désire déposer son jeton.
'env.agent_iter()' est une liste contenant qui sur lequel on itere au cours d'une ou plusieurs parties afin de connaitre le joueur/l'agent dont c'est au tour de jouer.
'env.step(action)' place un jeton dans la grille de l'agent en question, en placant un 1 dans le tableau/matrice de jeu, vérifie si une des conditions de victoire est atteinte. 
'env.last()' renvoie la grille de l'agent en question(observation), un score indiquant la qualité de la position de l'agent (reward), si la partie est finie ou non (termination), (truncation) ainsi que des informations complémentaires. 

  
