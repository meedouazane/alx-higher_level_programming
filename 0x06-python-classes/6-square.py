#!/usr/bin/python3
""" class Square that defines a square """


class Square:

    """ class Square that defines a square by: (based on 6-square.py) """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data.
        Args:
        size : must be an integer, otherwise raise a TypeError
               if size is less than 0, raise a ValueError
        position :  must be a tuple of 2 positive integers
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """  to retrieve it """
        return self.__position

    @position.setter
    def position(self, value):
        """position must be a tuple of 2 positive integers,
        otherwise raise a TypeError"""
        if not isinstance(value, tuple) or \
                len(value) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ the current square area """
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.__size == 0:
            print()

        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for t in range(0, self.__size):
                print("#", end="")
            print("")
