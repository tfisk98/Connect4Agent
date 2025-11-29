import random

from loguru import logger


from smart_agent.py import SmartAgent, logger, random


class EnhancedSmartAgent(SmartAgent):
    """Smart Agent with enhanced tactics like detecting double threats and order of column preferences"""
         
    def __init__(self, env, player_name=None):
        """
        Initialize the enhanced smart agent

        Parameters:
            env: PettingZoo environment
            player_name: Optional string name for the agent (for display)
        """
        super().__init__(env, player_name)

    def choose_action(self, observation, moves = None, reward=0.0, terminated=False, truncated=False, info=None, action_mask=None):
        """
        Choose an action using rule-based strategy

        Strategy priority:
        1. Win if possible
        2. Block opponent from winning
        3. Play center if available
        4. Random valid move

        Returns : 
        None if there is no action to play, an integer between 0 and 6 otherwise
        """

        action=None
        if terminated or truncated :
            print("Truncated")
            return action
        elif action_mask == None :
            action_mask=observation["action_mask"]
        else :
            mask=action_mask
        
        # Get valid actions
        valid_actions = self._get_valid_actions(action_mask)

        # Rule 1: Try to win
        winning_move = self._find_winning_move(observation, valid_actions, channel=0)
        if winning_move is not None:
            logger.success(f"{self.name}: WINNING MOVE -> column {winning_move}")
            return winning_move
        
        # Rule 2: Block opponent
        blocking_move = self._find_winning_move(observation, valid_actions, channel=1)
        if blocking_move is not None:
            logger.warning(f"{self.name}: BLOCKING -> column {blocking_move}")
            return blocking_move


       # Rule 3: Create double threat (TODO - Advanced)
       # A double threat is when you create two ways to win at once
        double_threat = self._creates_double_threat(observation, valid_actions, channel=0 )
        if double_threat is not None:
            logger.warning(f"{self.name}: CREATE DOUBLE THREAT -> column {double_threat}")
            return double_threat
        
        #Rule 4: Detect double threat
        double_threat = self._creates_double_threat(observation, valid_actions, channel=1 )
        if double_threat is not None:
            logger.warning(f"{self.name}: DETECTED DOUBLE THREAT -> column {double_threat}")
            return double_threat
       
        #Rule 5 : Default ordering choice  
        center_preference = [3, 2, 4, 1, 5, 0, 6]
        for col in center_preference:
            if col in valid_actions:
                logger.warning(f"{self.name}: COLUMN PREFERENCE -> column {col}")
                return col
        
        
        #Rule 3: Prefer center
        #if 3 in valid_actions:
        #    logger.info(f"{self.name}: CENTER PREFERENCE -> column 3")
        #    return 3

        # Rule 4: Random fallback
        logger.debug(f"{self.name}: RANDOM -> column {action}")
        return random.choice(valid_actions)   
     


    def _creates_double_threat(self, observation, valid_actions, channel):
         """
        Looks for a column col that creates two separate winning threats

        A double threat is unbeatable because opponent can only block one.

        Parameters : 
            observation : state of the game, especially for the boards
            valid_actions : list of legal columns and the columns to be checked
            channel : current player (0) or opponent(1)

        Returns:
            col if a move creates a double threat, None otherwise
        """
         
         board = observation['observation']
         for col in valid_actions: 
              if self._detects_double_threat(board, col, channel) :
                   return col
              
         return None 
    

    def _detects_double_threat(self, board, col, channel):
        """
        Check if playing column col creates two separate winning threats.

        Parameters : 
            board : board to place the token in 
            col : column of the tested token 
            channel : current player (0) or opponent(1)

        Returns:
            True if move creates double threat, False otherwise
        """
        # TODO: This is advanced - implement if you have time
        # Hint: After placing piece, count how many ways you can win next turn

        row = self._get_next_row(board= board, col=col)
        if row >= 2:
            if self._check_win_from_position(board, row -1, col, channel ) and self._check_win_from_position(board, row -2, col, channel ) :
                return True
        if col <= 2 :
            board[col, row] = 1
            if self._check_win_from_position(board, row, col, channel ) and self._check_win_from_position(board, row, col + 4, channel ) :
                board[col, row] = 0
                return True
            board[col, row] = 0
        #if row >= 4 and col <= 2 : 
        #    if self._check_win_from_position(board, row, col, channel ) and self._check_win_from_position(board, row-4, col + 4, channel ) :
        #        return True
        return False 