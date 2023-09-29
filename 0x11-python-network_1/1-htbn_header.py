#!/usr/bin/python3
""" This module  uses the Universal resource library to make a request"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen('sys.argv') as resp:
        html = resp.headers["X-Request-Id"]
        print(html)
