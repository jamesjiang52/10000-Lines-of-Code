# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:09:49 2017

@author: James Jiang
"""

input = 368078

def move_right(x):
    return ([x[0] + 1, x[1]])

def move_up(x):
    return ([x[0], x[1] + 1])

def move_left(x):
    return ([x[0] - 1, x[1]])

def move_down(x):
    return ([x[0], x[1] - 1])

def move_right_up(x):
    return ([x[0] + 1, x[1] + 1])

def move_right_down(x):
    return ([x[0] + 1, x[1] - 1])

def move_left_up(x):
    return ([x[0] - 1, x[1] + 1])

def move_left_down(x):
    return ([x[0] - 1, x[1] - 1])

moves = [move_right, move_up, move_left, move_down, move_right_up, move_right_down, move_left_up, move_left_down]

def x_coordinate(n):
    if n == 1:
        return 0
    move_current = 0
    times_to_move = 1
    number = 1
    coordinates = [0, 0]
    while True:
        for i in range(2):
            for j in range(times_to_move):
                coordinates = moves[move_current](coordinates)
                number += 1 
                if number == n:
                    return(coordinates[0])
            if move_current == 3:
                move_current = 0
            else:
                move_current += 1
        times_to_move += 1
        
def y_coordinate(n):
    if n == 1:
        return 0
    move_current = 0
    times_to_move = 1
    number = 1
    coordinates = [0, 0]
    while True:
        for i in range(2):
            for j in range(times_to_move):
                coordinates = moves[move_current](coordinates)
                number += 1 
                if number == n:
                    return(coordinates[1])
            if move_current == 3:
                move_current = 0
            else:
                move_current += 1
        times_to_move += 1
        
all_numbers_dict = {}
all_numbers_dict['00'] = 1
all_numbers_dict['10'] = 1
all_numbers_dict['11'] = 2

def key(n):
    key1 = ''
    key1 += str(x_coordinate(n))
    key1 += str(y_coordinate(n))
    return(key1)
    
def key_coordinates(x):
    key1 = ''
    key1 += str(x[0])
    key1 += str(x[1])
    return(key1)
    
number = 4 
while True:
    sum_num = 0
    coordinates = [x_coordinate(number), y_coordinate(number)]
    for i in range(8):
        coordinates_alt = moves[i](coordinates)
        if key_coordinates(coordinates_alt) in all_numbers_dict:
            sum_num += all_numbers_dict[key_coordinates(coordinates_alt)]
    all_numbers_dict[key(number)] = sum_num
    if sum_num > input:
        print(sum_num)
        break
    number += 1
