if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))

num = 2**1000
digits = [int(i) for i in str(num)]

progress_ = Progress("Problem 016: Power digit sum", 0, len(digits))

sum_ = 0
for i in range(len(digits)):
    progress_.count = i
    progress_.progress()
    sum_ += digits[i]

progress_.count = sum_
progress_.total = answers_list[16]
progress_.progress()

if __name__ == '__main__':
    input()
