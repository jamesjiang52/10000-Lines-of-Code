if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 035: Circular primes", 0, 1000000)

count = 1
for k in range(3, 1000000, 2):
    if k % 1729 == 0: #arbitrary number for display purposes
        progress_.count = k
        progress_.progress()
    if not is_digits_divisible(k):
        if is_prime(k):
            for n in arrangements(k):
                if not is_prime(n):
                    break
            else:
                count += 1

progress_.count = count
progress_.total = answers_list[35]
progress_.progress()

if __name__ == '__main__':
    input()
