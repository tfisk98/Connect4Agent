#Comparaison des performances

Dans l'état actuel du code

##Taux de victoires

Plusieurs séries de cent parties ont été réalisé entre le Smart Agent et le Random Agent pour mesurer les performances du Smart Agent. Sur 10 000 parties, le taux moyen de victoires se situe à 99,09% et 4 parties nulles ont été observé. La victoire est donc quasi-systématique.

Lorsque le Random Agent commence. Le pourcentage de victoire pour le SmartAgent tombe à 97.9% ce qui pourrait être expliqué par des fois où le RandomAgent arrive à créer des doubles voies de victoires sur la première ligne. Le nombre moyen de tours approche les 13. 

Contre un Agent Aléatoire qui a pour consigne de privilégier le centre, le pourcentage de victoire est à 97.5% lorsque le Smart Agent commence. Le nombre de tour moyens par partie augmente pour passer à 16. Lorsque l'autre agent commence le Smart Agent enregistre 92% de victoires et 7.3% de défaites.  


##Efficacité de la stratégie 

Le coup se déclanchant le plus souvent est la préférence au centre. Ce constat est sans surpise face à un agent aléatoire qui ne détecte pas les 'puissance 4' et n'a pas pour consigne de privilégier une colonne en particulier. Une partie dure en moyenne 11,2 coups et les victoires sont souvent acquises en 7 coups par le SmartAgent. Les coups se déclanchant les plus fréquemment sont dans l'ordre d'apparition : les coups gagnants, les coups aléatoires, et les coups bloquants.

Contre un agent aléatoire le coup aléatoire devient le coup le plus utilisé par le SmartAgent, suivi de la préférence au centre, de la victoire puis de la défaite. 

Le temps moyen pour jouer un coup par le SmartAgent est de l'ordre du centième de seconde et son pic de consommation de mémoire se situe autour de 4.7 kilobits. 


#A rédiger
## Cas d'échecs

A priori doubles puissance 4.

## Améliorations 

Diminuer la part d'aléatoire.
Détecter les doubles menaces.


# A mettre en forme
#### Smart Agent vs Random Agent 

(Average number of turns per game     11.2095
Minimum number of turns in a game     7.0000
Maximum number of turns in a game    42.0000
Name: Statistics on the length of a game, dtype: float64,           Frequency of win  Frequency of draw  Frequency of loss  Average time to play  Maximum time to play  Average memory usage peak  Maximum memory usage peak
player_0            0.9909             0.0004             0.0087              0.000176              0.010628                3313.937366                       4793
player_1            0.0087             0.0004             0.9909              0.000049              0.001434                1596.188519                       3195)


#### Random Agent vs Smart Agent 

(Average number of turns per game     12.7302
Minimum number of turns in a game     7.0000
Maximum number of turns in a game    42.0000
Name: Statistics on the length of a game, dtype: float64,           Frequency of win  Frequency of draw  Frequency of loss  Average time to play (s)  Maximum time to play (s)  Average memory usage peak  Maximum memory usage peak
player_0            0.0200             0.0006             0.9794                  0.000048                  0.001353                1590.520168                       3395
player_1            0.9794             0.0006             0.0200                  0.000180                  0.010860                3312.556760                       4609)


#### Smart Agent vs Weigthed Random

(Average number of turns per game     16.7734
Minimum number of turns in a game    11.0000
Maximum number of turns in a game    42.0000
Name: Statistics on the length of a game, dtype: float64,           Frequency of win  Frequency of draw  Frequency of loss  Average time to play (s)  Maximum time to play (s)  Average memory usage peak  Maximum memory usage peak
player_0            0.9748             0.0038             0.0214                  0.000175                  0.012168                3315.625409                       4793
player_1            0.0214             0.0038             0.9748                  0.000029                  0.000864                 902.946523                       3187)


#### Weigthed Random vs Smart Agent 

(Average number of turns per game     22.0297
Minimum number of turns in a game    11.0000
Maximum number of turns in a game    42.0000
Name: Statistics on the length of a game, dtype: float64,           Frequency of win  Frequency of draw  Frequency of loss  Average time to play (s)  Maximum time to play (s)  Average memory usage peak  Maximum memory usage peak
player_0            0.0729             0.0073             0.9198                  0.000036                  0.001220                1127.830577                       3187
player_1            0.9198             0.0073             0.0729                  0.000185                  0.014552                3310.667627                       4673)
