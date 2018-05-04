# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 00:45:51 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

all_pairs = [pair.split('-') for pair in all_lines]
all_pairs_int = []
for pair in all_pairs:
    pair_int = [int(i) for i in pair]
    all_pairs_int.append(pair_int)
    
all_pairs_int.sort()

current_max = all_pairs_int[0][1]

for i in range(1, len(all_pairs_int)):
    pair_min = all_pairs_int[i][0]
    pair_max = all_pairs_int[i][1]
    if pair_min > current_max + 1:
        print(current_max + 1)
        break
    else:
        current_max = max(pair_max, current_max)
    
