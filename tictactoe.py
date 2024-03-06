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
    """
    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)
    return "X" if x_count == o_count else "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] is None}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not None:
        raise ValueError("Invalid action")

    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    lines = []
    # Rows and columns
    lines.extend(board)
    lines.extend([[row[i] for row in board] for i in range(3)])
    # Diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    for line in lines:
        if line == ["X", "X", "X"]:
            return "X"
        if line == ["O", "O", "O"]:
            return "O"
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    return all(board[i][j] is not None for i in range(3) for j in range(3))


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    if winner(board) == "O":
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == "X":
        value, move = max_value(board)
        return move
    else:
        value, move = min_value(board)
        return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float("-inf")
    best_move = None
    for action in actions(board):
        min_result, _ = min_value(result(board, action))
        if min_result > v:
            v = min_result
            best_move = action
        if v == 1:
            break
    return v, best_move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float("inf")
    best_move = None
    for action in actions(board):
        max_result, _ = max_value(result(board, action))
        if max_result < v:
            v = max_result
            best_move = action
        if v == -1:
            break
    return v, best_move
