#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err:
         sys.stderr.write(f'Exception: {str(err)}\n')
    except (TypeError, ValueError):
        return False
