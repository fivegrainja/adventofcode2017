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

# g = grid
# p = position
# d = nswe direction

g = [list(r.strip()) for r in input_lines]
size_x = len(g[0])
size_y = len(g)
print('size: %d, %d' % (size_x, size_y))


d = collections.deque(list('NESW'))
pos_x = (size_x - 1) // 2
pos_y = (size_y - 1) // 2
#print('x, y: %d, %d' % (pos_x, pos_y))


def turn():
    if g[pos_y][pos_x] == '#':
        d.rotate(-1)
    else:
        d.rotate(1)

def move():
    global pos_y
    global pos_x
    global g

    #pdb.set_trace()

    # Return True if infected
    result = False
    if g[pos_y][pos_x] == '#':
        g[pos_y][pos_x] = '.'
    else:
        g[pos_y][pos_x] = '#'
        result = True
    if d[0] == 'N':
        pos_y -= 1
    elif d[0] == 'S':
        pos_y += 1
    elif d[0] == 'W':
        pos_x -= 1
    elif d[0] == 'E':
        pos_x += 1
    else:
        raise Exception('huh')
    if pos_x < 0:
        print('grow left side')
        for i, row in enumerate(g):
            g[i].insert(0, '.')
        pos_x += 1
        print('new x is %d' % pos_x)
    if pos_x >= len(g[0]):
        print('grow right side')
        for i, row in enumerate(g):
            g[i].append('.')
        print('new x is %d' % pos_x)
    if pos_y < 0:
        print('grow top')
        g.insert(0, ['.'] * len(g[0]))
        pos_y += 1
        print('new y is %d' % pos_y)
    if pos_y >= len(g):
        print('grow bottom')
        g.append(['.'] * len(g[0]))
        print('new y is %d' % pos_y)
    if pos_x < 0 or pos_x >= len(g[0]):
        #raise Exception('x is %d' % pos_x)
        pdb.set_trace()
    if pos_y < 0 or pos_y >= len(g):
        #raise Exception('y is %d' % pos_y)
        pdb.set_trace()
    return result
    
        

num_bursts = 10000
#num_bursts = 70

num_caused_infection = 0
for n in range(num_bursts):
    print('n = %d' % n)
    #print('pos(x,y): %d, %d' % (pos_x, pos_y))
    #print('direction: %s' % d[0])
    #for row in g:
    #    print(''.join(row))
    turn()
    #print('new direction: %s' % d[0])
    if move():
        num_caused_infection += 1
    #print('new position: x,y: %d, %d' % (pos_x, pos_y))
    
    print()

print('num moves caused infection: %d' % num_caused_infection)

