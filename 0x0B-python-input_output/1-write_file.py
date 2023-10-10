#!/usr/bin/python3
''' function that write a text file (UTF8)  '''


def write_file(filename="", text=""):
    ''' write in a file '''
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
