if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))

all_lines = [line.rstrip('\n') for line in open('C:\\Users\\James Jiang\\Documents\\Project Euler\\data\\problem_13_data.txt')]
all_nums = [int(i) for i in all_lines]

progress_ = Progress("Problem 013: Large sum", 0, len(all_nums))

sum_ = 0
for i in range(len(all_nums)):
    progress_.count = i
    progress_.progress()
    sum_ += all_nums[i]

progress_.count = int(str(sum_)[:10])
progress_.total = answers_list[13]
progress_.progress()

if __name__ == '__main__':
    input()
