# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 16:03:43 2018

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]
del all_lines[-2]

original_molecule = all_lines[-1]
del all_lines[-1]

all_data = [line.split(' => ') for line in all_lines]
all_originals = [data[0] for data in all_data]
all_replacements = [data[1] for data in all_data]

all_molecules = []

for i in range(len(all_data)):
    original = all_originals[i]
    replacement = all_replacements[i]
    index = 0
    while index < len(original_molecule):
        if original == original_molecule[index:index + len(original)]:
            new_molecule = original_molecule[:index] + replacement + original_molecule[index + len(original):]
            if new_molecule not in all_molecules:
                all_molecules.append(new_molecule)
        index += 1

print(len(all_molecules))
