# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 00:00:43 2018

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]
all_weights = [int(i) for i in all_lines]
all_weights.sort()

target_weight = sum(all_weights)//3

min_num_packages = len(all_weights)
min_qe = 1
for weight in all_weights:
    min_qe *= weight

i = 0

while i < 2**len(all_weights):
    number_bin = bin(i)[2:].zfill(28)
    if number_bin.count('1') <= min_num_packages:
        sum_weights = 0
        product = 1
        for j in range(len(all_weights)):
            if number_bin[j] == '1':
                sum_weights += all_weights[j]
                if sum_weights > target_weight:
                    break
                product *= all_weights[j]
        if sum_weights == target_weight:
            if product < min_qe:
                min_qe = product
            min_num_packages = number_bin.count('1')
            i += 2**number_bin[::-1].index('1')
        else:
            i += 1
    else:
        i += 1
 
print(min_qe)
