if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 030: Digit fifth powers", 0, 354295)

total = 0
for n in range(2, 354295):
    if n % 1729 == 0:
        progress_.count = n
        progress_.progress()
    power_digits = 0
    for i in str(n):
        power_digits += int(i)**5
    if n == power_digits:
        total += n

progress_.count = total
progress_.total = answers_list[30]
progress_.progress()

if __name__ == '__main__':
    input()
