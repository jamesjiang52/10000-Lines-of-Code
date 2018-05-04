if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 036: Double-base palindromes", 0, answers_list[36])

for i in range(1, 1000000, 2):
    if (is_palindrome(str(i))) and (is_palindrome(bin(i)[2:])):
        progress_.count += i
        progress_.progress()

if __name__ == '__main__':
    input()
