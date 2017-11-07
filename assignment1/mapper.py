#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(" - - ")[0]
    print(data)