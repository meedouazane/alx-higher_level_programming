#!/usr/bin/python3
''' class MyInt that inherits from int '''


class MyInt(int):
    ''' MyInt is a rebel. MyInt has == and != operators inverted '''
    def __init__(self, value):
        super().__init__()
        self.value = value

    def __eq__(self, other):
        ''' invert == '''
        if isinstance(other, MyInt):
            return self.value != other.value
        return False

    def __ne__(self, other):
        ''' invert != '''
        if isinstance(other, MyInt):
            return self.value == other.value
        return True
