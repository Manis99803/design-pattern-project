import SudokuGenerator
from SudokuSolution import SudokuSolution
from SudokuForm import SudokuForm
from Cell import Cell
from Square import Square
from Board import Board
from User import User
import copy

#Objects
user = ''
sudoku_form = ''
sudoku_board = ''

# list of list containting the square details, cell details
sudoku_board_list = list()
square_objects = list()
previous_state = list()


def map_row_to_objects(sudoku_board_values, square_objects, diff_cell):
    offset_value = 0
    square_number = 0
    
    for i in range(0, 9, 3):    
        offset_value = 0
        for j in range(0, 3):
            cell_number = 0
            cell_objects = []
            for row_number in range(i, i + 3):
                for k in range(0 + offset_value, 3 + offset_value):
                    if sudoku_board_values[row_number][k] != 0:
                        cell = Cell(
                            cell_number, sudoku_board_values[row_number][k], sudoku_board_values[row_number][k], row_number, k)
                    else:
                        cell = Cell(cell_number, '', diff_cell[(row_number, k)], row_number, k)
                    cell_objects.append(cell)
                    cell_number += 1

            square = Square(square_number, cell_objects)
            square_objects.append(square)
            square_number += 1
            offset_value += 3

def update_cell_value(cell_data):
    global square_objects
    global previous_state
    global sudoku_board_list
    global sudoku_form

    # Means that the user is clearing the value in that particular cell.
    if cell_data["value"] == 0:
        # The actual value is being just set as '' whenever a user sends a value to update cell.
        user_cell_object = Cell(int(cell_data["cellNumber"]), '', '', int(cell_data["rowNumber"]),
                            int(cell_data["columnNumber"]))
    else:
        user_cell_object = Cell(int(cell_data["cellNumber"]), int(cell_data["value"]), '', int(cell_data["rowNumber"]),
                            int(cell_data["columnNumber"]))
    
    
    row_wise_sudoku = sudoku_form.convert_square_wise_to_row_wise()
    column_wise_sudoku = sudoku_form.convert_square_wise_to_column_wise()

    cell_objects = square_objects[int(cell_data["squareNumber"])].get_squares_cell()
    square_elements = [cell.get_cell_value() for cell in cell_objects if cell.get_cell_number() != user_cell_object.get_cell_number()]
    
    row_elements = row_wise_sudoku[user_cell_object.get_row_number()]
    row_elements = [cell["value"] for cell in row_elements if cell["cellNumber"] != user_cell_object.get_cell_number()]
    
    column_elements = column_wise_sudoku[user_cell_object.get_column_number()]
    column_elements = [cell["value"] for cell in column_elements if cell["cellNumber"] != user_cell_object.get_cell_number()]

    # Means that the user is clearing the value in that particular cell.
    if user_cell_object.get_cell_value() == 0:
        cell = cell_objects[user_cell_object.get_cell_number()]
        previous_state.append(copy.deepcopy(cell_objects[user_cell_object.get_cell_number()]))
        cell.set_cell_value(user_cell_object.get_cell_value())

        return True

    elif(user_cell_object.get_cell_value() not in square_elements) and (user_cell_object.get_cell_value() not in column_elements) \
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

def compute_diff_cell(sudoku_board_values, sudoku_solution):
    diff_cell = dict()
    for i in range(9):
        for j in range(9):
            if sudoku_board_values[i][j] != sudoku_solution[i][j]:
                diff_cell[(i, j)] = sudoku_solution[i][j]
    return diff_cell

def create_game_environment(sudoku_board_values):
    
    global sudoku_board_list
    global square_objects
    global sudoku_form
    global sudoku_board

    diff_cell = dict()

    sudoku_solution = get_board_solution(sudoku_board_values)
    diff_cell = compute_diff_cell(sudoku_board_values, sudoku_solution)

    # Mapping row to class structure 
    map_row_to_objects(sudoku_board_values, square_objects, diff_cell)
    
    sudoku_board = Board(square_objects)
    sudoku_board_list = sudoku_board.get_list_representation()
    sudoku_form = SudokuForm(sudoku_board_list)

    row_wise_sudoku = sudoku_form.convert_square_wise_to_row_wise()
    
    return row_wise_sudoku
    
def get_board_solution(row_wise_sudoku):
    sudoku_solution = []
    row_wise_sudoku = SudokuGenerator.final_grid
    sudoku_string = [str(cell_value) for row in row_wise_sudoku for cell_value in row]
    sudoku_solution = SudokuSolution(''.join(sudoku_string))
    row_wise_solved_sudoku = sudoku_solution.get_solved_puzzle()
    return row_wise_solved_sudoku

def get_sudoku_board():
    return SudokuGenerator.final_grid

def check_board_status():
    sudoku_board.check_board_status()

def get_resultant_cell_value(cell_data):
    global square_objects
    row_number = cell_data["rowNumber"]
    column_number = cell_data["columnNumber"]

    value = dict()
    for square in square_objects:
        for cell in square:
            if ((cell.get_row_number() == row_number) and (cell.get_column_number() == column_number)):
                value["value"] = cell.get_actual_value()
                return value

def create_user_object(user_data):
    global user
    user = User(user_data["name"], user_data["password"])

def delete_user_object():
    global user
    del(user)
    User.reset()
    user = ''
    
