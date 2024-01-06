#!/usr/bin/python3
''' cript that takes your GitHub credentials and display ID '''
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(username, password))
    if r.status_code == 200:
        user = r.json()
        print(f"{user['id']}")
    else:
        print("None")
