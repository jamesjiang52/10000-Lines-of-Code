if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 049: Prime permutations", 1000, int(str(answers_list[49])[:4]))

done = 0
n = 1488
while True:
    if is_prime(n):
        progress_.count = n
        progress_.progress()
        for a in range(1000, 5000):
            if is_prime(n + a) and is_prime(n + 2*a):
                digits_1 = [int(i) for i in str(n)]
                digits_2 = [int(i) for i in str(n + a)]
                digits_3 = [int(i) for i in str(n + 2*a)]
                if (sorted(digits_1) == sorted(digits_2)) and (sorted(digits_1) == sorted(digits_3)):
                    done = 1
                    break
    if done:
        break
    n += 1

progress_.count = int(''.join([str(n), str(n + a), str(n + 2*a)]))
progress_.total = answers_list[49]
progress_.progress()

if __name__ == '__main__':
    input()
