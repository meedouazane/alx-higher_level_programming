#!/usr/bin/python3
''' adds a new attribute to an object '''


def add_attribute(obj, attr_name, attr_value):
    ''' adds a new attribute to an object '''
    if hasattr(obj, '__dict__') and isinstance(obj.__dict__, dict):
        obj.__dict__[attr_name] = attr_value
    else:
        raise TypeError("can't add new attribute")
