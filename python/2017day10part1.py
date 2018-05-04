# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 00:25:29 2017

@author: James Jiang
"""

elements = list(range(256))
lengths = [130, 126, 1, 11, 140, 2, 255, 207, 18, 254, 246, 164, 29, 104, 0, 224]

skip = 0
elements_pointer = 0

for i in range(len(lengths)):
    current_length = lengths[i]
    if elements_pointer + current_length > len(elements):
        sublist1 = elements[elements_pointer:]
        sublist2 = elements[0:current_length - len(sublist1)]
        sublist = sublist1 + sublist2
    else:
        sublist = elements[elements_pointer:elements_pointer + current_length]
    sublist.reverse()
    if elements_pointer + current_length > len(elements):
        elements[elements_pointer:] = sublist[0:len(sublist1)]
        elements[0:current_length - len(sublist1)] = sublist[len(sublist1):]
    else:
        elements[elements_pointer:elements_pointer + current_length] = sublist
    if elements_pointer + (current_length + skip) > len(elements):
        elements_pointer = elements_pointer + current_length + skip - len(elements)
    else:
        elements_pointer += (current_length + skip)
    skip += 1
    
print(elements[0]*elements[1])
