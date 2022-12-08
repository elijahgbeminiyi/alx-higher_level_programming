def square_matrix_simple(matrix=[]):
    new_matrix = []
    for element in matrix:
        square = list(map(lambda x: x**2, element))
        new_matrix.append(square)
    return new_matrix
