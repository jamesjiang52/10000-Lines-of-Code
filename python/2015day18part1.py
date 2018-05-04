# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 15:00:34 2018

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

grid = [[i for i in line] for line in all_lines]
grid_num_neighbors = []
for i in range(100):
    row = [0 for j in range(100)]
    grid_num_neighbors.append(row)

def neighbors_on(x, y):
    if x_position == 0:
        if y_position == 0:
            neighbors = [grid[y + 1][x], grid[y][x + 1], grid[y + 1][x + 1]]
        elif y_position == 99:
            neighbors = [grid[y - 1][x], grid[y][x + 1], grid[y - 1][x + 1]]
        else:
            neighbors = [grid[y + 1][x], grid[y - 1][x], grid[y][x + 1], grid[y + 1][x + 1], grid[y - 1][x + 1]]
    elif y_position == 0:
        if x_position == 99:
            neighbors = [grid[y + 1][x], grid[y][x - 1], grid[y + 1][x - 1]]
        else:
            neighbors = [grid[y + 1][x], grid[y][x + 1], grid[y][x - 1], grid[y + 1][x + 1], grid[y + 1][x - 1]]
    elif x_position == 99:
        if y_position == 99:
            neighbors = [grid[y - 1][x], grid[y][x - 1], grid[y - 1][x - 1]]
        else:
            neighbors = [grid[y + 1][x], grid[y - 1][x], grid[y][x - 1], grid[y + 1][x - 1], grid[y - 1][x - 1]]
    elif y_position == 99:
        neighbors = [grid[y - 1][x], grid[y][x + 1], grid[y][x - 1], grid[y - 1][x + 1], grid[y - 1][x - 1]]
    else:
        neighbors = [grid[y + 1][x], grid[y - 1][x], grid[y][x + 1], grid[y][x - 1], grid[y + 1][x + 1], grid[y + 1][x - 1], grid[y - 1][x + 1], grid[y - 1][x - 1]]
    return(neighbors.count('#'))
                           
def next_state(x, y):
    if grid_num_neighbors[y][x] == 3:
        return('#')
    elif (grid_num_neighbors[y][x] == 2) and (grid[y][x] == '#'):
        return('#')
    else:
        return('.')

for i in range(100):
    for y_position in range(100):
        for x_position in range(100):
            grid_num_neighbors[y_position][x_position] = neighbors_on(x_position, y_position)
    for y_position in range(100):
        for x_position in range(100):
            grid[y_position][x_position] = next_state(x_position, y_position)
            
total = 0
for y in range(100):
    total += grid[y].count('#')
                 
print(total)