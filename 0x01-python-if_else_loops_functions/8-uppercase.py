#!/usr/bin/python3
def uppercase(str):
    str = str + '\n'
    for c in str:
        if 'a' <= c <= 'z':
            c = ord(c) - 32
            print("{}".format(chr(c)), end="")
        else:
            print("{}".format(c), end="")
