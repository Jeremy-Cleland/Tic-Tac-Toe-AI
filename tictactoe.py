"""
Tic Tac Toe Player

This module implements a Tic Tac Toe game player that uses the Minimax algorithm to determine the optimal move.
"""
import math

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
    Returns player who has the next turn on a board.

    The function calculates the number of 'X' and 'O' on the board.
    If the counts are equal, or there are fewer 'X's, it's 'X's turn.
    Otherwise, it's 'O's turn.

    Args:
    board (list): The current state of the Tic Tac Toe board, a 3x3 list of lists.

    Returns:
    str: 'X' or 'O' indicating which player's turn it is.
    """
    # Count 'X' on the board
    cnt_X = sum(cell == "X" for row in board for cell in row)

    # Count 'O' on the board
    cnt_O = sum(cell == "O" for row in board for cell in row)

    # If there are as many 'X's as 'O's or fewer, it's 'X's turn, because 'X' starts the game.
    return "X" if cnt_X <= cnt_O else "O"


def actions(board):
    """
    Identifies and returns all the possible actions on a Tic Tac Toe board or an appropriate value for terminal boards.

    Actions are represented as tuples (i, j), where i is the row index and j is the column index
    of an empty spot on the board. Only empty cells (those without 'X' or 'O') can be chosen for a new move.

    If the board is terminal (the game is over), any return value is acceptable. Here, we choose to return an empty set.

    Args:
    board (list): A 3x3 matrix representing the current state of the board, with each cell containing 'X', 'O', or None.

    Returns:
    set: A set of tuples, each representing a possible action (move) on the board, or an empty set if the board is terminal.
    """

    if terminal(board):
        return set()

    # Otherwise, return a set of all empty cells on the board.
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] is None}


def result(board, action):
    """
    Calculates and returns the new board state resulting from a specific move.

    This function first validates the proposed action to ensure it's a legal move,
    then applies the move to a copy of the board, ensuring the original board remains unchanged.

    Args:
    board (list): The current state of the Tic Tac Toe board as a 3x3 list of lists.
    action (tuple): The proposed move as a tuple (i, j), where i is the row index and j is the column index.

    Returns:
    list: A new board state reflecting the result of the move.

    Raises:
    Exception: If the proposed action is not valid (i.e., if the cell is not empty).
    """
    # Ensure the proposed action is valid (i.e., the cell is empty)
    if action not in actions(board):
        raise Exception(
            "Invalid Action: The cell is already occupied or out of bounds."
        )

    # Create a deep copy of the board to avoid modifying the original board.
    new_board = [row[:] for row in board]

    # Determine the current player
    current_player = player(board)

    # Place the current player's symbol at the specified action position on the new board

    new_board[action[0]][action[1]] = current_player

    return new_board


def winner(board):
    """
    Determines the winner of the Tic Tac Toe game by checking all possible winning combinations.

    The function checks each row, column, and both diagonals for three identical symbols ('X' or 'O'),
    indicating a win. If such a line is found, the function returns the winning symbol. If there is
    no winner yet, it returns None.

    Args:
    board (list): The current state of the Tic Tac Toe board, represented as a 3x3 list of lists.

    Returns:
    str: 'X' or 'O' indicating the winner, if there is one. None if the game is still ongoing or if it's a tie.
    """
    # All possible winning combinations on the board: three rows, three columns, and two diagonals.
    lines = []

    # Rows: Add each row as a new list in the lines list.
    lines.extend(board)

    # Columns: Add each column as a new list in the lines list.
    lines.extend([[row[i] for row in board] for i in range(3)])

    # Diagonals: Add the two diagonals as new lists in the lines list.
    lines.append([board[i][i] for i in range(3)])  # Top-left to bottom-right diagonal
    lines.append(
        [board[i][2 - i] for i in range(3)]
    )  # Top-right to bottom-left diagonal

    # Check each row, column, and diagonal to see if they contain three of the same symbol, indicating a win
    for line in lines:
        if line == ["X", "X", "X"]:
            return "X"  # 'X' wins
        if line == ["O", "O", "O"]:
            return "O"  # 'O' wins

    # If no winner is found, return None.
    return None


def terminal(board):
    """
    Determines whether the Tic Tac Toe game has ended.

    The game is considered over if there is a winner or if all cells on the board are filled,
    indicating either a victory or a tie. This function checks for these conditions in order.

    Args:
    board (list): The current state of the Tic Tac Toe board, represented as a 3x3 list of lists.

    Returns:
    bool: True if the game is over, either by victory or tie. False if the game can still continue.
    """
    # Check if there's a winner. If so, the game is over.
    if winner(board) is not None:
        return True  # Game is over due to a win.

    # Check if the board is fully occupied. If so, the game is over.
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:  # If any cell is empty, the game is not over yet.
                return False

    return True


def utility(board):
    """
    Evaluates and returns the utility value of the Tic Tac Toe board state.

    In the context of Tic Tac Toe, the utility value is a numerical representation of the game's outcome from the perspective of player 'X':
    - If 'X' wins, the utility is 1, indicating a favorable outcome for 'X'.
    - If 'O' wins, the utility is -1, indicating a favorable outcome for 'O' and thus unfavorable for 'X'.
    - If the game is a tie or still in progress (no winner), the utility is 0, indicating a neutral outcome.

    This function is typically used in the context of game theory and AI decision-making, such as evaluating terminal states in the Minimax algorithm.

    Args:
    board (list): The current state of the Tic Tac Toe board, represented as a 3x3 list of lists.

    Returns:
    int: The utility value of the board state, either 1, -1, or 0.
    """

    # Determine the winner of the game.
    current_winner = winner(board)  # Check the board state for a winner.

    if current_winner == "X":
        return 1  # 'X' has won, so the utility is favorable for 'X'.
    elif current_winner == "O":
        return -1  # 'O' has won, so the utility is unfavorable for 'X'.
    else:
        return 0  # The game is a tie, so the utility is neutral.


def minimax(board):
    """
    Executes the Minimax algorithm to find the optimal move for the current player.

    The Minimax algorithm is a decision-making tool used in artificial intelligence (AI)
    for finding the optimal move in a zero-sum game. This implementation determines the best move
    by exploring all possible moves, predicting the opponent's response, and choosing the move
    that maximizes the player's chances of winning while minimizing the chances of losing.

    Args:
        board (list): A 3x3 matrix representing the current Tic Tac Toe board state.

    Returns:
        tuple: The optimal move for the current player, as a tuple (row, column).
    """

    # Base case: If the board represents a game that is finished, return None for no further moves.
    if terminal(board):
        return None

    def max_value(board):
        """
        Evaluate the maximum score that the maximizing player can achieve from the current board state.

        This function iterates through all possible actions, recursively calling min_value to consider
        the opponent's response. It returns the action leading to the highest possible score for 'X'.

        Args:
            board: The game board at the current state.

        Returns:
            A tuple containing the highest score achievable and the move (as a tuple) that leads to that score.
        """
        if terminal(board):
            return utility(
                board
            ), None  # Return the utility if the game is already decided.
        v = -math.inf  # Initialize with the worst possible score.
        best_move = None
        for action in actions(board):
            # Explore the opponent's optimal response to each possible move.
            score, _ = min_value(result(board, action))
            if score > v:  # Found a better score, update v and best_move.
                v, best_move = score, action
                if v == 1:  # Maximum possible score for 'X', no need to search further.
                    break
        return v, best_move

    def min_value(board):
        """
        Evaluate the minimum score that the minimizing player can achieve from the current board state.

        Similar to max_value, it explores all possible actions, but here it aims to minimize the opponent's score.
        It returns the action that leads to the lowest score for 'O'.

        Args:
            board: The game board at the current state.

        Returns:
            A tuple containing the lowest score achievable and the move (as a tuple) that leads to that score.
        """
        if terminal(board):
            return utility(
                board
            ), None  # Return the utility if the game is already decided.
        v = math.inf  # Initialize with the best possible score.
        best_move = None
        for action in actions(board):
            # Explore the opponent's optimal response to each possible move.
            score, _ = max_value(result(board, action))
            if (
                score < v
            ):  # Found a better (lower) score for 'O', update v and best_move.
                v, best_move = score, action
                if (
                    v == -1
                ):  # Minimum possible score for 'O', no need to search further.
                    break
        return v, best_move

    # Determine whether the current player is maximizing ('X') or minimizing ('O') and call the respective function.
    currentPlayer = player(board)
    if currentPlayer == X:
        # Current player is 'X', aim to maximize the score.
        _, action = max_value(board)
    else:
        # Current player is 'O', aim to minimize the score.
        _, action = min_value(board)
    return action
