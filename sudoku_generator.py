class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.num_removed_cells = removed_cells
        self.row_length = row_length
        self.board = []

    def get_board(self):        # Creates list of 9 lists that each have 9 elements
        for i in range(9):
            row = []
            for j in range(9):
                row.append(0)
            self.board.append(row)
        return self.board

    def print_board(self):
        for i in range(9):
            print(self.board[i])

    def valid_in_row(self, row, num):   # Checks if the desired number is in the row. (True = num not row)
        row_list = self.board[row]
        for i in range(9):
            if num == row_list[i]:
                return False
        return True

    def valid_in_col(self, col, num):   # Checks if the desired number is in the column (True = num not in col)
        for i in range(9):
            row = self.board[i]
            col_value = row[col]
            if num == col_value:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):  # Checks if desired number is in 3X3 box (False = num in box)
        nums_in_box = []    # Creates new list that will hold the values in the box

        '''
        The following for loop selects the first row and calls the value in the column spot. It appends that value to
        the nums_in_box list. It continues for the next 2 column spots. After adding those three values to the list, it
        hops to next row and repeats the process of adding such values. 
        '''
        for row_num in range(row_start, row_start + 3):
            selected_row = self.board[row_num]
            for col_num in range(col_start, col_start + 3):
                cell_value = selected_row[col_num]
                nums_in_box.append(cell_value)

        if nums_in_box.count(0) > 0:                    # This if statement deletes any empty cells in the box
            num_empty_spaces = nums_in_box.count(0)
            while num_empty_spaces != 0:
                nums_in_box.remove(0)
                num_empty_spaces -= 1

        nums_in_box.sort()  # Sorts the list of numbers that were contained in the box

        for number in nums_in_box:  # This searches the values in the box for the desired number
            if number == num:
                return False
        return True

    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) is False or self.valid_in_col(col, num) is False:
            return False

        # The following two if statements help determine the row start and col start value for the valid_in_box function
        if 0 <= row <= 2:
            row_start = 0
        elif 3 <= row <= 5:
            row_start = 3
        elif 6 <= row <= 8:
            row_start = 6

        if 0 <= col <= 2:
            col_start = 0
        elif 3 <= col <= 5:
            col_start = 3
        elif 6 <= col <= 8:
            col_start = 6

        if self.valid_in_box(row_start, col_start, num) is False:
            return False
        else:
            return True

    def fill_box(self, row_start, col_start):
        pass

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):
        pass

    def fill_values(self):
        pass

    def remove_cells(self):
        pass


def generate_sudoku(size, removed):  # This function produces the sudoku board by calling functions in sudoku_generator
    sudoku = SudokuGenerator(size, removed)
    return sudoku
