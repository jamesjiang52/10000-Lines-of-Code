# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:09:17 2018

@author: James Jiang
"""

row = 3010
column = 3019

def code_number(row_num, column_num):
    return(((row + column)**2 - row - column)//2 - row + 1)
    
limit = code_number(row, column)
code = 20151125

for i in range(1, limit):
    code = (code*252533) % 33554393

print(code)
    