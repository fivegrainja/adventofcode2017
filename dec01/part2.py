#! /usr/bin/env python3

f = open('input.txt', 'r')
t = f.read().strip()
f.close()

#t = '91212129'
#t = '1122'
#t = '1111'
#t = '1234'
#t = '12131415'

ints = [int(c) for c in t]
num_ints = len(ints)
halfway = int(len(ints) / 2)

sum = 0
for i in range(len(ints)):
    if ints[i] == ints[(i + halfway) % num_ints]:
        sum += ints[i]
        
print('sum is %d' % sum)
