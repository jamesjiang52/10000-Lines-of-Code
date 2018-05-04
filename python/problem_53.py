if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))

progress_ = Progress("Problem 053: Combinatoric selections", 0, answers_list[53])

for n in range(23, 101):
    for r in range(1, n):
        if choose(n, r) > 1000000:
            progress_.count += 1
            progress_.progress()

if __name__ == '__main__':
    input()
