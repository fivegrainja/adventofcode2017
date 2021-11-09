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
lengths = [ord(c) for c in input_lines[1].strip()] + [17, 31, 73, 47, 23]

skip_size = 0
total_skips = 0

for round in range(64):
    for length in lengths:
        #print('length: %s' % length)
        sub_l = l[:length]
        sub_l.reverse()
        #print('sub_l reversed: %s' % sub_l)
        l = sub_l + l[length:]
        #print('new l: %s' % l)
        this_skip = length + skip_size
        #print('this_skip: %s' % this_skip)
        d = collections.deque(l)
        d.rotate(-this_skip)
        l = list(d)
        #print('new l: %s' % l)
        skip_size += 1
        total_skips += this_skip
        #print('')

d = collections.deque(l)
d.rotate(total_skips)
l = list(d)
#print('l: %s' % l)
#print(l[0] * l[1])

dense_hash = []
for i in range(16):
    start = i * 16
    sub = l[start:start+16]
    z = 0
    for s in sub:
        z ^= s
    dense_hash.append(z)

dense_hex = [hex(h) for h in dense_hash]
print('dense_hex: %s' % dense_hex)
z = ''
for h in dense_hex:
    h = h[2:]
    if len(h) == 2:
        z += h
    else:
        z += '0' + h

print('z: %s' % z)
