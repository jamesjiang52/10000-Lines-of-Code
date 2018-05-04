if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 009: Special Pythagorean triplet", 1, 1000)

for a in range(1, 1000):
    progress_.count = a
    progress_.progress()
    for b in range(a, 1000):
        if a**2 + b**2 == (1000 - a - b)**2:
            break
    else:
        continue
    break

progress_.count = a*b*(1000 - a - b)
progress_.total = answers_list[9]
progress_.progress()

if __name__ == '__main__':
    input()
