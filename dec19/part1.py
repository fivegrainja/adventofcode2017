#! /usr/bin/env python3

import argparse
import string
import collections
#import hashlib
#import re
#import itertools
#import csv
#import sympy
#import numpy
#import llist

# Collections documentation:
# https://docs.python.org/3/library/collections.html
#
# c = collections.Counter(name)
# common = sorted(c.most_common(), key=cmp_key, reverse=False)
#
# d = collections.deque(iterable, maxlen)
# 
# hashlib.md5(b"Nobody inspects the spammish repetition").hexdigest()
#
# @lru_cache(maxsize=None) - decorator to memoize return values
#
# m = re.search('(?<=abc)def', 'abcdef')
# m.group(0)
#
# double_linked_list = llist.dllist(iterator)  - rotate, pop, append, appendright, nodeat
#
# Prime factorization
# from sympy.ntheory import factorint
# factorint(2000)    # 2000 = (2**4) * (5**3)
# {2: 4, 5: 3}
#
# reader = csv.reader(file, delimiter=',', quotechar='|') # each row in reader is a list
# dictreader = csv.DictReader(file) # each row in dictreader is a dict

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file')
args = parser.parse_args()

input_file = open(args.input_file)
input_lines = list(input_file.readlines())
input_file.close()

rows = [line.strip('\n') for line in input_lines]
width = len(input_lines[0])
height = len(input_lines)

visited = set()
path = []
letters = []


def get_neighbors(x, y):
    global rows
    global width
    global height
    n = []
    c = rows[y][x]
    if c == '+' or c in string.ascii_uppercase:
        prev = path[-1]
        was_going_horiz = prev[1] == y
        was_going_vert = prev[0] == x
        if was_going_horiz == was_going_vert:
            print('x,y: %d,%d' % (x,y))
            raise('Hmmm')
        
        if c == '+':
            if was_going_vert:
                if x > 0:
                    n.append((x-1, y))
                if x < width-1:
                    n.append((x+1, y))
            if was_going_horiz:
                if y > 0:
                    n.append((x, y-1))
                if y < height-1:
                    n.append((x, y+1))
        if c in string.ascii_uppercase:
            if was_going_horiz:
                if x > 0:
                    n.append((x-1, y))
                if x < width-1:
                    n.append((x+1, y))
            if was_going_vert:
                if y > 0:
                    n.append((x, y-1))
                if y < height-1:
                    n.append((x, y+1))
    if c == '-':
        if x > 0:
            if rows[y][x-1] == '|':
                n.append((x-2, y))
            else:
                n.append((x-1, y))
        if x < width-1:
            if rows[y][x+1] == '|':
                n.append((x+2, y))
            else:
                n.append((x+1, y))
    if c == '|':
        if y > 0:
            if rows[y-1][x] == '-':
                n.append((x, y-2))
            else:
                n.append((x, y-1))
        if y < height-1:
            if rows[y+1][x] == '-':
                n.append((x, y+2))
            else:
                n.append((x, y+1))
    n = [(x, y) for (x, y) in n if rows[y][x] != ' ']
    return n

def find_start():
    global rows
    for x, c in enumerate(rows[0]):
        if c != ' ':
            return (x, 0)
    raise('Didnt find start')

def travel(x, y):
    # if rows[y][x] == 'F':
    #     print('hit F')
    #     return None
    if rows[y][x] in string.ascii_uppercase:
        letters.append(rows[y][x])
    neighbors = set(get_neighbors(x, y))
    visited.add((x, y))
    path.append((x, y))
    next = neighbors - visited
    if len (next) > 1:
        print('path: %s' % path)
        print('x, y (%s): (%d, %d)' % (rows[y][x], x, y))
        print('next: %s' % next)
        print('neighbors: %s' % neighbors)
        # for nn in neighbors:
        #     print('%s in visited')
        #print('visited: %s' % visited)
        raise('bad')
    if len(next) == 0:
        return None
    next = next.pop()
    return (next[0], next[1])

next = find_start()
steps = 1
while True:
    prev = next
    next = travel(next[0], next[1])
    if next is None:
        break
    dif_x = abs(prev[0] - next[0])
    dif_y = abs(prev[1] - next[1])
    if dif_x == 2 and dif_y == 0:
        steps += 2
    elif dif_x == 0 and dif_y == 2:
        steps += 2
    elif dif_x == 1 and dif_y == 0:
        steps += 1
    elif dif_x == 0 and dif_y == 1:
        steps += 1
    else:
        print('prev: %s' % str(prev))
        print('next: %s' % str(next))
        print(dif_x)
        print(dif_y)
        raise('hughh')


#print('path: %s' % path)
print('letters: %s' % ''.join(letters))
print('steps: %d' % steps)

# 15988 too low x 2
# 15989 too low