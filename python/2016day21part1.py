# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 00:23:31 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]
all_instructions = [line.split(' ') for line in all_lines]

password = [i for i in 'abcdefgh']

def rotate_right(amount):
    amount = amount % 8
    return(password[-amount:] + password[:-amount])
    
def rotate_left(amount):
    amount = amount % 8
    return(password[amount:] + password[:amount])
    
for instruction in all_instructions:
    if instruction[0] == 'swap':
        if instruction[1] == 'position':
            index1 = int(instruction[2])
            index2 = int(instruction[-1])
            password[index1], password[index2] = password[index2], password[index1]
        elif instruction[1] == 'letter':
            index1 = password.index(instruction[2])
            index2 = password.index(instruction[-1])
            password[index1], password[index2] = password[index2], password[index1]
    elif instruction[0] == 'rotate':
        if instruction[1] == 'based':
            amount = 1 + password.index(instruction[-1])
            if password.index(instruction[-1]) >= 4:
                amount += 1
            password = rotate_right(amount)
        else:
            if instruction[1] == 'left':
                password = rotate_left(int(instruction[2]))
            elif instruction[1] == 'right':
                password = rotate_right(int(instruction[2]))
    elif instruction[0] == 'reverse':
        index1 = int(instruction[2])
        index2 = int(instruction[-1])
        password[index1:index2 + 1] = password[index1:index2 + 1][::-1]
    elif instruction[0] == 'move':
        index1 = int(instruction[2])
        index2 = int(instruction[-1])
        a = password[index1]
        del password[index1]
        password.insert(index2, a)
        
print(''.join(password)) 
       
