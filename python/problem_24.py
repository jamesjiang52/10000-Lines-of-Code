import math

if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 024: Lexicographic permutations", 0, answers_list[24])

remaining_digits = list(range(10))
current = 999999
string = ''

for i in range(10):
    factorial_ = math.factorial(9 - i)
    index = current//factorial_
    string += str(remaining_digits[index])
    del remaining_digits[index]
    current = current % factorial_
    progress_.count = int(string)
    progress_.progress()

if __name__ == '__main__':
    input()
