# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 13:29:11 2018

@author: James Jiang
"""

boss_hp = 71
boss_damage = 10

def mana_cost_total(player_hp, mana, boss_hp, shield_timer, poison_timer, recharge_timer, player_turn):
    if boss_hp <= 0:
        return(0)
        
    new_shield_timer = max(0, shield_timer - 1)
    new_poison_timer = max(0, poison_timer - 1)
    new_recharge_timer = max(0, recharge_timer - 1)
    
    if player_turn == True:
        if poison_timer > 0:
            boss_hp -= 3
            if boss_hp <= 0:
                return(0)
        if recharge_timer > 0:
            mana += 101
        mana_cost = 99999
        if mana >= 53:
            mana_cost = min(mana_cost, 53 + mana_cost_total(player_hp, mana - 53, boss_hp - 4, new_shield_timer, new_poison_timer, new_recharge_timer, False))
        if mana >= 73:
            mana_cost = min(mana_cost, 73 + mana_cost_total(player_hp + 2, mana - 73, boss_hp - 2, new_shield_timer, new_poison_timer, new_recharge_timer, False))
        if (mana >= 113) and (new_shield_timer == 0):
            mana_cost = min(mana_cost, 113 + mana_cost_total(player_hp, mana - 113, boss_hp, 6, new_poison_timer, new_recharge_timer, False))
        if (mana >= 173) and (new_poison_timer == 0):
            mana_cost = min(mana_cost, 173 + mana_cost_total(player_hp, mana - 173, boss_hp, new_shield_timer, 6, new_recharge_timer, False))
        if (mana >= 229) and (new_recharge_timer == 0):
            mana_cost = min(mana_cost, 229 + mana_cost_total(player_hp, mana - 229, boss_hp, new_shield_timer, new_poison_timer, 5, False))
        return(mana_cost)
        
    else:
        if shield_timer > 0:
            player_armor = 7
        else:
            player_armor = 0
        if poison_timer > 0:
            boss_hp -= 3
            if boss_hp <= 0:
                return(0)
        if recharge_timer > 0:
            mana += 101
        player_hp -= max(1, boss_damage - player_armor)
        if player_hp <= 0:
            return(99999)
        else:
            return mana_cost_total(player_hp, mana, boss_hp, new_shield_timer, new_poison_timer, new_recharge_timer, True)
    
print(mana_cost_total(50, 500, boss_hp, 0, 0, 0, True)) 
