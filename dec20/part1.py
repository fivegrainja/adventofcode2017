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

# Vector = namedtuple('Vector', ['x', 'y', 'z'])
# Point = namedtuple('Point', [])

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


ps = []
for i, line in enumerate(input_lines):
    parts = line.strip('\n').split()
    #print('parts: %s' % parts)
    ps.append(Point(
        Vector(*[int(p) for p in parts[0].strip('p=<>,').split(',')]),
        Vector(*[int(p) for p in parts[1].strip('v=<>,').split(',')]),
        Vector(*[int(p) for p in parts[2].strip('a=<>,').split(',')])
    ))

min_accel = None
min_i = []
for i, p in enumerate(ps):
    accel = p.a.length()
    if min_accel is None or accel < min_accel:
        min_accel = accel
        min_i = [i]
    elif min_accel is not None and accel == min_accel:
        min_i.append(i)

print('min accel: %d' % min_accel)
print('min i: %s' % min_i)

closest_dist = None
closest_i = None
for i in min_i:
    dist = ps[i].p.length()
    if closest_dist is None or dist < closest_dist:
        closest_dist = dist
        closest_i = i


print('closest is %d' % closest_i)

for i in min_i:
    print('i:%3d p:%3d v:%3d a:%3d' % (i, ps[i].p.length(), ps[i].v.length(), ps[i].a.length()))

# 336 too low
