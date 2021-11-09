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
    these_children = [s.strip(',') for s in parts[3:]]

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
root = root.pop()

total_weights = {}
def assign_weight(name):
    total = weights[name]
    for child in children[name]:
        total += assign_weight(child)
    total_weights[name] = total
    return total

assign_weight(root)

def check_children(name):
    kids = children[name]
    if not kids:
        return
    kid_weight = total_weights[kids[0]]
    for kid in kids[1:]:
        if total_weights[kid] != kid_weight:
            print('unbalanced parent is %s' % name)
            print('kid weights are')
            for kid in kids:
                print('%s: %s %s' % (kid, weights[kid], total_weights[kid]))
            break
    for kid in kids:
        check_children(kid)
    
check_children(root)

