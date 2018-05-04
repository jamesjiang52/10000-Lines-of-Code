# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 23:56:29 2017

@author: James Jiang
"""

string = ''
with open('Data.txt') as f:
    for line in f:
        string = line

def fix(input):
    input_chars = [i for i in input]
    del input_chars[0]
    del input_chars[-1]
    fixed_string = ''.join(input_chars)
    output = fixed_string.split('x')
    return([int(i) for i in output])

def length(input):
    if '(' not in input:
        return(len(input))
    else:
        total = 0
        index = 0
        while index in range(len(input)):
            if input[index] != '(':
                index += 1
                total += 1
            else:
                index_other = input.index(')', index)
                pair = fix(input[index:index_other + 1])
                total += pair[1] * length(input[index_other + 1:index_other + 1 + pair[0]])
                index += (index_other + pair[0] - index + 1)
        return(total)

entire_length = 0
index = 0
while index in range(len(string)):
    if string[index] == '(':
        index_other = string.index(')', index)
        pair = fix(string[index:index_other + 1])
        end = index_other + 1 + pair[0]
        entire_length += length(string[index:end])
        index += (index_other + pair[0] - index + 1)
    else:
        entire_length += 1
        index += 1
        
print(entire_length)
