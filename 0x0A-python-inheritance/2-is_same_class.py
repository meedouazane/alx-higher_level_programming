#!/usr/bin/python3
''' function that returns True if the object is exactly '''


def is_same_class(obj, a_class):
    '''returns True if the object is exactly
        an instance of the specified class
        Args:
            obj: object that we want to test
            a_class: the class'''

    if type(obj) == a_class:
        return True
    else:
        return False
