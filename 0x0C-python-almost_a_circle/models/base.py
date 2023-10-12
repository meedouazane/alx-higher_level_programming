#!/usr/bin/python3
'''  the “base” of all other classes in this project '''


class Base:
    '''  the “base” of all other classes in this project '''

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the data.
        Args:
        id: assign the public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
