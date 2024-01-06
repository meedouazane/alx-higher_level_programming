#!/usr/bin/python3
''' Python script that fetches website '''
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    content = requests.get(url).text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
