#!/usr/bin/python3
"""
This script uses the 'requests' library to make an HTTP GET request to a specified URL
and prints the response content.

Usage: python3 script.py

The script sends a GET request to the URL 'https://alx-intranet.hbtn.io/status',
fetches the content of the response, and prints it.
"""
import requests


if __name__ == "__main__":
    html = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(html.text)))
    print("\t- content: {}".format(html.text))