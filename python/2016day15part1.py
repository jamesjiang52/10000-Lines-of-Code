# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 00:31:27 2017

@author: James Jiang
"""

discs = [[1, 7, 0], [2, 13, 0], [3, 3, 2], [4, 5, 2], [5, 17, 0], [6, 19, 7]]

counter = 0
while True:
    for disc in discs:
        if (counter + disc[0] + disc[2]) % disc[1] != 0:
            break
    else:
        print(counter)
        break
    counter += 1
