"""
Tic Tac Toe Player
"""
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
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
    # Count 'X' on the board using sum and list comprehension
    # The inner list comprehension creates a list of boolean values,
    # where True (counted as 1) if the cell is 'X', and False (counted as 0) otherwise.
    # The sum function then adds up these values to count all 'X's.
    cnt_X = sum(cell == "X" for row in board for cell in row)

    # Similarly, count 'O' on the board
    cnt_O = sum(cell == "O" for row in board for cell in row)

    # If there are as many 'X's as 'O's or fewer, it's 'X's turn, because 'X' starts the game.
    # If there are more 'X's than 'O's, it's 'O's turn.
    # This logic ensures players alternate turns starting with 'X'.
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
    # If the board is terminal, return an empty set indicating no further actions are possible.
    if terminal(board):
        return set()

    # For a non-terminal board, return all possible actions (empty cells).
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
    # Validate the action
    if action not in actions(board):
        raise Exception(
            "Invalid Action: The cell is already occupied or out of bounds."
        )

    # Deep copy the board to avoid modifying the original
    # Using list comprehension to copy each row ensures that we get a new list object for each row
    new_board = [row[:] for row in board]

    # Determine the current player's symbol ('X' or 'O')
    current_player = player(board)

    # Apply the action to the copied board
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
    lines = []

    # Rows: Already in the desired format, just extend the lines list with the board itself.
    lines.extend(board)

    # Columns: Create new lists representing each column and add them to the lines list.
    lines.extend([[row[i] for row in board] for i in range(3)])
    # Diagonals: Two diagonals are possible, from top-left to bottom-right and top-right to bottom-left.
    # Add each diagonal as a new list in the lines list.
    lines.append([board[i][i] for i in range(3)])  # Top-left to bottom-right diagonal
    lines.append(
        [board[i][2 - i] for i in range(3)]
    )  # Top-right to bottom-left diagonal

    # Check each line for a win condition: three 'X's or three 'O's.
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
    # First, check if there is a winner. The game ends immediately if either 'X' or 'O' wins.
    if winner(board) is not None:
        return True  # Game is over due to a win.

    # If there's no winner, check if the board is fully occupied (a tie situation). Iterate over each cell on the board; if any cell is None (empty), the game is still ongoing.
    for i in range(3):
        for j in range(3):
            if (
                board[i][j] == None
            ):  # Found an empty cell, so the game can still continue.
                return False

    # If no empty cell is found and there's no winner, the game is a tie, thus over.
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
    # First, determine if there is a winner and assign utility values accordingly.
    current_winner = winner(board)  # Check the board state for a winner.

    if current_winner == "X":
        return 1  # 'X' has won, so the utility is favorable for 'X'.
    elif current_winner == "O":
        return (
            -1
        )  # 'O' has won, so the utility is unfavorable for 'X' (favorable for 'O').
    else:
        return 0  # No winner yet or a tie, indicating a neutral outcome.


def minimax(board):
    """
    Executes the Minimax algorithm to determine the optimal move for the current player on a Tic Tac Toe board.

    Args:
    board: The current state of the game board as a 2D list.

    Returns:
    tuple: The optimal move (i, j) for the current player.
    """

    # Terminal state check: If the game is over, return None as no moves are possible.
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
                if v == 1:  # Break early if the best possible outcome is found.
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

    # Start the Minimax algorithm based on the current player.
    currentPlayer = player(board)
    if currentPlayer == X:
        _, action = max_value(board)  # For 'X', seek to maximize the utility.
    else:
        _, action = min_value(board)  # For 'O', seek to minimize the utility.
    return action
