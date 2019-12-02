from Cell import Cell
class Square:
    def __init__(self, square_number, cell_objects):
        self.square_number = square_number
        self.cell_objects = cell_objects
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.cell_objects):
            self.i += 1
            return self.cell_objects[self.i - 1]
        else:
            raise StopIteration
    
    def get_square_number(self):
        return self.square_number

    def get_squares_cell(self):
        return self.cell_objects

    def get_dictionary_representation(self):
        self.square_dictionary = dict()
        self.square_dictionary[self.square_number] = []
        for cell in self.cell_objects:
            self.square_dictionary[self.square_number].append(cell.get_dictionary_representation())

        return self.square_dictionary
