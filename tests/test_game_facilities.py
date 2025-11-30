""" 
Testing the main functions of game_facilities.py. You can refer to the 
annex of Readm.md to visualize the state of game represented 
by predefined list of Connect4 actions in game_facilities.py.
The test are designed to be executed with the library pytest.
WARNING : Working directory must be the parent of this file's directory
"""

### Working directory must be the parent of this file's directory

import sys
import os
sys.path.append(os.getcwd())

from pettingzoo.classic import connect_four_v3
import src.random_agent as rnda
import src.game_facilities as gf

# Testing print_board

def test_print_board() : 
    expected_board1  = ". . . . . . . \n" 
    expected_board1 += ". . . . . . . \n" 
    expected_board1 += ". . . . . . . \n" 
    expected_board1 += ". . . . . . . \n" 
    expected_board1 += ". . . . . . . \n" 
    expected_board1 += "X O X O . . . \n" 
    action_list1=[0,1,2]

    expected_board2  = ". . . . . . . \n" 
    expected_board2 += ". . . . . . . \n" 
    expected_board2 += "O . . . . . . \n" 
    expected_board2 += "X . . . . . . \n" 
    expected_board2 += "O . . . . . . \n" 
    expected_board2 += "X . . . . . . \n" 
    action_list2=[0,0,0]

    env = connect_four_v3.env(render_mode=None)

    env.reset(seed=42)
    gf.generate_state(env, action_list1)
    observation, reward, termination, truncation, info = env.last()
    action=3
    function_board1=gf.print_board(observation, "player_1", action, is_print=False)

    env.reset(seed=42)
    gf.generate_state(env, action_list2)
    observation, reward, termination, truncation, info = env.last()
    action=0
    function_board2=gf.print_board(observation, "player_1", action, is_print=False)

    env.close()

    assert function_board1==expected_board1 and function_board2==expected_board2
    return


# Testing connect4_game_with_stats using full_game_list

def test_connect4_game_with_stats() :
    stats=gf.connect4_game_with_stats(4, None, None, 42, True)
    expected_average_turn_number = (3*7 + 8)/4
    expected_min_turn_number = 7
    expected_max_turn_number = 8
    expected_frequency_win_player0 = 3/4
    expected_frequency_draw_player0 = 0
    assert expected_average_turn_number==stats[0]["Average number of turns per game"]
    assert expected_min_turn_number==stats[0]["Minimum number of turns in a game"]
    assert expected_max_turn_number==stats[0]["Maximum number of turns in a game"]
    assert expected_frequency_win_player0==stats[1]["Frequency of win"]["player_0"]
    assert expected_frequency_draw_player0==stats[1]["Frequency of draw"]["player_0"]
    return


# Testing testing_strategy

def test_testing_strategy() :
    action_list=[]
    expected_action_list= [3]
    assert gf.testing_strategy( action_list, rnda.WeightedRandomAgent, expected_action_list )
    return