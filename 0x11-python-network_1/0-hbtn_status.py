#!/usr/bin/python3
""" This module  uses the Universal resource library to make a fetch request"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        html = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(str(html, 'UTF-8')))
