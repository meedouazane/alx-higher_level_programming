#!/usr/bin/python3
""" class Rectangle that defines a rectangle """


class Rectangle:
    """ class Rectangle that defines a rectangle by:
        (based on 0-rectangle.py)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the data.
        Args:
        width : must be an integer, bigger than 0
        height : must be an integer, bigger than 0
        """
        Rectangle.number_of_instances += 1
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
                rtn += str(self.print_symbol)
            if i != self.__height - 1:
                rtn += "\n"
        return rtn

    def __repr__(self):
        ''' return a string representation of the rectangle '''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        ''' Print the message when instance is deleted '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' returns the biggest rectangle based on the area
            Args:
            rect_1:  must be an instance of Rectangle
            rect_2:  must be an instance of Rectangle
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        ''' returns a new Rectangle instance
            Args:
                size: size of the square
        '''
        return cls(size, size)
