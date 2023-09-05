#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lt = abs(number) % 10
if number < 0:
    lt = -lt
if lt > 5:
    print(f"Last digit of {number :d} is {lt} and is greater than 5")
elif lt == 0:
    print(f"Last digit of {number :d} is {lt} and is 0")
else:
    print(f"Last digit of {number :d} is {lt} and is less than 6 and not 0")
