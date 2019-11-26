from Cell import Cell
from Square import Square
from Board import Board
from User import User
import dbdata as db
from flask import Flask, render_template, jsonify, request, session
import SudokuGameLogic

app = Flask(__name__)




def LoginCheck(function_name):
    if User.instance != None:
        def function(*args):
            return function_name(*args)
        return function
    else:
        return login

@app.route("/api/v1/user_login", methods = ["POST"])
def user_login():
    if request.method == "POST":
        user_data = request.get_json()
        if db.check_user_name_in_db(user_data):
            session["name"] = user_data["name"]
            session["logged_in"] = True
            return jsonify({}), 200
        else:
            return jsonify({}), 400
    else:
        return jsonify({}), 405


@app.route("/api/v1/set_cell_value", methods = ["POST"])
def set_cell_value():
    if request.method == "POST":
        data = request.get_json()
        status = SudokuGameLogic.update_cell_value(data)
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



@app.route("/api/v1/save_game", methods = ["POST"])
def save_game():
    if request.method == "POST":
        row_wise_sudoku = request.get_json()
        db.save_game(row_wise_sudoku)
        return jsonify({}), 200
    else:
        return jsonify({}), 405



@app.route("/login", methods = ["GET"])
def login():
    return render_template("Login.html")



@app.route("/older_game")
def older_game():
    user_name = "Manish"
    sudoku_board_values = db.get_older_game(user_name)
    row_wise_sudoku = SudokuGameLogic.create_game_environment(sudoku_board_values)
    return render_template("Board.html", row_wise_board = row_wise_sudoku)


@app.route("/new_game")
# @LoginCheck
def new_game():
    
    sudoku_board_values = SudokuGameLogic.get_sudoku_board()
    print(sudoku_board_values)
    row_wise_sudoku = SudokuGameLogic.create_game_environment(sudoku_board_values)
    
    return render_template("Board.html", row_wise_board = row_wise_sudoku)

if __name__ == "__main__":
    app.secret_key = "123456789"
    app.run(debug = True)
    

