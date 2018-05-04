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
        
for instruction in all_instructions:
    if instruction[0] == 'R':
        direction = turn_right(direction)
    elif instruction[0] == 'L':
        direction = turn_left(direction)
    if direction == 'north':
        y_position += int(instruction[1:])
    elif direction == 'east':
        x_position += int(instruction[1:])
    elif direction == 'south':
        y_position -= int(instruction[1:])
    elif direction == 'west':
        x_position -= int(instruction[1:])
        
print(abs(x_position) + abs(y_position))
