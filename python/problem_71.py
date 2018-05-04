if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 071: Ordered fractions", 0, 1000001)

min_distance = 1
min_number = 0

for d in range(2, 1000001):
    if d % 283 == 0: #arbitrary number for display purposes
        progress_.count = d
        progress_.progress()
    i = 3*d//7
    if (3/7 - i/d > 0) and (3/7 - i/d < min_distance):
        min_distance = 3/7 - i/d
        min_number = i

progress_.count = min_number
progress_.total = answers_list[71]
progress_.progress()

if __name__ == '__main__':
    input()
