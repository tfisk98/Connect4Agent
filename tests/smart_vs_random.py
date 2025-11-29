import sys
import os
sys.path.append(os.getcwd())


from pettingzoo.classic import connect_four_v3


from src.agents.smart_agent import SmartAgent
import src.agents.random_agent as rnda
import src.game_facilities as gl

import numpy as np

### Testing RandomAgent with choose_action

# Player 0 : SmartAgent && Player 1 : RandomAgent

#gl.connect4_game(100, SmartAgent, rnda.RandomAgent,  True )
stats = gl.connect4_game_with_stats(100, SmartAgent, rnda.RandomAgent,  True )

print("SmartAgent is Agent0 and RandomAgent is Agent1")

## Player 0 : RandomAgent && Player 1 : SmartAgent

#gl.connect4_game(100, rnda.RandomAgent, SmartAgent,  True )

#print("SmartAgent is Agent0 and RandomAgent is Agent1")

## Player 0 : SmartAgent && Player 1 : WeightedRandomAgent privilegies center

#gl.connect4_game(100, SmartAgent, rnda.WeightedRandomAgent,  True )

#print("SmartAgent is Agent0 and RandomAgent is Agent1")

## Player 0 : WeightedRandomAgent && Player 1 : SmartAgent

#data = gl.connect4_game_with_data(100, rnda.WeightedRandomAgent, SmartAgent,  True )

#print("SmartAgent is Agent0 and RandomAgent is Agent1. \n")

print("Game Stats : \n")
print(stats)
