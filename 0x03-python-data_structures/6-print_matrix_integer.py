#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        for element in row:
            if i == len(row) - 1:
                print(element, end='')
            else:
                print(element, end=' ')
                i = i + 1
        print()
