"""
Functions to help to visualize the board or 
making Connect4 games
"""


### Import

from pettingzoo.classic import connect_four_v3
import numpy as np
import tracemalloc
import time

### Functions 

def print_board(observation, agents, playing_agent, action):
    """
    Print a human-readable version of the board. 'X' will represent
    agents[0] tokens, 'O' those of it's opponent. A '.' will
    indicate en empty position.

    Parameters :
        observation: numpy array of shape (6, 7, 2)
            observation[:,:,0] = playing's tokens
            observation[:,:,1] = opponent's tokens
        agents : the list containing the name of the
        agents of the environnement
        playin_agent : the name of the agent currently
        playing
        action : the index of the column of observartion
        where the next tokens will be put

    Return : 
        None
    """

    board_0 = np.copy(observation['observation'][:,:,0])
    board_1 = observation['observation'][:,:,1]
    n_row = np.shape(board_0)[0]
    n_col = np.shape(board_0)[1]
    human_board = ""

    # Including playing_agent action in board_0 :

    for i in range(n_row-1,-1,-1) : 
         if board_0[i,action]==0 and board_1[i,action]==0 :
            board_0[ i ,action]=1
            break

    # Checking which agent is playing

    if playing_agent==agents[0] :
        check_player0 = True
    else :
        check_player0 = False 

    # Preparing information for readibbility

    board_title = "Next turn :\n"
    board_title = board_title + agents[0] + " tokens : 'X'\n" 
    board_title = board_title + agents[1] + " tokens : 'O'\n" 


    # Constructing the string representing the real board

    for i in range(n_row) :
        for j in range(n_col) :
            if board_0[i][j] == 1 :
                if check_player0 :
                    human_board+="X "
                else :
                    human_board+="O "
            elif board_1[i][j] == 1 : 
                if check_player0 :
                    human_board+="O "
                else :
                    human_board+="X "
            else : 
                human_board+=". "
        human_board+="\n"
   
    # Printing human readable state of the board

    print(board_title)
    print(human_board)
    return 
    

def setting_custom_agent(env,Custom_Agent0, Custom_Agent1) :
    """ 
    Setting the two custom agents that will play in 
    env.

    Parameters :
    env : a connect4 environement
    Custom_Agent0 : the type of the first custom agent
    Custom_Agent1 : the type of the second custom agent

    Return : 
        agent_list : the list containing the 
        two agent created (agent0 at index 0)
    """
    agent0=Custom_Agent0(env, env.agents[0])
    agent1=Custom_Agent1(env, env.agents[1])
    agent_list=[agent0, agent1]
    return agent_list


def select_current_agent(agent_list, playing_agent) :
    """ 
    Getting the custom agent object corresponding 
    to agent currently playing in the game loop.

    Parameters :
    agent_list : the list of custom agent type object 
    in the environement
    playing_agent : the name of the agent currently playing
    
    Return : 
        current_agent the custom agent playing
    """

    if agent_list[0].name==playing_agent :
        current_agent=agent_list[0]

    else :
        current_agent=agent_list[1]
    return current_agent


def Connect4_game(num_games, Custom_Agent0, Custom_Agent1, custom_render_option=False, render_option=None, seed_option=42) :
    """ 
    Make a certain number of connect4 game with the given
    agents.

    Parameters : 
        num_games : the number of game to be played
        Custom_Agent0 : the type of the first custom agent
        Custom_Agent1 : the type of the second custom agent
        custom_render_option : boolean asserting if print_board has
        to be used
        render_option : setting string for pettingzoo environment render_mode
        seed_option : a positive integer to be used as seed for 
        pettingzoo environment 

    Return :
        None
    """

    # Setting environment and agents

    env = connect_four_v3.env(render_mode=render_option)
    env.reset(seed=seed_option)
    agent_list=setting_custom_agent(env,Custom_Agent0, Custom_Agent1)

    # Gameloop

    for game in range(0,num_games) :

        print(f"\nGAME NUMBER {game+1} :\n\n")

        env.reset(seed=seed_option)

        for agent in env.agent_iter():
            observation, reward, termination, truncation, info = env.last()

            if termination or truncation:
                action = None
                if reward == 1:
                    print(f"{agent} wins!\n")
                elif reward == 0:
                    print("It's a draw!\n")
            else:
                current_agent=select_current_agent(agent_list, agent)
                action = current_agent.choose_action(observation)
                if custom_render_option :
                    print_board(observation, env.agents, agent, action)
            env.step(action)


def Connect4_game_with_data(num_games, Custom_Agent0, Custom_Agent1, seed_option=42) :
    """ 
    Make a certain number of connect4 game with the given
    agents and get data for later analysis.

    Parameters : 
        num_games : the number of game to be played
        Custom_Agent0 : the type of the first custom agent 
        Custom_Agent1 : the type of the second custom agent
        seed_option : a positive integer to be used as seed for 
        pettingzoo environment 

    Return :
        data : a tuple containing for each game another tuple 
        of the form (turn_count, data0, data1).
        turn_count is the total number of turns played during this game. 
        data0 (for the first agent) and data1 (for the second agent) are tuples 
        containing the following informations in this order: the agent result ("win", "loss" or "draw"), 
        a tuple containing the time (in second) taken by the agent to play for each turn,
        a tuple of size num_games containing the memory usage peak reached by the agent for each turn.
        Please note that we want the returned data to be immutable to prevent them to be
        mistakenly changed during their usage. Hence, a library like pandas does not 
        have been used to store sampled informations.
    """

    # Setting environment and agents

    env = connect_four_v3.env(render_mode=None)
    env.reset(seed=seed_option)
    agent_list=setting_custom_agent(env,Custom_Agent0, Custom_Agent1)

    
    # Game loop

    data=[]

    for game in range(0,num_games) :

        env.reset(seed=seed_option)

        # Setting data collectors

        data0=[ 0 for i in range(3)]
        data1=[ 0 for i in range(3)]
        turn_count=0
        time_list0=[]
        time_list1=[]
        memory_list0=[]
        memory_list1=[]

        # Playing

        for agent in env.agent_iter():
            observation, reward, termination, truncation, info = env.last()


            # Saving the result of the game
            
            if termination or truncation:
                action = None
                if reward == 1:
                    if agent=='player_0' :
                        data0[0]="win"
                        data1[0]="loss"
                    else :
                        data0[0]="loss"
                        data1[0]="win"
                       
                elif reward == 0:
                    print(f"{agent} draw!\n")
                    data0[0]="draw"
                    data1[0]="draw"


            # Playing and measuring time taken and memory usage 

            else:
                turn_count+=1
                current_agent=select_current_agent(agent_list, agent)
                tracemalloc.start()
                start_time = time.time()
                action = current_agent.choose_action(observation)
                time_used= time.time()-start_time
                memory_peak=tracemalloc.get_traced_memory()[1]
                tracemalloc.stop()

                # Saving time and memory data of this turn

                if current_agent.name==env.agents[0] :
                    time_list0.append(time_used)
                    memory_list0.append(memory_peak)

                else : 
                    time_list1.append(time_used)
                    memory_list1.append(memory_peak)

            env.step(action)
        

        # Saving the data of the current game

        data0[1]=time_list0
        data0[2]=memory_list0
        data1[1]=time_list1
        data1[2]=memory_list1
        game_data=(turn_count, tuple(data0), tuple(data1))
        data.append(game_data)
    
    data=tuple(data)
    return data