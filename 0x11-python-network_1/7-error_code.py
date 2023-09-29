#!/usr/bin/python3

import requests
import sys
"""
This script uses the 'requests' library to send an HTTP GET request to a specified URL
and prints the response content or an error message if the status code is 400 or greater.

The script fetches the response from the URL and prints its content. If the HTTP status code
is 400 or greater, it prints an error message with the status code.
"""

if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
