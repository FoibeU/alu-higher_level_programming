#!/usr/bin/python3
"""
<<<<<<< HEAD
script that takes in a URL, sends request to the URL and
=======
script that takes in a URL, sends a request to the URL and
>>>>>>> 100a83f6d6b5069d2915cb11d8f568340e932e68
displays the value of the 'X-Request-Id' variable found in the response header
"""
import sys
from urllib import request


if __name__ == '__main__':
    url = sys.argv[1]

    with request.urlopen(url) as site:
        print(site.headers['X-Request-Id'])
<<<<<<< HEAD

=======
>>>>>>> 100a83f6d6b5069d2915cb11d8f568340e932e68
