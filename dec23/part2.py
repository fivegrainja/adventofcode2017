#! /usr/bin/env python3

import sys
import sympy

a = 1
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0

def report():
    return 'a:%d b:%d c:%d d:%d e:%d f:%d g:%d h:%d' % (a,b,c,d,e,f,g,h)

a = 1
b = (99 * 100) + 100000
c = b + 17000

while True: # line 32 comes here
    # f = 1
    # d = 2

    # while True: # jnz -13 comes here
    #     e = 2

    #     # while True: # jnz -8 comes here
    #     #     if d*e == b:
    #     #         f = 0
    #     #     e += 1
    #     #     if e == b:
    #     #         break
    #     if b % d == 0:
    #         f = 0

    #     d += 1
    #     if d == b:
    #         break

    # # if b is not prime inc h
    # if f == 0:
    #     h += 1

    if not sympy.ntheory.primetest.isprime(b):
        h += 1

    if b == c:
        print('h: %d' % h)
        sys.exit()   

    b += 17

    print(report())
