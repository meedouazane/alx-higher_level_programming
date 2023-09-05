#!/usr/bin/python3
def remove_char_at(str, n):
    length = len(str)
    new = str
    if length >= n and n > -1:
        new = new[:n] + "" + new[n+1:]
    return (new)
