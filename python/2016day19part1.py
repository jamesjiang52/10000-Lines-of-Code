# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 15:31:19 2017

@author: James Jiang
"""

input = 3014603

circle = list(range(1, input + 1))

while len(circle) > 1:
    if len(circle) % 2 == 0:
        new_circle = [circle[2*i] for i in range(int(len(circle)/2))]
    else:
        new_circle = [circle[2*i] for i in range(int((len(circle) - 1)/2))]
        new_circle.insert(0, circle[-1])
    circle = new_circle
    
print(circle[0])
