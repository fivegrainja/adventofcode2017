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

start = '.#./..#/###'

rules = {}

def rotate_cw(g):
    new_p = []
    size = len(g[0])
    for i in range(size):
        new_p.append(''.join(reversed([r[i] for r in g])))
    return new_p

def rotate_ccw(g):
    new_p = []
    size = len(g[0])
    for i in range(size-1, -1, -1):
        new_p.append(''.join([r[i] for r in g]))
    return new_p

def flip_side(g):
    return [''.join(reversed(l)) for l in g]

def flip_top(g):
    return list(reversed(g))


def get_permutations(cell):
    g = cell.split('/')
    size = len(g[0])
    p = [cell]
    # flip top bottom
    p.append('/'.join(flip_top(g)))
    # flip side to side
    p.append('/'.join(flip_side(g)))
    # rotate clockwise
    p.append('/'.join(rotate_cw(g)))
    # rotate counterclockwise
    p.append('/'.join(rotate_ccw(g)))
    #if size == 3:
    # flip top left to lower right
    # reverse each row, then rotate cw
    new_p = flip_side(g)
    new_p = rotate_cw(new_p)
    p.append('/'.join(new_p))
    # flip top right to lower left
    # reverse rows, the ccw
    new_p = flip_side(g)
    new_p = rotate_ccw(new_p)
    p.append('/'.join(new_p))

    return p

def get_rules():
    global input_lines
    rules = {}
    for line in input_lines:
        parts = line.strip().split()
        src = parts[0]
        dst = parts[2]
        perms = get_permutations(src)
        for p in perms:
            if p in rules:
                raise Exception('whoa')
        for p in perms:
            rules[p] = dst
    return rules

def grow(g):
    global rules
    size = len(g[0])
    newg = []
    if size % 2 == 0:
        for y in range(0, size, 2):
            newg.extend(['','',''])
            for x in range(0, size, 2):
                cell = g[y][x:x+2] + '/' + g[y+1][x:x+2]
                new_cell = rules[cell]
                new_cell_rows = new_cell.split('/')
                newg[-3] += new_cell_rows[0]
                newg[-2] += new_cell_rows[1]
                newg[-1] += new_cell_rows[2]
    elif size % 3 == 0:
        for y in range(0, size, 3):
            newg.extend(['','','',''])
            for x in range(0, size, 3):
                cell = g[y][x:x+3] + '/' + g[y+1][x:x+3] + '/' + g[y+2][x:x+3]
                new_cell = rules[cell]
                new_cell_rows = new_cell.split('/')
                newg[-4] += new_cell_rows[0]
                newg[-3] += new_cell_rows[1]
                newg[-2] += new_cell_rows[2]
                newg[-1] += new_cell_rows[3]
    else:
        raise Exception('huh? size=%d g=%s' % (size, str(g)))
    return newg

if __name__ == '__main__':
    rules = get_rules()
    g = start.split('/')
    n = 5
    pprint(g)
    for i in range(n):
       g = grow(g)
    
    count = 0
    for row in g:
        count += row.count('#')
    print('count: %d' % count)
     



