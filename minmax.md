# A completer 
#Comprendre l'algorithme minmax 

##Pk min puis max 

Le but pour le joueur qui utilise le minmax est de soit jouer le coup qui maximise son score d'évaluation, soit minimise celui de son adversaire 

## Que contrôle depth ?

Depth correspond à la profondeur de calcul de minmax. Il contrôle le nombre de positions à évaluer, qui dépend de façon exponentielle de depth. 

## Depth trop grand ? 

MinMax ne parvient pas à terminer son évaluation, le programme plante. ( Pas assez de mémoire, temps,...)

## Elagage 

Permet de réduire le nombre d'évaluations de positions. (en retirant les positions qui offrent un score trop faible pour le joueur ou un score trop élevé à l'adversaire). 
