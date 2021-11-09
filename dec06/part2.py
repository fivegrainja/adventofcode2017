#! /usr/bin/env python3

import argparse
import string
import collections
import hashlib
import re
import itertools
import csv
import sympy
import numpy
import llist

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

# parser = argparse.ArgumentParser()
# parser.add_argument('input_file', help='input file')
# args = parser.parse_args()

# input_file = open(args.input_file)
# input_lines = list(input_file.readlines())
# input_file.close()

input = '10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6'
#input = '0 2 7 0'

banks = [int(d) for d in input.split()]
num_banks = len(banks)

def get_largest_bank():
    large_bank_index = 0
    large_bank_size = 0
    for i in range(num_banks):
        if banks[i] > large_bank_size:
            large_bank_index = i
            large_bank_size = banks[i]
    return large_bank_index

def redistribute(bank_index):
    count = banks[bank_index]
    banks[bank_index] = 0 
    for i in range(count):
        bank_index = (bank_index + 1) % num_banks
        banks[bank_index] += 1

cycles = 0
started_loop = False
history = set()

while True:
    lengths = ','.join([str(banks[i]) for i in range(num_banks)])
    if lengths in history:
        if started_loop:
            break
        history = set()
        started_loop = True
        cycles = 0
    history.add(lengths)
    print(lengths)

    bank_index = get_largest_bank()
    redistribute(bank_index)
    cycles += 1

print(cycles)
