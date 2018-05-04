# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 07:41:33 2018

@author: James Jiang
"""

with open('Data.txt') as f:
    for line in f:
        string = line
        
x_position = 0
y_position = 0
grid = [['visited']]

for i in range(len(string)):
    if string[i] == '^':
        if y_position == 0:
            insert_list = ['.' for i in range(len(grid[0]))]
            grid.insert(0, insert_list)
        else:
            y_position -= 1
        grid[y_position][x_position] = 'visited'
    elif string[i] == 'v':
        if y_position == len(grid) - 1:
            insert_list = ['.' for i in range(len(grid[0]))]
            grid.append(insert_list)
            y_position = len(grid) - 1
        else:
            y_position += 1
        grid[y_position][x_position] = 'visited'
    elif string[i] == '>':
        if x_position == len(grid[0]) - 1:
            for row in grid:
                row.append('.')
            x_position = len(grid[0]) - 1
        else:
            x_position += 1
        grid[y_position][x_position] = 'visited'
    elif string[i] == '<':
        if x_position == 0:
            for row in grid:
                row.insert(0, '.')
        else:
            x_position -= 1
        grid[y_position][x_position] = 'visited'

total = 0
for row in grid:
    total += row.count('visited')
    
print(total)