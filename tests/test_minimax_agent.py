### Working directory must be the parent of this file's directory

import sys
import os
sys.path.append(os.getcwd())

from pettingzoo.classic import connect_four_v3
from src.connect4_agent.minimax_agent import MinimaxAgent
from src.connect4_agent.evaluate_pos import *
import src.connect4_agent.game_facilities as gf


number_of_games=1000


def test_check_win():
    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.full_game0)
    board=env.last()[0]["observation"]
    player_channel = 1
    assert (agent0._check_win(board, player_channel) == True )
    player_channel = 0
    assert (agent0._check_win(board, player_channel) == False )

    env.close()
    return


def test_get_valid_actions():
    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.full_column)
    board=env.last()[0]["observation"]
    assert (agent0._get_valid_moves(board) == [1,2,3,4,5,6] )

    env.close()
    return

def test_evaluate():
    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.full_game0)
    board=env.last()[0]["observation"]
    assert agent0._evaluate(board) == -20000

    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.connect_twos)
    board=env.last()[0]["observation"]
    assert agent0._evaluate(board) == -3

    env.close()
    return


def test_minimax():
    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.full_game0)
    board=env.last()[0]["observation"]
    assert agent0._minimax(board, 0, -1e6, 1e6, True) == agent0._evaluate(board)

    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.connect_twos)
    board=env.last()[0]["observation"]
    assert agent0._minimax(board, 0, -1e6, 1e6, True) == agent0._evaluate(board)

    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.win_state0)
    board=env.last()[0]["observation"]
    assert agent0._minimax(board, 1, -1e6, 1e6, True) == 20000

    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.win_state_depth3)
    board=env.last()[0]["observation"]
    assert agent0._minimax(board, 3, -1e6, 1e6, True) == 20000

    #env.reset(seed=42)
    #agent0=MinimaxAgent(env)
    #gf.generate_state(env, gf.win_state_depth52)
    #board=env.last()[0]["observation"]
    #assert agent0._minimax(board, 5, -1e6, 1e6, True) == 20000

    env.close()
    return


def test_chose_action(): 
    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.win_state0)
    observation=env.last()[0]
    action_mask = [1,1,1,1,1,1,1]
    assert agent0.choose_action(observation, action_mask) == 0

    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.win_state_depth3)
    observation=env.last()[0]
    assert agent0.choose_action(observation, action_mask) == 1

    #env.reset(seed=42)
    #agent0=MinimaxAgent(env)
    #gf.generate_state(env, gf.win_state_depth32)
    #board=env.last()[0]["observation"]
    #action = agent0.choose_action(observation= env.last()[0],action_mask=action_mask)
    #print("action :", action)
    #assert action == 6 # agent

    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.win_state_depth5)
    observation=env.last()[0]
    action = agent0.choose_action(observation, action_mask=action_mask)
    assert action == 6

    env.close()
    return

"""

def test_Minimax_vs_Random_first() :
    stats=gf.connect4_game_with_stats(number_of_games, MinimaxAgent, rnda.RandomAgent)
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

def test_Minimax_vs_Random_second() :
    stats=gf.connect4_game_with_stats(number_of_games, rnda.RandomAgent, MinimaxAgent)
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

def test_Minimax_vs_Smart_first() :
    stats=gf.connect4_game_with_stats(number_of_games, MinimaxAgent,sa.SmartAgent)
    minimal_win_rate = 0.7
    maximum_time = 2.8
    maximum_memory_peak = 364*10e6
    stat_win_rate0 = stats[1]["Frequency of win"]["player_0"]
    stat_maximum_time0 = stats[1]["Maximum time to play"]["player_0"]
    stat_maximum_peak0 = stats[1]["Maximum memory usage peak"]["player_0"]
    assert stat_win_rate0 > minimal_win_rate
    assert stat_maximum_time0 < maximum_time
    assert stat_maximum_peak0 < maximum_memory_peak
    return

def test_Minimax_vs_Smart_second() :
    stats=gf.connect4_game_with_stats(number_of_games, sa.SmartAgent, MinimaxAgent)
    minimal_win_rate = 0.7
    maximum_time = 2.8
    maximum_memory_peak = 364*10e6
    stat_win_rate1 = stats[1]["Frequency of win"]["player_1"]
    stat_maximum_time1 = stats[1]["Maximum time to play"]["player_1"]
    stat_maximum_peak1= stats[1]["Maximum memory usage peak"]["player_1"]
    assert stat_win_rate1 > minimal_win_rate
    assert stat_maximum_time1 < maximum_time
    assert stat_maximum_peak1 < maximum_memory_peak
    return


"""