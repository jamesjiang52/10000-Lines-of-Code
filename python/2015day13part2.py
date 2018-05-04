# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 14:06:52 2018

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]
all_data = [line.split(' ') for line in all_lines]

all_people = []
for data in all_data:
    if data[0] not in all_people:
        all_people.append(data[0])

happiness_change = {}
happiness_change_net = {}

for data in all_data:
    if data[2] == 'gain':
        happiness_change[(data[0], data[10][:-1])] = int(data[3])
    else:
        happiness_change[(data[0], data[10][:-1])] = -int(data[3])

for i in range(len(all_people) - 1):
    for j in range(i + 1, len(all_people)):
        happiness_change_net[(all_people[i], all_people[j])] = happiness_change[(all_people[i], all_people[j])] + happiness_change[(all_people[j], all_people[i])]

for person in all_people:
    happiness_change_net[('Myself', person)] = 0
all_people.append('Myself')
      
def happiness(list_order):
    total = 0
    for i in range(len(list_order) - 1):
        if (list_order[i], list_order[i + 1]) in happiness_change_net:
            total += happiness_change_net[(list_order[i], list_order[i + 1])]
        else:
            total += happiness_change_net[(list_order[i + 1], list_order[i])]
    if (list_order[0], list_order[-1]) in happiness_change_net:
        total += happiness_change_net[(list_order[0], list_order[-1])]
    else:
        total += happiness_change_net[(list_order[-1], list_order[0])]
    return(total)

permutations = []
    
for person_0 in all_people:
    remaining_people_0 = all_people[:]
    remaining_people_0.remove(person_0)
    for person_index_1 in range(8):
        person_1 = remaining_people_0[person_index_1]
        remaining_people_1 = remaining_people_0[:]
        del remaining_people_1[person_index_1]
        for person_index_2 in range(7):
            person_2 = remaining_people_1[person_index_2]
            remaining_people_2 = remaining_people_1[:]
            del remaining_people_2[person_index_2]
            for person_index_3 in range(6):
                person_3 = remaining_people_2[person_index_3]
                remaining_people_3 = remaining_people_2[:]
                del remaining_people_3[person_index_3]
                for person_index_4 in range(5):
                    person_4 = remaining_people_3[person_index_4]
                    remaining_people_4 = remaining_people_3[:]
                    del remaining_people_4[person_index_4]
                    for person_index_5 in range(4):
                        person_5 = remaining_people_4[person_index_5]
                        remaining_people_5 = remaining_people_4[:]
                        del remaining_people_5[person_index_5]
                        for person_index_6 in range(3):
                            person_6 = remaining_people_5[person_index_6]
                            remaining_people_6 = remaining_people_5[:]
                            del remaining_people_6[person_index_6]
                            for person_index_7 in range(2):
                                person_7 = remaining_people_6[person_index_7]
                                remaining_people_7 = remaining_people_6[:]
                                del remaining_people_7[person_index_7]
                                person_8 = remaining_people_7[0]
                                permutations.append([person_0, person_1, person_2, person_3, person_4, person_5, person_6, person_7, person_8])
                            
print(max([happiness(permutation) for permutation in permutations]))
