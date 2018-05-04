if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 064: Odd period square roots", 0, answers_list[64])

for N in range(2, 10001):
    if not is_square(N):
        if len_fraction_expansion_sqrt_period(N) % 2 == 1:
            progress_.count += 1
            progress_.progress()

if __name__ == '__main__':
    input()
