#!/usr/bin/python3
'''  prints a square with the character # '''


def print_square(size):
    '''
     prints a square with the character #
     size is the size length of the square
    '''

    if (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        for t in range(0, size):
            print("#", end="")
        print('')
