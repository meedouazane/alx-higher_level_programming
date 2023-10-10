#!/usr/bin/python3
'''  returns a list of lists of integers representing 
the Pascal’s triangle of n '''


def pascal_triangle(n):
    ''' returns a list of lists of integers representing
    the Pascal’s triangle of n '''
    lst = []
    if n <= 0:
        return lst
    for i in range(0, n):
        lst.append(i)
    return lst
