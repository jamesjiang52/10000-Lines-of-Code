# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 00:06:18 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

instructions = []
for line in all_lines:
    strings = line.split()
    instructions.append(strings)
    
values_dict = {}

for i in range(len(instructions)):
    values_dict[instructions[i][0]] = 0

maximums = []

for i in range(len(instructions)):
    if instructions[i][-2] == '>':
        if values_dict[instructions[i][-3]] > int(instructions[i][-1]):
            if instructions[i][1] == 'inc':
                values_dict[instructions[i][0]] += int(instructions[i][2])
            else:
                values_dict[instructions[i][0]] -= int(instructions[i][2])
    if instructions[i][-2] == '<':
        if values_dict[instructions[i][-3]] < int(instructions[i][-1]):
            if instructions[i][1] == 'inc':
                values_dict[instructions[i][0]] += int(instructions[i][2])
            else:
                values_dict[instructions[i][0]] -= int(instructions[i][2])
    if instructions[i][-2] == '>=':
        if values_dict[instructions[i][-3]] >= int(instructions[i][-1]):
            if instructions[i][1] == 'inc':
                values_dict[instructions[i][0]] += int(instructions[i][2])
            else:
                values_dict[instructions[i][0]] -= int(instructions[i][2])
    if instructions[i][-2] == '<=':
        if values_dict[instructions[i][-3]] <= int(instructions[i][-1]):
            if instructions[i][1] == 'inc':
                values_dict[instructions[i][0]] += int(instructions[i][2])
            else:
                values_dict[instructions[i][0]] -= int(instructions[i][2])
    if instructions[i][-2] == '==':
        if values_dict[instructions[i][-3]] == int(instructions[i][-1]):
            if instructions[i][1] == 'inc':
                values_dict[instructions[i][0]] += int(instructions[i][2])
            else:
                values_dict[instructions[i][0]] -= int(instructions[i][2])
    if instructions[i][-2] == '!=':
        if values_dict[instructions[i][-3]] != int(instructions[i][-1]):
            if instructions[i][1] == 'inc':
                values_dict[instructions[i][0]] += int(instructions[i][2])
            else:
                values_dict[instructions[i][0]] -= int(instructions[i][2])
        
    maximum = values_dict[instructions[0][0]]
    for i in values_dict:
        if values_dict[i] > maximum:
            maximum = values_dict[i]
    maximums.append(maximum)
    
print(max(maximums))

