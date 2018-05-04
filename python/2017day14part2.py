# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 00:25:29 2017

@author: James Jiang
"""

input = 'ugkiagan'

def knot_hash(n):
    elements = list(range(256))

    string = input

    lengths = [ord(i) for i in string]

    lengths.append(ord('-'))
    
    n_digits = [i for i in str(n)]
    for i in range(len(n_digits)):
        lengths.append(ord(n_digits[i]))

    lengths += [17, 31, 73, 47, 23]

    skip = 0
    elements_pointer = 0

    for count in range(64):
        for i in range(len(lengths)):
            current_length = lengths[i]
            if elements_pointer + current_length >= len(elements):
                sublist1 = elements[elements_pointer:]
                sublist2 = elements[0:current_length - len(sublist1)]
                sublist = sublist1 + sublist2
            else:
                sublist = elements[elements_pointer:elements_pointer + current_length]
            sublist.reverse()
            if elements_pointer + current_length >= len(elements):
                elements[elements_pointer:] = sublist[0:len(sublist1)]
                elements[0:current_length - len(sublist1)] = sublist[len(sublist1):]
            else:
                elements[elements_pointer:elements_pointer + current_length] = sublist
            if elements_pointer + (current_length + skip) >= len(elements):
                elements_pointer = elements_pointer + current_length + skip - len(elements) 
                while True:
                    if elements_pointer in range(len(elements)):
                        break
                    else:
                        elements_pointer -= len(elements)
            else:
                elements_pointer += (current_length + skip)
            skip += 1

    dense_hash_list = []

    for i in range(0, len(elements), 16):
        hash = elements[i] ^ elements[i + 1] ^ elements[i + 2] ^ elements[i + 3] ^ elements[i + 4] ^ elements[i + 5] ^ elements[i + 6] ^ elements[i + 7] ^ elements[i + 8] ^ elements[i + 9] ^ elements[i + 10] ^ elements[i + 11] ^ elements[i + 12] ^ elements[i + 13] ^ elements[i + 14] ^ elements[i + 15]
        dense_hash_list.append(hash)

    knot_hash_output = ''

    for i in range(0, len(dense_hash_list)):
        string = bin(dense_hash_list[i])[2:]
        while len(string) < 8:
            string = '0' + string
        knot_hash_output += string 
        
    return(knot_hash_output)

all_hashes = []
  
for i in range(128):
    bits = [k for k in knot_hash(i)]
    all_hashes.append(bits)

numbered = []
for i in range(128):
    nums = []
    for j in range(128):
        nums.append(128 * i + j)
    numbered.append(nums)
    
def connections(i, j):
    if all_hashes[i][j] == '1':
        connections_output = [numbered[i][j]]
        if i > 0:
            if all_hashes[i - 1][j] == '1':
                connections_output.append(numbered[i - 1][j])
        if j > 0:
            if all_hashes[i][j - 1] == '1':
                connections_output.append(numbered[i][j - 1])
        if i < 127:
            if all_hashes[i + 1][j] == '1':
                connections_output.append(numbered[i + 1][j])
        if j < 127:
            if all_hashes[i][j + 1] == '1':
                connections_output.append(numbered[i][j + 1])
        return(connections_output)
    else:
        return([9999])
    
all_connections = []
for i in range(128):
    for j in range(128):
        if connections(i, j) != [9999]:
            all_connections.append(connections(i, j))

def group(n):
    master = []
    master.extend(all_connections[n])
    memory = []
    while True:
        for i in range(len(all_connections)):
            for j in range(len(all_connections[i])):
                if all_connections[i][j] in master:
                    for k in range(len(all_connections[i])):
                        if all_connections[i][k] not in master:
                            master.append(all_connections[i][k])
        if len(master) not in memory:
            memory.append(len(master))
        else:
            return(master)
           
all_groups = []
all_groups.append(group(0))
            
for i in range(len(all_connections)):
    for j in range(len(all_groups)):
        if all_connections[i][0] in all_groups[j]:
            break
    else:
        all_groups.append(group(i))

print(len(all_groups))                   

    
