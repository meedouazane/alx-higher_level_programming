#!/usr/bin/python3
'''  function that divides all elements of a matrix. '''


def matrix_divided(matrix, div):

    ''' Divide a matrix '''
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
        return
    for lst in matrix:
        if not isinstance(lst, list):
            raise TypeError(
                "matrix must be a matrix"
                " (list of lists) of integers/floats")
            return
        for i in lst:
            if not (isinstance(i, int) or isinstance(i, float)):
                raise TypeError(
                    "matrix must be a matrix "
                    "(list of lists) of integers/floats")
                return
    size = len(matrix[0])
    for lst in matrix:
        if size != len(lst):
            raise TypeError("Each row of the matrix must have the same size")
            return

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")

    new_list = []
    for lst in matrix:
        row = []
        for i in lst:
            d = float(i) / div
            d = round(d, 2)
            row.append(d)
        new_list.append(row)
    return new_list

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
