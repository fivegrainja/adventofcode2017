#! /usr/bin/env python3

test = False
if test:
    startA = 65
    startB = 8921
    n = 1100
else:
    startA = 512
    startB = 191
    n = 5000000

factorA = 16807
factorB = 48271

def count_matches():
    matches = 0
    a = startA
    b = startB
    for i in range(n):
        if False and i % 100000 == 0:
            print('i=%d' % i)
            print('matches=%d' % matches)
        while True:
            a = (a * factorA) % 2147483647
            if a % 4 == 0:
                break
        while True:
            b = (b * factorB) % 2147483647
            if b % 8 == 0:
                break
        bin_a = bin(a)[2:].zfill(16)[-16:]
        bin_b = bin(b)[2:].zfill(16)[-16:]
        if test and False:
            print('a: %s' % bin_a)
            print('b: %s' % bin_b)
        if bin_a == bin_b:
            matches += 1
    return(matches)

num_matches = count_matches()
print('matches: %d' % num_matches)






