#!/usr/bin/paython3
def square(x):
    return x ** 2

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for i in range(len(matrix)):
        new_matrix[i] = list(map(square, matrix[i]))
    return new_matrix
