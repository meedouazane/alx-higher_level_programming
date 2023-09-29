#!/usr/bin/python3

def add_integer(a, b=98):
    """
    function that adds 2 integers.
    Args:
    a : first integer.
    b : second integer.
    """
    if not (isinstance(b, int) or isinstance(b, float)):
        """ check if b is float or int """

        raise TypeError("b must be an integer")
    elif not (isinstance(a, int) or isinstance(a, float)):
        """ check if a is float or int """

        raise TypeError("a must be an integer")
    if isinstance(b, float):
        """ convert b to int if its float """
        b = int(b)
    if isinstance(a, float):
        """ convert a to int if its float """
        a = int(a)
    return a + b
