#! /usr/bin/env python3

import argparse
import string
import collections

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file')
args = parser.parse_args()

input_file = open(args.input_file)
input_lines = list(input_file.readlines())
input_file.close()

n = int(input_lines[0].strip())
l = list(range(n))
lengths = [int(w) for w in input_lines[1].split(',')]

print('n: %s' % n)
print('l: %s' % l)
print('lengths: %s' % lengths)

skip_size = 0
i = 0

for length in lengths:
    print('length: %s' % length)
    sub_l = l[:length]
    sub_l.reverse()
    print('sub_l reversed: %s' % sub_l)
    l = sub_l + l[length:]
    print('new l: %s' % l)
    this_skip = length + skip_size
    print('this_skip: %s' % this_skip)
    d = collections.deque(l)
    d.rotate(-this_skip)
    l = list(d)
    print('new l: %s' % l)
    skip_size += 1
    i += this_skip
    print('')

d = collections.deque(l)
d.rotate(i)
l = list(d)
print('l: %s' % l)
print(l[0] * l[1])
    