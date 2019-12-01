class Board:
    def __init__(self, square_objects):
        self.square_objects = square_objects

    def get_square_objects(self):
        return self.square_objects

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.square_objects):
            self.i += 1
            return self.square_objects[self.i - 1]
        else:
            raise StopIteration

    def get_list_representation(self):
        self.board_list = []
        for square in self.square_objects:
            self.board_list.append(square.get_dictionary_representation())

        return self.board_list

    def check_board_status(self):
        for square in self.square_objects:
            for cell in square:
                if cell.get_cell_value() == '':
                    return False

        return True