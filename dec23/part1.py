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
for c in 'abcdefgh':
    reg[c] = 0

def get_value(x):
    global reg
    if x in string.ascii_lowercase:
        return reg.get(x, 0)
    return int(x)

# set X Y sets register X to the value of Y.
# sub X Y decreases register X by the value of Y.
# mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
# jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)

num_mul = 0
i = 0
while i < len(input_lines):
    print('\nStep %d' % i)
    pprint(reg)
    print(input_lines[i])
    p = input_lines[i].strip().split()
    op = p[0]
    r = p[1]
    if len(p) > 2:
        o = p[2]
    else:
        o = None
    print(op)
    if op == 'set':
        reg[r] = get_value(o)
    elif op == 'sub':
        reg[r] -= get_value(o)
    elif op == 'mul':
        num_mul += 1
        reg[r] = get_value(r) * get_value(o)
    elif op == 'jnz':
        if get_value(r) != 0:
            i += get_value(o)
            continue
    else:
        raise Exception('Unknown op %s' % op)
    i += 1

print('num_mul: %d' % num_mul)
print('done')
