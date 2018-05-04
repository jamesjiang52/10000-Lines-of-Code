# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 21:00:24 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

def has_abba(string):
    chars = [i for i in string]
    for i in range(1, len(chars) - 2):
        if chars[i] == chars[i + 1]:
            if (chars[i - 1] == chars[i + 2]) and (chars[i - 1] != chars[i]):
                return True
    else:
        return False
    
def process_input(string):
    chars = [i for i in string]
    outside = []
    inside = []
    string_outside = ''
    string_inside = ''
    toggle = 0
    for i in range(len(chars)):
        char = chars[i]
        if (char != '[') and (char != ']'):
            if toggle == 0:
                string_outside += char
            elif toggle == 1:
                string_inside += char
            if i == len(chars) - 1:
                outside.append(string_outside)
        elif char == '[':
            toggle = 1
            outside.append(string_outside)
            string_outside = ''
        elif char == ']':
            toggle = 0
            inside.append(string_inside)
            string_inside = ''
    return([outside, inside])
 
count = 0

for ip in all_lines:
    ip_outside = process_input(ip)[0]
    ip_inside = process_input(ip)[1]
    for string in ip_inside:
        if has_abba(string) == True:
            break
    else:
        for string in ip_outside:
            if has_abba(string) == True:
                count += 1
                break
           
print(count)
    
