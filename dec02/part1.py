#! /usr/bin/env python3

f = open('input.txt', 'r')
t = f.readlines()
f.close()

sum = 0
for line in t:
    ints = [int(i) for i in line.split()]
    sum += max(ints) - min(ints)
        
print('sum is %d' % sum)
