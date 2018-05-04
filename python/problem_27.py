if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 027: Quadratic primes", 0, 2000)

max_number = 0
max_number_ab = 0
for a in range(-1000, 1000):
    progress_.count = 1000 + a
    progress_.progress()
    for b in range(-1000, 1000):
        if (a != 0) and (b != 0):
            count = 0
            n = 0
            while True:
                if is_prime(n**2 + a*n + b):
                    count += 1
                else:
                    if count > max_number:
                        max_number = count
                        max_number_ab = a*b
                    break
                n += 1

progress_.count = max_number_ab
progress_.total = answers_list[27]
progress_.progress()

if __name__ == '__main__':
    input()
