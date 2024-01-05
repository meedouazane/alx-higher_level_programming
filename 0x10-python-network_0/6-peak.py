#!/usr/bin/python3
''' finds a peak in a list of unsorted integers'''

def find_peak(list_of_integers):
    if list_of_integers:
        for i in range(len(list_of_integers) - 1):
            if list_of_integers[i] >= list_of_integers[i + 1] and list_of_integers[i] >= list_of_integers[i - 1]:
                peak = list_of_integers[i]
                return peak
    else:
        return None
