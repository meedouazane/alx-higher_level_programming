#!/usr/bin/python3
''' manage error exceptions and print: Error code '''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    content = requests.get(url)
    if content.status_code >= 400:
        print(f"Error code: {content.status_code}")
    else:
        print(content.text)
