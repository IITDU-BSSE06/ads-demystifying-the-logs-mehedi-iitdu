#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
	file_ = data[6].split("/")
    	print(file_[len(file_)-1])