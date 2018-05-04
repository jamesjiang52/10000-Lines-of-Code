# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 07:28:32 2018

@author: James Jiang
"""

with open('Data.txt') as f:
    for line in f:
        string = line

floor = 0
      
for i in range(len(string)):
    if string[i] == '(':
        floor += 1
    elif string[i] == ')':
        floor -= 1
    if floor < 0:
        print(i + 1)
        break