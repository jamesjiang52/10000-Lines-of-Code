if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 058: Spiral primes", 0, answers_list[58])

a = 2
n = 0
while (n/(4*a - 3) >= 0.10) or (n == 0):
    if is_prime(4*a**2 - 10*a + 7):
        n += 1
    if is_prime(4*a**2 - 8*a + 5):
        n += 1
    if is_prime(4*a**2 - 6*a + 3):
        n += 1
    #bottom-right diagonal is always an odd square
    a += 1
    if a % 11 == 0: #arbitrary number for display purposes
        progress_.count = 2*a - 1
        progress_.progress()

progress_.count = 2*a - 1
progress_.progress()

if __name__ == '__main__':
    input()
