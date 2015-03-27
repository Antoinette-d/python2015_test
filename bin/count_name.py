#!/usr/bin/env python

import sys

if len(sys.argv) != 3:
        sys.exit("Usage: count_name.py expects a filename and protein name")

def count_name(filename, protein_name):
    try:
        input_file = open(filename)
    except IOError as e:
        print >>sys.stderr, "failed to open {}: {}".format(filename,e.stderr)
        return False
    else:
        count = 0
        for line in input_file:
                if line.rstrip() == protein_name:
                        count += 1
        return count

filename = sys.argv[1]
protein_name = sys.argv[2]
name_count = count_name(filename, protein_name)
print protein_name, name_count
