from pettingzoo.classic import connect_four_v3
import numpy as np

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

    
