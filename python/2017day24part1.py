# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 23:41:27 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

pairs = [line.split('/') for line in all_lines]
pairs_int = []
for i in range(len(pairs)):
    pairs_int.append([int(pairs[i][0]), int(pairs[i][1])])

def next_port(list1, list2):
    if (list2[0] == list1[0]) or (list2[0] == list1[1]):
        return list2[1]
    elif (list2[1] == list1[0]) or (list2[1] == list1[1]):
        return list2[0]
    
def strength(pairs_list):
    total = 0
    for pair in pairs_list:
        total += pair[0]
        total += pair[1]
    return(total)
    
strongest_bridge = []
strongest_bridge_strength = 0

def build(pairs_list_all, pairs_list):
    global strongest_bridge, strongest_bridge_strength
    
    if len(pairs_list) >= 2:
        port = next_port(pairs_list[-2], pairs_list[-1])
    elif len(pairs_list) == 1:
        port = next_port([0, 0], pairs_list[-1])
    else:
        port = 0
    for pair in pairs_list_all:
        if port in pair:
            next_pairs_list = pairs_list[:]
            next_pairs_list.append(pair)
            next_pairs_list_all = pairs_list_all[:]
            next_pairs_list_all.remove(pair)
            build(next_pairs_list_all, next_pairs_list)
    else:
        if strength(pairs_list) > strongest_bridge_strength:
            strongest_bridge = pairs_list
            strongest_bridge_strength = strength(pairs_list)
        
build(pairs_int, [])
print(strongest_bridge_strength)
