# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 17:53:02 2017

@author: James Jiang
"""

floors = [[-7, -6, -1, 1, 6, 7], [2, 3, 4, 5], [-5, -4, -3, -2], []]

def position_allowed(floor):
    if floor == []:
        return True
    if floor[-1] < 0:
        return True
    for component in floor:
        if (component < 0) and (-component not in floor):
            return False
    else:
        return True

def all_position_allowed(floors_list):
    return all(position_allowed(floor_single) for floor_single in floors_list)

def position_encode(elevator_position_int, floors_list):
    output_list = [elevator_position_int]
    for floor_single in floors_list:
        pairs = 0
        floor_test = [floor_single[i] > 0 for i in range(len(floor_single))]
        for component in floor_single:
            if -component in floor_single:
                pairs += 1
        output_list.extend([floor_test.count(False), floor_test.count(True), int(pairs/2)])
    return(output_list)
     
floors_seen = [[floors, 0, 0]]
floors_seen_encoded = [position_encode(0, floors)]

dummy = 0
for floor_position in floors_seen:
    elevator_position = floor_position[1]
    steps = floor_position[2]
    floors = floor_position[0]
    current_floor = floors[elevator_position]
    for i in range(len(current_floor)):
        if elevator_position < 3:
            new_floors = [floor[:] for floor in floors]
            new_floors[elevator_position + 1].append(current_floor[i])
            del new_floors[elevator_position][i]
            for floor in new_floors:
                floor.sort()
            if (position_encode(elevator_position + 1, new_floors) not in floors_seen_encoded) and (all_position_allowed(new_floors) == True):
                floors_seen.append([new_floors, elevator_position + 1, steps + 1])
                floors_seen_encoded.append(position_encode(elevator_position + 1, new_floors))
            if len(new_floors[3]) == 14:
                print(steps + 1)
                dummy = 1
                break
            for j in range(len(current_floor)):
                if i != j:
                    new_floors = [floor[:] for floor in floors]
                    new_floors[elevator_position + 1].extend([current_floor[i], current_floor[j]])
                    if i < j:
                        del new_floors[elevator_position][j]
                        del new_floors[elevator_position][i]
                    else:
                        del new_floors[elevator_position][i]
                        del new_floors[elevator_position][j]
                    for floor in new_floors:
                        floor.sort()
                    if (position_encode(elevator_position + 1, new_floors) not in floors_seen_encoded) and (all_position_allowed(new_floors) == True):
                        floors_seen.append([new_floors, elevator_position + 1, steps + 1])
                        floors_seen_encoded.append(position_encode(elevator_position + 1, new_floors))
                    if len(new_floors[3]) == 14:
                        print(steps + 1)
                        dummy = 1
                        break
        if elevator_position > 0:
            new_floors = [floor[:] for floor in floors]
            new_floors[elevator_position - 1].append(current_floor[i])
            del new_floors[elevator_position][i]
            for floor in new_floors:
                floor.sort()
            if (position_encode(elevator_position - 1, new_floors) not in floors_seen_encoded) and (all_position_allowed(new_floors) == True):
                floors_seen.append([new_floors, elevator_position - 1, steps + 1])
                floors_seen_encoded.append(position_encode(elevator_position - 1, new_floors))
            for j in range(len(current_floor)):
                if i != j:
                    new_floors = [floor[:] for floor in floors]
                    new_floors[elevator_position - 1].extend([current_floor[i], current_floor[j]])
                    if i < j:
                        del new_floors[elevator_position][j]
                        del new_floors[elevator_position][i]
                    else:
                        del new_floors[elevator_position][i]
                        del new_floors[elevator_position][j]
                    for floor in new_floors:
                        floor.sort()
                    if (position_encode(elevator_position - 1, new_floors) not in floors_seen_encoded) and (all_position_allowed(new_floors) == True):
                        floors_seen.append([new_floors, elevator_position - 1, steps + 1])
                        floors_seen_encoded.append(position_encode(elevator_position - 1, new_floors))
        if dummy == 0:
            continue
        break
    if dummy == 1:
        break
