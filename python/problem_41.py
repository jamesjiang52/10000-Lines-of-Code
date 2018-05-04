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
progress_ = Progress("Problem 041: Pandigital prime", 0, 2)
progress_.progress()

all_nums = '1234567'
all_rearrangements = []
for i in range(1, 8):
    rearrangements_lists = itertools.permutations(all_nums[:i], i)
    rearrangements_str = [''.join(rearrangement) for rearrangement in rearrangements_lists]
    all_rearrangements.extend(rearrangements_str)

progress_.count = 1
progress_.progress()

all_rearrangements_int = [int(i) for i in all_rearrangements]
all_rearrangements_int.sort(reverse=True)

for rearrangement in all_rearrangements_int:
    if is_prime(rearrangement):
        break

progress_.count = rearrangement
progress_.total = answers_list[41]
progress_.progress()

if __name__ == '__main__':
    input()
