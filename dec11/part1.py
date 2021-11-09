#! /usr/bin/env python3

import argparse
import collections

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file')
args = parser.parse_args()

input_file = open(args.input_file)
input_lines = list(input_file.readlines())
input_file.close()

def get_distance(text):

    steps = text.strip().split(',')

    y = 0
    x = 0

    for step in steps:
        if step == 'n':
            y += 1
        elif step == 'ne':
            y += 1
            x += 1
        elif step == 'se':
            x += 1
        elif step == 's':
            y -= 1
        elif step == 'sw':
            x -= 1
            y -= 1
        elif step == 'nw':
            x -= 1
        else:
            raise('Unknown step %s' % step)
    
    distance = max(abs(x), abs(y), abs(x - y))
    return distance

print(get_distance(input_lines[0]))

