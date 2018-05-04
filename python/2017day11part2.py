# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 00:14:19 2017

@author: James Jiang
"""

def distance(x, y):
    if (x >= 0) and (y >= 0):
        return(x + y)
    if (x <= 0) and (y >= 0):
        return(max(-x, y))
    if (x >= 0) and (y <= 0):
        return(max(x, -y))
    if (x <= 0) and (y <= 0):
        return(-(x + y))
    
str = ''

with open('Data.txt') as f:
    for line in f:
        str += line
        
list = str.split(',')

all_distances = []

x_coordinate = 0
y_coordinate = 0

for i in range(len(list)):
    if list[i] == 'nw':
        y_coordinate -= 1
    if list[i] == 'n':
        x_coordinate += 1
        y_coordinate -= 1
    if list[i] == 'ne':
        x_coordinate += 1
    if list[i] == 'se':
        y_coordinate += 1
    if list[i] == 's':
        x_coordinate -= 1
        y_coordinate += 1
    if list[i] == 'sw':
        x_coordinate -= 1
    all_distances.append(distance(x_coordinate, y_coordinate))
    
print(max(all_distances))

