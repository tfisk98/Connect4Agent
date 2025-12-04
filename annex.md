# Annexe : 

Les grilles de jeux correspondant aux listes d'actions prédéfinies dans 
`game_facilities.py` sont représentées ci-dessous (`X` pour les jetons de `player_0`, 
`O` pour ceux de `player_1`) :

| full_game0 <br> (player_0 win) |full_game1 <br> (player_0 loose)| full_column <br> (player_0 will play)| win_state0 <br> (player_0 will play)|
| --- |  --- | --- | --- | 
| <pre>. . . . . . .<br>. . . . . . .<br>X . . . . . . <br>X . . . . . . <br>X O . . . . . <br>X O O . . . .| <pre>. . . . . . .<br>. . . . . . .<br>. O . . . . . <br>. O . . . . .<br>X O X . . . .<br>X O X . . . .|<pre>O . . . . . .<br>X . . . . . .<br>O . . . . . .<br>X . . . . . .<br>O . . . . . .<br>X . . . . . .|<pre>. . . . . . .<br>. . . . . . .<br>. . . . . . . <br>X . . . . . .<br>X . . . . . .<br>X O O O . . .|

| win_state1 <br> (player_0 will play)| win_state2 <br> (player_1 will play) | win_state3 <br> (player_1 will play) | win_state4 <br> (player_1 will play)|
| --- |  --- | --- | --- | 
|<pre>. . . . . . .<br>. . . . . . .<br>. . . . . . . <br>. . . . . . O<br>. . . . . . O<br>X X X . . . O| <pre>. . . . . . .<br>. . . . . . .<br>. . . . . . .<br>. . . . . . .<br>. . . . X X X<br>. . . O O O X|<pre>. . . . . . .<br>. . . . . . .<br>. . . . . . .<br>. . X O X . .<br>. X O X O . .<br>X O X O O X .|<pre>. . . . . . .<br>. . . . . . .<br>. . . . . . .<br>. . X O X . .<br>. . O X O X .<br>. X O O X O X|

|  win_state5 <br> (player_1 will play)| win_state6 <br> (player_1 will play) | block_state0  <br> (player_0 will play)| empty_state |
| --- |  --- | --- | --- | 
|<pre>. . . . . . .<br>. . . . . . O<br>O . . . . . X<br>X O . . . X O<br>O O O . X X X<br>X X X . O O X|<pre>. . . . . . .<br>O . . . . . .<br>X . . . . . O<br>O X . . . O X<br>X X X . O O O<br>X O O . X X X|<pre>. . . . . . .<br>. . . . . . .<br>O . . . . . .<br>O . . . . . <br>O . . . . . .<br>X . . . . X X|<pre>. . . . . . .<br>. . . . . . .<br>. . . . . . .<br>. . . . . . .<br>. . . . . . .<br>. . . . . . .|
>>>>>>> dd110aa (Premerge)
