#!/usr/bin/python3
"""This script uses urllib to send a POST request to a specified URL with email data.
Arguments:
    <URL>   : The target URL to send the POST request.
    <email> : The email address to include as data in the request.

The script encodes the email data and sends it as a POST request to the specified URL.
It then reads and prints the HTML content of the response.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    data = {}
    data['email'] = sys.argv[2]
    url_end = urllib.parse.urlencode(data)
    url_end = url_end.encode('ascii')
    with urllib.request.urlopen(sys.argv[1], url_end) as resp:
        html = resp.read()
        print(str(html, 'utf-8'))