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
        return self.__width

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
        return self.__height

    @height.setter
    def height(self, value):
        ''' height : must be an integer, bigger than 0 '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        ''' returns the rectangle area '''
        return self.width * self.height

    def perimeter(self):
        '''  returns the rectangle perimeter '''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        ''' print the rectangle with the character # '''
        rtn = ""
        if self.width == 0 or self.height == 0:
            return rtn
        for i in range(0, self.__height):
            for x in range(0, self.__width):
                rtn += "#"
            if i != self.__height - 1:
                rtn += "\n"
        return rtn
