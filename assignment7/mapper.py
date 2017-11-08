#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        request_type = data[5].split('"')[1]
        print(request_type)