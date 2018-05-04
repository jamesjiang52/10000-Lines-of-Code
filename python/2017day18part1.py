# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 23:58:16 2017

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

for instruction in all_instructions:
    if instruction[1] not in dict_values:
        if is_int(instruction[1]) == False:
            dict_values[instruction[1]] = 0
            
def value(n):
    if is_int(n) == True:
        return(int(n))
    else:
        return(dict_values[n]) 
   
sound = 0       
i = 0
while i in list(range(len(all_instructions))):
    current_instruction = all_instructions[i]
    if current_instruction[0] == 'snd':
        sound = value(current_instruction[1])
    elif current_instruction[0] == 'set':
        dict_values[current_instruction[1]] = value(current_instruction[2])
    elif current_instruction[0] == 'add':
        dict_values[current_instruction[1]] += value(current_instruction[2])
    elif current_instruction[0] == 'mul':
        dict_values[current_instruction[1]] *= value(current_instruction[2])
    elif current_instruction[0] == 'mod':
        dict_values[current_instruction[1]] %= value(current_instruction[2])
    elif current_instruction[0] == 'rcv':
        if value(current_instruction[1]) != 0:
            break
    if current_instruction[0] == 'jgz':
        if value(current_instruction[1]) > 0:
            i += value(current_instruction[2])
        else:
            i += 1
    else:
        i += 1
        
print(sound)
