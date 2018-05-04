if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 063: Powerful digit counts", 0, answers_list[63])

for n in range(1, 22):
    for a in range(1, 10):
        num_str = str(a**n)
        if len(num_str) == n:
            progress_.count += 1
            progress_.progress()

if __name__ == '__main__':
    input()
