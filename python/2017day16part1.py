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

for move in list_moves:
    chars = [i for i in move]
    if chars[0] == 's':
        num = ''.join(chars[1:])
        position_1 = position[-int(num):]
        position_2 = position[:16 - int(num)]
        position = position_1 + position_2
    elif chars[0] == 'x':
        nums = ''.join(chars[1:])
        nums_list = nums.split('/')
        position[int(nums_list[0])], position[int(nums_list[1])] = position[int(nums_list[1])], position[int(nums_list[0])]
    elif chars[0] == 'p':
        index_1 = position.index(chars[1])
        index_2 = position.index(chars[3])
        position[index_1], position[index_2] = position[index_2], position[index_1]

result = ''.join(position)
print(result)
