#!/usr/bin/python

import fileinput
import re
import sys

pattern = re.compile(sys.argv[1])

for line in fileinput.input(sys.argv[2:]):
    if pattern.search(line):
        if fileinput.isstdin():
            fmt = '{lineno}:{line}'
        else:
            fmt = '{filename:<20}:{lineno:02}:{line}'
        print fmt.format(filename=fileinput.filename(), 
                lineno = fileinput.filelineno(),
                line = line.strip())
