import math

if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 073: Counting fractions in a range", 0, 12001)

count = 0
for n in range(2, 12001):
    progress_.count = n
    progress_.progress()
    for i in range(math.floor(n/3) + 1, math.ceil(n/2)):
        if math.gcd(n, i) == 1:
            count += 1

progress_.count = count
progress_.total = answers_list[73]
progress_.progress()

if __name__ == '__main__':
    input()
