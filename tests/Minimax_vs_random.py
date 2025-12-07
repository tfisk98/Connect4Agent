import sys
import os
sys.path.append(os.getcwd())


from src.connect4_agent.minimax_agent import MinimaxAgent
#from src.connect4_agent.evaluate_pos import *


import src.connect4_agent.game_facilities as gf

from pettingzoo.classic import connect_four_v3

import src.connect4_agent.random_agent as rnda
import src.connect4_agent.smart_agent as sa

number_of_games=1000

env = connect_four_v3.env(render_mode=None) 
stats=gf.connect4_game_with_stats(number_of_games, MinimaxAgent, sa.SmartAgent)
minimal_win_rate = 0.95
maximum_time = 2.8
maximum_memory_peak = 364*10e6
stat_win_rate0 = stats[1]["Frequency of win"]["player_0"]
stat_maximum_time0 = stats[1]["Maximum time to play"]["player_0"]
stat_maximum_peak0 = stats[1]["Maximum memory usage peak"]["player_0"]


stat_win_rate1 = stats[1]["Frequency of win"]["player_1"]
stat_maximum_time1 = stats[1]["Maximum time to play"]["player_1"]
stat_maximum_peak1 = stats[1]["Maximum memory usage peak"]["player_1"]

print("stat_win_rate0 :", stat_win_rate0)
print("stat_maximum_time0 :", stat_maximum_time0)
print("stat_maximum_peak0 :", stat_maximum_peak0)

print("stat_win_rate1 :", stat_win_rate1)
print("stat_maximum_time1 :", stat_maximum_time1)
print("stat_maximum_peak1 :", stat_maximum_peak1)