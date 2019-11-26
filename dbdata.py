from User import User
import sqlite3 as db

# Need a better way to handle this
user = ''

def check_user_name_in_db(user_object):
    global user
    connection_state = db.connect("Sudoku.db")
    cursor = connection_state.cursor()

    user = User(user_object["name"], user_object["password"])
    print(user.get_dictionary_representation())

    query = "SELECT * from User where name = ? and password = ?"
    cursor.execute(query, [user.get_user_name(), user.get_user_password()])

    data = cursor.fetchone()
    connection_state.commit()
    connection_state.close()

    if data == None:
        return False
    
    return True


def save_game(row_wise_sudoku):
    connection_state = db.connect("Sudoku.db")
    cursor = connection_state.cursor()
    
    board_values = [i for row in row_wise_sudoku for i in row]
    board_values.insert(0, "Manish")
    
    cursor.execute("INSERT INTO Board VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
    ?, ?, ?, ?, ?, ?)", board_values)

    connection_state.commit()
    connection_state.close()


def get_older_game(user_name):
    
    connection_state = db.connect("Sudoku.db")
    cursor = connection_state.cursor()

    query = "SELECT * FROM Board where name = ?"
    cursor.execute(query, [user_name,])

    db_board_values = cursor.fetchall()[0]

    sudoku_board_values = list()
    row = list()
    
    for cell_number in range(1, 82):
        row.append(db_board_values[cell_number])
        if cell_number % 9 == 0:
            sudoku_board_values.append(row)
            row = []
    
    print(sudoku_board_values)
    return sudoku_board_values