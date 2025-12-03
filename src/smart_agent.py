import random

from loguru import logger


CONNECT_FOUR = 4

class SmartAgent:

    def __init__(self, env, player_name=None):
        """
        Initialize the smart agent

        Parameters:
            env: PettingZoo environment
            player_name: Optional name for the agent
        """
        self.env = env
        self.action_space = env.action_space(env.agents[0])
        self.name = player_name or "SmartAgent"

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
        
        #Rule 3: Prefer center
        if 3 in valid_actions:
            logger.info(f"{self.name}: CENTER PREFERENCE -> column 3")
            return 3

        # Rule 4: Random fallback
        logger.debug(f"{self.name}: RANDOM -> column {action}")
        return random.choice(valid_actions)
    
    def _get_valid_actions(self, action_mask):
        """
        Get list of valid column indices

        Parameters:
            action_mask: numpy array (7,) with 1 for valid, 0 for invalid

        Returns:
            list of valid column indices
        """
        # TODO: Implement this
        valid_cols = []
        for col in range(len(action_mask)) :
            if action_mask[col] == 1 : 
                valid_cols.append(col)

        return valid_cols 
    
    def _find_winning_move(self, observation, valid_actions, channel):
        """
        Find a move that creates 4 in a row for the specified player

        Parameters:
            observation: numpy array (6, 7, 2) - current board state
            valid_actions: list of valid column indices
            channel: 0 for current player, 1 for opponent

        Returns:
            column index (int) if winning move found, None otherwise
        """
        # TODO: For each valid action, check if it would create 4 in a row
        # Hint: Simulate placing the piece, then check for wins

        board = observation['observation']

        # winning_cols = [] option of we want to get all winning cols, for example, for when the opponent plays 
    

        for col in valid_actions: 
            row = self._get_next_row(board, col)
            if self._check_win_from_position(board, row, col, channel) :
                return col

        return None 
    
    def _get_next_row(self, board, col):
        """
        Find which row a piece would land in if dropped in column col

        Parameters:
            board: numpy array (6, 7, 2)
            col: column index (0-6)

        Returns:
            row index (0-5) if space available, None if column full
        """
        # TODO: Implement this
        # Hint: Start from bottom row (5) and go up
        # A position is empty if board[row, col, 0] == 0 and board[row, col, 1] == 0
        
        for row in range(5,-1,-1):
            if (board[row, col, 0] == 0 and board[row, col, 1] == 0): 
                return row

        print("This Column is full") 
        return None 
    
    def _check_win_from_position(self, board, row, col, channel):
        """
        Check if placing a piece at (row, col) would create 4 in a row

        Parameters:
            board: numpy array (6, 7, 2)
            row: row index (0-5)
            col: column index (0-6)
            channel: 0 or 1 (which player's pieces to check)

        Returns:
            True if this position creates 4 in a row/col/diag, False otherwise
        """
        # TODO: Check all 4 directions: horizontal, vertical, diagonal /, diagonal \
        # Hint: Count consecutive pieces in both directions from (row, col)
        
        start_count = 1

        token_count = start_count 
        token_row = row 
        token_col = col
        player_board = board[:,:,channel]

        # Vertical

        if row < 3 :
            row += 1
            while (row <= 5 and player_board[row, col] == 1): 
                token_count += 1
                if token_count == 4 : 
                    return True 
                row += 1
                
            token_count= start_count 
            row = token_row

        # Horizontal

        #Left
        col = token_col - 1
        
        while col >= 0 and player_board[row, col] == 1 : 
            token_count += 1 
            if token_count == 4 : 
                    return True 
            col -= 1

        col = token_col + 1 

        # Right

        while col <= 6 and player_board[row, col] == 1 : 
            token_count += 1 
            if token_count == 4 : 
                    return True 
            col += 1

        #col = token_col
        token_count = 1

        # Ascending Diagonal


        #Left

        col = token_col - 1
        row = token_row - 1

        while (row >= 0 and col >= 0 and player_board[row, col] == 1 ) : 
            token_count += 1 
            if token_count == 4 : 
                    return True 
            col -= 1
            row -= 1 

        col = token_col + 1
        row = token_row + 1 

        #Right

        while (row <= 5 and col <= 6 and player_board[row, col] == 1 )  : 
            token_count += 1 
            if token_count == 4 : 
                    return True 
            col += 1
            row += 1 

        token_count = 1


        # Descending Diagonal


        #Left

        col = token_col + 1
        row = token_row - 1

        while (row >= 0 and col <= 6 and player_board[row, col] == 1 ) : 
            token_count += 1 
            if token_count == 4 : 
                    return True 
            col += 1
            row -= 1 

        col = token_col - 1
        row = token_row + 1 

        #Right

        while (row <= 5 and col >= 0 and player_board[row, col] == 1 )  : 
            token_count += 1 
            if token_count == 4 : 
                    return True 
            col -= 1
            row += 1 

        #col = token_col
        #row = token_row

        return False 
    
    def choose_action_manual(self, observation, moves = None, reward=0, terminated=False, truncated=False, info=None, action_mask=None):

        """
        Same name as twin function in random_player to be able to play against random_player that plays only legal move
        """
        action=None
        if terminated or truncated :
            print("Truncated")
            return action
        elif action_mask == None :
            mask=observation["action_mask"]
        else :
            mask=action_mask
        return self.choose_action(observation, moves, reward, terminated, truncated, info, action_mask)



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


            board[col + 1, row] = 1
            if self._check_win_from_position(board, row, col, channel ) and self._check_win_from_position(board, row, col + 4, channel ) :
                board[col, row] = 0
                return True
            board[col, row] = 0
        #if row >= 4 and col <= 2 : 
        #    if self._check_win_from_position(board, row, col, channel ) and self._check_win_from_position(board, row-4, col + 4, channel ) :
        #        return True
        return False 