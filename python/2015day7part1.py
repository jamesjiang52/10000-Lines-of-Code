# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 11:01:30 2018

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]
all_instructions = [line.split(' -> ') for line in all_lines]
for instruction in all_instructions:
    instruction[0] = instruction[0].split(' ')
   
dict_wires = {}
    
def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
    
def value(string):
    if is_int(string) == True:
        return(int(string))
    else:
        return(dict_wires[string])

def bit_not_16(dec):
    return(2**16 + ~dec)
    
def left_shift_16(dec, amount):
    return((dec << amount) % 2**16)

while len(dict_wires) < len(all_instructions):
    for instruction in all_instructions:
        if len(instruction[0]) == 1:
            if is_int(instruction[0][0]) == True:
                dict_wires[instruction[1]] = int(instruction[0][0])
            elif instruction[0][0] in dict_wires:
                dict_wires[instruction[1]] = dict_wires[instruction[0][0]]
        elif instruction[0][0] == 'NOT':
            if instruction[0][1] in dict_wires:
                dict_wires[instruction[1]] = bit_not_16(dict_wires[instruction[0][1]])
        elif instruction[0][1] == 'AND':
            if is_int(instruction[0][0]) == True:
                if instruction[0][2] in dict_wires:
                    dict_wires[instruction[1]] = int(instruction[0][0]) & dict_wires[instruction[0][2]]
            elif (instruction[0][0] in dict_wires) and (instruction[0][2] in dict_wires):
                dict_wires[instruction[1]] = dict_wires[instruction[0][0]] & dict_wires[instruction[0][2]]
        elif instruction[0][1] == 'OR':
            if (instruction[0][0] in dict_wires) and (instruction[0][2] in dict_wires):
                dict_wires[instruction[1]] = dict_wires[instruction[0][0]] | dict_wires[instruction[0][2]]
        elif instruction[0][1] == 'LSHIFT':
            if instruction[0][0] in dict_wires:
                dict_wires[instruction[1]] = left_shift_16(dict_wires[instruction[0][0]], int(instruction[0][2]))
        elif instruction[0][1] == 'RSHIFT':
            if instruction[0][0] in dict_wires:
                dict_wires[instruction[1]] = dict_wires[instruction[0][0]] >> int(instruction[0][2])
                
print(dict_wires['a'])  
              