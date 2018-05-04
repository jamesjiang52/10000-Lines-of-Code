# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 13:36:20 2017

@author: James Jiang
"""

multiply_c = 76
multiply_d = 84

a = 7
b = a

for i in range(1, b):
    a *= i
    
a += multiply_c*multiply_d
print(a)
