from sudoku_generator import SudokuGenerator


def generate_sudoku(size, removed):  # This function produces the sudoku board by calling functions in sudoku_generator
    sudoku = SudokuGenerator(size, removed)
    return sudoku


# The following functions are optional for a single cell
class Cell:
    def __init__(self, value, row, col, screen):
        pass

    def set_cell_value(self, value):
        pass

    def draw(self):
        pass


# The following functions are optional for an entire Sudoku Board. A Board object has 81 Cell objects
class Board:
    def __init__(self, width, height, screen, difficulty):
        pass

    def draw(self):
        pass

    def select(self, row, col):
        pass

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass


if __name__ == '__main__':
    game_mode = ""
    if game_mode == "easy":
        sudoku = generate_sudoku(9, 30)

    elif game_mode == "medium":
        sudoku = generate_sudoku(9, 40)

    elif game_mode == "hard":
        sudoku = generate_sudoku(9, 50)
