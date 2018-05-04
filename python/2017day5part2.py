# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 00:14:21 2017

@author: James Jiang
"""

def index_allow(x, list):
    try:
        list[x]
        return True
    except IndexError:
        return False

with open('Data.txt') as f:
    numbers = []
    for line in f:
        numbers.append(int(line))
        
index = 0
steps = 0
while index_allow(index, numbers) == True:
    a = numbers[index]
    if numbers[index] >= 3:
        numbers[index] -= 1
    else:
        numbers[index] += 1
    index += a
    steps += 1
    
print(steps)    
