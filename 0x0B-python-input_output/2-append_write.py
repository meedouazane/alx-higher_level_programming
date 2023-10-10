#!/usr/bin/python3
''' function that write a text file (UTF8)  '''


def append_write(filename="", text=""):
    ''' write in a file '''
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
