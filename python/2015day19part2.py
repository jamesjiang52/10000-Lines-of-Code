# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 16:03:43 2018

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]
del all_lines[-2]

original_molecule = all_lines[-1]

capital_letters = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
count_elements = 0
for letter in original_molecule:
    if letter in capital_letters:
        count_elements += 1

count_Rn = original_molecule.count('Rn')
count_Ar = original_molecule.count('Ar')
count_Y = original_molecule.count('Y')

print(count_elements - (count_Rn + count_Ar) - 2*count_Y - 1)
