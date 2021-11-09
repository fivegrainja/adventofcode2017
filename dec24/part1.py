#! /usr/bin/env python3

import argparse
import string
import collections
from pprint import pprint
import copy
#import hashlib
#import re
#import itertools
#import csv
#import sympy
#import numpy
#import llist

# Collections documentation:
# https://docs.python.org/3/library/collections.html
#
# c = collections.Counter(name)
# common = sorted(c.most_common(), key=cmp_key, reverse=False)
#
# d = collections.deque(iterable, maxlen)
# 
# hashlib.md5(b"Nobody inspects the spammish repetition").hexdigest()
#
# @lru_cache(maxsize=None) - decorator to memoize return values
#
# m = re.search('(?<=abc)def', 'abcdef')
# m.group(0)
#
# double_linked_list = llist.dllist(iterator)  - rotate, pop, append, appendright, nodeat
#
# Prime factorization
# from sympy.ntheory import factorint
# factorint(2000)    # 2000 = (2**4) * (5**3)
# {2: 4, 5: 3}
#
# reader = csv.reader(file, delimiter=',', quotechar='|') # each row in reader is a list
# dictreader = csv.DictReader(file) # each row in dictreader is a dict
#
# EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
# import csv
# for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
#     print(emp.name, emp.title)
#
# sympy.ntheory.primetest.isprime(n)

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file')
args = parser.parse_args()

input_file = open(args.input_file)
input_lines = list(input_file.readlines())
input_file.close()

# comps = collections.defaultdict(list)

# def add_comp(p1, p2):
#     comps[p1].append(p2)
#     comps[p2].append(p1)

# def rem_comp(p1, p2):
#     comps[p1].remove(p2)
#     comps[p2].remove(p1)

all_comps = set()
for line in input_lines:
    p1, p2 = sorted([int(p) for p in line.strip().split('/')])
    all_comps.add((p1, p2))

def build(bridge, size, comps):
    # given a single list in bridge
    # return a list of all possible bridges starting with bridge using comps
    bridges = [bridge]
    options = [tuple(sorted(list(c))) for c in comps if size == c[0] or size == c[1]]
    for option in options:
        next_comps = copy.deepcopy(comps)
        next_comps.remove(option)
        if option[0] == size:
            next_size = option[1]
        else:
            next_size = option[0]
        bridges.extend(build(bridge + [option], next_size, next_comps))
    return bridges

def strength(bridge):
    s = 0
    for c in bridge:
        s += c[0]
        s += c[1]
    return s

#import pdb; pdb.set_trace()
all_bridges = build([], 0, all_comps)
# for b in all_bridges:
#     print(str(b))

strong_bridge = None
strong_strength = -1
for b in all_bridges:
    s = strength(b)
    if s > strong_strength:
        strong_bridge = b
        strong_strength = s

print('num bridges: %d' % len(bridges))
print('strongest: %d' % strong_strength)
print('strongest: %s' % str(strong_bridge))



