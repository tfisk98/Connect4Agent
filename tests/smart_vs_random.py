import sys
import os
sys.path.append(os.getcwd())


from pettingzoo.classic import connect_four_v3
import numpy as np


from src.agents.smart_agent import SmartAgent
from src.agents.enhanced_smart import EnhancedSmartAgent
from src.agents.random_agent import RandomAgent
from src.agents.weighted_random import WeightedRandomAgent
from src.game_facilities import connect4_game_with_stats



""" Testing file : of SmartAgents versus """

## Player 0 : SmartAgent && Player 1 : RandomAgent

stats = connect4_game_with_stats(10000,  WeightedRandomAgent, SmartAgent,  True )

print("SmartAgent is Agent0 and RandomAgent is Agent1")


print("Game Stats : \n")
print(stats)
