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
    
def up(string):
    if string == '3':
        return('1')
    elif string in [i for i in '678']:
        return(str(int(string) - 4))
    elif string == 'A':
        return('6')
    elif string == 'B':
        return('7')
    elif string == 'C':
        return('8')
    elif string == 'D':
        return('B')
    else:
        return('NotAllowed')
    
def down(string):
    if string == 'B':
        return('D')
    elif string == '6':
        return('A')
    elif string == '7':
        return('B')
    elif string == '8':
        return('C')
    elif string in [i for i in '234']:
        return(str(int(string) + 4))
    elif string == '1':
        return('3')
    else:
        return('NotAllowed')
        
def right(string):
    if string in [i for i in '235678']:
        return(str(int(string) + 1))
    elif string == 'A':
        return('B')
    elif string == 'B':
        return('C')
    else:
        return('NotAllowed')
        
def left(string):
    if string in [i for i in '346789']:
        return(str(int(string) - 1))
    elif string == 'B':
        return('A')
    elif string == 'C':
        return('B')
    else:
        return('NotAllowed')
        
sequence = ''
state = '5'

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
    sequence += state
 
print(sequence)
