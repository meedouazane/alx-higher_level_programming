#!/usr/bin/python3
"""
function that adds 2 integers.
add_integer(a, b)

"""


def add_integer(a, b=98):
    """
    function that adds 2 integers a and b.
    Args:
        a : first number
        b : Second number
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    if isinstance(b, float):
        b = int(b)
    if isinstance(a, float):
        a = int(a)
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
