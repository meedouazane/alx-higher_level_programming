#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    c = 0
    div = 0
    new_list = [list_length]
    while c != list_length:
        try:
            div = my_list_1[c] / my_list_2[c]
        except ZeroDivisionError:
            print('division by 0')
            div = 0
        except (TypeError, ValueError):
            print('wrong type')
            div = 0
        except IndexError:
            print('out of range')
            div = 0
        finally:
            new_list.append(div)
        c = c + 1
    return new_list
