#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except (IndexError, ZeroDivisionError) as err:
        sys.stderr.write('Exception: {}\n'.format(err))
        return None
