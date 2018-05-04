# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 23:19:46 2017

@author: James Jiang
"""

steps = 12794428
state = 'A'

tape = [0]
cursor = 0

def move_right(position):
    if position == len(tape) - 1:
        tape.append(0)
        return(len(tape) - 1)
    else:
        return(position + 1)
        
def move_left(position):
    if position == 0:
        tape.insert(0, 0)
        return(0)
    else:
        return(position - 1)

for i in range(steps):
    if state == 'A':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor = move_right(cursor)
            state = 'B'
        else:
            tape[cursor] = 0
            cursor = move_left(cursor)
            state = 'F'
    elif state == 'B':
        if tape[cursor] == 0:
            state = 'C'
        else:
            tape[cursor] = 0
            state = 'D'
        cursor = move_right(cursor)
    elif state == 'C':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor = move_left(cursor)
            state = 'D'
        else:
            cursor = move_right(cursor)
            state = 'E'
    elif state == 'D':
        if tape[cursor] == 0:
            state = 'E'
        else:
            tape[cursor] = 0
        cursor = move_left(cursor)
    elif state == 'E':
        if tape[cursor] == 0:
            state = 'A'
        else:
            state = 'C'
        cursor = move_right(cursor)
    elif state == 'F':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor = move_left(cursor)
        else:
            cursor = move_right(cursor)
        state = 'A'
        
print(sum(tape))
