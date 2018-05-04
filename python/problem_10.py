if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 010: Summation of primes", 2, answers_list[10])

toggle = 0
for i in range(3, 2000000, 2):
    if is_prime(i):
        progress_.count += i
        toggle += 1
        if toggle % 201 == 0: #arbitrary number for display purposes
            progress_.progress()
            toggle = 0

progress_.progress()

if __name__ == '__main__':
    input()
