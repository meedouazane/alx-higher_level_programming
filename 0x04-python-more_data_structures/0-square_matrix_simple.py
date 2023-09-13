#!/usr/bin/paython3
def square(x):
    return x ** 2
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(lambda row: list(map(square, row)), matrix))
    return new_matrix
