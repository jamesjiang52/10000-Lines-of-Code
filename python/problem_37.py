if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 037: Truncatable primes", 0, answers_list[37])

i = 11
total = 0
count = 0

while count < 11:
    if is_prime(i):
        progress_.count = i
        progress_.progress()
        for j in truncate(i):
            if not is_prime(j):
                break
        else:
            total += i
            count += 1
    i += 1

progress_.count = total
progress_.progress()

if __name__ == '__main__':
    input()
