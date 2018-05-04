# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 12:31:27 2017

@author: James Jiang
"""

with open('Data.txt') as f:
    for line in f:
        number = line
        
digits = [i for i in str(number)]
step = int(len(digits)/2)

for i in range(int(len(digits)/2)):
    digits.append(digits[i])

sum = 0
for i in range(int(len(digits)*2/3)):
    if digits[i] == digits[i + step]:
        sum += int(digits[i])
        
print(sum)
