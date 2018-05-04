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

dummy = 0
sum = 0
for i in range(len(all_rows)):
    dummy = 0
    for j in range(len(all_rows[i])):
        if dummy == 0:
            for k in range(len(all_rows[i])):
                if (float(all_rows[i][j]/all_rows[i][k]).is_integer() == True) and (all_rows[i][j] != all_rows[i][k]):
                    sum += int(all_rows[i][j]/all_rows[i][k])
                    dummy += 1
                    break
    
print(sum)
