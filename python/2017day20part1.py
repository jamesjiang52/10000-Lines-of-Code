# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 00:01:21 2017

@author: James Jiang
"""

def fix_input(string):
    chars = [i for i in string]
    for i in range(3):
        del chars[0]
    del chars[-1]
    return(''.join(chars))

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

all_lines_properties = []
for line in all_lines:
    properties = line.split(', ')
    all_lines_properties.append(properties)

all_positions = []
all_velocities = []	
all_accelerations = []

for i in range(len(all_lines_properties)):
    values = fix_input(all_lines_properties[i][0]).split(',')
    int_values = [int(k) for k in values]
    absolute_position = abs(int_values[1]) + abs(int_values[1]) + abs(int_values[2])
    all_positions.append([absolute_position])
    values = fix_input(all_lines_properties[i][1]).split(',')
    int_values = [int(k) for k in values]
    absolute_velocity = abs(int_values[0]) + abs(int_values[1]) + abs(int_values[2])
    all_velocities.append([absolute_velocity])
    values = fix_input(all_lines_properties[i][2]).split(',')
    int_values = [int(k) for k in values]
    absolute_acceleration = abs(int_values[0]) + abs(int_values[1]) + abs(int_values[2])
    all_accelerations.append([absolute_acceleration])

min_acceleration = min(all_accelerations)

min_velocity_list = []
min_acceleration_list = []

for i in range(len(all_accelerations)):
    if all_accelerations[i] == min_acceleration:
        min_acceleration_list.append(i)
if len(min_acceleration_list) == 1:
    print(min_acceleration_list[0])
else:
    velocities = []
    for i in min_acceleration_list:
        velocities.append(all_velocities[i])
    min_velocity = min(velocities)
    for i in min_acceleration_list:
        if all_velocities[i] == min_velocity:
            min_velocity_list.append(i)
    if len(min_velocity_list) == 1:
        print(min_velocity_list[0])
    else:
        positions = []
        for i in min_velocity_list:
            positions.append(all_positions[i])
        min_position = min(positions)
        for i in min_velocity_list:
            if all_positions[i] == min_position:
                print(min_velocity_list[0])
    
