if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 017: Number letter counts", 0, answers_list[17])

for x in range(1, 1001):
    progress_.count += written(x)
    progress_.progress()

if __name__ == '__main__':
    input()
