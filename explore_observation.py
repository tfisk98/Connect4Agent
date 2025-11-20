from pettingzoo.classic import connect_four_v3
import numpy as np

def print_board(observation):
    """
    Print a human-readable version of the board

    observation: numpy array of shape (6, 7, 2)
        observation[:,:,0] = current player's pieces
        observation[:,:,1] = opponent's pieces

    La ligne du bas de l'affichage correspond à la ligne du bas de la grille du puissance 4, 
    et à la ligne 0 de la matrice observation
    
    """
    # TODO: Implement this function
    # Hint: Loop through rows and columns
    # Use symbols like 'X', 'O', and '.' for current player, opponent, and empty

    board_0 = observation['observation'][:,:,0]
    board_0[0,3] = 1

    board_1 = observation['observation'][:,:,1]
    board_1[5,3] = 1

    for i in range(board_0.shape[0] -1 , -1, -1) :
        for j in range(board_0.shape[1]) :
            if board_0[i][j] == 1 :
                print('X', end='')
            elif board_1[i][j] == 1 : 
                print('O', end='')
            else : 
                print('.', end='')
        print("\n")

    for i in range(board_1.shape[0] -1 , -1, -1) :
        for j in range(board_1.shape[1]) :
            if board_1[i][j] == 1 :
                print('X', end='')
            elif board_0[i][j] == 1 : 
                print('O', end='')
            else : 
                print('.', end='')
        print("\n")

    


# TODO: Create environment
env = connect_four_v3.env()
env.reset(seed=42)

# TODO: Get first observation
for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()

    if termination or truncation:
        break

    # TODO: Print the observation structure
    print("Agent:", agent)
    print("Observation keys:", observation.keys())
    print("Observation shape:", observation['observation'].shape)
    print("Action mask:", observation['action_mask'])
    print_board(observation=observation)

    # TODO: Take a random action (column 3)
    env.step(3)
    break

env.close()