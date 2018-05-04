import math

if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))

digits = [int(i) for i in str(math.factorial(100))]

progress_ = Progress("Problem 020: Factorial digit sum", 0, len(digits))

sum_ = 0
for i in range(len(digits)):
    progress_.count = i
    progress_.progress()
    sum_ += digits[i]

progress_.count = sum_
progress_.total = answers_list[20]
progress_.progress()

if __name__ == '__main__':
    input()
