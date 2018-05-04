import math

if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 003: Largest prime factor", 0, round(math.sqrt(600851475143)))

x = 600851475143
for n in range(round(math.sqrt(x)), 1, -1):
    if x % n == 0:
        progress_.count = round(math.sqrt(x)) - n
        progress_.progress()
        if is_prime(n):
            break

progress_.count = n
progress_.total = answers_list[3]
progress_.progress()

if __name__ == '__main__':
    input()
