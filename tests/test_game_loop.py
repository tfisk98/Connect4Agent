""" 
Testing the main utilities of game_loop.py. You can refer to the 
annex of Readm.md to visualize the state of game represented 
by predefined list of Connect4 actions in game_loop.py.
The test are designed to be executed with the library pytest.
WARNING : Working directory must be the parent of this file's directory
"""

### Working directory must be the parent of this file's directory

import sys
import os
sys.path.append(os.getcwd())

from pettingzoo.classic import connect_four_v3
import src.random_agent as rnda
import src.game_loop as gl

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
    gl.generate_state(env, action_list1)
    observation, reward, termination, truncation, info = env.last()
    action=3
    function_board1=gl.print_board(observation, env.agents, "player_2", action, is_print=False)

    env.reset(seed=42)
    gl.generate_state(env, action_list2)
    observation, reward, termination, truncation, info = env.last()
    action=0
    function_board2=gl.print_board(observation, env.agents, "player_2", action, is_print=False)

    env.close()

    assert function_board1==expected_board1 and function_board2==expected_board2

# Testing testing_strategy


def test_testing_strategy() :
    action_list=[]
    expected_action= 3
    assert gl.testing_strategy( action_list, rnda.WeightedRandomAgent, expected_action )
    return
