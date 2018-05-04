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
progress_ = Progress("Problem 046: Goldbach's other conjecture", 9, answers_list[46])

while True:
    progress_.progress()
    if not is_prime(progress_.count):
        for prime in range(3, progress_.count - 1):
            if is_prime(prime):
                for square in range(1, int(math.sqrt((progress_.count - 3)//2)) + 1):
                    if progress_.count == prime + 2*square**2:
                        break
                else:
                    continue
                break
        else:
            break
    progress_.count += 2

if __name__ == '__main__':
    input()
