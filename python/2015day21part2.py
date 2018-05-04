# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 13:03:04 2018

@author: James Jiang
"""

boss_hp = 109
boss_damage = 8
boss_armor = 2

weapons_damage = [4, 5, 6, 7, 8]
weapons_cost = [8, 10, 25, 40, 74]
armor_defense = [0, 1, 2, 3, 4, 5]
armor_cost = [0, 13, 31, 53, 75, 102]
rings_damage = [0, 0, 1, 2, 3, 0, 0, 0]
rings_defense = [0, 0, 0, 0, 0, 1, 2, 3]
rings_cost = [0, 0, 25, 50, 100, 20, 40, 80]

def player_attack(player_damage):
    global boss_hp, boss_armor
    boss_hp -= max(1, player_damage - boss_armor)
    
def boss_attack(player_armor):
    global player_hp, boss_damage
    player_hp -= max(1, boss_damage - player_armor)
    
costs_all = []

for i in range(len(weapons_damage)):
    for j in range(len(armor_defense)):
        for k in range(len(rings_damage)):
            for l in range(len(rings_damage)):
                if l == k:
                    continue
                boss_hp = 109
                boss_damage = 8
                boss_armor = 2
                player_hp = 100
                while (boss_hp > 0) and (player_hp > 0):
                    player_attack(weapons_damage[i] + rings_damage[k] + rings_damage[l])
                    boss_attack(armor_defense[j] + rings_defense[k] + rings_defense[l])
                    if player_hp <= 0:
                        costs_all.append(weapons_cost[i] + armor_cost[j] + rings_cost[k] + rings_cost[l])

print(max(costs_all))
