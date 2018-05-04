# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 20:48:38 2018

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]
all_containers = [int(i) for i in all_lines]
all_containers.sort(reverse=True)

total_number = 2**(len(all_containers))

count = 0
min_nums = []

i = 0
while i < total_number:
    number_bin = bin(i)[2:].zfill(len(all_containers))
    sum_containers = 0
    for j in range(len(all_containers)):
        if number_bin[j] == '1':
            sum_containers += all_containers[j]
            if sum_containers > 150:
                break
    if sum_containers == 150:
        count += 1
        i += 2**number_bin[::-1].index('1')
    else:
        i += 1
        
print(count)
