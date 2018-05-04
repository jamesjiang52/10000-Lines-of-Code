if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 042: Coded triangle numbers", 0, answers_list[42])

with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\data\\problem_42_data.txt') as f:
    for line in f:
        all_words = line.split('","')

all_words[0] = all_words[0][1:]
all_words[-1] = all_words[-1][:-1]

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = list(range(1, 27))

for word in all_words:
    value = 0
    for letter in word:
        value += numbers[letters.index(letter)]
    if is_triangle(value):
        progress_.count += 1
        progress_.progress()

if __name__ == '__main__':
    input()
