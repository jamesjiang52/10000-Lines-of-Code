# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 07:32:06 2018

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]
all_triples = [line.split('x') for line in all_lines]
all_triples_int = []
for triple in all_triples:
    all_triples_int.append([int(num) for num in triple])

total = 0    
for triple in all_triples_int:
    total += 2*(triple[0]*triple[1] + triple[0]*triple[2] + triple[1]*triple[2]) + min(triple[0]*triple[1], triple[0]*triple[2], triple[1]*triple[2])
    
print(total)
