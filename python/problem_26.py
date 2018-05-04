if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 026: Reciprocal cycles", 0, 1000)

max_length = 0
max_length_num = 0

for i in range(10, 1001):
    progress_.count = i
    progress_.progress()
    if is_prime(i):
        if recurring_decimals_length(i) > max_length:
            max_length = recurring_decimals_length(i)
            max_length_num = i

progress_.count = max_length_num
progress_.total = answers_list[26]
progress_.progress()

if __name__ == '__main__':
    input()
