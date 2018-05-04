if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 069: Totient maximum", 1, answers_list[69])

p = 1
while True:
    if is_prime(p):
        if progress_.count*p > 1000000:
            break
        progress_.count *= p
        progress_.progress()
    p += 1

if __name__ == '__main__':
    input()
