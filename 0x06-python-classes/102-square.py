#!/usr/bin/python3
""" class Square that defines a square """


class Square:

    """ class Square that defines a square by: (based on 3-square.py) """

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

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()

    def __ne__(self, other):
        if isinstance(other, Square):
            return self.area() != other.area()

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()

    def __le__(self, other):
        if isinstance(other, Square):
            return self.area() <= other.area()

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area() >= other.area()
