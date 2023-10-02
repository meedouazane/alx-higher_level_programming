#!/usr/bin/python3
""" class Rectangle that defines a rectangle """


class Rectangle:
    """ class Rectangle that defines a rectangle by:
        (based on 0-rectangle.py)
    """

    def __init__(self, width=0, height=0):
        """Initializes the data.
        Args:
        width : must be an integer, bigger than 0
        height : must be an integer, bigger than 0
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ property def width(self): to retrieve it """
        return width.__self

    @width.setter
    def width(self, value):
        ''' width : must be an integer, bigger than 0 '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ property def height(self): to retrieve it """
        return height.__self

    @height.setter
    def height(self, value):
        ''' height : must be an integer, bigger than 0 '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
