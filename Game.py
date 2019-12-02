from dbdata import DataBase
from flask import Flask, render_template, jsonify, request, session
import SudokuGameLogic
from User import User
from GameLogic import GameLogic

app = Flask(__name__)

data_base_object = ''
game_logic = ''

def LoginCheck(function_name):
    if User.instance != None:
        def function(*args):
            return function_name(*args)
        return function
    else:
        return login


@app.route("/api/v1/user_signup", methods=["POST"])
def user_signup():
    if request.method == "POST":
        user_data = request.get_json()
        global data_base_object
        if not data_base_object.check_user_name_in_db(user_data):
            data_base_object.add_user_to_db(user_data)
            return jsonify({}), 200
        else:
            return jsonify({}), 400
    else:
        return jsonify({}), 405


@app.route("/api/v1/user_login", methods = ["POST"])
def user_login():
    if request.method == "POST":
        global data_base_object
        user_data = request.get_json()
        if data_base_object.check_user_name_in_db(user_data):
            SudokuGameLogic.create_user_object(user_data)
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
        global game_logic
        status = game_logic.update_cell_value(data)
    
        if status:
            # Could be optimised by having counter
            if not game_logic.check_board_status():
                return jsonify({"message": "0"}), 200       # 0 means the game is still on and 1 means the user is winner.
            else:
                return jsonify({"message" : "1"}), 200
        else:
            return jsonify({}), 400
    else:
        return jsonify({}), 405


@app.route("/api/v1/restore_previous_state", methods = ["POST"])
def restore_previous_state():
    if request.method == "POST":
        global game_logic
        previous_cell = game_logic.restore_previous_state()
        if previous_cell == False:
            return jsonify({}), 400
        else:
            return jsonify(previous_cell), 200
    else:
        return jsonify({}), 405


@app.route("/api/v1/save_game", methods = ["POST"])
def save_game():
    if request.method == "POST":
        global data_base_object
        row_wise_sudoku = request.get_json()
        data_base_object.save_game_to_db(row_wise_sudoku)
        return jsonify({}), 200
    else:
        return jsonify({}), 405


@app.route('/api/v1/get_hint', methods = ['POST'])
def get_hint():
    if request.method == 'POST':
        cell_data = request.get_json()
        global game_logic
        value = game_logic.get_resultant_cell_value(cell_data)
        return jsonify(value), 200

    else:
        return jsonify({}), 405


@app.route("/login", methods = ["GET"])
def login():
    return render_template("Login.html")


@app.route("/logout", methods=["GET"])
def logout():
    SudokuGameLogic.delete_user_object()

@app.route("/signup")
def signup():
    return render_template("Signup.html")

@app.route("/older_game")
# @LoginCheck
def older_game():
    user_name = "Manish"
    global data_base_object
    sudoku_board_values = data_base_object.get_older_game_from_db(user_name)
    row_wise_sudoku = SudokuGameLogic.create_game_environment(sudoku_board_values)
    return render_template("Board.html", row_wise_board = row_wise_sudoku)


@app.route("/new_game")
# @LoginCheck
def new_game():
    
    global game_logic
    sudoku_board_values = SudokuGameLogic.get_sudoku_board()
    game_logic = GameLogic(sudoku_board_values)
    row_wise_sudoku = game_logic.create_game_environment()

    return render_template("Board.html", row_wise_board = row_wise_sudoku)

if __name__ == "__main__":
    app.secret_key = "123456789"
    data_base_object = DataBase("Sudoku.db")
    app.run(debug = True)
    

