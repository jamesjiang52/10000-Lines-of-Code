# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 21:10:45 2017

@author: James Jiang
"""

from hashlib import md5

input = 'jlmsuwbz'

all_chars = [i for i in '1234567890abcdef']

memory = {}

def md5_hash_2017(string):
    for i in range(2017):
        string = md5(string.encode('utf-8')).hexdigest()
    return(string)

def has_triple(string):
    for i in range(len(string) - 2):
        if (string[i] == string[i + 1]) and (string[i] == string[i + 2]):
            return(string[i])
    else:
        return(False)
        
def is_key(index, char):
    for i in range(index + 1, index + 1001):
        if i in memory:
            md5_hash = memory[i]
        else:
            md5_hash = md5_hash_2017(input + str(i))
            memory[i] = md5_hash
        if 5*char in md5_hash:
            return True
    else:
        return False

index = 0
counter = 0

while counter < 64:
    if index in memory:
        md5_hash = memory[index]
    else:
        md5_hash = md5_hash_2017(input + str(index))
        memory[index] = md5_hash
    if has_triple(md5_hash) != False:
        if is_key(index, has_triple(md5_hash)) == True:
            counter += 1
    if counter == 64:
        print(index)
        break
    else:
        index += 1
