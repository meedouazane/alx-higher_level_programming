#!/usr/bin/python3
''' Python script that fetches website '''
import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        if content:
            print("Body response:")
            print(f"\t - type: {type(content)}")
            print(f"\t - content: {content}")
            print(f"\t - utf8 content: {content.decode('utf-8')}")
