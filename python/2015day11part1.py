# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:07:30 2018

@author: James Jiang
"""

input = 'hepxcrrq'

letters = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
illegals = ['i', 'o', 'l']

def increment(string):
    if string[-1] != 'z':
        chars = [char for char in string]
        chars[-1] = letters[letters.index(chars[-1]) + 1]
        return(''.join(chars))
    else:
        return(increment(string[:-1]) + 'a')
        
def has_three_increasing(string):
    for i in range(len(string) - 2):
        if letters.index(string[i]) < 24:
            if (string[i + 1] == letters[letters.index(string[i]) + 1]) and (string[i + 2] == letters[letters.index(string[i]) + 2]):
                return True
    else:
        return False
    
def has_illegal(string):
    for illegal in illegals:
        if illegal in string:
            return True
    else:
        return False
    
def has_two_pairs(string):
    for i in range(len(string) - 3):
        if string[i] == string[i + 1]:
            for j in range(i + 2, len(string) - 1):
                if (string[j] == string[j + 1]) and (string[i] != string[j]):
                    return True
    else:
        return False
      
current_password = input
while True:
    if (has_illegal(current_password) == False) and (has_three_increasing(current_password) == True) and (has_two_pairs(current_password) == True):
        print(current_password)
        break
    else:
        current_password = increment(current_password)
