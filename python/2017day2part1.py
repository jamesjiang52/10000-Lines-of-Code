# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 12:38:57 2017

@author: James Jiang
"""

with open('Data.txt') as f:
    all_lines = []
    for line in f:
        line = line.strip()
        all_lines.append(line)
        
all_rows = []
for line in all_lines:
    row = line.split('\t')
    row_int = [int(i) for i in row]
    all_rows.append(row_int)

sum = 0
for i in range(len(all_rows)):
    sum += (max(all_rows[i]) - min(all_rows[i]))
    
print(sum)
