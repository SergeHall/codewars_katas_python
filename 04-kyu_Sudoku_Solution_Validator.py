# Sudoku Background
#
# Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
# (More info at: http://en.wikipedia.org/wiki/Sudoku)
#
# Sudoku Solution Validator
#
# Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.
#
# The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

def valid_solution(board):
    control_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    m = 0
    n = 0
    print(board)
    for i in board:
        if control_set != set(i) or \
                control_set != {board[0][m], board[1][m], board[2][m],
                                board[3][m], board[4][m], board[5][m],
                                board[6][m], board[7][m], board[8][m]} or \
                control_set != {board[0][n], board[0][n + 1], board[0][n + 2],
                                board[1][n], board[1][n + 1], board[1][n + 2],
                                board[2][n], board[2][n + 1], board[2][n + 2]}:
            return False
        m += 1
        n += 3
        if n == 9:
            n = 0

    return True