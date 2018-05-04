# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:56:06 2018

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]
all_data = [line.split(' ') for line in all_lines]

dict_data = {}

for data in all_data:
    dict_data[data[0]] = [int(data[3]), int(data[6]), int(data[-2])]
    
def distance_travelled(time, input_list):
    increments = time//(input_list[1] + input_list[2])
    distance = increments*(input_list[0]*input_list[1])
    remainder = time % (input_list[1] + input_list[2])
    if remainder <= input_list[1]:
        distance += remainder*input_list[0]
    else:
        distance += input_list[0]*input_list[1]
    return(distance)

print(max([distance_travelled(2503, dict_data[i]) for i in dict_data]))
