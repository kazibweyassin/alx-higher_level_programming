#!/bin/bash
# This script shows the body size of a response for code 200
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -Ls "$1"; fi

