import sys
import os
sys.path.append(os.getcwd())


from src.agents.smart_agent import SmartAgent
from pettingzoo.classic import connect_four_v3


from src.game_facilities import generate_state, print_board

import numpy as np

env = connect_four_v3.env(render_mode="human") # ou render_mode="rdb_array" ou bien None

env.reset(seed=42)
agent0=SmartAgent(env,env.agents[0])

###### Valid_actions 

def test_valid_actions() :
    #Start of the game: all columns should be considered valid
    
    action_mask_1 = [1,1,1,1,1,1,1]
    valid_actions_1 = agent0._get_valid_actions(action_mask_1)

    #Middle of the : only column corresponding to indexes with a value of 1
    #  in the action_mask should be selected as valid

    action_mask_2 = [1,0,0,1,0,1,1]
    valid_actions_2 = agent0._get_valid_actions(action_mask_2)


    assert valid_actions_1 == [0,1,2,3,4,5,6] and valid_actions_2 == [0,3,5,6]

######## Test : _Get_next_row


def test_get_next_row():
    # Empty board - piece goes to bottom (row == 5)
    board = np.zeros((6, 7, 2))
    assert agent0._get_next_row(board, 3) == 5

    # An agent drops a token in Column 3 - next piece goes on top (row == 4)
    board[5, 3, 0] = 1
    assert agent0._get_next_row(board, 3) == 4


    # Column 4 is filled with 5 pieces - agent_1's token shopuld be placed on the top row 
    # (row == 0)
    board[5, 4, 0] = 1
    board[4, 4, 1] = 1
    board[3, 4, 0] = 1
    board[2, 4, 1] = 1
    board[1, 4, 0] = 1
    assert agent0._get_next_row(board, 4) == 0


    # Synthesis of previous tests 
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

    # Column 6 is now full. Agent_1 should not be allowed to play in there (row == None)
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

    ##### Center column filled with the players pieces. Will agent_0 find a win ? 

    board = np.zeros((6, 7, 2))
    board[5, 3, 0] = 1
    board[4, 3, 0] = 1
    board[3, 3, 0] = 1
    row = 2
    col = 3
    channel = 0
    assert agent0._check_win_from_position(board, row, col, channel) == True



    ##### 3rd lign filled with a non-contiguous collection of opponent's pieces. Will agent_0 block agent_1's connect_4 ? 


    board = np.zeros((6, 7, 2))
    board[2, 3, 1] = 1
    board[2, 4, 1] = 1
    board[2, 6, 1] = 1
    row = 2
    col = 5
    channel = 1 # checking agent_1's board
    assert agent0._check_win_from_position(board, row, col, channel) == True


    #####

    ##### No win for nobody, as agent_0's and agent_1's pieces are mixed together. Will agent_0 think there's a win in there ? 

    board = np.zeros((6, 7, 2))
    board[2, 3, 1] = 1
    board[2, 4, 0] = 1
    board[2, 5, 1] = 1
    row = 2
    col = 6
    channel = 1
    assert agent0._check_win_from_position(board, row, col, channel) == False 


    ##### Ascending Diagonal win for agent_0 in coordinates (3,4)

    board = np.zeros((6, 7, 2))
    board[1, 2, 0] = 1
    board[2, 3, 0] = 1
    board[4, 5, 0] = 1
    row = 3
    col = 4
    channel = 0
    assert agent0._check_win_from_position(board, row, col, channel) == True

    ##### Descending Diagonal win for agent_0 in coordinates (3,2)

    board = np.zeros((6, 7, 2))
    board[4, 3, 0] = 1
    board[2, 1, 0] = 1
    board[1, 0, 0] = 1
    row = 3
    col = 2
    channel = 0
    assert agent0._check_win_from_position(board, row, col, channel) == True

    ##### Agent is observing the wrong board. Will he detect nothing in (3,2) ?

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

    ### All tests take into account the structure, way it takes decisions of the agents and are realistic game scenarioss

    ### Test case 1 : Winnning start against a random agent.
    """ 
    The SmartAgent, following his center preference, arrives at a winning position turn 7 against another RandomAgent, who dispersed
    his tokens randomly without spotting the vertical 'connect 4' threat of the SmartAgent.
    test 1.1 : Will the play center because of its center preference (winning_move == None), or will it spot the potential
    connect 4 (winning_move == 3) ?
    test 1.2 : Will it see that the opponent doesn't threaten anything (blocking_move == None), or will it spot a non-existing
    threat (blocking_move == 'int') ?  
    """
    action_list1=[3,0,3,2,3,4]

    env = connect_four_v3.env(render_mode=None)

    env.reset(seed=42)
    agent0=SmartAgent(env,env.agents[0])
    generate_state(env, action_list1)
    observation, reward, termination, truncation, info = env.last()
    action_mask = [1,1,1,1,1,1,1]
    valid_actions = agent0._get_valid_actions(action_mask)

    #print_board(observation, agent0, action=None, is_print=True)

    print_board(observation, "agent0", action=None, is_print=True)

    #test 1.1
    channel = 0 
    winning_move = agent0._find_winning_move(observation, valid_actions, channel)
    print("winning_move :", winning_move)

    #test 1.2
    channel = 1
    blocking_move = agent0._find_winning_move(observation, valid_actions, channel)
    print("blocking_move :", blocking_move)

    assert winning_move == 3 and blocking_move == None



    ### Limit 1 : Conceiding early two way win against Smart Agents. Can occur if preference is implemented and 
    ### detection of two way wins not 
    """
    In a game between two SmartAgents, agent_1 managed to put in place a two-way line win possibility. Following its implementation 
    agent_0 only managed to detect it once three tokens of agent_1 were connected and so could not prevent it.
    test 2.1 : What is supposed to happen is that agent_0 is supposed to 'block' the 'connect 4' picking the left-most column, here column 0. 
    test 2.2 : In response to which agent_1 is supposed to spot that column 4 offers the win and select that way. 
    """

    action_list2=[3,3,3,3,3,3,2,5,1]
    print("len(action_list) :", len(action_list2))

    env = connect_four_v3.env(render_mode=None)

    env.reset(seed=42)
    agent0=SmartAgent(env,env.agents[0])
    agent1= SmartAgent(env, env.agents[1])
    generate_state(env, action_list2)
    observation, reward, termination, truncation, info = env.last()
    action_mask = [1,1,1,0,1,1,1]
    valid_actions = agent0._get_valid_actions(action_mask)

    print_board(observation, "agent0", action=0, is_print=True)
    
    #test 2.1
    channel = 1
    blocking_move = agent1._find_winning_move(observation, valid_actions, channel)
    print("blocking_move :", blocking_move)
    #print("blocking_move :", blocking_move)
    env.step(blocking_move)
    observation, reward, termination, truncation, info = env.last()

    print_board(observation, "agent1", action=None, is_print=True)

    #print_board(observation, agent1, action=None, is_print=True)
    #test 2.2
    channel = 0
    winning_move = agent0._find_winning_move(observation, valid_actions, channel)
    print("winning_move :", winning_move)

    assert blocking_move == 0 and winning_move == 4

    ###### Real Game test : 

    """
    Real advanced position in a game between two RandomAgents where both failed to finc the winning column 3. 
    """

    action_list3=[3,1,0,2,0,4,1,3,2,5,2,5,4,6,5,4,5,4,5,3,4,5]

    env = connect_four_v3.env(render_mode=None)

    env.reset(seed=42)
    agent0=SmartAgent(env,env.agents[0])
    generate_state(env, action_list3)
    observation, reward, termination, truncation, info = env.last()
    action_mask = [1,1,1,1,1,0,1]
    valid_actions = agent0._get_valid_actions(action_mask)

    print_board(observation, "agent0", action=None, is_print=True)

    channel = 0
    assert agent0._find_winning_move(observation, valid_actions, channel) == 3



#test_valid_actions()
#test_get_next_row()
#test_check_win_from_position()
#test_find_winning_move()