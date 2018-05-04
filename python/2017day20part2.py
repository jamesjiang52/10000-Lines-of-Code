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
    all_positions.append(int_values)
    values = fix_input(all_lines_properties[i][1]).split(',')
    int_values = [int(k) for k in values]
    all_velocities.append(int_values)
    values = fix_input(all_lines_properties[i][2]).split(',')
    int_values = [int(k) for k in values]
    all_accelerations.append(int_values)
    
def next_frame():
    for i in range(len(all_lines_properties)):
        if 'removed' not in all_positions[i]:
            for j in range(3):
                all_velocities[i][j] += all_accelerations[i][j]
                all_positions[i][j] += all_velocities[i][j]

memory_counts = [0]
timeout = 0

while True:
    count = 0
    for i in range(len(all_lines_properties) - 1):
        if 'removed' not in all_positions[i]:
            copy = all_positions[i][:]
            stop = 0
            for j in range(i + 1, len(all_lines_properties)):
                if all_positions[j] == copy:
                    all_positions[j].append('removed')
                    all_positions[i].append('removed')
    for i in range(len(all_lines_properties)):
        if 'removed' in all_positions[i]:
            count += 1
    if count not in memory_counts:
        memory_counts.append(count)
    else:
        timeout += 1
    if timeout > 1000:
        break
    next_frame()
    
print(len(all_lines_properties) - memory_counts[-1])  
