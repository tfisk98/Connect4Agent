
<br><center>![Erreur d'affichage](pictures/connect_4.png "data_frame_exemple" )
</center><br>


# connect4_agent : un package pour le jeu Connect4 de la librairie PettingZoo


## 1. Présentation générale du package

`connect4_agent` est un package dont l'objectif est de faciliter la manipulation du jeu Connect4 de la librairie `pettingzoo` (https://pettingzoo.farama.org/). Il fournit les modules suivants :
- `game_factilities.py` : diverses fonctionnalités permettant de manipuler plus facilement l'environnement de jeu Connect4 de `pettingzoo`;
- `random_agent.py` : définit deux classes d'agents aléatoires simples;
- `smart_agent.py` : définit une classe d'agent employant des stratégies simples.

Les agents précédemment mentionnés sont également définis de sorte à respecter les conditions de perfomances de d'une compétition du site ML-Arena (https://ml-arena.com/viewcompetition/2).

Davantage d'informations peuvent être trouvées dans les liens fournis dans le pragrapghe 3 de ce fichier. Voir notamment les présentations d'agents pour les modules d'agents, ainsi que la discussion sur les tests et l'annexe pour  `game_factilities.py`. Les fichiers sources documentés du package peuvent être également consultés.

## 2. Installer et utiliser le package

Le package peut-être téléchargé ici : https://github.com/tfisk98/Connect4Agent.

Le package nécéssite une des versions de Python compatible avec `pettingzoo`. Il s'agit des versions 3.9 à 3.12 (incluses).

Le package peut-être installé dans l'environnemment de votre choix en exécutant dans le terminal la commande `python -m pip install -e .` à la racine du package. Les dépendances nécessaires (`pettingzoo`, `pygame`, `pandas` et `loguru`) seront alors elles-aussi installées automatiquement.

Le package possède le namespace `connect4_agent`. Ainsi, pour importer l'un des modules mentionnés au paragraphe 1, une commande telle que `import connect4_agent.game_facilities as gf` peut par exemple être utilisée. 

L'ensemble des tests du package ont été écrits pour être exécuté avec `pytest` qui doit être installé à part. Une fois ceci fait, la commande éponyme `pytest` peut être utilisé dans le terminal à la racine du package pour exécuter l'ensemble des tests.


## 3. Informations supplémentaires

1) [Présentation générale du jeu et de l'environnement ](general_presentation.md#top)
2) [Présentation de l'agent `RandomAgent`](random_agent_presentation.md)
3) [Présentation de l'agent `SmartAgent`](smart_agent_presentation.md)
4) [Mise en place de tests](testing_plan.md)
5) [Annexe](annex.md#top)
