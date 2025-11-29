from src.agents.random_agent import RandomAgent
from src.agents.smart_agent import random

class WeightedRandomAgent(RandomAgent):
    """
    Random agent that prefers the center column
    """

    def __init__(self, env, player_name=None):
        """
        Initialize the random agent

        Parameters:
            env: PettingZoo environment
            player_name: Optional string name for the agent (for display)
        """
        super().__init__(env, player_name)
        
    

    def choose_action(self, observation, reward=0.0, terminated=False, truncated=False, info=None, action_mask=None):
        """
        Choose a random valid action

        Parameters:
            observation: numpy array (6, 7, 2) - current board state
            reward: float - reward from previous action
            terminated: bool - is the game over?
            truncated: bool - was the game truncated?
            info: dict - additional info
            action_mask: numpy array (7,) - which columns are valid (1) or full (0)

        Returns:
            action : None if the game is over or there is no legal play,
            or an int (0-6) - which column to play - otherwise
        """
        action=None
        if terminated or truncated :
            return action 
        
        else :
            mask=observation["action_mask"]
            if mask[3]==1 :
                action=3
            else :
                action=super().choose_action(observation, reward, terminated, truncated, info, action_mask)
        return action