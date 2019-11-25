def get_row_number(square_number, cell_number):
    if square_number == cell_number:
        return (square_number, cell_number)
    quotient = square_number // 3
    remainder = square_number % 3
    print(quotient, remainder)
    if quotient == 0 and remainder == 0:
        return (cell_number % 3 , cell_number % 3)
    elif quotient == 0 and remainder == 1:
        return (cell_number % 3, cell_number % 3 + 3)
    elif quotient == 0 and remainder == 2:
        return (cell_number % 3, cell_number % 3 + 6)
    elif quotient == 1 and remainder == 0:
        return (cell_number % 3 + 2 , cell_number % 3)
    elif quotient == 1 and remainder == 1:
        return (cell_number % 3 + 3, cell_number % 3 + 3)
    elif quotient == 1 and remainder == 2:
        return (cell_number % 3 + 2, cell_number % 3 + 6)
    elif quotient == 2 and remainder == 0:
        return (cell_number % 3 + 6, cell_number % 3)
    elif quotient == 2 and remainder == 1:
        return (cell_number % 3 + 2, cell_number % 3 + 3)
    else:
        return (cell_number % 3 + 6, cell_number % 3 + 6)
    
    
# print(get_row_number(0, 0))
# print(get_row_number(0, 1))
# print(get_row_number(1, 1))
# print(get_row_number(8, 7))
# print(get_row_number(5, 5))
# print(get_row_number(6, 0))
# print(get_row_number(8, 8))
    
