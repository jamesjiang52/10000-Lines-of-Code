# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 00:03:00 2017

@author: James Jiang
"""

step = 335
circle = [0]
i = 0

for n in range(1, 50000001):
    i = (i + step) % len(circle)
    if circle[i] == 0:
        value = n
    circle.append(n)
    i = (i + 1) % len(circle)

print(value)
