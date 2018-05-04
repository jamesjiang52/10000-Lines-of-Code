# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 14:43:08 2018

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]
all_distances = [line.split(' ') for line in all_lines]
for list_distance in all_distances:
    del list_distance[1]
    del list_distance[2]
    list_distance[2] = int(list_distance[2])

distances_dict = {}
all_locations = []

for pair in all_distances:
    distances_dict[(pair[0], pair[1])] = int(pair[2])
    if pair[0] not in all_locations:
        all_locations.append(pair[0])
    if pair[1] not in all_locations:
        all_locations.append(pair[1])
    
def min_distance(current_location, total_distance, remaining_locations):
    if remaining_locations == []:
        return(total_distance)
    else:
        min_list = []
        for location in remaining_locations:
            new_remaining_locations = remaining_locations[:]
            new_remaining_locations.remove(location)
            if (current_location, location) in distances_dict:
                new_total_distance = total_distance + distances_dict[(current_location, location)]
            else:
                new_total_distance = total_distance + distances_dict[(location, current_location)]
            min_list.append(min_distance(location, new_total_distance, new_remaining_locations))
        return(min(min_list))
    
all_min_distances = []
for starting_location in all_locations:
    all_locations_starting = all_locations[:]
    all_locations_starting.remove(starting_location)
    all_min_distances.append(min_distance(starting_location, 0, all_locations_starting))
    
print(min(all_min_distances))
    