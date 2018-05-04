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

total = 0
    
for i in range(len(all_nodes)):
    node_i = all_nodes[i]
    for j in range(len(all_nodes)):
        node_j = all_nodes[j]
        if i != j:
            if (int(node_i[2][:-1]) != 0) and (int(node_i[2][:-1]) < int(node_j[3][:-1])):
                total += 1
                
print(total)
