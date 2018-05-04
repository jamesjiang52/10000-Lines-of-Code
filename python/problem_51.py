import itertools

if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 051: Prime digit replacements", 0, 2000) #arbitary number for display purposes

ones_digits = [1, 3, 7, 9]
n = 5

for a in range(0, n - 1):
    for b in range(a + 1, n):
        for i, j, k in itertools.product(ones_digits, range(10), range(10)):
            progress_.count += 1
            progress_.progress()
            if (a == 0) and (k == 0):
                continue
            count = 0
            first = 0
            for x in range(0, 10):
                if (a != 0) and (b != 0) and (x == 0):
                    continue
                num = i + 10**(n - a)*k + 10**(n - b)*j
                for l in range(0, n):
                    if (l == a) or (l == b):
                        continue
                    num += 10**(n - l)*x
                if is_prime(num):
                    if (first == 0):
                        first = num
                    count += 1
            if count == 8:
                break
        else:
            continue
        break
    else:
        continue
    break

progress_.count = first
progress_.total = answers_list[51]
progress_.progress()

if __name__ == '__main__':
    input()
