if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 056: Powerful digit sum", 0, 100)

max_digital_sum = 0

for a in range(1, 100):
    progress_.count = a
    progress_.progress()
    for b in range(1, 100):
        digits = [int(i) for i in str(a**b)]
        max_digital_sum = max(max_digital_sum, sum(digits))

progress_.count = max_digital_sum
progress_.total = answers_list[56]
progress_.progress()

if __name__ == '__main__':
    input()
