class Cell():
    def __init__(self, cell_number, value, row_number, column_number):
        self.cell_number = cell_number
        self.value = value
        self.row_number = row_number
        self.column_number = column_number
    
    def get_cell_number(self):
        return self.cell_number
    
    def get_cell_value(self):
        return self.value
    
    def set_cell_value(self, value):
        self.value = value

    def get_row_number(self):
        return self.row_number

    def get_column_number(self):
        return self.column_number

    def get_dictionary_representation(self):
        self.cell_dict = dict()
        self.cell_dict["cellNumber"] = self.cell_number
        self.cell_dict["value"] = self.value
        self.cell_dict["rowNumber"] = self.row_number
        self.cell_dict["columnNumber"] = self.column_number
        return self.cell_dict
