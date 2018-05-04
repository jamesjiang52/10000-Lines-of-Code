if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 023: Non-abundant sums", 0, 1)
progress_.progress()

abundant_nums = []
for i in range(12, 28124):
    if is_abundant(i):
        abundant_nums.append(i)

progress_.total = len(abundant_nums)

all_nums = list(range(1, 28124))
abundant_sums = set([])
for i in range(len(abundant_nums)):
    progress_.count = i
    progress_.progress()
    for j in range(i + 1):
        abundant_sum = abundant_nums[i] + abundant_nums[j]
        if abundant_sum > 28123:
            break
        abundant_sums.add(abundant_sum)

for i in range(len(all_nums)):
    if all_nums[i] in abundant_sums:
        all_nums[i] = 0

progress_.count = sum(all_nums)
progress_.total = answers_list[23]
progress_.progress()

if __name__ == '__main__':
    input()
