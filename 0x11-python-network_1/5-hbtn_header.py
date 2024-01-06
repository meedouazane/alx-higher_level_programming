#!/usr/bin/python3
''' displays the value of the variable X-Request-Id '''
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    content = requests.get(url)
    if 'X-Request-Id' in content.headers:
        print(content.headers['X-Request-Id'])
