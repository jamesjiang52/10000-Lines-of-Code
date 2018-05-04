# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 14:33:06 2017

@author: James Jiang
"""

with open('Data.txt') as f:
    for line in f:
        string = line
        
all_instructions = string.split(', ')

x_position = 0
y_position = 0
direction = 'north'

def turn_left(string):
    if string == 'north':
        return('west')
    if string == 'east':
        return('north')
    if string == 'south':
        return('east')
    if string == 'west':
        return('south')
        
def turn_right(string):
    if string == 'north':
        return('east')
    if string == 'east':
        return('south')
    if string == 'south':
        return('west')
    if string == 'west':
        return('north')

memory = [[0, 0]]
dummy = 0
       
for instruction in all_instructions:
    if dummy != 0:
        break
    if instruction[0] == 'R':
        direction = turn_right(direction)
    elif instruction[0] == 'L':
        direction = turn_left(direction)
    if direction == 'north':
        for i in range(int(instruction[1:])):
            y_position += 1
            if [x_position, y_position] in memory:
                print(abs(x_position) + abs(y_position))
                dummy = 1
                break
            else:
                memory.append([x_position, y_position])
    elif direction == 'east':
        for i in range(int(instruction[1:])):
            x_position += 1
            if [x_position, y_position] in memory:
                print(abs(x_position) + abs(y_position))
                dummy = 1
                break
            else:
                memory.append([x_position, y_position])
    elif direction == 'south':
        for i in range(int(instruction[1:])):
            y_position -= 1
            if [x_position, y_position] in memory:
                print(abs(x_position) + abs(y_position))
                dummy = 1
                break
            else:
                memory.append([x_position, y_position])
    elif direction == 'west':
        for i in range(int(instruction[1:])):
            x_position -= 1
            if [x_position, y_position] in memory:
                print(abs(x_position) + abs(y_position))
                dummy = 1
                break
            else:
                memory.append([x_position, y_position])
