# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 16:18:06 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

all_rows = [[i for i in line] for line in all_lines]

def allowed_directions(x_position, y_position):
    directions = []
    if all_rows[y_position][x_position - 1] != '#':
        directions.append('left')
    if all_rows[y_position][x_position + 1] != '#':
        directions.append('right')
    if all_rows[y_position - 1][x_position] != '#':
        directions.append('up')
    if all_rows[y_position + 1][x_position] != '#':
        directions.append('down')
    return(directions)

positions_dict = {}
distances_dict = {}

for num in range(8):
    for i in range(len(all_rows)):
        for j in range(len(all_rows[i])):
            if all_rows[i][j] == str(num):
                positions_dict[str(num)] = [j, i]

for num1 in range(7):
    for num2 in range(num1 + 1, 8):
        coordinates_start = positions_dict[str(num1)]
        coordinates_end = positions_dict[str(num2)]
        seen = [coordinates_start + [0]]
        seen_coordinates = [coordinates_start]
        for coordinates in seen:
            directions = allowed_directions(coordinates[0], coordinates[1])
            if 'left' in directions:
                new_coordinates = [coordinates[0] - 1, coordinates[1], coordinates[2] + 1]
                if new_coordinates[:2] == coordinates_end:
                    distances_dict[(str(num1), str(num2))] = new_coordinates[2]
                    break
                if new_coordinates[:2] not in seen_coordinates:
                    seen.append(new_coordinates)
                    seen_coordinates.append(new_coordinates[:2])
            if 'right' in directions:
                new_coordinates = [coordinates[0] + 1, coordinates[1], coordinates[2] + 1]
                if new_coordinates[:2] == coordinates_end:
                    distances_dict[(str(num1), str(num2))] = new_coordinates[2]
                    break
                if new_coordinates[:2] not in seen_coordinates:
                    seen.append(new_coordinates)
                    seen_coordinates.append(new_coordinates[:2])
            if 'up' in directions:
                new_coordinates = [coordinates[0], coordinates[1] - 1, coordinates[2] + 1]
                if new_coordinates[:2] == coordinates_end:
                    distances_dict[(str(num1), str(num2))] = new_coordinates[2]
                    break
                if new_coordinates[:2] not in seen_coordinates:
                    seen.append(new_coordinates)
                    seen_coordinates.append(new_coordinates[:2])
            if 'down' in directions:
                new_coordinates = [coordinates[0], coordinates[1] + 1, coordinates[2] + 1]
                if new_coordinates[:2] == coordinates_end:
                    distances_dict[(str(num1), str(num2))] = new_coordinates[2]
                    break
                if new_coordinates[:2] not in seen_coordinates:
                    seen.append(new_coordinates)
                    seen_coordinates.append(new_coordinates[:2])
                    
def min_distance(current_num, current_distance, nums_remaining):
    if len(nums_remaining) == 0:
        return(current_distance)
    else:
        min_list = []
        for num in nums_remaining:
            next_nums_remaining = nums_remaining[:]
            next_nums_remaining.remove(num)
            if (current_num, num) in distances_dict:
                min_list.append(min_distance(num, current_distance + distances_dict[current_num, num], next_nums_remaining))
            else:
                min_list.append(min_distance(num, current_distance + distances_dict[num, current_num], next_nums_remaining))
        return(min(min_list))
    
print(min_distance('0', 0, [i for i in '1234567']))
