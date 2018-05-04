if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 038: Pandigital multiples", 0, 5000)

for i in range(10000, 5000, -1):
    progress_.count = 10000 - i
    progress_.progress()
    if is_pandigital(str(i) + str(2*i)):
        break

progress_.count = int(str(i) + str(2*i))
progress_.total = answers_list[38]
progress_.progress()

if __name__ == '__main__':
    input()
