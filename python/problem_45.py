if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 045: Triangular, pentagonal, and hexagonal", 0, answers_list[45])

n = 144

while True:
    progress_.count = n*(2*n - 1)
    progress_.progress()
    if is_pentagon(progress_.count):
        break
    n += 1

if __name__ == '__main__':
    input()
