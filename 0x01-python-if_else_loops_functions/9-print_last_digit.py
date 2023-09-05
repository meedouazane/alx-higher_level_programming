#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    n = number % 10
    print(n, end="")
    return (n)
