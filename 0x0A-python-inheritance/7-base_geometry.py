#!/usr/bin/python3
''' Improve Geometry '''


class BaseGeometry:
    ''' base geometry class '''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' validates value
        Args:
        name: the name
        value: the value '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
