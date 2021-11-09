#! /usr/bin/env python3

input = '10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6'
#input = '0 2 7 0'

banks = [int(d) for d in input.split()]
num_banks = len(banks)

def get_largest_bank():
    large_bank_index = 0
    large_bank_size = 0
    for i in range(num_banks):
        if banks[i] > large_bank_size:
            large_bank_index = i
            large_bank_size = banks[i]
    return large_bank_index

def redistribute(bank_index):
    count = banks[bank_index]
    banks[bank_index] = 0 
    for i in range(count):
        bank_index = (bank_index + 1) % num_banks
        banks[bank_index] += 1

cycles = 0
history = set()

while True:
    lengths = ','.join([str(banks[i]) for i in range(num_banks)])
    if lengths in history:
        break
    history.add(lengths)
    print(lengths)

    bank_index = get_largest_bank()
    redistribute(bank_index)
    cycles += 1

print(cycles)
