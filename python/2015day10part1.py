# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 14:58:08 2018

@author: James Jiang
"""

input = '1113222113'

def look_and_say(string):
    out_string = ''
    i = 0
    while i in range(len(string)):
        consecutive_equal = 0
        n = i
        while string[n] == string[i]:
            consecutive_equal += 1
            n += 1
            if n not in range(len(string)):
                break
        out_string += str(consecutive_equal)
        out_string += string[i]
        i += consecutive_equal
    return(out_string)

current_num = input
for i in range(40):
    current_num = look_and_say(current_num)
    
print(len(current_num))
