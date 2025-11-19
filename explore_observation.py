from pettingzoo.classic import connect_four_v3
import numpy as np

def print_board(observation):
    """
    Print a human-readable version of the board

    observation: numpy array of shape (6, 7, 2)
        observation[:,:,0] = current player's pieces
        observation[:,:,1] = opponent's pieces
    """
    # TODO: Implement this function
    # Hint: Loop through rows and columns
    # Use symbols like 'X', 'O', and '.' for current player, opponent, and empty

    board_0 = observation['observation'][:,:,0]
    board_0 = np.where(board_0 == 1, 'X','0')
    board_0 = '\n'.join(" ".join(str(j) for j in i) for i in board_0)
    print("Board_0 : \n",board_0)

    board_1 = observation['observation'][:,:,1]
    board_1 = np.where(board_1 == 1, 'X','0')
    board_1 = '\n'.join(" ".join(str(j) for j in i) for i in board_1)
    print("Board_1 : \n",board_1)
    


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