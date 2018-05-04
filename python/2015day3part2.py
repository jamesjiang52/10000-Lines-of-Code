# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 07:41:33 2018

@author: James Jiang
"""

with open('Data.txt') as f:
    for line in f:
        string = line
        
x_position_santa = 0
y_position_santa = 0
x_position_robo = 0
y_position_robo = 0
grid = [['visited']]

for i in range(0, len(string), 2):
    if string[i] == '^':
        if y_position_santa == 0:
            y_position_robo += 1
        if y_position_santa == 0:
            insert_list = ['.' for i in range(len(grid[0]))]
            grid.insert(0, insert_list)
        else:
            y_position_santa -= 1
        grid[y_position_santa][x_position_santa] = 'visited'
    elif string[i] == 'v':
        if y_position_santa == len(grid) - 1:
            insert_list = ['.' for i in range(len(grid[0]))]
            grid.append(insert_list)
            y_position_santa = len(grid) - 1
        else:
            y_position_santa += 1
        grid[y_position_santa][x_position_santa] = 'visited'
    elif string[i] == '>':
        if x_position_santa == len(grid[0]) - 1:
            for row in grid:
                row.append('.')
            x_position_santa = len(grid[0]) - 1
        else:
            x_position_santa += 1
        grid[y_position_santa][x_position_santa] = 'visited'
    elif string[i] == '<':
        if x_position_santa == 0:
            for row in grid:
                row.insert(0, '.')
            x_position_robo += 1
        else:
            x_position_santa -= 1
        grid[y_position_santa][x_position_santa] = 'visited'
        
for i in range(1, len(string), 2):
    if string[i] == '^':
        if y_position_robo == 0:
            insert_list = ['.' for i in range(len(grid[0]))]
            grid.insert(0, insert_list)
        else:
            y_position_robo -= 1
        grid[y_position_robo][x_position_robo] = 'visited'
    elif string[i] == 'v':
        if y_position_robo == len(grid) - 1:
            insert_list = ['.' for i in range(len(grid[0]))]
            grid.append(insert_list)
            y_position_robo = len(grid) - 1
        else:
            y_position_robo += 1
        grid[y_position_robo][x_position_robo] = 'visited'
    elif string[i] == '>':
        if x_position_robo == len(grid[0]) - 1:
            for row in grid:
                row.append('.')
            x_position_robo = len(grid[0]) - 1
        else:
            x_position_robo += 1
        grid[y_position_robo][x_position_robo] = 'visited'
    elif string[i] == '<':
        if x_position_robo == 0:
            for row in grid:
                row.insert(0, '.')
        else:
            x_position_robo -= 1
        grid[y_position_robo][x_position_robo] = 'visited'

total = 0
for row in grid:
    total += row.count('visited')
    
print(total)