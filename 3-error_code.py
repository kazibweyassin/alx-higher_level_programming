#!/usr/bin/python3
"""
This script uses urllib to send a GET request to a specified URL and prints the HTML content.
Arguments:
    <URL> : The target URL to send the GET request.

The script fetches the content of the URL and prints it. If an HTTP error occurs,
it prints the error code.
"""
import urllib.request
import urllib.parse
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            html = resp.read()
            print(str(html, 'utf-8'))
    except urllib.error.HTTPError as h:
        print('Error code: {}'.format(h.code))