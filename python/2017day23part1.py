# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 21:15:20 2017

@author: James Jiang
"""

def is_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

all_instructions = []
for line in all_lines:
    components = line.split(' ')
    all_instructions.append(components)
    
dict_values = {}

for i in [j for j in 'abcdefgh']:
    dict_values[i] = 0

def value(n):
    if is_int(n) == True:
        return(int(n))
    else:
        return(dict_values[n])

total = 0
i = 0       
while i in list(range(len(all_instructions))):
    current_instruction = all_instructions[i]
    if current_instruction[0] == 'set':
        dict_values[current_instruction[1]] = value(current_instruction[2])
    elif current_instruction[0] == 'sub':
        dict_values[current_instruction[1]] -= value(current_instruction[2])
    elif current_instruction[0] == 'mul':
        dict_values[current_instruction[1]] *= value(current_instruction[2])
        total += 1
    if current_instruction[0] == 'jnz':
        if value(current_instruction[1]) != 0:
            i += value(current_instruction[2])
        else:
            i += 1
    else:
        i += 1
        
print(total) 
