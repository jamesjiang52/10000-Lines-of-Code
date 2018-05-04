if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 066: Diophantine equation", 0, 1000)

max_x = 0
max_D = 0

for D in range(2, 1001):
    progress_.count = D
    progress_.progress()
    if not is_square(D):
        d = minimal_solution(D)
        if d > max_x:
            max_x = d
            max_D = D

progress_.count = max_D
progress_.total = answers_list[66]
progress_.progress()

if __name__ == '__main__':
    input()
