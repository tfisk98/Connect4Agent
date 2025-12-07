"""
Testing the class MinimaxAgent from random_agent.py.
WARNING: Working directory must be the parent of this file's directory
"""


### Working directory must be the parent of this file's directory

import sys
import os
sys.path.append(os.getcwd())

from pettingzoo.classic import connect_four_v3
from pettingzoo.classic import connect_four_v3
from src.connect4_agent.minimax_agent import MinimaxAgent
from src.connect4_agent.evaluate_pos import *
import src.connect4_agent.game_facilities as gf

from src.connect4_agent.random_agent import RandomAgent
from src.connect4_agent.smart_agent import SmartAgent


number_of_games=100

### Checking the evaluation of an agent 

def test_evaluate():
    env = connect_four_v3.env(render_mode=None) 

    #Player_0 lost
    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.full_game0)
    board=env.last()[0]["observation"]
    assert agent0._evaluate(board) == -20000

    #Player_0 has 3 chains of 2 while player 1 has a chain of three (also counted as two chains of two)
    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.connect_twos)
    board=env.last()[0]["observation"]
    assert agent0._evaluate(board) == -3

    env.close()
    return

### Checks the agent correctly evaluates a winning position, from immediate wins to win that are a few steps ahead 

def test_minimax():
    env = connect_four_v3.env(render_mode=None) 

    #Straight win
    env.reset(seed=42)
    agent0=MinimaxAgent(env,1)
    gf.generate_state(env, gf.win_state0)
    board=env.last()[0]["observation"]
    assert agent0._minimax(board, 1, -1e6, 1e6, True) == 20000
    
    #Win in 3 moves 
    env.reset(seed=42)
    agent0=MinimaxAgent(env,3)
    gf.generate_state(env, gf.win_state_depth3)
    board=env.last()[0]["observation"]
    assert agent0._minimax(board, 3, -1e6, 1e6, True) == 20000

    #Win in 5 moves 
    env.reset(seed=42)
    agent0=MinimaxAgent(env,5)
    gf.generate_state(env, gf.win_state_depth5)
    board=env.last()[0]["observation"]
    assert agent0._minimax(board, 5, -1e6, 1e6, True) == 20000

    env.close()
    return

### Checks an agent picks the right columns in cases where there is a forced way to victory

def test_choose_action(): 
  
    assert gf.testing_strategy(gf.win_state0, MinimaxAgent, [0], depth=1)
    assert gf.testing_strategy(gf.win_state_depth3, MinimaxAgent, [1], depth=3)
    assert gf.testing_strategy(gf.win_state_depth32, MinimaxAgent, [6], depth=3)
    assert gf.testing_strategy(gf.win_state_depth5, MinimaxAgent, [6], depth=5)
 
    return
 
### Testing MinimaxAgent against RandomAgent, MinimaxAgent plays first: checking 
### ML-Arena requirements and statistical superiority of MinimaxAgent

def test_Minimax_vs_Random_first() :
    stats=gf.connect4_game_with_stats(number_of_games, MinimaxAgent, RandomAgent)
    minimal_win_rate = 0.95
    maximum_time = 2.8
    maximum_memory_peak = 364*10e6
    stat_win_rate0 = stats[1]["Frequency of win"]["player_0"]
    stat_maximum_time0 = stats[1]["Maximum time to play"]["player_0"]
    stat_maximum_peak0 = stats[1]["Maximum memory usage peak"]["player_0"]
    assert stat_win_rate0 > minimal_win_rate
    assert stat_maximum_time0 < maximum_time
    assert stat_maximum_peak0 < maximum_memory_peak
    return

### Testing MinimaxAgent against RandomAgent, MinimaxAgent plays second: checking 
### ML-Arena requirements and statistical superiority of MinimaxAgent

def test_Minimax_vs_Random_second() :
    stats=gf.connect4_game_with_stats(number_of_games, RandomAgent, MinimaxAgent)
    minimal_win_rate = 0.95
    maximum_time = 2.8
    maximum_memory_peak = 364*10e6
    stat_win_rate1 = stats[1]["Frequency of win"]["player_1"]
    stat_maximum_time1 = stats[1]["Maximum time to play"]["player_1"]
    stat_maximum_peak1= stats[1]["Maximum memory usage peak"]["player_1"]
    assert stat_win_rate1 > minimal_win_rate
    assert stat_maximum_time1 < maximum_time
    assert stat_maximum_peak1 < maximum_memory_peak
    return

### Testing MinimaxAgent against SmartAgent, MinimaxAgent plays first: checking 
### ML-Arena requirements and statistical superiority of MinimaxAgent

def test_Minimax_vs_Smart_first() :
    stats=gf.connect4_game_with_stats(number_of_games, MinimaxAgent, SmartAgent)
    minimal_win_rate = 0.8
    maximum_time = 2.8
    maximum_memory_peak = 364*10e6
    stat_win_rate0 = stats[1]["Frequency of win"]["player_0"]
    stat_maximum_time0 = stats[1]["Maximum time to play"]["player_0"]
    stat_maximum_peak0 = stats[1]["Maximum memory usage peak"]["player_0"]
    assert stat_win_rate0 > minimal_win_rate
    assert stat_maximum_time0 < maximum_time
    assert stat_maximum_peak0 < maximum_memory_peak
    return

### Testing MinimaxAgent against SmartAgent, MinimaxAgent plays second: checking 
### ML-Arena requirements and statistical superiority of MinimaxAgent

def test_Minimax_vs_Smart_second() :
    stats=gf.connect4_game_with_stats(number_of_games, SmartAgent, MinimaxAgent)
    minimal_win_rate = 0.55
    maximum_time = 2.8
    maximum_memory_peak = 364*10e6
    stat_win_rate1 = stats[1]["Frequency of win"]["player_1"]
    stat_maximum_time1 = stats[1]["Maximum time to play"]["player_1"]
    stat_maximum_peak1= stats[1]["Maximum memory usage peak"]["player_1"]
    assert stat_win_rate1 > minimal_win_rate
    assert stat_maximum_time1 < maximum_time
    assert stat_maximum_peak1 < maximum_memory_peak
    return


