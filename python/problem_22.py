if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 022: Names scores", 0, answers_list[22])

with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\data\\problem_22_data.txt') as f:
    for line in f:
        names = line.split('","')
names[0] = names[0][1:]
names[-1] = names[-1][:-1]
names.sort()

for i in range(len(names)):
    name_score = 0
    for letter in names[i]:
        name_score += score(letter)
    progress_.count += name_score*(i + 1)
    progress_.progress()

if __name__ == '__main__':
    input()
