# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 00:03:00 2017

@author: James Jiang
"""

step = 335
circle = [0]
i = 0

for n in range(1, 2018):
    i = (i + step) % len(circle)
    dummy = i
    circle.insert(i + 1, n)
    i = (i + 1) % len(circle)
    
print(circle[dummy + 2])
