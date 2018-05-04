# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 14:52:07 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

all_instructions = []
for string in all_lines:
    chars = [i for i in string]
    all_instructions.append(chars)
    
def up(number):
    if (number > 3) and (number < 10):
        return(number - 3)
    else:
        return('NotAllowed')
    
def down(number):
    if (number > 0) and (number < 7):
        return(number + 3)
    else:
        return('NotAllowed')
        
def right(number):
    allowable = [1, 2, 4, 5, 7, 8]
    if number in allowable:
        return(number + 1)
    else:
        return('NotAllowed')
        
def left(number):
    allowable = [2, 3, 5, 6, 8, 9]
    if number in allowable:
        return(number - 1)
    else:
        return('NotAllowed')
        
sequence = ''
state = 5

for instruction in all_instructions:
    for move in instruction:
        if move == 'U':
            if up(state) != 'NotAllowed':
                state = up(state)
        elif move == 'R':
            if right(state) != 'NotAllowed':
                state = right(state)
        elif move == 'D':
            if down(state) != 'NotAllowed':
                state = down(state)
        elif move == 'L':
            if left(state) != 'NotAllowed':
                state = left(state)
    sequence += str(state)
 
print(int(sequence))
