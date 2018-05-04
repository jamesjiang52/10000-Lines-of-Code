# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 18:20:56 2018

@author: James Jiang
"""

input = 29000000
input_modified = int(input/10)

def sum_factors(n):
    output = 0
    if n % 2 == 1:
        step = 2
    else:
        step = 1
    for i in range(1, int(n**0.5) + 1, step):
        if n % i == 0:
            if i**2 == n:
                output += i
            else:
                output += i + n//i
    return(output)

number = 2    
while True:
    if sum_factors(number) >= input_modified:
        print(number)
        break
    number += 1
    