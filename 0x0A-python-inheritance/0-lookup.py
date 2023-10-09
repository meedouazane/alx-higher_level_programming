#!/usr/bin/python3
''' function that returns the list of available
    attributes and methods of an object '''


def lookup(obj):
    ''' list of available attributes and methods of an object '''

    list_op = []
    list_op = dir(obj)
    return list_op
