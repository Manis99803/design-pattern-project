class Cell():
    def __init__(self, cell_number, value):
        self.cell_number = cell_number
        self.value = value
    
    def get_cell_number(self):
        return self.cell_number
    
    def get_cell_value(self):
        return self.value
    
    def set_cell_value(self, value):
        self.value = value

    def get_dictionary_representation(self):
        self.cell_dict = dict()
        self.cell_dict["cellNumber"] = self.cell_number
        self.cell_dict["value"] = self.value
        return self.cell_dict