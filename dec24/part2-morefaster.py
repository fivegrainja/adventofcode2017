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

# All this works on the assumption that there are no duplice
# components - that is two components that share the same
# two port sizes. I confirmed this for my input.

# all_comps a dictionary allowing lookup of components by size
# key is the size, value is list of sizes pair with that one
# each component is actually in there twice, once for each of the 
# two sizes.
all_comps = collections.defaultdict(list)
for line in input_lines:
    p1, p2 = [int(p) for p in line.strip().split('/')]
    all_comps[p1].append(p2)
    all_comps[p2].append(p1)

# Get list of all components from all_comps that match size and haven't been used yet.
def get_options(size, comps):
    # Options are returned with size as the first element in each option
    return [(size, c) for c in comps[size]]

def build(bridge, size, comps):
    # given a single list in bridge
    # return a list of all possible bridges starting with bridge using comps
    # used is things in comps that have already been used
    bridges = [bridge]
    options = get_options(size, comps)
    for option in options:
        comps[option[0]].remove(option[1])
        comps[option[1]].remove(option[0])
        bridges.extend(build(bridge + [option], option[1], comps))
        comps[option[0]].append(option[1])
        comps[option[1]].append(option[0])
    return bridges

def strength(bridge):
    s = 0
    for c in bridge:
        s += c[0]
        s += c[1]
    return s

def get_highest_strength(bridges):
    return max([strength(b) for b in bridges])

def get_longest_length(bridges):
    return max([len(b) for b in bridges])

def get_longest_bridges(bridges):
    max_length = 0
    longest = []
    for b in bridges:
        l = len(b)
        if l > max_length:
            max_length = l
            longest = [b]
        elif l == max_length:
            longest.append(b)
    return longest

all_bridges = build([], 0, all_comps)

print('Strength of strongest bridge: %d' % get_highest_strength(all_bridges))

print('Strength of longest bridges: %d' % get_highest_strength(get_longest_bridges(all_bridges)))