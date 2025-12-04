# Implementer un agent basé sur des règles 
## Partie 1 : Planification de la stratégie 
### 3.1 : Conception de la stratégie

#### 1: Classement des priorités 

La priorité 0 est de ne pas jouer de coups illégaux. Ensuite énumérées dans l'ordre du plus au moins important, les priorités sont de : 
_ Chercher les colonnes menant à une victoire immédiate. 
_ Bloquer les colonnes menant à une défaite immédiate.  
_ Ne pas jouer un coup qui mènerait à une défaite immédiate. Id est, le point précedant consiste à repérer les chaine de 3 jetons de l'adversaire et bloquer la chaine. A mon sens, il ne prends pas en compte le cas où une chaine de 3 jetons apparaît par dessus le jeton que l'on vient de déposer. 
_ Améliorer notre position (quelques idées seront énumérées par la suite pour éclaircir ce point).

### 2 : Règles essentielles

_ Suivre la stratégie élaboré dans l'ordre énnoncé. 
_ Ne pas ommettre de motifs de victoires lors de la phase d'observation, que ce soit pour le joueur ou l'adversaire. 
_ Savoir évaluer la position après le dépot d'un jeton ( cf point 3 des concepts stratégiques).
_ Favoriser le centre en début de partie (colonnes 3,4 et 5).  
_ En milieu de partie, chercher à créer des chaines de jetons pour créer des situations de 'puissance 4' lorsqu'aucun des deux agents ne peut prétendre à la victoire dans l'immédiat.

### 3 : Règles souhaitables 

_ Respecter les règles éssentielles.
_ Eviter les coups aléatoires.
_ Pouvoir anticiper/ calculer l'état du jeu après quelques coups en se focalisant sur le prochain coup le plus probable pour l'adversaire. 
_ Plus difficle: Essayer de créer des situations de 'doubles puissance 4' plus difficiles à parer.(une ligne qui rejoint une diagonale par exemple ). 
_ Plus difficile: créer des situations de puissance 4 inévitables, par exemple, deux chaines de 3 jetons sur deux lignes contigues qui se complètent en 4 sur la même colonne. 
_ Eviter les puissances 4 en colonnes qui sont faciles à parer (pour un humain).
_ Eviter les colonnes 1 et 7 qui sont trop isolé en début de partie et qui sont stratégiquement mauvaises.

Très avancés (Exercice 5): 
_ Laisser l'agent explorer et découvrir d'autres stratégies. 
