class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.num_removed_cells = removed_cells
        self.row_length = row_length
        self.board = []

    def get_board(self):        # Creates list of 9 lists that each have 9 elements
        for i in range(9):
            row = []
            for j in range(9):
                row.append(" ")
            self.board.append(row)
        return self.board

    def print_board(self):
        for i in range(9):
            print(self.board[i])

    def valid_in_row(self, row, num):   # Checks if the desired number is in the row. (True means num is in row)
        row_list = self.board[row]
        for i in range(9):
            if num == row_list[i]:
                return True
        return False

    def valid_in_col(self, col, num):   # Checks if the desired number is in the column (True means num is in col)
        for i in range(9):
            row = self.board[i]
            col_value = row[col]
            if num == col_value:
                return True
        return False

    def valid_in_box(self, row_start, col_start, num):
        pass

    def is_valid(self, row, col, num):
        pass

    def fill_box(self, row_start, col_start):
        pass

    def fill_diagonal(self):
        pass

    def fill_remaining(self, row, col):
        pass

    def fill_values(self):
        pass

    def remove_cells(self):
        pass
