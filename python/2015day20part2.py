# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 18:20:56 2018

@author: James Jiang
"""

input = 29000000
input_modified = int(input/11)

def sum_factors(n):
    output = 0
    for i in range(1, 51):
        if n % i == 0:
            output += n//i
    return(output)

number = 2    
while True:
    if sum_factors(number) >= input_modified:
        print(number)
        break
    number += 1
    