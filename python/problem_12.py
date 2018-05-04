if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 012: Highly divisible triangular number", 1, answers_list[12])

num = 1
while True:
    progress_.count = int((num**2 - num)/2)
    progress_.progress()
    if num_factors(int((num**2 - num)/2)) > 500:
        break
    num += 1

if __name__ == '__main__':
    input()
