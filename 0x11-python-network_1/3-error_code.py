#!/usr/bin/python3
''' manage urllib.error.HTTPError exceptions and print: Error code '''
from urllib import request, error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
