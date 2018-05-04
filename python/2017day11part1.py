# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 00:14:19 2017

@author: James Jiang
"""

str = ''

with open('Data.txt') as f:
    for line in f:
        str += line
        
list = str.split(',')

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
        
if (x_coordinate >= 0) and (y_coordinate >= 0):
    print(x_coordinate + y_coordinate)
if (x_coordinate <= 0) and (y_coordinate >= 0):
    print(max(-x_coordinate, y_coordinate))
if (x_coordinate >= 0) and (y_coordinate <= 0):
    print(max(x_coordinate, -y_coordinate))
if (x_coordinate <= 0) and (y_coordinate <= 0):
    print(-(x_coordinate + y_coordinate))
