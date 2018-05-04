if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))

min_num = 0
min_quotient = 2

primes = []
for i in range(9999, 1000, -2):
    if is_prime(i):
        primes.append(i)

progress_ = Progress("Problem 070: Totient permutations", 0, len(primes))

done = 0
for a in range(len(primes)):
    progress_.count = a
    progress_.progress()
    for b in range(a, len(primes)):
        i = primes[a]*primes[b]
        totient_i = (primes[a] - 1)*(primes[b] - 1)
        if i < 10**7:
            if sorted(str(i)) == sorted(str(totient_i)):
                if i/totient_i < min_quotient:
                    min_quotient = i/totient_i
                    min_num = i
                    break

progress_.count = min_num
progress_.total = answers_list[70]
progress_.progress()

if __name__ == '__main__':
    input()
