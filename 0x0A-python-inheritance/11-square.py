#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
'''  Square #1 '''


class Square(Rectangle):
    ''' Square that inherits from Rectangle (9-rectangle.py) '''
    def __init__(self, size):
        ''' size must be int bigger than 0 '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        ''' calculate the area '''
        return self.__size ** 2

    def __str__(self):
        ''' print the rectangle '''
        txt = "[Rectangle] "
        txt += str(self.__size) + "/" + str(self.__size)
        return txt
