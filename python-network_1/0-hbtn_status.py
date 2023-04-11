#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    from urllib import request
    with request.urlopen("https://alx-intranet.hbtn.io/status") as status:
        status = status.read()

    url_type = type(status)
    content = status
    utf8_content = status.decode('UTF-8')
    print("Body response:")
    print(f"\t- type: {url_type}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {utf8_content}")
