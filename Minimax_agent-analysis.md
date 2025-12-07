# Presentation de `Minimax_Agent`

## 1 Description 


La classe `Minimax_Agent` simule un agent, qui joue un coup selon l'algorithme d'évaluation Minimax, pour une profondeur donnée. La profondeur désigne ici le nombre de coups à simuler pour avant de passer à l'évaluation de la grille. 

### L'algorithme Minimax

L'algorithme Minimax est un algorithme très connu en théorie des jeux et très utilisé dans des jeux à 2 joueurs, où le but est la victoire de l'un au dépends de l'autre, comme le morpion, le jeux d'échecs ou encore ici Puissance 4. A partir d'une mesure chargée de fournir une évaluation objective de la grille et de déterminer ainsi que de quantifier l'avantage ou non d'une position pour l'agent minimax. La mesure se veut donc positive si l'avantage est pour l'agent Minimax et son ordre d'autant plus conséquent que la position lui est favorable.

L'algorithme simule un nombre de coup égal à la  profondeur donnée en paramètre avant de procéder à l'évaluation de la grille. 