"""
A simple random agent
"""

import numpy as np
import random as rnd

class RandomAgent:
    """
    A simple agent that chooses randomly and uniformly a legal play.
    """

    def __init__(self, env, player_name=None):
        """
        Initialize the random agent

        Parameters:
            env: PettingZoo environment
            player_name: Optional string name for the agent (for display)
        """
        self.env=env
        self.name=player_name
        self.action_space=self.env.action_space(self.env.agents[0])
        return

    def choose_action(self, observation, moves = None, reward=0.0, terminated=False, truncated=False, info=None, action_mask=None):
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
            action=self.action_space.sample(mask)
        return action
    
    def choose_action_manual(self, observation, reward=0.0, terminated=False, truncated=False, info=None, action_mask=None):
        """
        Choose a random valid action without using .sample()

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
            legal_action=[]
            for i,legal in enumerate(mask) :
                if legal==1 :
                    legal_action.append(i)
            action=rnd.choice(legal_action)
        return action 
    

class WeightedRandomAgent(RandomAgent):
    """
    Random agent that prefers center columns
    """

    def __init__(self, env, player_name=None):
        """
        Initialize the random agent

        Parameters:
            env: PettingZoo environment
            player_name: Optional string name for the agent (for display)
        """
        super().__init__(env, player_name)
        return
    

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