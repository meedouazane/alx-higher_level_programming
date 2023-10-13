#!/usr/bin/python3
'''  the class Square that inherits from Rectangle '''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''  the class Square that inherits from Rectangle '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' Initializes the data: 
        args:
        size: The width and height from rectangle.
        x = x from rectangle
        y = y from rectangle
        id = id from rectangle
        '''
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        ''' getter for size '''
        return self.__width

    @size.setter
    def size(self, value):
        ''' setter for size '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        ''' overloading __str__ method  [Square] '''
        return  f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        ''' Update of the class Square '''
        if len(args) == 0:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
        else:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
    def to_dictionary(self):
        ''' returns the dictionary representation of a Square '''
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
