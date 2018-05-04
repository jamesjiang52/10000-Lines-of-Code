# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:14:40 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]
        
all_lines_characters = []
for line in all_lines:
    characters = line.split()
    all_lines_characters.append(characters)
 
current = all_lines_characters[0][0]
index = 0

while True:
    for i in range(0, len(all_lines_characters)):
        current_other = current + ','
        if (current in all_lines_characters[i]) and (i != index):
            current = all_lines_characters[i][0]
            index = i
            break
        elif (current_other in all_lines_characters[i]) and (i != index):
            current = all_lines_characters[i][0]
            index = i
            break
    else:
        print(current)
        break
