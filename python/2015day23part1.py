# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 23:38:33 2018

@author: James Jiang
"""

initial_a = 0
a = initial_a

a += 1
a *= 3
a += 1
a *= 3
a += 1
a *= 9
a += 2
a *= 9
a += 2
a *= 3
a += 2
a *= 3

b = 0       
while a != 1:
    b += 1
    if a % 2 == 0:
        a //= 2
    else:
        a = 3*a + 1
    
print(b)
    