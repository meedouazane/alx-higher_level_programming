#!/usr/bin/python3
''' displays the value of the variable X-Request-Id '''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    content = requests.get(url)
    if 'X-Request-Id' in content.headers:
        print(content.headers['X-Request-Id'])
