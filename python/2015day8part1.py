# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 12:27:16 2018

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

total = 0

for line in all_lines:
    subtotal = 0
    i = 0
    while i in range(len(line)):
        if line[i] == '\\':
            if line[i + 1] in ['"', '\\']:
                subtotal += 1
                i += 2
            elif line[i + 1] == 'x':
                subtotal += 3
                i += 4
        else:
            i += 1
    total += subtotal + 2
    
print(total)
