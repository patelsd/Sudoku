from itertools import product
from generator import generate_board

sudoku_board = generate_board()


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board, num, position):
    # Check row for matching numbers
    for i in range(len(board[0])):
        if board[position[0]][i] == num and position[1] != i:
            return False

    # Check column for matching numbers
    for i in range(len(board)):
        if board[i][position[1]] == num and position[0] != i:
            return False

    # Check 3x3 square for matching numbers
    b_x = position[1] // 3
    b_y = position[0] // 3

    for i in range(b_y * 3, b_y * 3 + 3):
        for j in range(b_x * 3, b_x * 3 + 3):
            if board[i][j] == num and (i, j) != position:
                return False

    return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - + - - - + - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Finds the first empty spot in the board and returns the (row, col) tuple
def find_empty(board):
    for i, j in product(range(len(board)), range(len(board[0]))):
        if board[i][j] == 0:
            return i, j

    return None


print_board(sudoku_board)
print("____________________________________________________")
solve(sudoku_board)
print_board(sudoku_board)
