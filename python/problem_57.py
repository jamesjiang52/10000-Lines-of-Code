if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 057: Square root convergents", 0, answers_list[57])

for i in range(1, 1001):
    if fraction_expansion_sqrt_2(i)[0] > fraction_expansion_sqrt_2(i)[1]:
        progress_.count += 1
        progress_.progress()

if __name__ == '__main__':
    input()
