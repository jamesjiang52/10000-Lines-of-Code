# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 10:27:50 2018

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

def has_two_pairs(string):
    for i in range(len(string) - 1):
        pair = string[i:i + 2]
        if (pair in string[:i]) or (pair in string[i + 2:]):
            return True
    else:
        return False
    
def has_repeat_with_space(string):
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True
    else:
        return False

def is_nice(string):
    if (has_two_pairs(string) == True) and( has_repeat_with_space(string) == True):
        return True
    else:
        return False

count = 0       
for string in all_lines:
    if is_nice(string) == True:
        count += 1
        
print(count)
