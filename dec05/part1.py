#! /usr/bin/env python3

import argparse
import string

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file')
args = parser.parse_args()

input_file = open(args.input_file)
input_lines = list(input_file.readlines())
input_file.close()

l = [int(line.strip()) for line in input_lines]
print(l)
len_l = len(l)
jumps = 0
i = 0
while True:
    jumps += 1
    this_jump = l[i]
    next_i = i + this_jump
    if next_i < 0 or next_i >= len_l:
        break
    l[i] += 1
    i = next_i

print(jumps)
    
