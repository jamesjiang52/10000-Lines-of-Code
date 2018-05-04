if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 007: 10001st prime", 1, answers_list[7])

counter = 0
while counter < 10001:
    if is_prime(progress_.count):
        counter += 1
        progress_.progress()
    progress_.count += 1

if __name__ == '__main__':
    input()
