#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    prev = 0
    for i in roman_string[::-1]:
        value = roman[i]
        if value < prev:
            number -= value
        else:
            number = number + value
        prev = value
    return number
