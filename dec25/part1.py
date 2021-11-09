#! /usr/bin/env python3

import argparse
import string
import collections
from pprint import pprint


# Begin in state A.
# Perform a diagnostic checksum after 12386363 steps.

state = 'A'
tape = [0] * 13000000
i = int(len(tape) / 2)

for step in range(12386363):

    if step % 1000000 == 0:
        print('step=%d' % step)

# In state A:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state B.
#   If the current value is 1:
#     - Write the value 0.
#     - Move one slot to the left.
#     - Continue with state E.

    if state == 'A':
        if tape[i] == 0:
            tape[i] = 1
            i += 1
            state = 'B'
        else:
            tape[i] = 0
            i -= 1
            state = 'E'


# In state B:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state C.
#   If the current value is 1:
#     - Write the value 0.
#     - Move one slot to the right.
#     - Continue with state A.

    elif state == 'B':
        if tape[i] == 0:
            tape[i] = 1
            i -= 1
            state = 'C'
        else:
            tape[i] = 0
            i += 1
            state = 'A'

# In state C:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state D.
#   If the current value is 1:
#     - Write the value 0.
#     - Move one slot to the right.
#     - Continue with state C.

    elif state == 'C':
        if tape[i] == 0:
            tape[i] = 1
            i -= 1
            state = 'D'
        else:
            tape[i] = 0
            i += 1
            state = 'C'

# In state D:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state E.
#   If the current value is 1:
#     - Write the value 0.
#     - Move one slot to the left.
#     - Continue with state F.
    elif state == 'D':
        if tape[i] == 0:
            tape[i] = 1
            i -= 1
            state = 'E'
        else:
            tape[i] = 0
            i -= 1
            state = 'F'

# In state E:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state A.
#   If the current value is 1:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state C.
    elif state == 'E':
        if tape[i] == 0:
            tape[i] = 1
            i -= 1
            state = 'A'
        else:
            tape[i] = 1
            i -= 1
            state = 'C'

# In state F:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state E.
#   If the current value is 1:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state A.
    elif state == 'F':
        if tape[i] == 0:
            tape[i] = 1
            i -= 1
            state = 'E'
        else:
            tape[i] = 1
            i += 1
            state = 'A'


print('checksum is %d' % sum(tape))

