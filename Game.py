from Cell import Cell
from Square import Square
from Board import Board
from flask import Flask, render_template, jsonify, request
import SudokuGameLogic

app = Flask(__name__)

sudoku_board = []
sudoku_board_list = []

@app.route("/api/v1/set_cell_value", methods = ["POST"])
def set_cell_value():
    if request.method == "POST":
        global sudoku_board
        global sudoku_board_list
        data = request.get_json()
        
        row_wise_sudoku = SudokuGameLogic.convert_square_wise_to_row_wise(
            sudoku_board_list)
        column_wise_sudoku = SudokuGameLogic.convert_square_wise_to_column_wise(
            sudoku_board_list)

        status = SudokuGameLogic.update_cell_value(data, row_wise_sudoku, column_wise_sudoku)
        if status:
            return jsonify({}), 200
        else:
            return jsonify({}), 400
    else:
        return jsonify({}), 405


@app.route("/api/v1/restore_previous_state", methods = ["POST"])
def restore_previous_state():
    if request.method == "POST":
        previous_cell = SudokuGameLogic.restore_previous_state()
        if previous_cell == False:
            return jsonify({}), 400
        else:
            return jsonify(previous_cell), 200
    else:
        return jsonify({}), 405


@app.route("/get_sudoku_board")
def get_sudoku_board():
    global sudoku_board
    global sudoku_board_list
    
    sudoku_board_values = SudokuGameLogic.get_sudoku_board()
    
    SudokuGameLogic.map_row_to_objects(sudoku_board_values)

    sudoku_board = Board(SudokuGameLogic.square_objects)
    sudoku_board_list = sudoku_board.get_list_representation()

    row_wise_sudoku = SudokuGameLogic.convert_square_wise_to_row_wise(sudoku_board_list)
    column_wise_sudoku = SudokuGameLogic.convert_square_wise_to_column_wise(sudoku_board_list)    

    return render_template("Board.html", row_wise_board = row_wise_sudoku)

if __name__ == "__main__":
    app.run(debug = True)
    

