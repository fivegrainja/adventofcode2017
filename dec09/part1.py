#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file')
args = parser.parse_args()

input_file = open(args.input_file)
stream = input_file.read()
input_file.close()

total_score = 0
total_garbage = 0

def consume_group(text, score=0):
    # text should start with {
    # score is score of containing group
    #return length of what was consumed
    global total_score
    global total_garbage
    if score == 0:
        total_score = 0

    i = 1
    is_garbage = False
    my_score = score + 1
    total_score += my_score
    while True:
        if text[i] == '!':
            i += 2
            continue
        if is_garbage:
            if text[i] == '>':
                is_garbage = False
            else:
                total_garbage += 1
            i += 1
            continue
        if text[i] == '<':
            is_garbage = True
            i += 1
            continue
        if text[i] == '{':
            subgroup_length = consume_group(text[i:], my_score)
            i += subgroup_length
            continue
        if text[i] == '}':
            return i + 1
        i += 1


consume_group(stream)
print('total_score: %s' % total_score)
print('total_garbage: %s' % total_garbage)

sys.exit()

consume_group('{}')
assert(total_score == 1)

consume_group('{{{}}}')
assert(total_score == 6)

consume_group('{{{},{},{{}}}}')
assert(total_score == 16)

consume_group('{<a>,<a>,<a>,<a>}')
assert(total_score == 1)

consume_group('{{<ab>},{<ab>},{<ab>},{<ab>}}')
assert(total_score == 9)

consume_group('{{<!!>},{<!!>},{<!!>},{<!!>}}')
assert(total_score == 9)

consume_group('{{<a!>},{<a!>},{<a!>},{<ab>}}')
assert(total_score == 3)






