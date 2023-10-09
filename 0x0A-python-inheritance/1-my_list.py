#!/usr/bin/python3
''' class MyList that inherits from list '''


class MyList(list):
    '''  inherits from list '''

    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        sort_a = sorted(self)
        print(sort_a)
