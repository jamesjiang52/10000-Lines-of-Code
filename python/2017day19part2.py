# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 13:21:23 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]
all_lines_chars = []

for i in range(len(all_lines)):
    chars = [j for j in all_lines[i]]
    all_lines_chars.append(chars)

index_list = 0
index_all = 0
    
for i in range(len(all_lines_chars[0])):
    if all_lines_chars[0][i] == '|':
        index_list = i
        
mode = 'down'

total = 0

while True:
    if all_lines_chars[index_all][index_list] == ' ':
        break
    if all_lines_chars[index_all][index_list] == '+':
        k = 0
        if (mode == 'down') or (mode == 'up'):
            if index_list != 0:
                if all_lines_chars[index_all][index_list - 1] != ' ':
                    mode = 'left'
                    k += 1
            if index_list != len(all_lines_chars[index_all]) - 1:
                if all_lines_chars[index_all][index_list + 1] != ' ':
                    mode = 'right'
                    k += 1
        elif (mode == 'left') or (mode == 'right'):
            if index_all != 0:
                if all_lines_chars[index_all - 1][index_list] != ' ':
                    mode = 'up'
                    k += 1
            if index_all != len(all_lines_chars) - 1:
                if all_lines_chars[index_all + 1][index_list] != ' ':
                    mode = 'down'
                    k += 1
        if k == 0:
            break
    if mode == 'down':
        index_all += 1
    elif mode == 'up':
        index_all -= 1
    elif mode == 'left':
        index_list -= 1
    elif mode == 'right':
        index_list += 1
    total += 1
        
print(total)   
    
    
