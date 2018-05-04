# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 22:25:08 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

grid = [[i for i in line] for line in all_lines]

x_position = int((len(grid) + 1)/2) - 1
y_position = int((len(grid) + 1)/2) - 1
direction = 'up'

def turn_left(input):
    if input == 'up':
        return('left')
    if input == 'right':
        return('up')
    if input == 'down':
        return('right')
    if input == 'left':
        return('down')
        
def turn_right(input):
    if input == 'up':
        return('right')
    if input == 'right':
        return('down')
    if input == 'down':
        return('left')
    if input == 'left':
        return('up')
        
def move_forward(x, y, string):
    if string == 'up':
        if y != 0:
            return([x, y - 1])
        else:
            grid.insert(0, ['.' for i in range(len(grid[-1]))])
            return([x_position, 0])
    elif string == 'down':
        if y != len(grid) - 1:
            return([x, y + 1])
        else:
            grid.append(['.' for i in range(len(grid[-1]))])
            return([x_position, len(grid) - 1])
    elif string == 'left':
        if x != 0:
            return([x - 1, y])
        else:
            for j in range(len(grid)):
                grid[j].insert(0, '.')
            return([0, y_position])
    elif string == 'right':
        if x != len(grid[0]) - 1:
            return([x + 1, y])
        else:
            for j in range(len(grid)):
                grid[j].append('.')
            return([len(grid[0]) - 1, y_position])

total = 0

for i in range(10000):
    position = grid[y_position][x_position]
    if position == '#':
        grid[y_position][x_position] = '.'
        direction = turn_right(direction)
    elif position == '.':
        grid[y_position][x_position] = '#'
        direction = turn_left(direction)
        total += 1
    new_coordinates = move_forward(x_position, y_position, direction)
    x_position = new_coordinates[0]
    y_position = new_coordinates[1]

print(total)  
