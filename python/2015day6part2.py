# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 10:46:03 2018

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]
all_instructions = [line.split(' ') for line in all_lines]

for instruction in all_instructions:
    if instruction[0] == 'turn':
        del instruction[0]
    del instruction[2]
    instruction[1] = [int(i) for i in instruction[1].split(',')]
    instruction[2] = [int(i) for i in instruction[2].split(',')]

grid = []
for i in range(1000):
    row = [0 for j in range(1000)]
    grid.append(row)

for instruction in all_instructions:
    if instruction[0] == 'on':
        for y in range(instruction[1][1], instruction[2][1] + 1):
            for x in range(instruction[1][0], instruction[2][0] + 1):
                grid[y][x] += 1
    elif instruction[0] == 'off':
        for y in range(instruction[1][1], instruction[2][1] + 1):
            for x in range(instruction[1][0], instruction[2][0] + 1):
                grid[y][x] = max(0, grid[y][x] - 1)
    elif instruction[0] == 'toggle':
        for y in range(instruction[1][1], instruction[2][1] + 1):
            for x in range(instruction[1][0], instruction[2][0] + 1):
                grid[y][x] += 2
                    
total = 0
for row in grid:
    total += sum(row)
    
print(total)
    