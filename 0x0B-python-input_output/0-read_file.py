#!/usr/bin/python3
''' function that reads a text file (UTF8) and prints it to stdout '''


def read_file(filename=""):
    ''' read from a file '''
    with open(filename, 'r', encoding='utf8') as f:
        read = f.read()
        print(read, end="")
