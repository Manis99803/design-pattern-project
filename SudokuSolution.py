from sudokulib.grid import StringGrid
from sudokulib.solver import SudokuSolver
import io
from contextlib import redirect_stdout
import re

class SudokuSolution:
    ''' row_wise_solved_sudoku should be a string with with the missing values represented either as DOT(.) or ZERO(0)'''
    ''' Example : [[1, 0, 3], [0, 2, 1]] = "102021 or 1.2.21" '''

    def __init__(self, row_wise_unsolved_sudoku):
        self.row_wise_unsolved_sudoku = row_wise_unsolved_sudoku

    def get_solved_puzzle(self):
        solver = SudokuSolver(self.row_wise_unsolved_sudoku, grid_class=StringGrid)
        solver.run()
        self.solved_string = str(solver)

        ansi_escape = re.compile(r'''
                        \x1B    # ESC
                        [@-_]   # 7-bit C1 Fe
                        [0-?]*  # Parameter bytes
                        [ -/]*  # Intermediate bytes
                        [@-~]   # Final byte
                    ''', re.VERBOSE)

        result = ansi_escape.sub('', self.solved_string)

        self.row_wise_solved_sudoku = list()
        self.row_elements = []

        for value in result:
            try:
                cell_value = int(value)
                self.row_elements.append(cell_value)
                if len(self.row_elements) == 9:
                    self.row_wise_solved_sudoku.append(self.row_elements)
                    self.row_elements = []
            except:
                continue

        return self.row_wise_solved_sudoku






