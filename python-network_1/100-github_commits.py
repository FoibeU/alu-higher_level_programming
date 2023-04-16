#!/usr/bin/python3
''' list the 10 most recent commits on a github repository '''

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])
    response = requests.get(url)
    commits = response.json()
    try:
        for each in range(10):
            print("{}: {}".format(
                commits[each].get("sha"),
                commits[each].get("commit").get("author").get("name")))

    except IndexError:
        pass
