class SudokuForm:
    def __init__(self, sudoku_board_list):
        self.sudoku_board_list = sudoku_board_list
    
    def convert_square_wise_to_row_wise(self):
        offset_value = 0
        square_offset = 0
        self.row_wise_sudoku = list()
        for i in range(0, 3):
            square_offset = 0
            for j in range(0, 3):
                row_elements = []
                for k in range(0 + offset_value, 3 + offset_value):
                    for l in range(0 + square_offset, 3 + square_offset):
                        self.sudoku_board_list[k][k][l]["squareNumber"] = k
                        row_elements.append(self.sudoku_board_list[k][k][l])
                square_offset += 3
                self.row_wise_sudoku.append(row_elements)
            offset_value += 3
        
        return self.row_wise_sudoku

    def convert_square_wise_to_column_wise(self):
        self.column_wise_sudoku = []
        for i in range(0, 9):
            column_cell = []
            for j in range(0, 9):
                for cell in self.sudoku_board_list[j][j]:
                    if cell["columnNumber"] == i:
                        column_cell.append(cell)
            self.column_wise_sudoku.append(column_cell)
            
        return self.column_wise_sudoku