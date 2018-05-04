# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 21:15:20 2017

@author: James Jiang
"""
        
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True

initial_b = 108400
initial_c = initial_b + 17000
step = 17

h = 0

for i in range(initial_b, initial_c + 1, step):
    if is_prime(i) == False:
        h += 1
        
print(h)        
