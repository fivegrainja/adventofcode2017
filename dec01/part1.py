#! /usr/bin/env python3

f = open('input.txt', 'r')
t = f.read().strip()
f.close()

#t = '91212129'
#t = '1122'
#t = '1111'
#t = '1234'

ints = [int(c) for c in t]
ints.append(ints[0])
sum = 0
for i in range(len(ints)-1):
    if ints[i] == ints[i+1]:
        sum += ints[i]
        
print('sum is %d' % sum)
