if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 047: Distinct prime factors", 0, answers_list[47])

i = 2
while True:
    if i % 283 == 0: #arbitrary number for display purposes
        progress_.count = i
        progress_.progress()
    if (num_prime_factors(i) == 4) and (num_prime_factors(i + 1) == 4) and (num_prime_factors(i + 2) == 4) and (num_prime_factors(i + 3) == 4):
        break
    i += 1

progress_.count = i
progress_.progress()

if __name__ == '__main__':
    input()
