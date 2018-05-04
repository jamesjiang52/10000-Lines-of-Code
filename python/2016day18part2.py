# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:47:37 2017

@author: James Jiang
"""

string = ''
with open('Data.txt') as f:
    for line in f:
        string = line

def is_safe(index, row):
    row = '.' + row + '.'
    index = index + 1
    if row[index - 1] == row[index + 1]:
        return True
    else:
        return False

string_list = [i for i in string]       
total = string_list.count('.')

for i in range(399999):
    new_row = ''
    for j in range(len(string)):
        if is_safe(j, string) == True:
            new_row += '.'
            total += 1
        else:
            new_row += '^'
    string = new_row

print(total)
