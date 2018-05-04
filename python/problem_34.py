if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 034: Digit factorials", 0, answers_list[34])

for n in range(3, answers_list[34]):
    if sum_factorial_digits(n) == n:
        progress_.count += n
        progress_.progress()

if __name__ == '__main__':
    input()
