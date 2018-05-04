# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:02:12 2017

@author: James Jiang
"""

all_lines = [line.rstrip('\n') for line in open('Data.txt')]

all_instructions = []
for line in all_lines:
    instruction = line.split(' ')
    all_instructions.append(instruction)
    
bot_dict = {}
output_dict = {}

for instruction in all_instructions:
    if instruction[0] == 'value':
        if instruction[-1] not in bot_dict:
            bot_dict[instruction[-1]] = []
    elif instruction[0] == 'bot':
        if instruction[1] not in bot_dict:
            bot_dict[instruction[1]] = []
        if instruction[5] == 'bot':
            if instruction[6] not in bot_dict:
                bot_dict[instruction[6]] = []
        else:
            if instruction[6] not in output_dict:
                output_dict[instruction[6]] = []
        if instruction[-2] == 'bot':
            if instruction[-1] not in bot_dict:
                bot_dict[instruction[-1]] = []
        else:
            if instruction[-2] not in output_dict:
                output_dict[instruction[-1]] = []

for i in range(len(all_instructions)):
    instruction = all_instructions[i]
    if instruction[0] == 'value':
        bot_dict[instruction[-1]].append(instruction[1])
        all_instructions[i] = ['removed']
        
for bot in bot_dict:
    bot_dict[bot] = [int(i) for i in bot_dict[bot]]

while True:
    for bot in bot_dict:
        if len(bot_dict[bot]) == 2:
            for i in range(len(all_instructions)):
                instruction = all_instructions[i]
                if (instruction[0] == 'bot') and (instruction[1] == bot):
                    if instruction[5] == 'bot':
                        bot_dict[instruction[6]].append(min(bot_dict[bot]))
                    else:
                        output_dict[instruction[6]].append(min(bot_dict[bot]))
                    if instruction[-2] == 'bot':
                        bot_dict[instruction[-1]].append(max(bot_dict[bot]))
                    else:
                        output_dict[instruction[-1]].append(max(bot_dict[bot]))
                    all_instructions[i] = ['removed']
        for value in list(bot_dict.values()):
            if (61 in value) and (17 in value):
                print(list(bot_dict.keys())[list(bot_dict.values()).index(value)])
                break
        else:
            continue
        break
    else:
        continue
    break
