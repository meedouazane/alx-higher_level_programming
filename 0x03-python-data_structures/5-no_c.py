#!/usr/bin/python3
def no_c(my_string):
    new = ""
    length = len(my_string)
    for i in range(length):
        if (my_string[i] != 'C' and my_string[i] != 'c'):
            new = new + my_string[i]
    return(new)
