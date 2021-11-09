#! /usr/bin/env python3

import sys

goal = 361527

z = 1
x = 0
y = 0
size_x = 1
size_y = 1

while True:
    for i in range(size_x):
        x += 1
        z += 1
        if z == goal:
            print('%d, %d' % (x, y))
            sys.exit()
    size_x += 1
    for i in range(size_y):
        y += 1
        z += 1
        if z == goal:
            print('%d, %d', (x, y))
            sys.exit()
    size_y += 1
    for i in range(size_x):
        x -= 1
        z += 1
        if z == goal:
            print('%d, %d' % (x, y))
            sys.exit()
    size_x += 1
    for i in range(size_y):
        y -= 1
        z += 1
        if z == goal:
            print('%d, %d', (x, y))
            sys.exit()
    size_y += 1
    



