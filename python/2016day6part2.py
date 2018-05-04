# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 17:53:51 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

all_strings_chars = []
for line in all_lines:
    all_strings_chars.append([i for i in line])

message = ''
   
for i in range(len(all_strings_chars[0])):
    counts_dict = {}
    for j in range(len(all_strings_chars)):
        if all_strings_chars[j][i] not in counts_dict:
            counts_dict[all_strings_chars[j][i]] = 1
        else:
            counts_dict[all_strings_chars[j][i]] += 1
    letters = list(counts_dict.keys())
    frequencies = list(counts_dict.values())
    letter = letters[frequencies.index(min(frequencies))]
    message += letter
    
print(message)
    
