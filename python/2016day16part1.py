# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 11:24:33 2017

@author: James Jiang
"""

input = '01110110101001000'
max_length = 272

def bit_not(bits):
    new_bits = ''
    for bit in bits:
        if bit == '0':
            new_bits += '1'
        else:
            new_bits += '0'
    return(new_bits)

while len(input) < max_length:
    input_reversed = input[::-1]
    input_reversed_complement = bit_not(input_reversed)
    input += '0' + input_reversed_complement
    
disc = input[:max_length]
checksum = disc

while len(checksum) % 2 == 0:
    new_checksum = ''
    for i in range(0, len(checksum), 2):
        if checksum[i] == checksum[i + 1]:
            new_checksum += '1'
        else:
            new_checksum += '0'
    checksum = new_checksum
    
print(checksum)
