# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:35:45 2018

@author: James Jiang
"""

with open('Data.txt') as f:
    for line in f:
        string = line
 
def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def sum_string(input_string):
    sum = 0
    for i in [j for j in ':[]{}']:  
        input_string = input_string.replace(i, ',')
    string_components = input_string.split(',')
    for component in string_components:
        if is_int(component) == True:
            sum += int(component)
    return(sum)

print(sum_string(string))