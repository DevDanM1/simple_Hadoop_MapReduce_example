#!/usr/bin/env python
import sys

stops = set(['the', 'and', 'is', 'or', 'not', 'for', 'i'])

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # remove punctuation
    line = line.replace('!','')
    line = line.replace('?','')
    line = line.replace(':','')
    line = line.replace(';','')
    line = line.replace('.','')
    line = line.replace(',','')

    # make lower case
    line = line.lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stops:
            print '%s\t%s' % (word, "1")
