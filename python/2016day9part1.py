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

total = 0
index = 0

while index in range(len(string)):
    if string[index] == '(':
        index_other = string.index(')', index)
        pair = fix(string[index:index_other + 1])
        total += pair[0] * pair[1]
        index += (index_other + pair[0] - index + 1)
    else:
        total += 1
        index += 1
        
print(total)
