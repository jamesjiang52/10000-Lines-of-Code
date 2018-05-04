if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 004: Largest palindrome product", 0, answers_list[4])

for a in range(100, 1000):
    for b in range(a, 1000):
        num = a*b
        if str(num) == str(num)[::-1]:
            progress_.count = max(progress_.count, num)
            progress_.progress()

if __name__ == '__main__':
    input()
