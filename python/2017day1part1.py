# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 12:31:27 2017

@author: James Jiang
"""

with open('Data.txt') as f:
    for line in f:
        number = line
        
digits = [i for i in str(number)]
digits.append(digits[0])

sum = 0
for i in range(len(digits) - 1):
    if digits[i] == digits[i + 1]:
        sum += int(digits[i])
        
print(sum)
