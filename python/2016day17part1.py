# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 11:45:42 2017

@author: James Jiang
"""

from hashlib import md5

input = 'qljzarfv'

open_letters = [i for i in 'bcedf']

def open_doors(string):
    out_list = []
    md5_hash = md5(string.encode('utf-8')).hexdigest()
    if md5_hash[0] in open_letters:
        out_list.append('up')
    if md5_hash[1] in open_letters:
        out_list.append('down')
    if md5_hash[2] in open_letters:
        out_list.append('left')
    if md5_hash[3] in open_letters:
        out_list.append('right')
    return(out_list)

moves = ''
seen = [[1, 1, '']]
    
for coordinates in seen:
    doors = open_doors(input + coordinates[2])
    if 'up' in doors and coordinates[1] > 1:
        new_coordinates = [coordinates[0], coordinates[1] - 1, coordinates[2] + 'U']
        seen.append(new_coordinates)
        if new_coordinates[:2] == [4, 4]:
            print(new_coordinates[2])
            break
    if 'down' in doors and coordinates[1] < 4:
        new_coordinates = [coordinates[0], coordinates[1] + 1, coordinates[2] + 'D']
        seen.append(new_coordinates)
        if new_coordinates[:2] == [4, 4]:
            print(new_coordinates[2])
            break
    if 'left' in doors and coordinates[0] > 1:
        new_coordinates = [coordinates[0] - 1, coordinates[1], coordinates[2] + 'L']
        seen.append(new_coordinates)
        if new_coordinates[:2] == [4, 4]:
            print(new_coordinates[2])
            break
    if 'right' in doors and coordinates[0] < 4:
        new_coordinates = [coordinates[0] + 1, coordinates[1], coordinates[2] + 'R']
        seen.append(new_coordinates)
        if new_coordinates[:2] == [4, 4]:
            print(new_coordinates[2])
            break

