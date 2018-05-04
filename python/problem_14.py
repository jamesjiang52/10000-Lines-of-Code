if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 014: Longest Collatz sequence", 1, 1000001)

lengths_dict = {}
max_length = 0
max_length_num = 0
for n in range(1, 1000001):
    if n % 283 == 0: #arbitrary number for display purposes
        progress_.count = n
        progress_.progress()
    length_sequence = 1
    k = n
    while k != 1:
        if k in lengths_dict:
            length_sequence += lengths_dict[k]
            break
        length_sequence += 1
        k = collatz(k)
    if length_sequence > max_length:
        max_length = length_sequence
        max_length_num = n
    lengths_dict[n] = length_sequence

progress_.count = max_length_num
progress_.total = answers_list[14]
progress_.progress()

if __name__ == '__main__':
    input()
