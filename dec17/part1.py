#! /usr/bin/env python3

import collections

test = False
if test:
    step_size = 3
else:
    step_size = 371

b = collections.deque([0])

for step in range(1, 2018):
    b.rotate(-(step_size+1))
    b.appendleft(step)

print(b[1])