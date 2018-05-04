import itertools

if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 043: Sub-string divisibility", 0, 9876543210)
progress_.progress()

potential = itertools.permutations(list(range(10)))

total = 0
for number in potential:
    if (100*number[7] + 10*number[8] + number[9]) % 17 == 0:
        if (100*number[6] + 10 * number[7] + number[8]) % 13 == 0:
            if (number[5] + number[7] - number[6]) % 11 == 0:
                progress_.count = int(''.join([str(i) for i in number]))
                progress_.progress()
                if (100*number[4] + 10*number[5] + number[6]) % 7 == 0:
                    if number[5] % 5 == 0:
                        if (number[2] + number[3] + number[4]) % 3 == 0:
                            if number[3] % 2 == 0:
                                total += int(''.join(map(str, number)))

progress_.count = total
progress_.total = answers_list[43]
progress_.progress()

if __name__ == '__main__':
    input()
