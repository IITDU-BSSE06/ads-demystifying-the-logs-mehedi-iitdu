#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    year_time = data[3].split("/")[2]
    year = year_time.split(":")[0]
    print(year)