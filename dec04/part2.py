#! /usr/local/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file')
args = parser.parse_args()

input_file = open(args.input_file)
input_lines = list(input_file.readlines())
input_file.close()

count = 0
for line in input_lines:
    words = line.strip().split()
    words = [''.join(sorted(list(w))) for w in words]
    if len(words) == len(set(words)):
        count += 1

print(count)