#!/usr/bin/python3
''' list 10 commits (from the most recent to oldest)
of the repository “rails” '''
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    name = sys.argv[2]
    url = f'https://api.github.com/repos/{name}/{repo}/commits'
    i = 0
    r = requests.get(url)
    if r.status_code == 200:
        commits = r.json()
        for c in commits:
            if i < 10:
                sha = c['sha']
                author = c['commit']['author']['name']
                print(f"{sha}: {author}")
                i = i + 1
            else:
                break
    else:
        print("None")
