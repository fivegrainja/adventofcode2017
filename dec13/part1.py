#! /usr/bin/env python3

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

layers = []
for l in range(num_layers):
    r = ranges.get(l, 0)
    layers.append([r, 0, 1])


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

severity = 0
for t in range(num_layers):
    print('t=%s layers=%s' % (t, layers))
    if layers[t][0] > 0 and layers[t][1] == 0:
        print('caught at layer %s with range %s' % (t, ranges[t]))
        severity += (t * ranges[t])
    advance_scanners()

print('severity: %s' % severity)


