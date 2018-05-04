# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 18:11:54 2017

@author: James Jiang
"""

initial_a = 1
initial_b = 1
initial_d = 26
multiply_c = 18
multiply_d = 11
  
a = initial_a
b = initial_b
c = a
d = initial_d

for i in range(d):
    b, a = a, a + b
    
a += 18*11
    
print(a)
  
