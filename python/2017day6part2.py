# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 00:02:18 2017

@author: James Jiang
"""

def get_highest_index(list):
    x = max(list)
    i = 0
    while True:
        if list[i] == x:
            return i
        i += 1

banks = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]

all_states_dict = {}
all_states_dict[str(banks)] = 1

count = 2
while True:
    index = get_highest_index(banks)
    blocks = banks[index]
    banks[index] = 0
    while blocks > 0:
        blocks -= 1
        if index == len(banks) - 1:
            index = 0
            banks[index] += 1
        else:
            index += 1
            banks[index] += 1
    count += 1
    if str(banks) in all_states_dict:
        print(count - all_states_dict[str(banks)])
        break
    all_states_dict[str(banks)] = count
