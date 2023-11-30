#!/bin/bash
# send a request with a header variable set
curl -H "X-School-User-Id: 98" -sX GET "$1"

