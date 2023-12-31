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
