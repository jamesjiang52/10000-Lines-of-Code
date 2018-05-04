if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 065: Convergents of e", 0, answers_list[65])
progress_.progress()

progress_.count = sum_numerator_fraction_expansion_e(99)
progress_.progress()

if __name__ == '__main__':
    input()
