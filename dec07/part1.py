#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file')
args = parser.parse_args()

input_file = open(args.input_file)
input_lines = list(input_file.readlines())
input_file.close()

weights = {}
children = {}
parents = {}

for line in input_lines:
    parts = line.split()
    name = parts[0]
    weight = int(parts[1][1:-1])
    these_children = set([s.strip(',') for s in parts[2:]])

    weights[name] = weight
    children[name] = these_children
    for child in these_children:
        parents[child] = name
    programs = {
        'name': parts[0],
        'weight': parts[1][1:-1]
    }

from pprint import pprint
root = set(weights.keys()) - set(parents.keys())
pprint(root)
