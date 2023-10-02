#!/usr/bin/python3
import sys

argc = len(sys.argv)

if argc != 2:
    print("Usage: nqueens N")
    exit(1)
else:
    number = int(sys.argv[1])
if not isinstance(number, int):
    print("N must be a number")
    exit(1)
if number < 4:
    print("N must be at least 4")
    exit(1)
