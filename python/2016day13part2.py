# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 18:55:11 2017

@author: James Jiang
"""

input = 1364

def is_open(x, y):
    if (x < 0) or (y < 0):
        return False
    elif sum([int(i) for i in bin(x*x + 3*x + 2*x*y + y + y*y + input)[2:]]) % 2 == 0:
        return True
    else:
        return False

seen = [[1, 1, 0]]

for coordinates in seen:
    if coordinates[2] == 51:
        break
    new_coordinates_x_inc = [coordinates[0] + 1, coordinates[1], coordinates[2] + 1]
    if is_open(new_coordinates_x_inc[0], new_coordinates_x_inc[1]) == True:
        for coordinates_seen in seen:
            if coordinates_seen[:2] == new_coordinates_x_inc[:2]:
                break
        else:
            seen.append(new_coordinates_x_inc)
    new_coordinates_x_dec = [coordinates[0] - 1, coordinates[1], coordinates[2] + 1]
    if is_open(new_coordinates_x_dec[0], new_coordinates_x_dec[1]) == True:
        for coordinates_seen in seen:
            if coordinates_seen[:2] == new_coordinates_x_dec[:2]:
                break
        else:
            seen.append(new_coordinates_x_dec)
    new_coordinates_y_inc = [coordinates[0], coordinates[1] + 1, coordinates[2] + 1]
    if is_open(new_coordinates_y_inc[0], new_coordinates_y_inc[1]) == True:
        for coordinates_seen in seen:
            if coordinates_seen[:2] == new_coordinates_y_inc[:2]:
                break
        else:
            seen.append(new_coordinates_y_inc)
    new_coordinates_y_dec = [coordinates[0], coordinates[1] - 1, coordinates[2] + 1]
    if is_open(new_coordinates_y_dec[0], new_coordinates_y_dec[1]) == True:
        for coordinates_seen in seen:
            if coordinates_seen[:2] == new_coordinates_y_dec[:2]:
                break
        else:
            seen.append(new_coordinates_y_dec)

total = 0
for coordinates in seen:
    if coordinates[2] < 51:
        total += 1
        
print(total)
           
