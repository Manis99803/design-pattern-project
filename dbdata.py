from User import User
import sqlite3 as db

class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection_state = db.connect(self.db_name, check_same_thread = False)
        self.cursor = self.connection_state.cursor()
    
    def check_user_name_in_db(self, user_object):
        query = "SELECT * from User where name = ? and password = ?"
        self.cursor.execute(query, [user_object["name"], user_object["password"]])

        data = self.cursor.fetchone()
        self.connection_state.commit()

        if data == None:
            return False
        
        return True

    def add_user_to_db(self, user_object):
        query = "INSERT INTO User VALUES (?, ?)"
        self.cursor.execute(query, [user_object["name"], user_object["password"], ])
        self.connection_state.commit()

    def save_game_to_db(self, row_wise_sudoku, user_name):
        
        query = "SELECT count(*) FROM Board where name = ?"
        self.cursor.execute(query, [user_name])
        number_of_games = self.cursor.fetchone()
        game_number = int()

        if number_of_games == None:
            game_number = 1
        else:
            game_number += 1

        board_values = [i for row in row_wise_sudoku for i in row]
        board_values.insert(0, user_name)
        board_values.insert(1, game_number)
        
        self.cursor.execute("INSERT INTO Board VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
        ?, ?, ?, ?, ?, ?, ?)", board_values)

        self.connection_state.commit()

    def get_older_game_from_db(self, user_name):
    
        query = "SELECT * FROM Board where name = ?"
        self.cursor.execute(query, [user_name,])
        boards = self.cursor.fetchall()
        print(boards)
        if len(boards) == 0:
            return False
        
        sudoku_games = list()
        for board in boards:
            row_wise_sudoku = list()
            row = list()
            for cell_number in range(2, 83):
                row.append(board[cell_number])
                if cell_number % 9 == 0:
                    row_wise_sudoku.append(row)
                    row = []
            sudoku_games.append(row_wise_sudoku)
        
        return sudoku_games
