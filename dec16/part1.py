#! /usr/bin/env python3

import argparse
import string
import collections

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file')
args = parser.parse_args()

input_file = open(args.input_file)
input_lines = list(input_file.readlines())
input_file.close()

count = int(input_lines[0].strip())
moves = input_lines[1].strip().split(',')

start_positions = list(string.ascii_lowercase[:count])

def do_dance(p, moves):
    for m in moves:
        if m[0] == 's':
            n = int(m[1:])
            p = p[-n:] + p[:-n]
        elif m[0] == 'x':
            parts = m[1:].split('/')
            a = int(parts[0])
            b = int(parts[1])
            x = p[a]
            p[a] = p[b]
            p[b] = x
        elif m[0] == 'p':
            (a, b) = m[1:].split('/')
            ia = p.index(a)
            ib = p.index(b)
            p[ia] = b
            p[ib] = a
        else:
            raise('problem1')
    return p

print(''.join(do_dance(start_positions, moves)))



