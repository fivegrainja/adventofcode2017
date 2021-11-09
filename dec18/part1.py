#! /usr/bin/env python3

import argparse
import string
import collections
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file')
args = parser.parse_args()

input_file = open(args.input_file)
input_lines = list(input_file.readlines())
input_file.close()

reg = {}

last_snd = None

def get_value(x):
    global reg
    if x in string.ascii_lowercase:
        return reg.get(x, 0)
    return int(x)

i = 0
while i < len(input_lines):
    pprint(reg)
    p = input_lines[i].strip().split()
    op = p[0]
    r = p[1]
    if len(p) > 2:
        o = p[2]
    else:
        o = None
    if op == 'snd':
        x = get_value(r)
        last_snd = x
    elif op == 'set':
        reg[r] = get_value(o)
    elif op == 'add':
        reg[r] += get_value(o)
    elif op == 'mul':
        reg[r] = get_value(r) * get_value(o)
    elif op == 'mod':
        reg[r] = get_value(r) % get_value(o)
    elif op == 'rcv':
        if get_value(r) != 0:
            print('recovered %d' % last_snd)
            break
    elif op == 'jgz':
        #import pdb; pdb.set_trace()
        if get_value(r) > 0:
            i += get_value(o)
            continue
    else:
        raise('Unknown op %s' % op)
    #import pdb; pdb.set_trace()
    i += 1

print('done')
