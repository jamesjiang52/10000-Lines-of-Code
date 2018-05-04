# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 15:32:46 2017

@author: James Jiang
"""

all_lines = [line.rstrip(']\n') for line in open('Data.txt')]

letters = [i for i in 'abcdefghijklmnopqrstuvwxyz']

def real(string):
    string_list = string.split('-')
    sector_id_checksum = string_list[-1].split('[')
    checksum_list = [i for i in sector_id_checksum[1]]
    checksum_list.sort()
    del string_list[-1]
    
    all_chars = []
    all_chars_dict = {}
    for name in string_list:
        chars = [i for i in name]
        all_chars.extend(chars)
    for char in all_chars:
        if char in all_chars_dict:
            all_chars_dict[char] += 1
        else:
            all_chars_dict[char] = 1
    max_list = []
    letters_index = 0
    while len(max_list) < 5:
        if letters[letters_index] in all_chars_dict:
            max_list.append(letters[letters_index])
        letters_index += 1
    for i in letters:
        if (i in all_chars_dict) and (i not in max_list):
            if all_chars_dict[i] > min([all_chars_dict[j] for j in max_list]):
                checker = []
                for j in max_list:
                    if all_chars_dict[j] == min([all_chars_dict[j] for j in max_list]):
                        checker.append(j)
                if len(checker) > 1:
                    checker.sort(reverse=True)
                    index = max_list.index(checker[0])
                else:
                    index = max_list.index(checker[0])
                max_list[index] = i
    max_list.sort()
    if max_list == checksum_list:
        return([int(sector_id_checksum[0]), string_list])
    else:
        return('NotReal')

def shift(letter, number):
    index = letters.index(letter)
    shifted_index = (number + index) % 26
    return(letters[shifted_index])

real_rooms = []
total = 0    

for room in all_lines:
    if real(room) != 'NotReal':
        real_rooms.append(real(room))

for room in real_rooms:
    phrase = ''
    for string in room[1]:
        word_string = ''
        chars = [i for i in string]
        for char in chars:
            word_string += shift(char, room[0])
        phrase += word_string
        phrase += ' '
    if phrase == 'northpole object storage ':
        print(room[0])
        break
