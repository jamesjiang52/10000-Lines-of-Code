if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 029: Distinct powers", 0, answers_list[29])

result = []
for a in range(2, 101):
    progress_.count = len(list(set(result)))
    progress_.progress()
    for b in range(2, 101):
        result.append(a**b)

progress_.count = len(list(set(result)))
progress_.progress()

if __name__ == '__main__':
    input()
