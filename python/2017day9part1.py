# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 00:03:57 2017

@author: James Jiang
"""

str = ''

with open('Data.txt') as f:
    for line in f:
        str += line
      
characters = [i for i in str]
characters_revised = []

for i in range(len(characters)):
    list = [characters[i]]
    characters_revised.append(list)

for i in range(len(characters_revised)):
    if characters_revised[i] == ['!']:
        characters_revised[i + 1].append('cancelled')
        
for i in range(len(characters_revised)):
    if characters_revised[i] == ['<']:
        start = i
        for j in range(start + 1, len(characters_revised)):
            if characters_revised[j] == ['>']:
                end = j
                break
        for j in range(start + 1, end):
            characters_revised[j].append('garbage')
            
total = 0
current_score = 0

for i in range(len(characters_revised)):
    if characters_revised[i] == ['{']:
        current_score += 1
        total += current_score
    if characters_revised[i] == ['}']:
        current_score -= 1
        
print(total)
        
