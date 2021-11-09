#! /usr/bin/env python3

import argparse
import string
import collections
from pprint import pprint
import pdb

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file')
args = parser.parse_args()

input_file = open(args.input_file)
input_lines = list(input_file.readlines())
input_file.close()

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def increment(self, v):
        self.x += v.x
        self.y += v.y
        self.z += v.z


class Point:

    def __init__(self, p, v, a):
        # a, v, p are Vectors
        self.p = p
        self.v = v
        self.a = a

    def move(self):
        self.v.increment(self.a)
        self.p.increment(self.v)

def get_current_positions():
    positions = collections.defaultdict(list) 
    for i, p in ps.items():
        positions[(p.p.x, p.p.y, p.p.z)].append(i)
    return positions

def remove_collisions():
    positions = get_current_positions()
    for position, inhabitants in positions.items():
        if len(inhabitants) > 1:
            for i in inhabitants:
                del ps[i]

def move_all():
    for i, p in ps.items():
        p.move()

ps = {}
for i, line in enumerate(input_lines):
    parts = line.strip('\n').split()
    ps[i] = (Point(
        Vector(*[int(p) for p in parts[0].strip('p=<>,').split(',')]),
        Vector(*[int(p) for p in parts[1].strip('v=<>,').split(',')]),
        Vector(*[int(p) for p in parts[2].strip('a=<>,').split(',')])
    ))

t = 0
while True:
    remove_collisions()
    move_all()
    t += 1
    if t > 100:
        break

print(len(ps))