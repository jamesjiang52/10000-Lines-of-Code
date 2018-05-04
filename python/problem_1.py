if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 001: Multiples of 3 and 5", 0, answers_list[1])

for x in range(1000):
    if (x % 3 == 0) or (x % 5 == 0):
        progress_.count += x
        progress_.progress()

if __name__ == '__main__':
    input()
