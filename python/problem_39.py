if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 039: Integer right triangles", 0, 1000)

max_count = 0
max_num = 0

for p in range(120, 1000, 2):
    progress_.count = p
    progress_.progress()
    count = count_triangles(p)
    if count > max_count:
        max_count = count
        max_num = p

progress_.count = max_num
progress_.total = answers_list[39]
progress_.progress()

if __name__ == '__main__':
    input()
