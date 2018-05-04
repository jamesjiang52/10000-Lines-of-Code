if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 050: Consecutive prime sum", 0, 1000000)

prime_sum = 0
primes = []
num = 2

while True:
    if is_prime(num):
        primes.append(num)
        if prime_sum + num >= 1000000:
            break
        prime_sum += num
        progress_.count = prime_sum
        progress_.progress()
    num += 1

while not is_prime(prime_sum):
    prime_sum -= primes[0]
    del primes[0]

progress_.count = prime_sum
progress_.total = answers_list[50]
progress_.progress()

if __name__ == '__main__':
    input()
