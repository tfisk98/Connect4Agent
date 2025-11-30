import numpy as np


def evaluate_position(board, player_channel):
    """
    Evaluate board position from player's perspective

    Returns:
        float: positive = good for player, negative = bad
    """
    score = 0

    # Check for wins
    if has_won(board, player_channel):
        return 10000

    if has_won(board, 1 - player_channel):
        return -10000

    # Count 3-in-a-row patterns (without the 4th piece blocked)
    score += count_three_in_row(board, player_channel) * 5

    # Count 2-in-a-row patterns
    score += count_two_in_row(board, player_channel) * 2

    # Prefer center positions
    score += count_pieces_in_center(board, player_channel) * 3

    return score


def has_won(board, player_channel):
    for row in range(5,-1,-1):
         for col in range(7):
              if board[row,col,player_channel] == 1 and check_win_from_position(board, row, col, player_channel):
                   return True
    return False 
    

def count_three_in_row(board, player_channel):
    curr_board = board[:,:, player_channel]
    count = 0
    for row in range(6):
        for col in range(7):
            if curr_board[row,col] == 1 : 
                for loc_row in range(-1,2,1):
                    for loc_col in range(-1,2,1): 
                        if curr_board[row + loc_row, col + loc_col] == 1 and curr_board[row + 2*loc_row, col + 2*loc_col] :
                            count += 1
                        if curr_board[row + loc_row, col + loc_col] == 1 and curr_board[row - loc_row, col - loc_col] :
                            count += 1/2 
    return count // 3 

def count_two_in_row(board, player_channel):
    curr_board = board[:,:, player_channel]
    count = 0 
    for row in range(6):
        for col in range(7):
            if curr_board[row,col] == 1 : 
                for loc_row in range(-1,2,1):
                    for loc_col in range(-1,2,1): 
                        if curr_board[row + loc_row, col + loc_col] == 1 :
                            count += 1 

    return count // 2 


def count_pieces_in_center(board, player_channel):
    count = 0
    for row in range(6) :
        if board[row,3,player_channel] == 1:
            count += 1 
    return count 



def check_win_from_position(self, board, row, col, channel):
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

        #col = token_col
        #row = token_row

        return False 