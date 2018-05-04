# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 12:27:16 2018

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

total = 0

for line in all_lines:
    subtotal = 0
    for i in range(len(line)):
        if (line[i] == '\\') or (line[i] == '"'):
            subtotal += 1
    total += subtotal + 2
    
print(total)
