"""
Tic Tac Toe Player

This module implements a Tic Tac Toe game player that uses the Minimax algorithm to determine the optimal move.
"""
import math

# Constants represent the players and the state of an empty cell.
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Initializes the game board to a 3x3 grid of None values, representing an empty board at the start of the game.
    """
    return [[None, None, None], [None, None, None], [None, None, None]]


def player(board):
    """
    Determines the current player of the Tic Tac Toe game.

    The current player is determined based on the number of 'X's and 'O's on the board. If there are as many 'X's as 'O's or fewer, it's 'X's turn, because 'X' starts the game. If there are more 'X's than 'O's, it's 'O's turn. This logic ensures players alternate turns starting with 'X'.

    Args:
    board (list): A 3x3 matrix representing the current state of the board, with each cell containing 'X', 'O', or None.

    Returns:
    str: The player to move, either 'X' or 'O'.
    """
    # Count 'X' on the board
    cnt_X = sum(cell == "X" for row in board for cell in row)

    # Count 'O' on the board
    cnt_O = sum(cell == "O" for row in board for cell in row)

    # If there are as many 'X's as 'O's or fewer, it's 'X's turn, because 'X' starts the game.
    return "X" if cnt_X <= cnt_O else "O"


def actions(board):
    """
    Returns a set of all possible actions (i.e., available cells) on the board.

    The function first checks if the board is terminal (i.e., the game is over), in which case it returns an empty set. If the game is still ongoing, it returns a set of all empty cells on the board.

    Args:
    board (list): The current state of the Tic Tac Toe board as a 3x3 list of lists.

    Returns:
    set: A set of all possible actions (i, j) on the board, where i is the row index and j is the column index.
    """

    # If the board is terminal, return an empty set.
    if terminal(board):
        return set()

    # Otherwise, return a set of all empty cells on the board.
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] is None}


def result(board, action):
    """
    Returns the board that results from making a move (i.e., placing the current player's symbol) on the board.

    The function first checks if the proposed action is valid (i.e., the cell is empty). If the action is valid, the function returns a new board with the proposed action applied. If the action is invalid, the function raises an exception.

    Args:
    board (list): The current state of the Tic Tac Toe board as a 3x3 list of lists.
    action (tuple): The proposed action (i, j) on the board, where i is the row index and j is the column index.

    Returns:
    list: A new board that results from applying the proposed action.
    """

    # Ensure the proposed action is valid (i.e., the cell is empty)
    if action not in actions(board):
        raise Exception(
            "Invalid Action: The cell is already occupied or out of bounds."
        )

    # Create a deep copy of the board to avoid modifying the original board.
    new_board = [row[:] for row in board]

    # Determine the current player's symbol ('X' or 'O')
    current_player = player(board)

    # Apply the action to the copied board
    new_board[action[0]][action[1]] = current_player

    return new_board


def winner(board):
    """
    Determines the winner of the Tic Tac Toe game.

    The function checks the board for a winner by examining each row, column, and diagonal for three consecutive 'X's or 'O's. If a winner is found, the function returns 'X' or 'O'. If no winner is found, the function returns None.

    Args:
    board (list): The current state of the Tic Tac Toe board, represented as a 3x3 list of lists.

    Returns:
    str: The winner of the game, either 'X' or 'O'. If no winner is found, returns None.
    """
    # Define the possible winning lines on the board: rows, columns, and diagonals.
    lines = []

    # Rows: Add each row as a new list in the lines list.
    lines.extend(board)

    # Columns: Add each column as a new list in the lines list.
    lines.extend([[row[i] for row in board] for i in range(3)])

    # Diagonals: Add the two diagonals as new lists in the lines list.
    lines.append([board[i][i] for i in range(3)])

    lines.append(  # Top-left to bottom-right diagonal
        [board[i][2 - i] for i in range(3)]
    )  # Top-right to bottom-left diagonal

    # Check each line for a winner.
    for line in lines:
        if line == ["X", "X", "X"]:
            return "X"  # 'X' wins
        if line == ["O", "O", "O"]:
            return "O"  # 'O' wins

    # If no winner is found, return None.
    return None


def terminal(board):
    """
    Determines if the Tic Tac Toe game is over.

    The game is over if there is a winner or if the board is fully occupied (i.e., a tie). If the game is over, the function returns True; otherwise, it returns False.

    Args:
    board (list): The current state of the Tic Tac Toe board, represented as a 3x3 list of lists.

    Returns:
    bool: True if the game is over, False otherwise.
    """
    # Check if there's a winner. If so, the game is over.
    if winner(board) is not None:
        return True

    # Check if the board is fully occupied. If so, the game is over.
    for i in range(3):
        for j in range(3):
            # If an empty cell is found, the game is not over.
            if board[i][j] is None:
                return False

    # If no empty cell is found and there's no winner, the game is a tie, thus over.
    return True


def utility(board):
    """
    Returns the utility value of the current board state from the perspective of the 'X' player.

    The utility value is determined based on the outcome of the game. If 'X' wins, the utility value is 1. If 'O' wins, the utility value is -1. If the game is a tie, the utility value is 0.

    Args:
    board (list): The current state of the Tic Tac Toe board, represented as a 3x3 list of lists.

    Returns:
    int: The utility value of the current board state from the perspective of the 'X' player.
    """

    # Determine the winner of the game.
    current_winner = winner(board)

    # Return the utility value based on the winner.
    if current_winner == "X":
        return 1  # 'X' has won, so the utility is favorable for 'X'.
    elif current_winner == "O":
        return -1  # 'O' has won, so the utility is unfavorable for 'X'.
        return 0  # The game is a tie, so the utility is neutral.


def minimax(board):
    """
    Returns the optimal action for the current player on the board using the Minimax algorithm.

    The Minimax algorithm is a recursive algorithm that seeks to maximize the utility value for 'X' and minimize the utility value for 'O'. The algorithm considers all possible moves and their potential outcomes to determine the best move for the current player.

    Args:
    board (list): The current state of the Tic Tac Toe board, represented as a 3x3 list of lists.

    Returns:
    tuple: The optimal action (i, j) for the current player, where i is the row index and j is the column index.
    """

    # Return None if the game is over.
    if terminal(board):
        return None

    def max_value(board):
        """
        Calculate the maximum utility value of the board state by considering all possible moves for 'X'.

        Args:
        board: The current state of the game board.

        Returns:
        tuple: The maximum utility value and the corresponding move leading to that value.
        """

        # Check for terminal state and return the utility value if the game has ended.
        if terminal(board):
            return utility(board), None

        v = -math.inf  # Initialize v to the lowest possible value.
        best_move = None
        for action in actions(board):
            # Recursively determine the minimum value the opponent can achieve from this move.
            score, _ = min_value(result(board, action))
            if score > v:
                v, best_move = score, action
                if v == 1:  # Break early if the best possible outcome for 'X' is found.
                    break
        return v, best_move

    def min_value(board):
        """
        Calculate the minimum utility value of the board state by considering all possible moves for 'O'.

        Args:
        board: The current state of the game board.

        Returns:
        tuple: The minimum utility value and the corresponding move leading to that value.
        """

        # Check for terminal state and return the utility value if the game has ended.
        if terminal(board):
            return utility(board), None
        v = math.inf  # Initialize v to the highest possible value.
        best_move = None
        for action in actions(board):
            # Recursively determine the maximum value the opponent can achieve from this move.
            score, _ = max_value(result(board, action))
            if score < v:
                v, best_move = score, action
                if (
                    v == -1
                ):  # Break early if the best possible outcome for 'O' is found.
                    break
        return v, best_move

    # Determine the current player and call the appropriate function to calculate the optimal move.
    currentPlayer = player(board)
    if currentPlayer == X:
        _, action = max_value(board)  # For 'X', seek to maximize the utility.
    else:
        _, action = min_value(board)  # For 'O', seek to minimize the utility.
    return action
