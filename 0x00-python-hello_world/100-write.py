#!/usr/bin/python3
import sys
filename = "F1"
with open(filename, "r") as file:
    for line in file:
        sys.stderr.write(line)
    exit(1)
