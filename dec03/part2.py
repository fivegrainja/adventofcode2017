#! /usr/bin/env python3

import sys

goal = 361527

x = 0
y = 0
size_x = 1
size_y = 1
lookup = {(0, 0): 1}

def get_neighbors(x, y):
    sum = lookup.get((x-1, y+1), 0)
    sum += lookup.get((x, y+1), 0)
    sum += lookup.get((x+1, y+1), 0)
    sum += lookup.get((x-1, y), 0)
    sum += lookup.get((x+1, y), 0)
    sum += lookup.get((x-1, y-1), 0)
    sum += lookup.get((x, y-1), 0)
    sum += lookup.get((x+1, y-1), 0)
    print('get_neighbors for %d, %d is %d' % (x, y, sum))
    return sum

while True:
    for i in range(size_x):
        x += 1
        z = get_neighbors(x, y)
        lookup[(x, y)] = z
        if z > goal:
            print(z)
            sys.exit()
    size_x += 1
    for i in range(size_y):
        y += 1
        z = get_neighbors(x, y)
        lookup[(x, y)] = z
        if z > goal:
            print(z)
            sys.exit()
    size_y += 1
    for i in range(size_x):
        x -= 1
        z = get_neighbors(x, y)
        lookup[(x, y)] = z
        if z > goal:
            print(z)
            sys.exit()
    size_x += 1
    for i in range(size_y):
        y -= 1
        z = get_neighbors(x, y)
        lookup[(x, y)] = z
        if z > goal:
            print(z)
            sys.exit()
    size_y += 1
