#!/usr/bin/python3
"""
This script uses the 'requests' library to send an HTTP POST request to a specific URL
(http://0.0.0.0:5000/search_user) with optional data provided as a command-line argument.

The script processes the response based on the HTTP status code and the content of the response.
If the status code is 204 or the response JSON content is empty, it prints 'No result.'
If the response contains valid JSON data, it extracts and prints the 'id' and 'name' fields.
If there's an issue with parsing JSON, it prints 'Not a valid JSON.'
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        datum = ""
    else:
        datum = sys.argv[1]
    resp = requests.post("http://0.0.0.0:5000/search_user", data={'q': datum})
    if resp.status_code == 204 or resp.json() == {}:
        print('No result')
    else:
        try:
            j = resp.json()
            print("[{}] {}".format(j.get('id', ''), j.get('name', '')))
        except:
            print('Not a valid JSON')