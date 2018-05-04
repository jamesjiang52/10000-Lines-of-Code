# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 19:32:26 2018

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]
all_data = [line.split(': ') for line in all_lines]

capacities = {}
durabilities = {}
flavors = {}
textures = {}
calories = {}

for data in all_data:
    data[1] = data[1].replace(',', '')
    properties = data[1].split(' ')
    capacities[data[0]] = int(properties[1])
    durabilities[data[0]] = int(properties[3])
    flavors[data[0]] = int(properties[5])
    textures[data[0]] = int(properties[-3])
    calories[data[0]] = int(properties[-1])

max_all_combinations = 0

for frosting_amount in range(101):
    for candy_amount in range(101):
        if frosting_amount + candy_amount > 100:
            break
        else:
            for butterscotch_amount in range(101):
                if frosting_amount + candy_amount + butterscotch_amount > 100:
                    break
                else:
                    sugar_amount = 100 - (frosting_amount + candy_amount + butterscotch_amount)
                    total_capacity = max(frosting_amount*capacities['Frosting'] +candy_amount*capacities['Candy'] + butterscotch_amount*capacities['Butterscotch'] + sugar_amount*capacities['Sugar'], 0)
                    total_durability = max(frosting_amount*durabilities['Frosting'] +candy_amount*durabilities['Candy'] + butterscotch_amount*durabilities['Butterscotch'] + sugar_amount*durabilities['Sugar'], 0)
                    total_flavor = max(frosting_amount*flavors['Frosting'] +candy_amount*flavors['Candy'] + butterscotch_amount*flavors['Butterscotch'] + sugar_amount*flavors['Sugar'], 0)
                    total_texture = max(frosting_amount*textures['Frosting'] +candy_amount*textures['Candy'] + butterscotch_amount*textures['Butterscotch'] + sugar_amount*textures['Sugar'], 0)
                    max_all_combinations = max(max_all_combinations, total_capacity*total_durability*total_flavor*total_texture)
                    
print(max_all_combinations)
