# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 15:31:19 2017

@author: James Jiang
"""

input = 3014603

log_3 = 2

while 3**(log_3 + 1) < input:
    log_3 += 1
    
if input <= 3**log_3 * 2:
    print(input - 3**log_3)
else:
    print(2*input - 3**(log_3 + 1))
