#! /usr/bin/env python3

import argparse
import collections
import binascii

parser = argparse.ArgumentParser()
#parser.add_argument('input_file', help='input file')
args = parser.parse_args()

#input = 'flqrgnkx'
input = 'jxqlasbh'

def get_knot_hash(text):
        
    #n = int(text.strip())
    n = 256
    l = list(range(n))
    lengths = [ord(c) for c in text.strip()] + [17, 31, 73, 47, 23]

    skip_size = 0
    total_skips = 0

    for round in range(64):
        for length in lengths:
            sub_l = l[:length]
            sub_l.reverse()
            l = sub_l + l[length:]
            this_skip = length + skip_size
            d = collections.deque(l)
            d.rotate(-this_skip)
            l = list(d)
            skip_size += 1
            total_skips += this_skip

    d = collections.deque(l)
    d.rotate(total_skips)
    l = list(d)

    dense_hash = []
    for i in range(16):
        start = i * 16
        sub = l[start:start+16]
        z = 0
        for s in sub:
            z ^= s
        dense_hash.append(z)

    dense_hex = [hex(h) for h in dense_hash]
    z = ''
    for h in dense_hex:
        h = h[2:]
        if len(h) == 2:
            z += h
        else:
            z += '0' + h

    return z


rows = []
for r in range(128):
    key = input + '-%d' % r
    row_hash = get_knot_hash(key)
    #print('row_hash: %s' % row_hash)
    row_bin = bin(int(row_hash, 16))[2:].zfill(128)
    #print('row_bin: %s' % row_bin)
    rows.append(row_bin)

# for r in range(8):
#     print(rows[r][:8])

count = 0
for row in rows:
    for c in row:
        if c == '1':
            count += 1
print('count: %d' % count)

