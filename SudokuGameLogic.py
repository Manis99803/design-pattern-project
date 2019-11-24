import SudokuGenerator
from Cell import Cell
from Square import Square

square_objects = []
def convert_square_wise_to_row_wise(sudoku_board_list):
    offset_value = 0
    row_wise_sudoku = []
    for i in range(0, 3):
            row_elements = []
            for j in range(0 + offset_value, 3 + offset_value):
                for k in range(0, 3):
                    sudoku_board_list[j][j][k]["squareNumber"] = j
                    row_elements.append(sudoku_board_list[j][j][k])
            row_wise_sudoku.append(row_elements)

            row_elements = []
            for j in range(0 + offset_value, 3 + offset_value):
                for k in range(3, 6):
                    sudoku_board_list[j][j][k]["squareNumber"] = j
                    row_elements.append(sudoku_board_list[j][j][k])
            row_wise_sudoku.append(row_elements)

            row_elements = []
            for j in range(0 + offset_value, 3 + offset_value):
                for k in range(6, 9):
                    sudoku_board_list[j][j][k]["squareNumber"] = j
                    row_elements.append(sudoku_board_list[j][j][k])
            row_wise_sudoku.append(row_elements)

            offset_value += 3
    
    return row_wise_sudoku


def convert_square_wise_to_column_wise(sudoku_board_list):
    column_wise_sudoku = []
    for i in range(0, 9):
        column_cell = []
        for j in range(0, 9):
            column_cell.append(sudoku_board_list[j][j][i])
        column_wise_sudoku.append(column_cell)
    
    return column_wise_sudoku

def map_row_to_objects(sudoku_board_values):
    offset_value = 0
    square_number = 0
    global square_objects
    
    for i in range(0, 9, 3):
            cell_number = 0
            cell_objects = []
            offset_value = 0
            for row_number in range(i, i + 3):
                for j in range(0 + offset_value, 3 + offset_value):
                    if sudoku_board_values[row_number][j] != 0:
                        cell = Cell(
                            cell_number, sudoku_board_values[row_number][j])
                    else:
                        cell = Cell(cell_number, '')
                    cell_objects.append(cell)
                    cell_number += 1

            square = Square(square_number, cell_objects)
            square_objects.append(square)
            square_number += 1
            offset_value += 3

            cell_objects = []
            cell_number = 0
            for row_number in range(i, i + 3):
                for j in range(offset_value, 3 + offset_value):
                    if sudoku_board_values[row_number][j] != 0:
                        cell = Cell(
                            cell_number, sudoku_board_values[row_number][j])
                    else:
                        cell = Cell(cell_number, '')
                    cell_number += 1
                    cell_objects.append(cell)

            square = Square(square_number, cell_objects)
            square_objects.append(square)
            offset_value += 3
            square_number += 1

            cell_number = 0
            cell_objects = []
            for row_number in range(i, i + 3):
                for j in range(offset_value, 3 + offset_value):
                    if sudoku_board_values[row_number][j] != 0:
                        cell = Cell(
                            cell_number, sudoku_board_values[row_number][j])
                    else:
                        cell = Cell(cell_number, '')
                    cell_number += 1
                    cell_objects.append(cell)
            square = Square(square_number, cell_objects)
            square_objects.append(square)
            square_number += 1
            offset_value += 3


def update_cell_value(cell_data, row_wise_sudoku, column_wise_sudoku):
    global square_objects
    square_number = int(cell_data["squareNumber"])
    cell_number = int(cell_data["cellNumber"])
    cell_value = int(cell_data["value"])
    
    cell_objects = square_objects[square_number].get_squares_cell()
    
    square_elements = [cell.get_cell_value() for cell in cell_objects]
    row_elements = row_wise_sudoku[cell_number]
    row_elements = [cell["value"] for cell in row_elements]
    
    column_elements = column_wise_sudoku[cell_number]
    column_elements = [cell["value"] for cell in column_elements]
    
    if (cell_value not in square_elements) and (cell_value not in column_elements) \
        and (cell_value not in row_elements):
        cell = cell_objects[cell_number]
        cell.set_cell_value(cell_value)
        return True
    else:
        return False

def get_sudoku_board():
    return SudokuGenerator.final_grid
