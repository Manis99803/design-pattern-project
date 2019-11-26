import SudokuGenerator
from Cell import Cell
from Square import Square
from Board import Board
import copy

square_objects = list()
previous_state = list()
sudoku_board = list()
sudoku_board_list = list()


def convert_square_wise_to_row_wise(sudoku_board_list):
    offset_value = 0
    row_wise_sudoku = list()
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
            for cell in sudoku_board_list[j][j]:
                if cell["columnNumber"] == i:
                    column_cell.append(cell)
        column_wise_sudoku.append(column_cell)
        
    return column_wise_sudoku

def map_row_to_objects(sudoku_board_values):
    offset_value = 0
    square_number = 0
    global square_objects
    
    square_objects = []
    for i in range(0, 9, 3):
            cell_number = 0
            cell_objects = []
            offset_value = 0
            for row_number in range(i, i + 3):
                for j in range(0 + offset_value, 3 + offset_value):
                    if sudoku_board_values[row_number][j] != 0:
                        cell = Cell(
                            cell_number, sudoku_board_values[row_number][j], row_number, j)
                    else:
                        cell = Cell(cell_number, '', row_number, j)
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
                            cell_number, sudoku_board_values[row_number][j], row_number, j)
                    else:
                        cell = Cell(cell_number, '', row_number, j)
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
                            cell_number, sudoku_board_values[row_number][j], row_number, j)
                    else:
                        cell = Cell(cell_number, '', row_number, j)
                    cell_number += 1
                    cell_objects.append(cell)
            square = Square(square_number, cell_objects)
            square_objects.append(square)
            square_number += 1
            offset_value += 3


def update_cell_value(cell_data):
    global square_objects
    global previous_state
    global sudoku_board_list
    
    row_wise_sudoku = convert_square_wise_to_row_wise(
        sudoku_board_list)
    column_wise_sudoku = convert_square_wise_to_column_wise(
        sudoku_board_list)


    user_cell_object = Cell(int(cell_data["cellNumber"]), int(cell_data["value"]), int(cell_data["rowNumber"]),
                        int(cell_data["columnNumber"]))
    
    cell_objects = square_objects[int(cell_data["squareNumber"])].get_squares_cell()
    
    square_elements = [cell.get_cell_value() for cell in cell_objects]
    row_elements = row_wise_sudoku[user_cell_object.get_row_number()]
    row_elements = [cell["value"] for cell in row_elements]
    
    column_elements = column_wise_sudoku[user_cell_object.get_column_number()]
    column_elements = [cell["value"] for cell in column_elements]
    
    if (user_cell_object.get_cell_value() not in square_elements) and (user_cell_object.get_cell_value() not in column_elements) \
            and (user_cell_object.get_cell_value() not in row_elements):
        
        cell = cell_objects[user_cell_object.get_cell_number()]
        previous_state.append(copy.deepcopy(cell_objects[user_cell_object.get_cell_number()]))
        cell.set_cell_value(user_cell_object.get_cell_value())
        
        return True
    else:
        return False
    

def restore_previous_state():
    global previous_state
    global square_objects

    if len(previous_state) != 0:
        previous_cell_object = previous_state.pop()
        for square in square_objects:
            for cell in square:
                if (cell.get_column_number() == previous_cell_object.get_column_number()) and \
                    (cell.get_row_number() == previous_cell_object.get_row_number()):    
                    cell.set_cell_value(previous_cell_object.get_cell_value())
                    cell_dictionary = cell.get_dictionary_representation()
                    cell_dictionary["squareNumber"] = square.get_square_number()
                    return cell_dictionary
    else:
        return False

def create_game_environment(sudoku_board_values):
    
    global sudoku_board
    global sudoku_board_list
    global square_objects

    print(sudoku_board_values)
    map_row_to_objects(sudoku_board_values)

    sudoku_board = Board(square_objects)
    sudoku_board_list = sudoku_board.get_list_representation()

    row_wise_sudoku = convert_square_wise_to_row_wise(
        sudoku_board_list)

    column_wise_sudoku = convert_square_wise_to_column_wise(
        sudoku_board_list)

    return row_wise_sudoku
    

def get_sudoku_board():
    return SudokuGenerator.final_grid