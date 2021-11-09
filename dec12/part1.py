#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file')
args = parser.parse_args()

input_file = open(args.input_file)
input_lines = list(input_file.readlines())
input_file.close()

routes = {}
for line in input_lines:
    parts = line.strip().split()
    src = int(parts[0])
    dest_list = [int(d.strip(',')) for d in parts[2:]]
    routes[src] = dest_list

visited = set()

def visit(x):
    global visited
    global to_visit
    global routes

    visited.add(x)
    for d in routes[x]:
        if d not in visited:
            visit(d)

visit(0)
print(len(visited))
