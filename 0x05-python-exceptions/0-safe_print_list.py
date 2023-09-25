#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    try:
        for i in range(0, x):
            if my_list[i] == my_list[-1] or x == i + 1:
                print("{}".format(my_list[i]))
                c = c + 1
            else:
                print("{}".format(my_list[i]), end="")
                c = c + 1
    except IndexError:
        None
    return c
