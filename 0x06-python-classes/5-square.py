#!/usr/bin/python3
""" class Square that defines a square """


class Square:

    """ class Square that defines a square by: (based on 5-square.py) """

    def __init__(self, size=0):
        """Initializes the data.
        Args:
        size : must be an integer, otherwise raise a TypeError
               if size is less than 0, raise a ValueError
        """
        self.__size = size

    @property
    def size(self):
        """ property def size(self): to retrieve it """
        return self.__size

    @size.setter
    def size(self, value):
        """ must be an integer, otherwise raise a TypeError
        if size is less than 0, raise a ValueError
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ the current square area """
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for x in range(0, self.__size):
                    print("#", end="")
                print()
