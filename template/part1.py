#! /usr/bin/env python3

import argparse
import string
import collections
from pprint import pprint
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


