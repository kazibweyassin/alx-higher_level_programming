#!/usr/bin/python3
"""
This script uses the 'requests' library to send an HTTP GET request to a specified URL
and prints the value of the 'X-Request-Id' header from the response.
Arguments:
    <URL>: The target URL to send the GET request.

The script fetches the response from the URL and prints the 'X-Request-Id' header value
if it exists in the response headers.
"""
import requests
import sys


if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    html = resp.headers.get("X-Request-Id", None)
    print(html)
