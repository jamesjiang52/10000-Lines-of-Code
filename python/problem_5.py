if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 005: Smallest multiple", 1, 	answers_list[5])

factors = []
for i in range(1, 21):
    list_prime_factors = prime_factors(i)
    for prime_factor in list_prime_factors:
        if list_prime_factors.count(prime_factor) > factors.count(prime_factor):
            for i in range(list_prime_factors.count(prime_factor) - factors.count(prime_factor)):
                factors.append(prime_factor)

for factor in factors:
    progress_.count *= factor
    progress_.progress()

if __name__ == '__main__':
    input()
