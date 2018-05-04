# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 00:02:52 2017

@author: James Jiang
"""

string = ''

with open('Data.txt') as f:
    for line in f:
        string += line
        
list_moves = string.split(',')

position = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
memory = []

for i in range(10**9):
    position_string = ''.join(position)
    if position_string in memory:
        result = ''.join(memory[10**9 % len(memory)])
        print(result)
        break
    memory.append(position_string)
    for move in list_moves:
        if move[0] == 's':
            num = ''.join(move[1:])
            position_1 = position[-int(num):]
            position_2 = position[:16 - int(num)]
            position = position_1 + position_2
        elif move[0] == 'x':
            nums = ''.join(move[1:])
            nums_list = nums.split('/')
            position[int(nums_list[0])], position[int(nums_list[1])] = position[int(nums_list[1])], position[int(nums_list[0])]
        elif move[0] == 'p':
            index_1 = position.index(move[1])
            index_2 = position.index(move[3])
            position[index_1], position[index_2] = position[index_2], position[index_1]
