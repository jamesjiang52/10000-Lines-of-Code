# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 10:27:50 2018

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

vowels = [char for char in 'aeiou']
illegals = ['ab', 'cd', 'pq', 'xy']

def is_nice(string):
    for illegal in illegals:
        if illegal in string:
            return False
    else:
        vowel_count = 0
        double_count = 0
        for i in range(len(string) - 1):
            if string[i] in vowels:
                vowel_count += 1
            if string[i] == string[i + 1]:
                double_count += 1
        if string[-1] in vowels:
            vowel_count += 1
        if vowel_count < 3:
            return False
        elif double_count == 0:
            return False
        else:
            return True

count = 0       
for string in all_lines:
    if is_nice(string) == True:
        count += 1
        
print(count)
