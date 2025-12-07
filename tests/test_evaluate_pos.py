### Working directory must be the parent of this file's directory

import sys
import os
sys.path.append(os.getcwd())

from pettingzoo.classic import connect_four_v3
from pettingzoo.classic import connect_four_v3
from src.connect4_agent.evaluate_pos import *
import src.connect4_agent.game_facilities as gf

### Testing has_won()
def test_has_won():

    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    gf.generate_state(env, gf.full_game0)
    board=env.last()[0]["observation"]
    player_channel = 1 
    assert (has_won(board, player_channel) == True )
    player_channel = 0
    assert (has_won(board, player_channel) == False )
    env.close()
    return

### Testing count_three_in_row()
def test_count_three_in_row():
    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    gf.generate_state(env, gf.connect_threes)
    board=env.last()[0]["observation"]
    player_channel = 0
    assert count_three_in_row(board, player_channel) == 2
    player_channel = 1
    assert count_three_in_row(board, player_channel) == 1


    env.close()
    return

### Testing count_two_in_row()
def test_count_two_in_row():
    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    gf.generate_state(env, gf.connect_twos)
    board=env.last()[0]["observation"]
    player_channel = 0
    assert count_two_in_row(board, player_channel) == 3
    player_channel = 1
    assert count_two_in_row(board, player_channel) == 2

    env.close()
    return

### Testing evaluate_position()
def test_evaluate_position():
    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    gf.generate_state(env, gf.full_game0)
    board=env.last()[0]["observation"]
    player_channel = 0
    assert evaluate_position(board, player_channel) == -10000
    player_channel = 1 
    assert evaluate_position(board, player_channel) == 10000

    env.reset(seed=42)
    gf.generate_state(env, gf.connect_twos)
    board=env.last()[0]["observation"]
    assert evaluate_position(board, player_channel) == 9
    player_channel = 0
    assert evaluate_position(board, player_channel) == 6

    env.close()
    return


