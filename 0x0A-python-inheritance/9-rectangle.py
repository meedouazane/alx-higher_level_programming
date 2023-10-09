#!/usr/bin/python3
''' Improve Geometry '''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' class Rectangle that inherits from BaseGeometry '''

    def __init__(self, width, height):
        ''' Instantiation with width and height
        Args:
            width: the width of rectangle
            height: the height of rectangle
        '''

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        ''' calculate the area of rectangle '''
        return self.__width * self.__height

    def __str__(self):
        ''' print the rectangle '''
        txt = "[Rectangle] "
        txt += str(self.__width) + "/" + str(self.__height)
        return txt
