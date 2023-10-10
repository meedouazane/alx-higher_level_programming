#!/usr/bin/python3
''' nserts a line of text to a file, after 
each line containing a specific string'''


def append_after(filename="", search_string="", new_string=""):
    ''' inserts a line of text '''
    text = ""
    with open(filename, 'r') as f:
        for i in f:
            text += i
            if search_string in i:
                text += new_string
    with open(filename, 'w') as f:
        f.write(text)

