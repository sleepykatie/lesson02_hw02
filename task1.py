class Matrix:

    def __init__(self, matrix_data):
        self.matrix_data = matrix_data
        for n in range(0, len(self.matrix_data)):
            check_length = len(self.matrix_data[0])
            if len(self.matrix_data[n]) != check_length:
                raise ValueError('Check data!')

    def __str__(self):
        row = ''
        for el in self.matrix_data:
            row += '| '
            for num in el:
                row += f'{num} '
            row += '|\n'
        return row

    def __add__(self, other):
        if len(self.matrix_data) != len(other.matrix_data) \
                or len(self.matrix_data[0]) != len(other.matrix_data[0]):
            raise ValueError('Matrices must be the same size')
        else:
            result_matrix = []
            for i in range(0, len(self.matrix_data)):
                result_row = []
                for j in range(0, len(self.matrix_data[i])):
                    result_el = self.matrix_data[i][j] + other.matrix_data[i][j]
                    result_row.append(result_el)
                result_matrix.append(result_row)
        return Matrix(result_matrix)


matrix_01 = Matrix([[3, 3], [2, 2], [4, 4]])
matrix_02 = Matrix([[1, 1], [1, 1], [1, 1]])
# print(matrix_01)
# print(matrix_02)
print(matrix_01 + matrix_02)
