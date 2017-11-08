#!/usr/bin/python

import sys

requests = {}

for line in sys.stdin:
    if line in requests:
	requests[line] = requests[line]+1
    else:
	requests[line] = 1

for item in requests:
    print(item)+" "+print(requests[item])