#!/usr/bin/python

import sys

files = {}
max_ = 0

for line in sys.stdin:
    if line in files:
	files[line] = files[line]+1
    else:
	files[line] = 1

for item in files:
    if files[item] > max_:
	path = item
	max_ = files[item]

print("/"+ path +" "+ max_)