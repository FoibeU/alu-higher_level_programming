#!/usr/bin/python3
"""Python script that fetches https://alu-intranet.hbtn.io/status"""
import urllib.requests


if __name__ == '__main__':
    with urllib.requests.urlopen(
            'https://alu-intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf-8')))
