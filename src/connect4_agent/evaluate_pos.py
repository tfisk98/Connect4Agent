import numpy as np

def evaluate_position(board, player_channel):
    """
    Evaluate board position from player's perspective

    Parameters :
        board : the (6,7,2) grid
        player_channel : 0 for current player, 1 for the opponent

    Returns:
        float: positive = good for player, negative = bad
    """
    score = 0

    # Check for wins
    if has_won(board, 0 if player_channel== 0 else 1):
        return 10000

    if has_won(board, 1 if player_channel== 0 else 0):
        return -10000

    # Count 3-in-a-row patterns (without the 4th piece blocked)
    score += count_three_in_row(board, player_channel) * 5

    # Count 2-in-a-row patterns
    score += count_two_in_row(board, player_channel) * 2

    # Prefer center positions
    score += count_pieces_in_center(board, player_channel) * 3

    return score


def has_won(board, player_channel):
    """
    Checks if the evaluated player has won or not 

    Parameters :
        board : the (6,7,2) grid
        player_channel : 0 for current player, 1 for the opponent

    Returns:
        True if there is a connect 4, False otherwise
    """
    for row in range(5,-1,-1):
         for col in range(7):
              if board[row,col,player_channel] == 1 and check_win_from_position(board, row, col, player_channel):
                   return True
    return False    


def count_pieces_in_center(board, player_channel):
    """
    Counts the number of tokens in the center column for a given player

    Parameters :
        board : the (6,7,2) grid
        player_channel : 0 for current player, 1 for the opponent

    Returns:
        Integer from 0 to 6
    """
    count = 0
    for row in range(6) :
        if board[row,3,player_channel] == 1:
            count += 1 
    return count 


def check_win_from_position(board, row, col, channel):
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


def count_two_in_row(board, player_channel): 
    """
    Counts the number of chains of horizontal, vertical, ascending diagonal and descending diagonal chains of tokens
    on the same board that are of length 2. 

    Parameters :
        board : the (6,7,2) grid
        player_channel : 0 for current player, 1 for the opponent

    Returns:
        Integer corresponding to the number of chains of 2 tokens a player has. 
    """
    curr_board = board[:,:, player_channel]
    count = 0 
    # Browsing the grid from bottom to top and left to right
    # Browsing the grid from bottom to top and left to right
    for row in range(5,-1,-1):
        for col in range(7):
            if curr_board[row,col] == 1 : 
                for loc_row in range(-1,1,1):
                    for loc_col in range(2): 
                        if loc_col == 0 and loc_row == 0:
                            pass 
                        elif row + loc_row == -1 or col + loc_col == 7:
                            pass 
                        elif curr_board[row + loc_row, col + loc_col] == 1 :
                            count += 1
    
    # Descending Diagonal
    # Descending Diagonal
    for row in range(4,-1,-1):
        for col in range(5):
            if curr_board[row,col] == 1 and curr_board[row + 1, col + 1 ] == 1:
                    count += 1

    return count 


def count_three_in_row(board, player_channel):
    """
    Counts the number of chains of horizontal, vertical, ascending diagonal and descending diagonal chains of tokens
    on the same board that are of length 3. 

    Parameters :
        board : the (6,7,2) grid
        player_channel : 0 for current player, 1 for the opponent

    Returns:
        Integer corresponding to the number of chains of 3 tokens a player has. 
    """
    curr_board = board[:,:, player_channel]
    count = 0
    # Browsing the grid from bottom to top and left to right
    # Browsing the grid from bottom to top and left to right
    for row in range(5,-1,-1):
        for col in range(7):
            if curr_board[row,col] == 1 : 
                for loc_row in range(-1,1,1):
                    if row == 0 and loc_row== -1 :
                        pass 
                    else :
                        for loc_col in range(2): 
                            if loc_row ==0 and loc_col == 0: 
                                pass 
                            elif col == 6 and loc_col == 1 :
                                pass 
                            elif row + 2*loc_row >0 and col + 2*loc_col < 7 :
                                    if curr_board[row + loc_row, col + loc_col] == 1 and curr_board[row + 2*loc_row, col + 2*loc_col] == 1 :
                                        count += 1
    
    # Descending Diagonal
    # Descending Diagonal
    for row in range(3,-1,-1):
        for col in range(4):
            if curr_board[row,col] == 1 : 
                if curr_board[row + 1, col + 1] == 1 and curr_board[row + 2, col + 2] == 1 :
                    count += 1
                            
    return count