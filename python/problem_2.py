if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 002: Even Fibonacci numbers", 0, answers_list[2])

a, b = 0, 1
while b < 4000000:
    if b % 2 == 0:
        progress_.count += b
        progress_.progress()
    a, b = b, a + b

if __name__ == '__main__':
    input()
