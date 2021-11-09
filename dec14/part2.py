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

for r in range(8):
    print(rows[r][:8])


group_membership = {}

def get_neighbors(row, col):
    global rows
    neighbors = []
    if col > 0:
        if rows[row][col-1] == '1':
            neighbors.append((row, col-1))
    if col < 127:
        if rows[row][col+1] == '1':
            neighbors.append((row, col+1))
    if row > 0:
        if rows[row-1][col] == '1':
            neighbors.append((row-1, col))
    if row < 127:
        if rows[row+1][col] == '1':
            neighbors.append((row+1, col))
    print('neighbors for r: %d  c: %d are %s' % (row, col, neighbors))
    return neighbors

def get_neighboring_groups(row, col):
    neighbors = get_neighbors(row, col)
    groups = []
    for n in neighbors:
        group = group_membership.get((n[0], n[1]), None)
        if group is not None:
            groups.append(group)
    return groups

def resolve_groups(groups):
    norm = groups[0]
    old_groups = groups[1:]
    for key, value in group_membership.items():
        if value in old_groups:
            group_membership[key] = norm
    return norm

#rows = rows[:2]

next_group_num = 0
for r_index, row in enumerate(rows):
    # if r_index == 2:
    #     break
    for c_index, c in enumerate(row):
        #print('group membership: %s' % group_membership)
        if c == '1':
            groups = get_neighboring_groups(r_index, c_index)
            if len(groups) == 1:
                group = groups[0]
            elif len(groups) > 1:
                group = resolve_groups(groups)
            else:
                group = next_group_num
                next_group_num += 1
            group_membership[(r_index, c_index)] = group
            print('group for r=%d c=%d is %d' % (r_index, c_index, group))

s = set(group_membership.values())
print(len(s))


