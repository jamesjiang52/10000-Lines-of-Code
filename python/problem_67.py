if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 067: Maximum path sum II", 0, 98)

all_lines = [line.rstrip('\n') for line in open('C:\\Users\\James Jiang\\Documents\\Project Euler\\data\\problem_67_data.txt')]
rows = [line.split(' ') for line in all_lines]
rows_int = []
for row in rows:
    rows_int.append([int(i) for i in row])

for k in range(98, -1, -1):
    progress_.count = 99 - k
    progress_.progress()
    next_row_k = []
    for i in range(len(rows_int[k])):
        next_row_k.append(rows_int[k][i] + max(rows_int[k + 1][i], rows_int[k + 1][i + 1]))
    rows_int[k] = next_row_k

progress_.count = rows_int[0][0]
progress_.total = answers_list[67]
progress_.progress()

if __name__ == '__main__':
    input()
