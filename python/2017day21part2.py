# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 00:04:08 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

all_pairs = []

for i in all_lines:
    pair = i.split(' => ')
    all_pairs.append(pair)
    
def matrix(string):
    out = []
    for row in string.split('/'):
        chars = [i for i in row]
        out.append(chars)
    return(out)    

enhancements_from = []
enhancements_to = []
for pair in all_pairs:
    enhancements_from.append(matrix(pair[0]))
    enhancements_to.append(matrix(pair[1]))

def transpose(rows):
    new = []
    for row in range(len(rows)):
        row_0 = []
        for col in range(len(rows[0])):
            row_0.append(0)
        new.append(row_0)
    for row in range(len(rows)):
        for col in range(len(rows[0])):
            new[col][row] = rows[row][col]
    return(new)

def flip_vertical(rows):
    new = []
    for row in range(len(rows)):
        row_0 = []
        for col in range(len(rows[0])):
            row_0.append(0)
        new.append(row_0)
    new[0], new[-1] = rows[-1], rows[0]
    if len(rows) == 3:
        new[1] = rows[1]
    return(new)
    
def flip_horizontal(rows):
    return(transpose(flip_vertical(transpose(rows))))
    
def rotate_90(rows):
    return(flip_vertical(transpose(rows)))
    
def rotate_180(rows):
    return(rotate_90(rotate_90(rows)))

def rotate_270(rows):
    return(transpose(flip_vertical(rows)))
    
operations = [flip_vertical, flip_horizontal, rotate_90, rotate_180, rotate_270]
   
def break_2(matrix):
    matrices = []
    for i in range(0, len(matrix), 2):
        for j in range(0, len(matrix), 2):
            matrices.append([matrix[i][j:j + 2], matrix[i + 1][j:j + 2]])
    return(matrices)
    
def break_3(matrix):
    matrices = []
    for i in range(0, len(matrix), 3):
        for j in range(0, len(matrix), 3):
            matrices.append([matrix[i][j:j + 3], matrix[i + 1][j:j + 3], matrix[i + 2][j:j + 3]])
    return(matrices)
    
def sqrt(n):
    for i in range(n + 1):
        if i**2 == n:
            return(i)
    
def make_4(matrices):
    out_matrix = []
    for i in range(0, len(matrices), int(sqrt(len(matrices)))):
        for j in range(4):
            row_j = []
            for k in range(int(sqrt(len(matrices)))):
                row_j.extend(matrices[i + k][j])
            out_matrix.append(row_j)
    return(out_matrix)  
    
def make_3(matrices):
    out_matrix = []
    for i in range(0, len(matrices), int(sqrt(len(matrices)))):
        for j in range(3):
            row_j = []
            for k in range(int(sqrt(len(matrices)))):
                row_j.extend(matrices[i + k][j])
            out_matrix.append(row_j)
    return(out_matrix)

image = matrix('.#./..#/###')

count = 0

while count < 18:
    new_image_components = []
    if len(image) % 2 == 0:
        divisions = break_2(image)
        for division in divisions:
            for i in range(8):
                if operations[i](division) in enhancements_from:
                    new_image_components.append(enhancements_to[enhancements_from.index(operations[i](division))])
                    break
        image = make_3(new_image_components)
    else:
        divisions = break_3(image)
        for division in divisions:
            for i in range(8):
                if operations[i](division) in enhancements_from:
                    new_image_components.append(enhancements_to[enhancements_from.index(operations[i](division))])
                    break
        image = make_4(new_image_components)
    count += 1

total = 0    
for i in range(len(image)):
    for j in range(len(image[0])):
        if image[i][j] == '#':
            total += 1
            
print(total)
