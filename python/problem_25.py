if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 025: 1000-digit Fibonacci number", 1, answers_list[25])

while True:
    progress_.count += 1
    progress_.progress()
    if len(str(fib(progress_.count))) == 1000:
        break

if __name__ == '__main__':
    input()
