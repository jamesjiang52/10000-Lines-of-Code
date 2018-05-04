# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:35:45 2018

@author: James Jiang
"""

with open('Data.txt') as f:
    for line in f:
        string = line
 
def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def sum_string(input_string):
    sum = 0
    for i in [j for j in ':[]{}']:  
        input_string = input_string.replace(i, ',')
    string_components = input_string.split(',')
    for component in string_components:
        if is_int(component) == True:
            sum += int(component)
    return(sum)
    
def has_red(string_object):
    left_brace_count = 0
    left_square_count = 0
    for i in range(len(string_object) - 2):
        if string_object[i] == '{':
            left_brace_count += 1
        elif string_object[i] == '}':
            left_brace_count -= 1
        elif string_object[i] == '[':
            left_square_count += 1
        elif string_object[i] == ']':
            left_square_count -= 1
        if (string_object[i:i + 3] == 'red') and (left_brace_count == 1) and (left_square_count == 0):
            return True
    else:
        return False

def has_objects(string_object):
    if '{' in string_object[1:]:
        return True
    else:
        return False

def matching_right_brace(index_left, entire_string):
    left_brace_count = 0
    for i in range(index_left, len(entire_string)):
        if entire_string[i] == '{':
            left_brace_count += 1
        elif entire_string[i] == '}':
            left_brace_count -= 1
            if left_brace_count == 0:
                return(i)
        
total = 0
index = 0
while '{' in string:
    if string[index] == '{':
        if has_red(string[index:matching_right_brace(index, string) + 1]) == False:
            if has_objects(string[index:matching_right_brace(index, string) + 1]) == False:
                total += sum_string(string[index:matching_right_brace(index, string) + 1])
                string = string[:index] + string[matching_right_brace(index, string) + 1:]
            else:
                index = string.index('{', index + 1)
        else:
            string = string[:index] + string[matching_right_brace(index, string) + 1:]
    elif index == len(string) - 1:
        index = 0
    else:
        index += 1

total += sum_string(string)
print(total)         

    