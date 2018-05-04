import itertools
import math

if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 068: Magic 5-gon ring", 0, math.factorial(10))

rearrangements = itertools.permutations(list(range(1, 11)))
max_16 = 0
for i in rearrangements:
    progress_.count += 1
    if progress_.count % 2831 == 0: #arbitrary number for display purposes
        progress_.progress()
    if (i[0] + i[6] + i[7]) == (i[1] + i[7] + i[8]) == (i[2] + i[8] + i[9]) == (i[3] + i[9] + i[5]) == (i[4] + i[5] + i[6]):
        start = min([i[0], i[1], i[2], i[3], i[4]])
        if i[0] == start:
            string = str(i[0]) + str(i[6]) + str(i[7]) + str(i[1]) + str(i[7]) + str(i[8]) + str(i[2]) + str(i[8]) + str(i[9]) + str(i[3]) + str(i[9]) + str(i[5]) + str(i[4]) + str(i[5]) + str(i[6])
        elif i[1] == start:
            string = str(i[1]) + str(i[7]) + str(i[8]) + str(i[2]) + str(i[8]) + str(i[9]) + str(i[3]) + str(i[9]) + str(i[5]) + str(i[4]) + str(i[5]) + str(i[6]) + str(i[0]) + str(i[6]) + str(i[7])
        elif i[2] == start:
            string = str(i[2]) + str(i[8]) + str(i[9]) + str(i[3]) + str(i[9]) + str(i[5]) + str(i[4]) + str(i[5]) + str(i[6]) + str(i[0]) + str(i[6]) + str(i[7]) + str(i[1]) + str(i[7]) + str(i[8])
        elif i[3] == start:
            string = str(i[3]) + str(i[9]) + str(i[5]) + str(i[4]) + str(i[5]) + str(i[6]) + str(i[0]) + str(i[6]) + str(i[7]) + str(i[1]) + str(i[7]) + str(i[8]) + str(i[2]) + str(i[8]) + str(i[9])
        elif i[4] == start:
            string = str(i[4]) + str(i[5]) + str(i[6]) + str(i[0]) + str(i[6]) + str(i[7]) + str(i[1]) + str(i[7]) + str(i[8]) + str(i[2]) + str(i[8]) + str(i[9]) + str(i[3]) + str(i[9]) + str(i[5])
        if len(string) == 16:
            max_16 = max(max_16, int(string))

progress_.count = max_16
progress_.total = answers_list[68]
progress_.progress()

if __name__ == '__main__':
    input()
