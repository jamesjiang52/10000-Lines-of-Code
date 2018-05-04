if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 006: Sum square difference", 1, 101)

sum = 0
squared_sum = 0
for n in range(1, 101):
    sum += n
    squared_sum += n**2
    progress_.count = n
    progress_.progress()

progress_.count = sum**2 - squared_sum
progress_.total = answers_list[6]
progress_.progress()

if __name__ == '__main__':
    input()
