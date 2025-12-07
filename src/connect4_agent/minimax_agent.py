"""
Minimax agent with alpha-beta pruning
"""

import numpy as np
import random
from loguru import logger
import time 

from src.connect4_agent.evaluate_pos import evaluate_position


class MinimaxAgent:
    """
    Agent using minimax algorithm with alpha-beta pruning
    """

    def __init__(self, env, depth=4, player_name=None):
        """
        Initialize minimax agent

        Parameters:
            env: PettingZoo environment
            depth: How many moves to look ahead
            player_name: Optional name
        """
        self.env = env
        self.action_space = env.action_space(env.agents[0])
        self.depth = depth
        self.player_name = player_name or f"Minimax(d={depth})"

    def choose_action(self, observation, reward=0.0, terminated=False, truncated=False, info=None, action_mask=None):
        """
        Choose action using minimax algorithm

        Parameters : 
            observation : State of the game (board of player_0 and player_1 plus action mask)
            reward : score which rewards the agent for a win and punishes the agent for a in order improve its evaluation for the next game(unused here)
            terminated : True if the game is over, False otherwise 
            truncated : True if the game stops brutally, False otherwise 
            info : unused here
            action_mask : filter to indicate to the agent which columns are playable and which are not
        return : 
            integer between 0 and 6, which gets the best evaluation by the minimax algorithm, randomly chosen otherwise
        """

        action=None
        if terminated or truncated :
            return action
        elif action_mask == None :
            action_mask=observation["action_mask"]
        else :
            mask=action_mask

        
        valid_actions = [i for i, valid in enumerate(action_mask) if valid == 1]

        best_action = None
        best_value = float('-inf')
        observation = observation['observation']

        # Try each valid action
        for action in valid_actions:
            # Simulate the move
            new_board = self._simulate_move(observation, action, channel=0)

            # Evaluate using minimax (opponent's turn, so minimizing)
            value = self._minimax(new_board, self.depth - 1, float('-inf'), float('inf'), False)

            if value > best_value:
                best_value = value
                best_action = action
        
        return best_action if best_action is not None else random.choice(valid_actions)

    def _minimax(self, board, depth, alpha, beta, maximizing):
        """
        Minimax algorithm with alpha-beta pruning

        Parameters:
            board: Current board state
            depth: Remaining depth to search
            alpha: Best value for maximizer
            beta: Best value for minimizer
            maximizing: True if maximizing player's turn

        Returns:
            float: evaluation score
        """


        # Base cases:
        #   - depth == 0: return evaluate(board)
        #   - game over: return win/loss score


        if self._check_win( board, 0): 
            return 20000

        if self._check_win( board, 1):
            return -20000

        if depth == 0  or self._get_valid_moves(board) == None : 
            return self._evaluate(board)
        
        # Recursive case:
        #   - Try all valid moves
        #   - Recursively evaluate
        #   - Update alpha/beta
        #   - Prune if possible
        
        elif maximizing : 
            max_eval = float('-inf')
            for move in self._get_valid_moves(board) :
                new_board = self._simulate_move(board, col=move, channel= 0)
                eval = self._minimax(new_board, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if alpha >= beta : 
                    break 
                     
            return max_eval
        else : 
            min_eval = float('inf') 
            for move in self._get_valid_moves(board) :
                new_board = self._simulate_move(board, col=move, channel= 1)
                eval = self._minimax(new_board, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if alpha >= beta  : 
                    break 
            return min_eval

    def _simulate_move(self, board, col, channel):
        """
        Simulate placing a piece without modifying original board

        Parameters:
            board: Current board state (6, 7, 2)
            col: Column to play
            channel: 0 for current player, 1 for opponent

        Returns:
            new_board: Copy of board with move applied
        """
        # 1. Copy board

        new_board = np.copy(board) # copy numpy array
        # 2. Find next available row in column
        row = self._get_next_row(new_board, col)
        # 3. Place piece
        new_board[row,col,channel] = 1 
        # 4. Return new board
        return new_board

    def _get_valid_moves(self, board):
        """
        Get list of valid column indices

        Parameters : 
            board: Current board(6,7,2)

        Returns:
            list of valid columns
        """
        valid_cols = []
        for col in range(7):
            if board[0,col,0] == 0 and board[0,col,1] == 0:
                valid_cols.append(col)

        if valid_cols == [] :
            return None 

        else :
            return valid_cols
        
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

    def _evaluate(self, board):
        """
        Evaluate board position

        Returns:
            float: score (positive = good for us)
        """
        return evaluate_position(board, 0) - evaluate_position(board, 1)

    def _check_win(self, board, channel):
        """
        Check if player has won

        Returns:
            bool: True if won
        """

        for row in range(5,-1,-1):
            for col in range(7):
                if board[row,col,channel] == 1 and self._check_win_from_position(board, row, col, channel):
                    return True
        return False 

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

        col = token_col
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

        return False 