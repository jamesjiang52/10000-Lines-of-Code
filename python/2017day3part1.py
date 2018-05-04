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

moves = [move_right, move_up, move_left, move_down]

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
        
print(abs(x_coordinate(input)) + abs(y_coordinate(input)))
