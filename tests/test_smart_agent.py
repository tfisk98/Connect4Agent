"""
Testing the class SmartAgent from smart_agent.py (stategies and battles against
other agents). Refer to the annex of readme.md to visualize the game states
used during the tests.
WARNING: Working directory must be the parent of this file's directory
"""

### Working directory must be the parent of this file's directory

import sys
import os
sys.path.append(os.getcwd())


from pettingzoo.classic import connect_four_v3
import src.connect4_agent.game_facilities as gf
import src.connect4_agent.random_agent as rnda
import src.connect4_agent.smart_agent as sa

number_of_games=1000

### Testing valid_actions 

def test_valid_actions():
    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    agent0=sa.SmartAgent(env)
    action_mask_1 = [1,1,1,1,1,1,1]
    valid_actions_1 = agent0._get_valid_actions(action_mask_1)
    action_mask_2 = [1,0,0,1,0,1,1]
    valid_actions_2 = agent0._get_valid_actions(action_mask_2)
    assert valid_actions_1 == [0,1,2,3,4,5,6] and valid_actions_2 == [0,3,5,6]

    env.close()
    return


### Testing _get_next_row

def test__get_next_row():
    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    agent0=sa.SmartAgent(env)
    gf.generate_state(env, gf.full_game0)
    board=env.last()[0]["observation"]
    assert agent0._get_next_row(board, 0) == 1
    assert agent0._get_next_row(board, 1) == 3
    assert agent0._get_next_row(board, 2) == 4
    assert agent0._get_next_row(board, 3) == 5
    assert agent0._get_next_row(board, 4) == 5
    assert agent0._get_next_row(board, 5) == 5
    assert agent0._get_next_row(board, 6) == 5
    
    env.reset(seed=42)
    gf.generate_state(env, gf.full_column)
    board=env.last()[0]["observation"]
    assert agent0._get_next_row(board, 0) == None

    env.close()
    return

### Test choose_action priorities

def test_choose_action():
    
    # Check that winning has the highest priority
    assert gf.testing_strategy(gf.win_state0, sa.SmartAgent, [0])
    
    # Check that blocking opponent has higher priority than playing
    # in the center
    assert gf.testing_strategy(gf.block_state1, sa.SmartAgent, [0])

    # Check that playing in the center has higher priority than playing
    # randomly
    assert gf.testing_strategy(gf.full_column, sa.SmartAgent, [3])

    return

### Test choose action in situations where the agent can win:

def test_winning_move():
    assert gf.testing_strategy(gf.win_state0, sa.SmartAgent, [0])
    assert gf.testing_strategy(gf.win_state1, sa.SmartAgent, [2])
    assert gf.testing_strategy(gf.win_state2, sa.SmartAgent, [2])
    assert gf.testing_strategy(gf.win_state3, sa.SmartAgent, [3])
    assert gf.testing_strategy(gf.win_state4, sa.SmartAgent, [2])
    assert gf.testing_strategy(gf.win_state5, sa.SmartAgent, [3])
    assert gf.testing_strategy(gf.block_state0.copy()+[3,3], sa.SmartAgent, [4])
    return

### Test choose action in situations where the agent can't win and should block it opponent:

def test_blocking_move():
    assert gf.testing_strategy(gf.win_state0.copy()+[4], sa.SmartAgent, [0])
    assert gf.testing_strategy(gf.win_state1.copy()+[6], sa.SmartAgent, [2])
    assert gf.testing_strategy(gf.win_state2.copy()+[3], sa.SmartAgent, [2])
    assert gf.testing_strategy(gf.win_state3.copy()+[0], sa.SmartAgent, [3])
    assert gf.testing_strategy(gf.win_state4.copy()+[0,2], sa.SmartAgent, [3])
    assert gf.testing_strategy(gf.block_state0, sa.SmartAgent, [3])
    assert gf.testing_strategy(gf.block_state1, sa.SmartAgent, [0])
    return 

### Testing SmartAgent against himself, checking ML-Arena requirements and statistical
### expected winrate and draw range with an advantage for the agent that play first

def test_SmartAgent():
    stats=gf.connect4_game_with_stats(number_of_games, sa.SmartAgent, sa.SmartAgent)
    minimal_win_rate0 = 0.5
    minimal_win_rate1 = 0.35
    minimal_draw_rate = 0.05
    maximum_time = 2.8
    maximum_memory_peak = 364*10e6
    stat_win_rate0 = stats[1]["Frequency of win"]["player_0"]
    stat_maximum_time0 = stats[1]["Maximum time to play"]["player_0"]
    stat_maximum_peak0 = stats[1]["Maximum memory usage peak"]["player_0"]
    stat_win_rate1 = stats[1]["Frequency of win"]["player_1"]
    stat_maximum_time1 = stats[1]["Maximum time to play"]["player_1"]
    stat_maximum_peak1 = stats[1]["Maximum memory usage peak"]["player_1"]
    stat_draw_win_rate = stats[1]["Frequency of draw"]["player_0"]
    assert stat_win_rate0 > minimal_win_rate0
    assert stat_win_rate1 > minimal_win_rate1 and stat_win_rate1 < minimal_win_rate0
    assert stat_draw_win_rate > minimal_draw_rate
    assert stat_maximum_time0 < maximum_time
    assert stat_maximum_time1 < maximum_time
    assert stat_maximum_peak0 < maximum_memory_peak
    assert stat_maximum_peak1 < maximum_memory_peak
    return

### Testing SmartAgent against WeightedRandomAgent, SmartAgent plays first: checking 
### ML-Arena requirements and statistical superiority of SmartAgent

def test_Smart_vs_Weighted_first():
    stats=gf.connect4_game_with_stats(number_of_games, sa.SmartAgent, rnda.WeightedRandomAgent)
    minimal_win_rate = 0.9
    maximum_time = 2.8
    maximum_memory_peak = 364*10e6
    stat_win_rate0 = stats[1]["Frequency of win"]["player_0"]
    stat_maximum_time0 = stats[1]["Maximum time to play"]["player_0"]
    stat_maximum_peak0 = stats[1]["Maximum memory usage peak"]["player_0"]
    assert stat_win_rate0 > minimal_win_rate
    assert stat_maximum_time0 < maximum_time
    assert stat_maximum_peak0 < maximum_memory_peak
    return


### Testing SmartAgent against WeightedRandomAgent, SmartAgent plays second: checking 
### ML-Arena requirements and statistical superiority of SmartAgent

def test_Smart_vs_Weighted_second():
    stats=gf.connect4_game_with_stats(number_of_games, rnda.WeightedRandomAgent, sa.SmartAgent)
    minimal_win_rate = 0.9
    maximum_time = 2.8
    maximum_memory_peak = 364*10e6
    stat_win_rate1 = stats[1]["Frequency of win"]["player_1"]
    stat_maximum_time1 = stats[1]["Maximum time to play"]["player_1"]
    stat_maximum_peak1= stats[1]["Maximum memory usage peak"]["player_1"]
    assert stat_win_rate1 > minimal_win_rate
    assert stat_maximum_time1 < maximum_time
    assert stat_maximum_peak1 < maximum_memory_peak
    return

### Testing SmartAgent against RandomAgent, SmartAgent plays first: checking 
### ML-Arena requirements and statistical superiority of SmartAgent

def test_Smart_vs_Random_first():
    stats=gf.connect4_game_with_stats(number_of_games, sa.SmartAgent, rnda.RandomAgent)
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


### Testing SmartAgent against RandomAgent, SmartAgent plays second: checking 
### ML-Arena requirements and statistical superiority of SmartAgent

def test_Smart_vs_Random_second():
    stats=gf.connect4_game_with_stats(number_of_games, rnda.RandomAgent, sa.SmartAgent)
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