if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 052: Permuted multiples", 0, 66 + 666 + 6666 + answers_list[52] - 100000)

n = 2
while True:
    min_ = 10**n
    max_ = min_ + round(2*min_/3) + 1
    for x in range(min_, max_):
        progress_.count += 1
        if x % 283 == 0: #arbitrary number for display purposes
            progress_.progress()
        if set(str(x)) == set(str(2*x)) == set(str(3*x)) == set(str(4*x)) == set(str(5*x)) == set(str(6*x)):
            break
    else:
        n += 1
        continue
    break

progress_.count = x
progress_.total = answers_list[52]
progress_.progress()

if __name__ == '__main__':
    input()
