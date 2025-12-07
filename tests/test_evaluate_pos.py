### Working directory must be the parent of this file's directory

import sys
import os
sys.path.append(os.getcwd())


from src.connect4_agent.minimax_agent import MinimaxAgent
from src.connect4_agent.evaluate_pos import *

import src.connect4_agent.game_facilities as gf

from pettingzoo.classic import connect_four_v3



def test_has_won():
    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.full_game0)
    board=env.last()[0]["observation"]

    start = time.time()
    player_channel = 1
    assert (has_won(board, player_channel) == True )
    stop = time.time() 
    print("has_won 1 Win :", stop - start)

    start = time.time()
    player_channel = 0
    assert (has_won(board, player_channel) == False )
    stop = time.time() 
    print("has_won 1 Lose :", stop - start)

    start = time.time()
    player_channel = 1
    assert (has_won2(board, player_channel) == True )
    stop = time.time() 
    print("has_won 2 Win:", stop - start)

    start = time.time()
    player_channel = 0
    assert (has_won2(board, player_channel) == False )
    stop = time.time() 
    print("has_won 2 Lose:", stop - start)


    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.full_game1)
    board=env.last()[0]["observation"]

    start = time.time()
    player_channel = 1
    assert (has_won2(board, player_channel) == True )
    stop = time.time() 
    print("has_won 2 Win:", stop - start)

    start = time.time()
    player_channel = 0
    assert (has_won2(board, player_channel) == False )
    stop = time.time() 
    print("has_won 2 Lose:", stop - start)

    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.full_game2)
    board=env.last()[0]["observation"]

    start = time.time()
    player_channel = 1
    assert (has_won2(board, player_channel) == True )
    stop = time.time() 
    print("has_won 2 Win:", stop - start)

    start = time.time()
    player_channel = 0
    assert (has_won2(board, player_channel) == False )
    stop = time.time() 
    print("has_won 2 Lose:", stop - start)

    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.full_game3)
    board=env.last()[0]["observation"]

    start = time.time()
    player_channel = 1
    assert (has_won2(board, player_channel) == True )
    stop = time.time() 
    print("has_won 2 Win:", stop - start)

    start = time.time()
    player_channel = 0
    assert (has_won2(board, player_channel) == False )
    stop = time.time() 
    print("has_won 2 Lose:", stop - start)

    env.close()
    return

test_has_won()


def test_count_three_in_row():
    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.connect_threes)
    board=env.last()[0]["observation"]

    start = time.time()
    player_channel = 0
    assert count_three_in_row(board, player_channel) == 2
    stop = time.time() 
    print("check threes 1 :", stop - start)

    start = time.time()
    player_channel = 1
    assert count_three_in_row(board, player_channel) == 1
    stop = time.time() 
    print("check threes 1 :", stop - start)
    return


def test_count_two_in_row():
    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.connect_twos)
    board=env.last()[0]["observation"]

    start = time.time()
    player_channel = 0
    assert count_two_in_row(board, player_channel) == 3
    stop = time.time() 
    print("check twos 1 :", stop - start)


    start = time.time()
    player_channel = 1
    assert count_two_in_row(board, player_channel) == 2
    stop = time.time() 
    print("check twos 1 :", stop - start)

    env.close()
    return
    

def test_count_center():
    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.full_center)
    board=env.last()[0]["observation"]

    player_channel = 0
    assert count_pieces_in_center(board, player_channel) == 2

    player_channel = 1
    assert count_pieces_in_center(board, player_channel) == 3 

    env.close()
    return


def test_evaluate_position():
    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.full_game0)
    board=env.last()[0]["observation"]

    player_channel = 0
    assert evaluate_position(board, player_channel) == -10000

    player_channel = 1 
    assert evaluate_position(board, player_channel) == 10000


    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.connect_twos)
    board=env.last()[0]["observation"]

    print("Board :", board[:,:,player_channel])

    assert evaluate_position(board, player_channel) == 9
    
    player_channel = 0

    print("Board :", board[:,:,player_channel])

    assert evaluate_position(board, player_channel) == 6


    env = connect_four_v3.env(render_mode=None) 
    env.reset(seed=42)
    agent0=MinimaxAgent(env)
    gf.generate_state(env, gf.full_center)
    board=env.last()[0]["observation"]

    assert evaluate_position(board, player_channel) == 6

    env.close()
    return


