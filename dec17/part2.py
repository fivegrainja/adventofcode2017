#! /usr/bin/env python3

import collections

test = False
if test:
    step_size = 3
else:
    step_size = 371

b = collections.deque([0])

n = 50000000
for step in range(1, n+1):
    if step % 1000000 == 0:
        print('step %d' % step)
    b.rotate(-(step_size+1))
    b.appendleft(step)

i0 = b.index(0)
print(b[(i0 + 1) % len(b)])