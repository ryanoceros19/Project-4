from sudoku_generator import SudokuGenerator


def generate_sudoku(size, removed):     # This function is NOT in the SudokuGenerator class
    pass


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
    pass
