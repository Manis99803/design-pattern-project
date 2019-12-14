from SudokuForm import SudokuForm
from SudokuSolution import SudokuSolution
from SudokuBoardGenerator import SudokuBoardGenerator
from dbdata import DataBase
from Board import Board
from Cell import Cell
import copy
from Square import Square

class GameLogic:
    def __init__(self, game_environment):
        self.game_environment = game_environment

    def check_board_status(self):
        return self.game_environment.get_sudoku_board_object().check_board_status()
    
    def get_sudoku_board(self):
        return SudokuBoardGenerator.get_sudoku_board()
        
    def get_resultant_cell_value(self, cell_data):
        return self.game_environment.get_sudoku_board_object().get_resultant_cell_value(cell_data)


class GameEnvironment:
    def __init__(self, sudoku_board_values):
        self.sudoku_board_values = sudoku_board_values
    
    def create_game_environment(self):
        
        diff_cell = dict()
    
        self.sudoku_solution = SudokuSolution(self.sudoku_board_values)
        print(self.sudoku_solution)
        diff_cell = self.sudoku_solution.compute_diff_cell()

        map_objects = MapObjects(self.sudoku_board_values)
        # Mapping row to class structure 
        square_objects = map_objects.map_row_to_objects(diff_cell)
    
        self.sudoku_board = Board(square_objects)
        sudoku_board_list = self.sudoku_board.get_list_representation()
        self.sudoku_form = SudokuForm(sudoku_board_list)

        row_wise_sudoku = self.sudoku_form.convert_square_wise_to_row_wise()
    
        return row_wise_sudoku

    def get_sudoku_form_object(self):
        return self.sudoku_form

    def get_sudoku_board_object(self):
        return self.sudoku_board


class MapObjects:
    def __init__(self, sudoku_board_values):
        self.sudoku_board_values = sudoku_board_values

    def map_row_to_objects(self, diff_cell):

        offset_value = 0
        square_number = 0
        
        square_objects = []
        for i in range(0, 9, 3):    
            offset_value = 0
            for j in range(0, 3):
                cell_number = 0
                cell_objects = []
                for row_number in range(i, i + 3):
                    for k in range(0 + offset_value, 3 + offset_value):
                        if self.sudoku_board_values[row_number][k] != 0:
                            cell = Cell(
                                cell_number, self.sudoku_board_values[row_number][k], self.sudoku_board_values[row_number][k], row_number, k)
                        else:
                            cell = Cell(cell_number, '', diff_cell[(row_number, k)], row_number, k)
                        cell_objects.append(cell)
                        cell_number += 1

                square = Square(square_number, cell_objects)
                square_objects.append(square)
                square_number += 1
                offset_value += 3

        return square_objects


class StateChange:
    def __init__(self, game_environment):
        self.previous_state = []
        self.game_environment = game_environment

    def update_cell_value(self, cell_data):
    
        # Means that the user is clearing the value in that particular cell.
        if cell_data["value"] == 0:
            # The actual value is being just set as '' whenever a user sends a value to update cell.
            user_cell_object = Cell(int(cell_data["cellNumber"]), '', '', int(cell_data["rowNumber"]),
                                int(cell_data["columnNumber"]))
        else:
            user_cell_object = Cell(int(cell_data["cellNumber"]), int(cell_data["value"]), '', int(cell_data["rowNumber"]),
                                int(cell_data["columnNumber"]))
        
        
        row_wise_sudoku = self.game_environment.get_sudoku_form_object().convert_square_wise_to_row_wise()
        column_wise_sudoku = self.game_environment.get_sudoku_form_object().convert_square_wise_to_column_wise()

        cell_objects = self.game_environment.get_sudoku_board_object().get_square_objects()[int(cell_data["squareNumber"])].get_squares_cell()



        square_elements = [cell.get_cell_value() for cell in cell_objects if cell.get_cell_number() != user_cell_object.get_cell_number()]
        
        row_elements = row_wise_sudoku[user_cell_object.get_row_number()]
        row_elements = [cell["value"] for cell in row_elements if cell["cellNumber"] != user_cell_object.get_cell_number()]
        
        column_elements = column_wise_sudoku[user_cell_object.get_column_number()]
        column_elements = [cell["value"] for cell in column_elements if cell["cellNumber"] != user_cell_object.get_cell_number()]

        # Means that the user is clearing the value in that particular cell.
        
        if user_cell_object.get_cell_value() == 0:
            cell = cell_objects[user_cell_object.get_cell_number()]
            self.previous_state.append(copy.deepcopy(cell_objects[user_cell_object.get_cell_number()]))
            cell.set_cell_value(user_cell_object.get_cell_value())

            return True

        elif(user_cell_object.get_cell_value() not in square_elements) and (user_cell_object.get_cell_value() not in column_elements) \
                and (user_cell_object.get_cell_value() not in row_elements):
            
            cell = cell_objects[user_cell_object.get_cell_number()]
            self.previous_state.append(copy.deepcopy(cell_objects[user_cell_object.get_cell_number()]))
            cell.set_cell_value(user_cell_object.get_cell_value())
            
            return True
        
        else:
            self.previous_state.append(copy.deepcopy(cell_objects[user_cell_object.get_cell_number()]))
            return False

    def restore_previous_state(self):
    
        if len(self.previous_state) != 0:
            previous_cell_object = self.previous_state.pop()
            for square in self.game_environment.get_sudoku_board_object().get_square_objects():
                for cell in square:
                    if (cell.get_column_number() == previous_cell_object.get_column_number()) and \
                        (cell.get_row_number() == previous_cell_object.get_row_number()):    
                        cell.set_cell_value(previous_cell_object.get_cell_value())
                        cell_dictionary = cell.get_dictionary_representation()
                        cell_dictionary["squareNumber"] = square.get_square_number()
                        return cell_dictionary
        # else:
        #     return False


class Game:
    def __init__(self, data_base_name):
        self.data_base_object = DataBase(data_base_name)
        self.game_environment = ''
        self.game_logic = ''
        self.state_change = ''
        self.user_object = ''
        
    def set_values(self):
        self.set_game_environment_object()
        self.set_game_logic_object()
        self.set_state_change_object()
        return self.sudoku_board_values

    def set_board_values(self, sudoku_board_values):
        self.sudoku_board_values = sudoku_board_values
    
    def generate_board_values(self):
        self.sudoku_board_values = SudokuBoardGenerator.get_sudoku_board()

    def get_data_base_object(self):
        return self.data_base_object
    
    def get_game_environment_object(self):
        return self.game_environment

    def set_game_environment_object(self):
        self.game_environment = GameEnvironment(self.sudoku_board_values)

    def get_game_logic_object(self):
        return self.game_logic

    def set_game_logic_object(self):
        self.game_logic = GameLogic(self.game_environment)

    def get_state_change_object(self):
        return self.state_change

    def set_state_change_object(self):
        self.state_change = StateChange(self.game_environment)
    
    def get_user_object(self):
        return self.user_object

    def set_user_object(self, user_object):
        self.user_object = user_object