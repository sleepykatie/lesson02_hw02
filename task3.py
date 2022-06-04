def type_checker(object):
    if type(object) == Cell:
        return True
    else:
        return False


class Cell:

    def __init__(self, num_units_in_cell):
        if type(num_units_in_cell) != int:
            raise TypeError('Number of cells must be integer')
        if num_units_in_cell <= 0:
            raise ValueError('Number of cells must be positive')
        else:
            self.num_units_in_cell = num_units_in_cell

    def __add__(self, other):
        if type_checker(self) == True and type_checker(other) == True:
            return Cell(self.num_units_in_cell + other.num_units_in_cell)

    def __sub__(self, other):
        if type_checker(self) == True and type_checker(other) == True:
            if (self.num_units_in_cell - other.num_units_in_cell) > 0:
                return Cell(self.num_units_in_cell - other.num_units_in_cell)
            elif (other.num_units_in_cell - self.num_units_in_cell) > 0:
                return Cell(other.num_units_in_cell - self.num_units_in_cell)
            else:
                raise ValueError('The difference is less than zero')

    def __mul__(self, other):
        if type_checker(self) == True and type_checker(other) == True:
            return Cell(self.num_units_in_cell * other.num_units_in_cell)

    def __floordiv__(self, other):
        if type_checker(self) == True and type_checker(other) == True:
            if self.num_units_in_cell > other.num_units_in_cell:
                return Cell(self.num_units_in_cell // other.num_units_in_cell)
            else:
                return Cell(other.num_units_in_cell // self.num_units_in_cell)

    def __str__(self):
        return f'Number of units in cell - {self.num_units_in_cell}.'

    @staticmethod
    def make_order(class_object, cells_in_row):
        # class_object = Cell(num_units_in_cell)
        # cells_in_row = 4
        num_of_rows = class_object.num_units_in_cell // cells_in_row
        row = '*' * cells_in_row
        if class_object.num_units_in_cell % cells_in_row == 0:
            return (row + "\\n") * (num_of_rows - 1) + row
        else:
            cells_in_last_row = class_object.num_units_in_cell % cells_in_row
            return (row + "\\n") * num_of_rows + '*' * cells_in_last_row


cell01 = Cell(6)
cell02 = Cell(12)
print(cell01, cell02)
print(cell01 + cell02, type(cell01 + cell02))
print(cell01 - cell02, type(cell01 - cell02))
print(cell01 * cell02, type(cell01 * cell02))
print(cell01 // cell02, type(cell01 // cell02))

print(Cell.make_order(cell01, 4))
print(Cell.make_order(cell02, 4))
