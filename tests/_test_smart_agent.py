import sys
import os
sys.path.append(os.getcwd())


from src.agents.smart_agent import SmartAgent
from pettingzoo.classic import connect_four_v3


from src.game_facilities import generate_state

import numpy as np

#env = connect_four_v3.env(render_mode="human") # ou render_mode="rdb_array" ou bien None

#env.reset(seed=42)
agent0=SmartAgent(env,env.agents[0])

###### Valid_actions 

def test_valid_actions() :
    
    action_mask_1 = [1,1,1,1,1,1,1]
    valid_actions_1 = agent0._get_valid_actions(action_mask_1)


    action_mask_2 = [1,0,0,1,0,1,1]
    valid_actions_2 = agent0._get_valid_actions(action_mask_2)


    assert valid_actions_1 == [0,1,2,3,4,5,6] and valid_actions_2 == [0,3,5,6]

######## Test : _Get_next_row


def test_get_next_row():
    # Empty board - piece goes to bottom
    board = np.zeros((6, 7, 2))
    assert agent0._get_next_row(board, 3) == 5

    # Column with one piece - next piece goes on top
    board[5, 3, 0] = 1
    assert agent0._get_next_row(board, 3) == 4


    # Column with 5 pieces - next piece goes on the top row
    board[5, 4, 0] = 1
    board[4, 4, 1] = 1
    board[3, 4, 0] = 1
    board[2, 4, 0] = 1
    board[1, 4, 0] = 1
    assert agent0._get_next_row(board, 4) == 0


    # Filling a column and checking the function keeps up every step
    board[5, 6, 0] = 1
    assert agent0._get_next_row(board, 6) == 4
    board[4, 6, 1] = 1
    assert agent0._get_next_row(board, 6) == 3
    board[3, 6, 0] = 1
    assert agent0._get_next_row(board, 6) == 2
    board[2, 6, 1] = 1
    assert agent0._get_next_row(board, 6) == 1
    board[1, 6, 0] = 1
    assert agent0._get_next_row(board, 6) == 0
    board[0, 6, 1] = 1
    assert agent0._get_next_row(board, 6) == None



######## Checking find the winning move :

def test_check_win_from_position():
    ##### New Board. The agent can't find a winning move 
    board = np.zeros((6, 7, 2))
    row = 0
    col = 5
    channel = 1
    assert agent0._check_win_from_position(board, row, col, channel) == False 

    ##### Center column filled with the players pieces. Will he find the win ? 

    board = np.zeros((6, 7, 2))
    board[5, 3, 0] = 1
    board[4, 3, 0] = 1
    board[3, 3, 0] = 1
    row = 2
    col = 3
    channel = 0
    assert agent0._check_win_from_position(board, row, col, channel) == True



    ##### 3rd lign filled with the opponents pieces. Will he block the loss ? 

    board = np.zeros((6, 7, 2))
    board[2, 3, 1] = 1
    board[2, 4, 1] = 1
    board[2, 6, 1] = 1
    row = 2
    col = 5
    channel = 1
    assert agent0._check_win_from_position(board, row, col, channel) == True


    #####

    ##### No win for nobody. Will he spot there's nothing in there ? 

    board = np.zeros((6, 7, 2))
    board[2, 3, 1] = 1
    board[2, 4, 1] = 0
    board[2, 5, 1] = 1
    row = 2
    col = 6
    channel = 1
    assert agent0._check_win_from_position(board, row, col, channel) == False 


    ##### Ascending Diagonal win for the agent 

    board = np.zeros((6, 7, 2))
    board[1, 2, 0] = 1
    board[2, 3, 0] = 1
    board[4, 5, 0] = 1
    row = 3
    col = 4
    channel = 0
    assert agent0._check_win_from_position(board, row, col, channel) == True

    ##### Descending Diagonal win for the agent 

    board = np.zeros((6, 7, 2))
    board[4, 3, 0] = 1
    board[2, 1, 0] = 1
    board[1, 0, 0] = 1
    row = 3
    col = 2
    channel = 0
    assert agent0._check_win_from_position(board, row, col, channel) == True

    ##### Agent is observing the wrong board

    board = np.zeros((6, 7, 2))
    board[4, 3, 0] = 1
    board[2, 1, 0] = 1
    board[1, 0, 0] = 1
    row = 3
    col = 2
    channel = 1
    assert agent0._check_win_from_position(board, row, col, channel) == False


######## Find winning move. Agent should be playing col 2 

def test_find_winning_move():

    ### Test case 1 : Winnning start against a random agent
    action_list1=[3,0,3,2,3,4]

    env = connect_four_v3.env(render_mode=None)

    env.reset(seed=42)
    agent0=SmartAgent(env,env.agents[0])
    generate_state(env, action_list1)
    observation, reward, termination, truncation, info = env.last()
    action_mask = [1,1,1,1,1,1,1]
    valid_actions = agent0._get_valid_actions(action_mask)

    channel = 1
    blocking_move = agent0._find_winning_move(observation, valid_actions, channel)

    channel = 0 
    winning_move = agent0._find_winning_move(observation, valid_actions, channel)

    assert winning_move == 3 and blocking_move == None



    ### Limit 1 : Conceiding early two way win against Smart Agents. Can occur if preference is implemented and 
    ### detection of two way wins not 

    action_list2=[3,3,3,3,3,3,2,5,1]

    env = connect_four_v3.env(render_mode=None)

    env.reset(seed=42)
    agent0=SmartAgent(env,env.agents[0])
    generate_state(env, action_list1)
    observation, reward, termination, truncation, info = env.last()
    action_mask = [1,1,1,0,1,1,1]
    valid_actions = agent0._get_valid_actions(action_mask)
    
    channel = 0
    blocking_move = agent0._find_winning_move(observation, valid_actions, channel)

    env.step(blocking_move)
    observation, reward, termination, truncation, info = env.last()

    channel = 1
    winning_move = agent0._find_winning_move(observation, valid_actions, channel)

    assert blocking_move == 0 and winning_move == 4

    observation, reward, termination, truncation, info = env.last()

    observation['observation'] = np.zeros((6, 7, 2))
    observation['observation'][4, 3, 0] = 1
    observation['observation'][2, 1, 0] = 1
    observation['observation'][1, 0, 0] = 1
    observation['observation'][5, 2, 0] = 1
    observation['observation'][4, 2, 0] = 1
    channel = 0

    action_mask = [1,1,1,1,1,1,1]
    valid_actions = agent0._get_valid_actions(action_mask)

    assert agent0._find_winning_move(observation, valid_actions, channel) == 2


    ####### Wrong agent. No winning move should be detected

    observation, reward, termination, truncation, info = env.last()

    observation['observation'] = np.zeros((6, 7, 2))
    observation['observation'][4, 3, 0] = 1
    observation['observation'][2, 1, 0] = 1
    observation['observation'][1, 0, 0] = 1
    observation['observation'][5, 2, 0] = 1
    observation['observation'][4, 2, 0] = 1
    channel = 1

    action_mask = [1,1,1,1,1,1,1]
    valid_actions = agent0._get_valid_actions(action_mask)

    assert agent0._find_winning_move(observation, valid_actions, channel) == None


    ###### Real Game test : 

    observation, reward, termination, truncation, info = env.last()

    observation['observation'] = np.zeros((6, 7, 2))
    observation['observation'][5, 0, 0] = 1
    observation['observation'][4, 0, 0] = 1
    observation['observation'][5, 1, 1] = 1
    observation['observation'][4, 1, 0] = 1
    observation['observation'][5, 2, 0] = 1
    observation['observation'][4, 2, 0] = 1
    observation['observation'][3, 2, 0] = 1
    observation['observation'][5, 3, 0] = 1
    observation['observation'][4, 3, 1] = 1
    observation['observation'][3, 3, 1] = 1
    observation['observation'][5, 4, 1] = 1
    observation['observation'][4, 4, 0] = 1
    observation['observation'][3, 4, 1] = 1
    observation['observation'][2, 4, 1] = 1
    observation['observation'][1, 4, 0] = 1
    observation['observation'][5, 5, 1] = 1
    observation['observation'][4, 5, 1] = 1
    observation['observation'][3, 5, 0] = 1
    observation['observation'][2, 5, 0] = 1
    observation['observation'][1, 5, 0] = 1
    observation['observation'][0, 5, 1] = 1
    observation['observation'][3, 3, 1] = 1
    observation['observation'][5, 2, 1] = 1
    channel = 0

    action_mask = [1,1,1,1,1,1,1]
    valid_actions = agent0._get_valid_actions(action_mask)

    assert agent0._find_winning_move(observation, valid_actions, channel) == 2

