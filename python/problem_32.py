if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 032: Pandigital products", 0, 51)

result = []
for a in range(1, 51):
    progress_.count = a
    progress_.progress()
    for b in range(a, 2001):
        digits = str(a) + str(b) + str(a*b)
        if is_pandigital(digits):
            result.append(a*b)

progress_.count = sum(list(set(result)))
progress_.total = answers_list[32]
progress_.progress()

if __name__ == '__main__':
    input()
