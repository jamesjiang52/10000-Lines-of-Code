# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 12:16:02 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

all_nodes = []
for line in all_lines:
    components = line.split(' ')
    while '' in components:
        components.remove('')
    all_nodes.append(components)
    
all_nodes = all_nodes[2:]

for i in range(len(all_nodes)):
    node_location_components = all_nodes[i][0].split('-')
    all_nodes[i][0] = [int(node_location_components[1][1:]), int(node_location_components[2][1:])]
    del all_nodes[i][-2:]
    for j in range(1, 3):
        all_nodes[i][j] = int(all_nodes[i][j][:-1])
                
grid = []
for i in range(all_nodes[-1][0][1] + 1):
    row = [0 for j in range(all_nodes[-1][0][0] + 1)]
    grid.append(row)

min_capacity = min([all_nodes[i][1] for i in range(len(all_nodes))])

for node in all_nodes:
    if (node[0][0] == all_nodes[-1][0][0]) and (node[0][1] == 0):
        grid[node[0][1]][node[0][0]] = 'G'
    elif node[2] == 0:
        grid[node[0][1]][node[0][0]] = '_'
    elif node[2] > min_capacity:
        grid[node[0][1]][node[0][0]] = '#'
    else:
        grid[node[0][1]][node[0][0]] = '.'
 
total = 0
       
for node in all_nodes:
    if node[2] == 0:
        position_empty = [node[0][0], node[0][1]]
        break

def column_has_full(column):
    for i in range(len(grid)):
        if grid[i][column] == '#':
            return True
    else:
        return False
    
while column_has_full(position_empty[0]) == True:
    total += 1
    position_empty[0] -= 1

total += all_nodes[-1][0][0] - position_empty[0]
total += position_empty[1]

for i in range(all_nodes[-1][0][0] - 1):
    total += 5
    
print(total)
