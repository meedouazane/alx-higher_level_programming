#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for i in my_string:
        if my_string[i] != 'C' and my_string[i] != 'c':
            new = new + my_string[i]
    return(new)
