# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 00:23:31 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]
all_instructions = [line.split(' ') for line in all_lines]
all_instructions.reverse()

password = [i for i in 'fbgdceah']

def rotate_right(input, amount):
    amount = amount % 8
    return(input[-amount:] + input[:-amount])
    
def rotate_left(input, amount):
    amount = amount % 8
    return(input[amount:] + input[:amount])
    
def based_rotate(input, letter):
    amount = 1 + input.index(letter)
    if input.index(letter) >= 4:
        amount += 1
    return(rotate_right(input, amount))
    
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
            password_copy = password[:]
            for i in range(8):
                password_check = rotate_left(password_copy, i)
                if based_rotate(password_check, instruction[-1]) == password:
                    password = password_check
                    break
        else:
            if instruction[1] == 'left':
                password = rotate_right(password, int(instruction[2]))
            elif instruction[1] == 'right':
                password = rotate_left(password, int(instruction[2]))
    elif instruction[0] == 'reverse':
        index1 = int(instruction[2])
        index2 = int(instruction[-1])
        password[index1:index2 + 1] = password[index1:index2 + 1][::-1]
    elif instruction[0] == 'move':
        index1 = int(instruction[-1])
        index2 = int(instruction[2])
        a = password[index1]
        del password[index1]
        password.insert(index2, a)
        
print(''.join(password)) 
       
