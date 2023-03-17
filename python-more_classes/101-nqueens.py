#!/usr/bin/python3

"""
Determines all posssible solutions to placing N non-attacking
queens on a N x N chessboard
Usage:
    $ ./101-nqueens.py N
N is an integer >= 4
Attributes:
    board (list): A list of lists representing the chessboard
    solutions (list): A list of lists containing the solution
Solutions are printed in the format [[row, col], [row, col], [row, col]].
Row and col represent where a queen must be placed on the chessboard
"""

import sys


def init_board(n):
    """Initialize an n x n sized chessboard"""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(" ") for i in range(n) for row in board]
    return (board)


def board_copy(board):
    """Return a copy of the board"""
    if isinstance(board, list):
        return list(map(board_copy, board))
    return (board)


def get_solution(board):
    """Return a list of lists of solved chessboard"""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                solution.append([row, col])
                break
    return (solution)


def markout(board, row, col):
    """Mark out spots on a chessboard
    Spots where non-attacking queens can no longer
    be played.
    Args:
        board(list): The current chessboard
        row(int): The row where a queen was last played
        col(int): The column where a queen was last played
    """

    # Mark out all forward positions
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # Mark out all backward positions
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # Mark out all positions below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # Mark out all positions above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"

    # Mark out all positions diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1

    # Mark out all positions diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1

    # Mark out all positions diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1

    # Mark out all positions diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    Args:
        board (list): The current chessboard
        row (int): The current row
        queens (int): The current placed queens
        solutions (list): A list of lists of solutions
    Returns:
        solutions
    """

    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            temp_board = board_copy(board)
            temp_board[row][c] = "Q"
            markout(temp_board, row, c)
            solutions = recursive_solve(
                temp_board, row + 1, queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])

    for sol in solutions:
        print(sol)
