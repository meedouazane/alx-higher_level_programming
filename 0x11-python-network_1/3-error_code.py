#!/usr/bin/python3
''' manage urllib.error.HTTPError exceptions and print: Error code '''
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")
