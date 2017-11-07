#!/usr/bin/python

import sys

count = 0
for line in sys.stdin:
    if "/assets/js/the-associates.js" in line:
	count = count + 1
print(count)