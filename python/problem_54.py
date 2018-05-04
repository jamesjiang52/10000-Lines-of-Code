if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 054: Poker hands", 0, answers_list[54])
progress_.progress()

hands = []
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\data\\problem_54_data.txt') as f:
    for line in f:
        hands.append(line.split(' '))

dict_values = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
for num in '123456789':
    dict_values[num] = int(num)

player_1_hands = [hand[:5] for hand in hands]
player_2_hands = [hand[5:] for hand in hands]
player_1_hands_values = []
player_2_hands_values = []
player_1_hands_suits = []
player_2_hands_suits = []

for i in range(len(hands)):
    player_1_hands_values.append([dict_values[card[0]] for card in player_1_hands[i]])
    player_2_hands_values.append([dict_values[card[0]] for card in player_2_hands[i]])
    player_1_hands_suits.append([card[1] for card in player_1_hands[i]])
    player_2_hands_suits.append([card[1] for card in player_2_hands[i]])

for i in range(len(hands)):
    if analyze_hand(player_1_hands_values[i], player_1_hands_suits[i])[0] > analyze_hand(player_2_hands_values[i], player_2_hands_suits[i])[0]:
        progress_.count += 1
        progress_.progress()
    elif analyze_hand(player_1_hands_values[i], player_1_hands_suits[i])[0] == analyze_hand(player_2_hands_values[i], player_2_hands_suits[i])[0]:
        if analyze_hand(player_1_hands_values[i], player_1_hands_suits[i])[1] > analyze_hand(player_2_hands_values[i], player_2_hands_suits[i])[1]:
            progress_.count += 1
            progress_.progress()

if __name__ == '__main__':
    input()
