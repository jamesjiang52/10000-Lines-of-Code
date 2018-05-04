# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 20:03:01 2018

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

children = {}
cats = {}
samoyeds = {}
pomeranians = {}
akitas = {}
vizslas = {}
goldfish = {}
trees = {}
cars = {}
perfumes = {}

dicts = [children, cats, samoyeds, pomeranians, akitas, vizslas, goldfish, trees, cars, perfumes]
values = [3, 7, 2, 3, 0, 0, 5, 3, 2, 1]

all_sues = []

for data in all_lines:
    data = data.replace(': ', ', ')
    possessions = data.split(', ')
    sue_number = possessions[0].split(' ')
    key = int(sue_number[1])
    all_sues.append(key)
    if 'children' in possessions:
        children[key] = int(possessions[possessions.index('children') + 1])
    if 'cats' in possessions:
        cats[key] = int(possessions[possessions.index('cats') + 1])
    if 'samoyeds' in possessions:
        samoyeds[key] = int(possessions[possessions.index('samoyeds') + 1])
    if 'pomeranians' in possessions:
        pomeranians[key] = int(possessions[possessions.index('pomeranians') + 1])
    if 'akitas' in possessions:
        akitas[key] = int(possessions[possessions.index('akitas') + 1])
    if 'vizslas' in possessions:
        vizslas[key] = int(possessions[possessions.index('vizslas') + 1])
    if 'goldfish' in possessions:
        goldfish[key] = int(possessions[possessions.index('goldfish') + 1])
    if 'trees' in possessions:
        trees[key] = int(possessions[possessions.index('trees') + 1])
    if 'cars' in possessions:
        cars[key] = int(possessions[possessions.index('cars') + 1])
    if 'perfumes' in possessions:
        perfumes[key] = int(possessions[possessions.index('perfumes') + 1])
            
possible_sues = all_sues[:]

for sue in all_sues:
    for i in range(len(dicts)):
        if sue in dicts[i]:
            if dicts[i][sue] != values[i]:
                possible_sues.remove(sue)
                break
            
print(possible_sues[0])
