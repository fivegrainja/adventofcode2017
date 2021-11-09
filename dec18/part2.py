#! /usr/bin/env python3

import argparse
import string
import collections
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file')
args = parser.parse_args()

input_file = open(args.input_file)
input_lines = list(input_file.readlines())
input_file.close()

reg0 = {'p': 0}
reg1 = {'p': 1}
regs = [reg0, reg1]

def get_value(p, x):
    global reg
    if x in string.ascii_lowercase:
        if p == 0:
            return reg0.get(x, 0)
        elif p == 1:
            return reg1.get(x, 0)
        else:
            raise('unknown pid %s' % p)
    return int(x)

pos=[0,0]
q0 = []
q1 = []
qs = [q0, q1]
done = [False, False]

p1sent = 0


def execute(p):
    #pprint(reg)
    #import pdb; pdb.set_trace()
    global qs
    global pos
    global p1sent
    global regs

    reg = regs[p]
    q = qs[p]
    if p == 0:
        other_q = qs[1]
    else:
        other_q = qs[0]

    while True:
        i = pos[p]
        parts = input_lines[i].strip().split()
        op = parts[0]
        r = parts[1]
        if len(parts) > 2:
            o = parts[2]
        else:
            o = None
        print('p:%d %s' % (p, ' '.join([op, r, str(o)])))
        if op == 'snd':
            x = get_value(p, r)
            other_q.append(x)
            if p == 1:
                p1sent += 1
            #last_snd = x
        elif op == 'set':
            reg[r] = get_value(p, o)
        elif op == 'add':
            reg[r] += get_value(p, o)
        elif op == 'mul':
            reg[r] = get_value(p, r) * get_value(p, o)
        elif op == 'mod':
            reg[r] = get_value(p, r) % get_value(p, o)
        elif op == 'rcv':
            if not q:
                return
            reg[r] = q.pop(0)

        if op == 'jgz':
            #import pdb; pdb.set_trace()
            if get_value(p, r) > 0:
                pos[p] += get_value(p, o)
            else:
                pos[p] += 1
        else:
            pos[p] += 1
        
        if pos[p] >= len(input_lines):
            done[p] = True
            return

execute(0)
execute(1)
while True:
    if q0 and not done[0]:
        execute(0)
    if q1 and not done[1]:
        execute(1)
    if not qs[0] and not qs[1]:
        break

print('p1sent: %d' % p1sent)