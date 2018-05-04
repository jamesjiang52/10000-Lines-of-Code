# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:06:08 2017

@author: James Jiang
"""

def position(range_firewall, time):
    offset = time % (2 * (range_firewall - 1))
    if offset > range_firewall - 1:
        return(2 * (range_firewall - 1) - offset)  
    else:
        return(offset)

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

ranges = {}

for i in all_lines:
    pair = i.split(': ')
    ranges[int(pair[0])] = int(pair[1])

severity = 0

for i in ranges:
    if position(ranges[i], i) == 0:
        severity += ranges[i] * i
        
print(severity)
