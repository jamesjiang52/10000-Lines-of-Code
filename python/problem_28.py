if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 028: Number spiral diagonals", 1, answers_list[28])

for a in range(2, 502):
    progress_.count += 4*a**2 - 10*a + 7
    progress_.count += 4*a**2 - 8*a + 5
    progress_.count += 4*a**2 - 6*a + 3
    progress_.count += 4*a**2 - 4*a + 1
    progress_.progress()

if __name__ == '__main__':
    input()
