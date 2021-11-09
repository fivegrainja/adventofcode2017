#! /usr/bin/env python3

f = open('input.txt', 'r')
t = f.readlines()
f.close()

#t = ['5 9 2 8', '9 4 7 3', '3 8 6 5']

sum = 0
for line in t:
    ints = [int(i) for i in line.split()]
    for x in ints:
        for y in ints:
            if x != y:
                if x % y == 0:
                    sum += x / y
        
print('sum is %d' % sum)
