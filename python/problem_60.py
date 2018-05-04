if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 060: Prime pair sets", 0, 160000) #arbitrary number for display purposes
progress_.progress()

#create list of first 1200 primes
primes = []
for i in range(3, 10000):
    if is_prime(i):
        primes.append(i)

for a in range(1, 1197):
    for b in range(a + 1, 1198):
        if not is_prime_concatenatable([primes[a], primes[b]]):
            continue
        for c in range(b + 1, 1199):
            progress_.count += 1
            progress_.progress()
            if not is_prime_concatenatable([primes[a], primes[b], primes[c]]):
                continue
            for d in range(c + 1, 1200):
                if not is_prime_concatenatable([primes[a], primes[b], primes[c], primes[d]]):
                    continue
                for e in range(d + 1, 1201):
                    if is_prime_concatenatable([primes[a], primes[b], primes[c], primes[d], primes[e]]):
                        break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break

progress_.count = sum([primes[a], primes[b], primes[c], primes[d], primes[e]])
progress_.total = answers_list[60]
progress_.progress()

if __name__ == '__main__':
    input()
