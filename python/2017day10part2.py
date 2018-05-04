# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 00:25:29 2017

@author: James Jiang
"""

elements = list(range(256))
lengths_not_ascii = [130, ',', 126, ',', 1, ',', 11, ',', 140, ',', 2, ',', 255, ',', 207, ',', 18, ',', 254, ',', 246, ',', 164, ',', 29, ',', 104, ',', 0, ',', 224]
lengths = []

for i in range(len(lengths_not_ascii)):
    digits = [j for j in str(lengths_not_ascii[i])]
    for k in range(len(digits)):
        lengths.append(ord(digits[k]))

lengths.extend([17, 31, 73, 47, 23])

skip = 0
elements_pointer = 0

for count in range(64):
    for i in range(len(lengths)):
        current_length = lengths[i]
        if elements_pointer + current_length >= len(elements):
            sublist1 = elements[elements_pointer:]
            sublist2 = elements[0:current_length - len(sublist1)]
            sublist = sublist1 + sublist2
        else:
            sublist = elements[elements_pointer:elements_pointer + current_length]
        sublist.reverse()
        if elements_pointer + current_length >= len(elements):
            elements[elements_pointer:] = sublist[0:len(sublist1)]
            elements[0:current_length - len(sublist1)] = sublist[len(sublist1):]
        else:
            elements[elements_pointer:elements_pointer + current_length] = sublist
        if elements_pointer + (current_length + skip) >= len(elements):
            elements_pointer = elements_pointer + current_length + skip - len(elements) 
            while True:
                if elements_pointer in range(len(elements)):
                    break
                else:
                    elements_pointer -= len(elements)
        else:
            elements_pointer += (current_length + skip)
        skip += 1

dense_hash_list = []

for i in range(0, len(elements), 16):
    hash = elements[i] ^ elements[i + 1] ^ elements[i + 2] ^ elements[i + 3] ^ elements[i + 4] ^ elements[i + 5] ^ elements[i + 6] ^ elements[i + 7] ^ elements[i + 8] ^ elements[i + 9] ^ elements[i + 10] ^ elements[i + 11] ^ elements[i + 12] ^ elements[i + 13] ^ elements[i + 14] ^ elements[i + 15]
    dense_hash_list.append(hash)

knot_hash = ''

for i in range(0, len(dense_hash_list)):
    string = hex(dense_hash_list[i])[2:]
    if len(string) == 1:
        string = '0' + string
    knot_hash += string
    
print(knot_hash)
    
