#! /usr/bin/env python3

# NB: This takes too long, part2.1.py is better.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file')
args = parser.parse_args()

input_file = open(args.input_file)
input_lines = list(input_file.readlines())
input_file.close()

ranges = {}
for line in input_lines:
    parts = line.strip().split()
    l = int(parts[0].strip(':'))
    r = int(parts[1])
    ranges[l] = r

layer_nums = ranges.keys()
layer_nums = sorted(layer_nums)
num_layers = layer_nums[-1] + 1

def advance_scanners():
    global layers
    for l in layers:
        range = l[0]
        pos = l[1]
        dir = l[2]
        if l[0] == 0:
            continue
        if dir == 1:
            if pos < range - 1:
                l[1] += 1
            else:
                l[1] -= 1
                l[2] = -1
        else:
            if pos > 0:
                l[1] -= 1
            else:
                l[1] += 1
                l[2] = 1


def try_with_delay(delay):
    global layers
    layers = []

    for l in range(num_layers):
        r = ranges.get(l, 0)
        layers.append([r, 0, 1])

    for d in range(delay):
        advance_scanners()
        
    for t in range(num_layers):
        if layers[t][0] > 0 and layers[t][1] == 0:
            return False
        advance_scanners()
    return True

delay = 0
while True:
    print('delay: %d' % delay)
    r = try_with_delay(delay)
    if r:
        break
    delay += 1

print('success delay=%d' % delay)

