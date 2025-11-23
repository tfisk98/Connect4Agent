"""
Testing the class RandomAgent from random_agent.py.
WARNING : Working directory must be the parent of this file's directory
"""


### Working directory must be the parent of this file's directory

import sys
import os
sys.path.append(os.getcwd())

import src.random_agent as rnda
import src.game_loop as gl


### Testing RandomAgent 

gl.Connect4_game(2, rnda.RandomAgent, rnda.RandomAgent, True)


### Getting data on numerous games beetween two random agent

data=gl.connect4_game_with_data(10, rnda.RandomAgent, rnda.RandomAgent)
#print(data[1][0])
#print(data[1][1])
#print(data[1][2])


### Getting statistics per game

stats_per_game=gl.getting_stats_per_game(data)
#print(stats_per_game[0])
#print(stats_per_game[1])
#print(stats_per_game[2])


### Getting global statistics over a given set of games

#stats=gl.connect4_game_with_stats(10000, rnda.RandomAgent, rnda.RandomAgent)
#print(stats[0])
#print(stats[1])

#stats=gl.connect4_game_with_stats(10000, rnda.WeightedRandomAgent, rnda.RandomAgent)
#print(stats[0])
#print(stats[1])

stats=gl.connect4_game_with_stats(10000, rnda.RandomAgent, rnda.WeightedRandomAgent)
print(stats[0])
print(stats[1])