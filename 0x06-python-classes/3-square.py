#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """ class Square that defines a square by: (based on 1-square.py) """
    def __init__(self, size=0):

        """ Private instance attribute: size
        Args:
        size : is less than 0, raise a ValueError exception with
        the message size must be >= 0
        """
        self.__size = True
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ the current square area """
        return self.__size ** 2
