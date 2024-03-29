import sqlite3 as db

connection_state = db.connect("Sudoku.db")
cursor = connection_state.cursor()

cursor.execute('''CREATE TABLE Board
                    (name TEXT,
                    gameNumber INTEGER,
                    cell0 INTEGER,
                    cell1 INTEGER,
                    cell2 INTEGER,
                    cell3 INTEGER,
                    cell4 INTEGER,
                    cell5 INTEGER,
                    cell6 INTEGER,
                    cell7 INTEGER,
                    cell8 INTEGER,
                    cell9 INTEGER,
                    cell10 INTEGER,
                    cell11 INTEGER,
                    cell12 INTEGER,
                    cell13 INTEGER,
                    cell14 INTEGER,
                    cell15 INTEGER,
                    cell16 INTEGER,
                    cell17 INTEGER,
                    cell18 INTEGER,
                    cell19 INTEGER,
                    cell20 INTEGER,
                    cell21 INTEGER,
                    cell22 INTEGER,
                    cell23 INTEGER,
                    cell24 INTEGER,
                    cell25 INTEGER,
                    cell26 INTEGER,
                    cell27 INTEGER,
                    cell28 INTEGER,
                    cell29 INTEGER,
                    cell30 INTEGER,
                    cell31 INTEGER,
                    cell32 INTEGER,
                    cell33 INTEGER,
                    cell34 INTEGER,
                    cell35 INTEGER,
                    cell36 INTEGER,
                    cell37 INTEGER,
                    cell38 INTEGER,
                    cell39 INTEGER,
                    cell40 INTEGER,
                    cell41 INTEGER,
                    cell42 INTEGER,
                    cell43 INTEGER,
                    cell44 INTEGER,
                    cell45 INTEGER,
                    cell46 INTEGER,
                    cell47 INTEGER,
                    cell48 INTEGER,
                    cell49 INTEGER,
                    cell50 INTEGER,
                    cell51 INTEGER,
                    cell52 INTEGER,
                    cell53 INTEGER,
                    cell54 INTEGER,
                    cell55 INTEGER,
                    cell56 INTEGER,
                    cell57 INTEGER,
                    cell58 INTEGER,
                    cell59 INTEGER,
                    cell60 INTEGER,
                    cell61 INTEGER,
                    cell62 INTEGER,
                    cell63 INTEGER,
                    cell64 INTEGER,
                    cell65 INTEGER,
                    cell66 INTEGER,
                    cell67 INTEGER,
                    cell68 INTEGER,
                    cell69 INTEGER,
                    cell70 INTEGER,
                    cell71 INTEGER,
                    cell72 INTEGER,
                    cell73 INTEGER,
                    cell74 INTEGER,
                    cell75 INTEGER,
                    cell76 INTEGER,
                    cell77 INTEGER,
                    cell78 INTEGER,
                    cell79 INTEGER,
                    cell80 INTEGER,
                    PRIMARY KEY(name, gameNumber),
                    FOREIGN KEY (name) REFERENCES User(name)
                    )
                ''')

connection_state.execute('''CREATE TABLE User 
                        (name TEXT PRIMARY KEY,
                        password TEXT)
                        ''')

connection_state.commit()
connection_state.close()
