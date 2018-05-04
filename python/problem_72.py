if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 072: Counting fractions", 0, 1000000)

print_ = 0
all_totients = list(range(1000001))
p = 2
while p < 1000000:
    if print_ % 13 == 0: #arbitrary number for display purposes
        progress_.count = p
        progress_.progress()
    for i in range(0, len(all_totients), p):
        all_totients[i] = all_totients[i]*(p - 1)//p
    p += 1
    print_ += 1
    while (p < 1000000) and (all_totients[p] != p):
        p += 1

progress_.count = sum(all_totients) - 1
progress_.total = answers_list[72]
progress_.progress()

if __name__ == '__main__':
    input()
