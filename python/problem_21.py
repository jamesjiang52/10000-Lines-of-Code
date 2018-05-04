if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 021: Amicable numbers", 0, answers_list[21])

for x in range(10, 10000):
    if (sum_factors(sum_factors(x)) == x) and (sum_factors(x) < 10000) and (sum_factors(x) != x):
        progress_.count += x
        progress_.progress()

if __name__ == '__main__':
    input()
