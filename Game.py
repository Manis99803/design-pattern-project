from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from User import User
import json
from GameLogic import Game

app = Flask(__name__)

user = ''
game_object = ''

def LoginCheck(function_name):
    if User.instance != None:
        def function(*args):
            return function_name(*args)
        return function
    else:
        return login


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route("/api/v1/user_signup", methods=["POST"])
def user_signup():
    if request.method == "POST":
        user_data = dict()
        user_data["name"] = request.form["email"]
        user_data["password"] = request.form["pass"]
        
        global game_object
        if not game_object.get_data_base_object().check_user_name_in_db(user_data):
            game_object.get_data_base_object().add_user_to_db(user_data)
            return redirect(url_for("login"))
        else:
            return jsonify(url_for("Signup"))
    else:
        return jsonify({}), 405


@app.route("/api/v1/user_login", methods = ["POST"])
def user_login():
    if request.method == "POST":
        global user
        
        global game_object
        user_data = dict()
        user_data["name"] = request.form["email"]
        user_data["password"] = request.form["pass"]

        if game_object.get_data_base_object().check_user_name_in_db(user_data):
            user = User(user_data["name"], user_data["password"])     
            session["name"] = user_data["name"]
            session["logged_in"] = True
            return redirect(url_for("game_history"))
        else:
            return render_template("login.html")
    else:
        return jsonify({}), 405


@app.route("/api/v1/set_cell_value", methods = ["POST"])
def set_cell_value():
    if request.method == "POST":
        data = request.get_json()
        global game_object
        status = game_object.get_state_change_object().update_cell_value(data)
    
        if status:
            # Could be optimised by having counter
            if not game_object.get_game_logic_object().check_board_status():
                return jsonify({"message": "0"}), 200       # 0 means the game is still on and 1 means the user is winner.
            else:
                return jsonify({"message" : "1"}), 200
        else:
            return jsonify({"message" : "2"}), 200
    else:
        return jsonify({}), 405


@app.route("/api/v1/restore_previous_state", methods = ["POST"])
def restore_previous_state():
    if request.method == "POST":
        global game_object
        previous_cell = game_object.get_state_change_object().restore_previous_state()

        if previous_cell == False:
            return jsonify({}), 400
        else:
            return jsonify(previous_cell), 200
    else:
        return jsonify({}), 405


@app.route("/api/v1/save_game", methods = ["POST"])
def save_game():
    if request.method == "POST":
        global game_object
        row_wise_sudoku = request.get_json()
        game_object.get_data_base_object().save_game_to_db(row_wise_sudoku, session.get("name"))
        return jsonify({}), 200
    else:
        return jsonify({}), 405


@app.route('/api/v1/get_hint', methods = ['POST'])
def get_hint():
    if request.method == 'POST':
        cell_data = request.get_json()
        global game_object
        value = game_object.get_game_environment_object().get_sudoku_board_object().get_resultant_cell_value(cell_data)
        return jsonify(value), 200

    else:
        return jsonify({}), 405


@app.route("/login", methods = ["GET"])
def login():
    return render_template("login.html")


@app.route("/logout", methods=["GET"])
def logout():
    global user
    del(user)
    User.reset()
    user = ''
    return redirect(url_for("login"))
    

@app.route("/game_history")
def game_history():
    
    global game_object
    sudoku_games = game_object.get_data_base_object().get_older_game_from_db(session.get("name"))
    # sudoku_games = game_object.get_data_base_object().get_older_game_from_db("msoni6226@gmail.com")
    if sudoku_games == False:
        return redirect(url_for("new_game"))
    else:
        return render_template("previous_games.html", sudoku_games = sudoku_games)

@app.route("/Signup")
def Signup():
    return render_template("signup.html")

@app.route("/older_game/<game_number>")
# @LoginCheck
def older_game(game_number):
    user_name = "msoni6226@gmail.com"
    global game_object
    
    sudoku_board_values = game_object.get_data_base_object().get_specific_game_from_db(user_name, int(game_number))
    print(sudoku_board_values)
    game_object.set_board_values(sudoku_board_values)
    game_object.set_values()

    row_wise_sudoku = game_object.get_game_environment_object().create_game_environment()

    return render_template("sudoku.html", row_wise_board = row_wise_sudoku)


@app.route("/new_game")
# @LoginCheck
def new_game():
    global game_object
    game_object.generate_board_values()
    game_object.set_values()

    row_wise_sudoku = game_object.get_game_environment_object().create_game_environment()
    return render_template("sudoku.html", row_wise_board = row_wise_sudoku)

if __name__ == "__main__":
    app.secret_key = "123456789"
    game_object = Game("Sudoku.db")
    app.run(debug = True)
    

