#!/usr/bin/python3
''' class Rectangle that inherits from Base '''
from models.base import Base


class Rectangle(Base):
    ''' class Rectangle that inherits from Base '''
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the data.
        Args:
        width: the width of rectangle
        height: the height of rectangle
        x:
        y:
        id: the id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' width getter '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width setter, must be int and < 0 '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        ''' height getter '''
        return height.__width

    @height.setter
    def height(self, value):
        ''' height setter, must be int and < 0 '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        ''' x getter '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' x setter, must be int and bigger than 0 '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        ''' y getter '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' y setter, must be int and bigger than 0 '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' returns the area value of the Rectangle instance. '''
        return self.__width * self.__height

    def display(self):
        ''' prints in stdout the Rectangle instance with the character # '''
        for u in range(0, self.__y):
            print()
        for x in range(0, self.__height):
            for i in range(0, self.__x):
                    print(" ", end="")
            for y in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        '''returns [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        return  f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        ''' public method using args '''
        if len(args) == 0:
            self.id = kwargs.get('id', self.id)
            self.__width = kwargs.get('width', self.__width)
            self.__height = kwargs.get('height', self.__height)
            self.__x = kwargs.get('x', self.__x)
            self.__y = kwargs.get('y', self.__y)
        else:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        ''' returns the dictionary representation of a Rectangle '''
        return { 
                'id': self.id,
                'width': self.__width,
                'height': self.__height,
                'x': self.__x,
                'y': self.__y
                }

