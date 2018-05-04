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
    
dict_values_0 = {}
dict_values_1 = {}

for instruction in all_instructions:
    if instruction[1] not in dict_values_0:
        if is_int(instruction[1]) == False:
            dict_values_0[instruction[1]] = 0
    if instruction[1] not in dict_values_1:
        if is_int(instruction[1]) == False:
            if instruction[1] == 'p':
                dict_values_1[instruction[1]] = 1
            else:
                dict_values_1[instruction[1]] = 0 

def value(n, values_dict):
    if is_int(n) == True:
        return(int(n))
    else:
        return(values_dict[n])
        
queue_0 = []
queue_1 = []
      
terminate_0 = 0
terminate_1 = 0

i_0 = 0
i_1 = 0

counter = 0

while True:
    if (terminate_0 == 1) and (terminate_1 == 1):
        break
    current_instruction_0 = all_instructions[i_0]
    current_instruction_1 = all_instructions[i_1]
    if (current_instruction_0[0] == 'rcv') and (current_instruction_1[0] == 'rcv') and (len(queue_0) == 0) and (len(queue_1) == 0):
        break
    if terminate_0 == 0:
        if current_instruction_0[0] == 'snd':
            queue_1.append(value(current_instruction_0[1], dict_values_0))
        elif current_instruction_0[0] == 'set':
            dict_values_0[current_instruction_0[1]] = value(current_instruction_0[2], dict_values_0)
        elif current_instruction_0[0] == 'add':
            dict_values_0[current_instruction_0[1]] += value(current_instruction_0[2], dict_values_0)
        elif current_instruction_0[0] == 'mul':
            dict_values_0[current_instruction_0[1]] *= value(current_instruction_0[2], dict_values_0)
        elif current_instruction_0[0] == 'mod':
            dict_values_0[current_instruction_0[1]] %= value(current_instruction_0[2], dict_values_0)
        elif current_instruction_0[0] == 'rcv':
            if len(queue_0) > 0:
                dict_values_0[current_instruction_0[1]] = queue_0[0]
                del queue_0[0]
            else:
                i_0 -= 1
        if current_instruction_0[0] == 'jgz':
            if value(current_instruction_0[1], dict_values_0) > 0:
                i_0 += value(current_instruction_0[2], dict_values_0)
            else:
                i_0 += 1
        else:
            i_0 += 1
        if i_0 not in list(range(len(all_instructions))):
            terminate_0 = 1
        
    if terminate_1 == 0:
        if current_instruction_1[0] == 'snd':
            queue_0.append(value(current_instruction_1[1], dict_values_1))
            counter += 1
        elif current_instruction_1[0] == 'set':
            dict_values_1[current_instruction_1[1]] = value(current_instruction_1[2], dict_values_1)
        elif current_instruction_1[0] == 'add':
            dict_values_1[current_instruction_1[1]] += value(current_instruction_1[2], dict_values_1)
        elif current_instruction_1[0] == 'mul':
            dict_values_1[current_instruction_1[1]] *= value(current_instruction_1[2], dict_values_1)
        elif current_instruction_1[0] == 'mod':
            dict_values_1[current_instruction_1[1]] %= value(current_instruction_1[2], dict_values_1)
        elif current_instruction_1[0] == 'rcv':
            if len(queue_1) > 0:
                dict_values_1[current_instruction_1[1]] = queue_1[0]
                del queue_1[0]
            else:
                i_1 -= 1
        if current_instruction_1[0] == 'jgz':
            if value(current_instruction_1[1], dict_values_1) > 0:
                i_1 += value(current_instruction_1[2], dict_values_1)
            else:
                i_1 += 1
        else:
            i_1 += 1  
        if i_1 not in list(range(len(all_instructions))):
            terminate_1 = 1

print(counter)
