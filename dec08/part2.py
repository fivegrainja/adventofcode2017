#! /usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file')
args = parser.parse_args()

input_file = open(args.input_file)
input_lines = list(input_file.readlines())
input_file.close()

registers = {}

mx = -9999

for line in input_lines:
    line = line.strip()
    parts = line.split()
    v = parts[0]
    inst = parts[1]
    amount = int(parts[2])
    cond_var = registers.get(parts[4], 0)
    cond_op = parts[5]
    cond_val = int(parts[6])

    do_op = False
 
    print('registers: %s' % registers)
    print('line: %s' % line)
    #import pdb; pdb.set_trace()

 
    if cond_op == '>':
        if cond_var > cond_val:
            do_op = True
    elif cond_op == '>=':
        if cond_var >= cond_val:
            do_op = True
    elif cond_op == '<':
        if cond_var < cond_val:
            do_op = True
    elif cond_op == '<=':
        if cond_var <= cond_val:
            do_op = True
    elif cond_op == '==':
        if cond_var == cond_val:
            do_op = True
    elif cond_op == '!=':
        if cond_var != cond_val:
            do_op = True
    else:
        print ('Unknown op %s' % cond_op)
        sys.exit()

    print('do_op: %s' % do_op)
    if do_op:
        if inst == 'inc':
            registers[v] = registers.get(v, 0) + amount
        elif inst == 'dec':
            registers[v] = registers.get(v, 0) - amount
        else:
            print('Unrecognized inst %s' % inst)
            sys.exit()
        if registers[v] > mx:
            mx = registers[v]

max_key = ''
max_value = -999999
for key, value in registers.items():
    if value > max_value:
        max_key = key
        max_value = value

print('%s: %s' % (max_key, max_value))
print('max: %s' % mx)
