# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 01:01:22 2018

@author: James Jiang
"""

multiply_b = 633
multiply_c = 4

counter = 1

while True:
    clock_list = []
    a = counter + multiply_b*multiply_c
    while a != 0:
        b = a % 2
        a = a // 2
        clock_list.append(b)
    if [int(i) for i in '010101010101'] == clock_list[:12]:
        print(counter)
        break
    counter += 1
    
