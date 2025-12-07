import random
from loguru import logger

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

    def choose_action(self, observation, moves = None, reward=0.0, terminated=False, truncated=False, info=None, action_mask=None):
        """
        Choose an action using rule-based strategy

        Strategy priority:
        1. Win if possible
        2. Block opponent from winning
        3. Play center if available
        4. Random valid move

        Returns: 
        Returns: 
        None if there is no action to play, an integer between 0 and 6 otherwise
        """

        action=None
        if terminated or truncated:
        if terminated or truncated:
            print("Truncated")
            return action
        
        action_mask=observation["action_mask"]
        
        # Get valid actions
        valid_actions = self._get_valid_actions(action_mask)

        # Rule 1: Try to win
        winning_move = self._find_winning_move(observation, valid_actions, channel=0)
        if winning_move is not None:
            #logger.success("SmartAgent: WINNING MOVE -> column {winning_move}")
            return winning_move
        
        # Rule 2: Block opponent
        blocking_move = self._find_winning_move(observation, valid_actions, channel=1)
        if blocking_move is not None:
            #logger.warning("SmartAgent: BLOCKING -> column {blocking_move}")
            return blocking_move        
        
        #Rule 3: Prefer center
        if 3 in valid_actions:
            #logger.info("SmartAgent: CENTER PREFERENCE -> column 3")
            return 3

        # Rule 4: Random fallback
        #logger.debug("SmartAgent: RANDOM -> column {action}")
        action=self.action_space.sample(action_mask)
        return action
    
    def _get_valid_actions(self, action_mask):
        """
        Get the list of valid actions.

        Parameters:
            action_mask: numpy array (7,) with 1 for valid, 0 for invalid

        Returns:
            list of valid column indexes
        """
        valid_cols = []
        for col in range(len(action_mask)):
            if action_mask[col] == 1: 
                valid_cols.append(col)

        return valid_cols 
    
    def _find_winning_move(self, observation, valid_actions, channel):
        """
        Search for a winning move.
        Parameters:
            observation: numpy array (6, 7, 2) - current board state
            valid_actions: list of valid column indices
            channel: 0 for current player, 1 for opponent

        Returns:
            column index (int) if winning move found, None otherwise
        """

        board = observation['observation']

        # winning_cols = [] option if we want to get all winning cols, for example, for when the opponent plays 
    
        for col in valid_actions: 
            row = self._get_next_row(board, col)
            if self._check_win_from_position(board, row, col, channel):
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
        
        for row in range(5,-1,-1):
            if (board[row, col, 0] == 0 and board[row, col, 1] == 0): 
                return row

        print("This Column is full") 
        return None 
    
    def _check_win_from_position(self, board, row, col, channel):
        """
        Check if there is a position where a given agent could win
        at it next turn.

        Parameters:
            board: numpy array (6, 7, 2)
            row: row index (0-5)
            col: column index (0-6)
            channel: 0 or 1 (which player's pieces to check)

        Returns:
            True if this position creates 4 in a row/col/diag, False otherwise
        """
        
        start_count = 1

        token_count = start_count 
        token_row = row 
        token_col = col
        player_board = board[:,:,channel]

        # Vertical

        if row < 3:
        if row < 3:
            row += 1
            while (row <= 5 and player_board[row, col] == 1): 
                token_count += 1
                if token_count == 4: 
                if token_count == 4: 
                    return True 
                row += 1
                
            token_count= start_count 
            row = token_row

        # Horizontal

        #Left

        col = token_col - 1
        
        while col >= 0 and player_board[row, col] == 1: 
        while col >= 0 and player_board[row, col] == 1: 
            token_count += 1 
            if token_count == 4: 
            if token_count == 4: 
                    return True 
            col -= 1

        col = token_col + 1 

        # Right

        while col <= 6 and player_board[row, col] == 1: 
        while col <= 6 and player_board[row, col] == 1: 
            token_count += 1 
            if token_count == 4: 
            if token_count == 4: 
                    return True 
            col += 1

        col = token_col
        token_count = 1

        # Ascending Diagonal


        #Left

        col = token_col - 1
        row = token_row - 1

        while (row >= 0 and col >= 0 and player_board[row, col] == 1 ): 
        while (row >= 0 and col >= 0 and player_board[row, col] == 1 ): 
            token_count += 1 
            if token_count == 4: 
            if token_count == 4: 
                    return True 
            col -= 1
            row -= 1 

        col = token_col + 1
        row = token_row + 1 

        #Right

        while (row <= 5 and col <= 6 and player_board[row, col] == 1 ) : 
        while (row <= 5 and col <= 6 and player_board[row, col] == 1 ) : 
            token_count += 1 
            if token_count == 4: 
            if token_count == 4: 
                    return True 
            col += 1
            row += 1 

        token_count = 1


        # Descending Diagonal


        #Left

        col = token_col + 1
        row = token_row - 1

        while (row >= 0 and col <= 6 and player_board[row, col] == 1 ): 
        while (row >= 0 and col <= 6 and player_board[row, col] == 1 ): 
            token_count += 1 
            if token_count == 4: 
            if token_count == 4: 
                    return True 
            col += 1
            row -= 1 

        col = token_col - 1
        row = token_row + 1 

        #Right

        while (row <= 5 and col >= 0 and player_board[row, col] == 1 ) : 
        while (row <= 5 and col >= 0 and player_board[row, col] == 1 ) : 
            token_count += 1 
            if token_count == 4: 
            if token_count == 4: 
                    return True 
            col -= 1
            row += 1 


        return False