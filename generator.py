import requests


# Fetches a partially filled Sudoku puzzle from an API - http://www.cs.utep.edu/cheon/ws/sudoku/
def get_valid_board():
    return requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/?size=9&level=2')


def generate_board():
    response = get_valid_board()
    if response:
        data = list(response.json().get("squares"))
        board = [[0] * 9 for i in range(9)]

        for val in data:
            board[val.get('x')][val.get('y')] = val.get('value')

        return board
