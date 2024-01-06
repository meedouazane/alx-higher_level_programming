#!/usr/bin/python3
''' script that takes in a letter and sends a POST request '''
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    try:
        variable = {'q': sys.argv[1]}
    except IndexError:
        variable = {'q': ''}
    req = requests.post(url, data=variable)
    data = req.json()
    if data:
        print(f"[{data['id']}] {data['name']}")
    else:
        print("Not a valid JSON")
