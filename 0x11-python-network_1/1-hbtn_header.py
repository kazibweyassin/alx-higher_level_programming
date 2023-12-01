#!/usr/bin/python3
""" This module uses the Universal Resource Library to make a request"""

import urllib.request
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    """if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        # Send an HTTP GET request to the specified URL
        with urllib.request.urlopen(url) as resp:
            # Check if the 'X-Request-Id' header is present in the response
            if 'X-Request-Id' in resp.headers:
                x_request_id = resp.headers['X-Request-Id']
                print("X-Request-Id:", x_request_id)
            else:
                print("X-Request-Id header not found in the response.")
    except urllib.error.URLError as e:
        print("Error:", e)
    except Exception as e:
        print("An error occurred:", e)"""
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
