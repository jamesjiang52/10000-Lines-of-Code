# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 22:25:08 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]
all_instructions = [line.split(' ') for line in all_lines]

display = []
for i in range(6):
    row = []
    for i in range(50):
        row.append('.')
    display.append(row)
    
def extend(length, height):
    for i in range(height):
        for j in range(length):
            display[i][j] = '#'
            
def rotate_horizontal(row_number, number):
    row = display[row_number][:]
    for i in range(number):
        row_last = row[-1]
        row[1:] = row[:-1]
        row[0] = row_last
    display[row_number] = row
    
def rotate_vertical(column_number, number):
    column = []
    for row in display:
        column.append(row[column_number])
    for i in range(number):
        column_last = column[-1]
        column[1:] = column[:-1]
        column[0] = column_last
    for i in range(len(display)):
        display[i][column_number] = column[i]

for instruction in all_instructions:
    if instruction[0] == 'rect':
        chars = instruction[1].split('x')
        extend(int(chars[0]), int(chars[1]))
    elif instruction[1] == 'row':
        chars = instruction[2].split('=')
        rotate_horizontal(int(chars[1]), int(instruction[-1]))
    elif instruction[1] == 'column':
        chars = instruction[2].split('=')
        rotate_vertical(int(chars[1]), int(instruction[-1]))
 
print(display)   
