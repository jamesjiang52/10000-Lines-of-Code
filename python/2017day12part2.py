# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 00:26:20 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

all_connections = []

for i in range(len(all_lines)):
    connections_1 = all_lines[i].split(' - ')
    connections_2 = connections_1[1].split(', ')
    connections = connections_1[0:1] + connections_2
    connections = [int(k) for k in connections]
    all_connections.append(connections)

def group(n):
    master = []
    master.extend(all_connections[n])
    memory = []
    while True:
        for i in range(len(all_connections)):
            for j in range(len(all_connections[i])):
                if all_connections[i][j] in master:
                    for k in range(len(all_connections[i])):
                        if all_connections[i][k] not in master:
                            master.append(all_connections[i][k])
        if len(master) not in memory:
            memory.append(len(master))
        else:
            return(master)
            
all_groups = []
all_groups.append(group(0))
            
for i in range(len(all_connections)):
    for j in range(len(all_groups)):
        if all_connections[i][0] in all_groups[j]:
            break
    else:
        all_groups.append(group(all_connections[i][0]))
        
print(len(all_groups))
