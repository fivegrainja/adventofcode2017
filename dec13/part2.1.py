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

periods = {}
for layer, range in ranges.items():
    if range == 1:
        raise('problem')
    periods[layer] = 2 * (range - 1)


def try_delay(delay):
    for l, r in ranges.items():
        if (delay + l) % periods[l]  == 0:
            return False
    return True

delay = 0
while True:
    print()
    if try_delay(delay):
        break
    delay += 1

print('delay: %d' % delay)
