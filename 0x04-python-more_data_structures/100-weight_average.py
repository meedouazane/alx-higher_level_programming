#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    weight = 0
    average = 0
    for i in my_list:
        total += (i[0] * i[1])
        weight += i[1]
    average = total / weight
    return average
