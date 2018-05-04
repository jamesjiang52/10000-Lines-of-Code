import math

if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 075: Singular integer right triangles", 0, round(math.sqrt(1500000/2)) + 1)

all_lengths = [0]*1500001

count = 0
for m in range(2, round(math.sqrt(1500000/2)) + 1):
    progress_.count = m
    progress_.progress()
    for n in range(1, m):
        if ((m + n) % 2 == 1) and (math.gcd(m, n) == 1):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            sum_ = a + b + c
            length = sum_
            while length <= 1500000:
                all_lengths[length] += 1
                if all_lengths[length] == 1:
                    count += 1
                elif all_lengths[length] == 2:
                    count -= 1
                length += sum_

progress_.count = count
progress_.total = answers_list[75]
progress_.progress()

if __name__ == '__main__':
    input()
