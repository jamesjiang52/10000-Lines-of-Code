if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 074: Digit factorial chains", 0, 1000000)

chain_lengths_dict = {}
count = 0

for a in range(3, 1000000):
    chain = []
    n = a
    if a % 3871 == 0: #arbitrary number for display purposes
        progress_.count = a
        progress_.progress()
    while True:
        if n in chain:
            chain_lengths_dict[a] = len(chain)
            break
        elif n in chain_lengths_dict:
            chain_lengths_dict[a] = len(chain) + chain_lengths_dict[n]
            break
        else:
            chain.append(n)
        n = sum_factorial_digits(n)
    if chain_lengths_dict[a] == 60:
        count += 1

progress_.count = count
progress_.total = answers_list[74]
progress_.progress()

if __name__ == '__main__':
    input()
