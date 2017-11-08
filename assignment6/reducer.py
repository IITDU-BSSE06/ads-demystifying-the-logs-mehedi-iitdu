#!/usr/bin/python

import sys

years = {}

for line.strip() in sys.stdin:
    if line in ['2009','2010','2011']:
	years[line] = years[line]+1
    else:
	years[line] = 1

for year in years:
    result = "{0} {1}".format(year,years[year])
    print(result)