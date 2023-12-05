#!/bin/bash
# send a request with a header variable set
curl -s -H "X-School-User-Id: 98" "$1"
