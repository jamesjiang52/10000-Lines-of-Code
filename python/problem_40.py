if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 040: Champernowne's constant", 0, answers_list[40])

number = ''
a = 1
while len(number) < 1000000:
    number += str(a)
    a += 1

progress_.count = int(number[0])*int(number[9])*int(number[99])*int(number[999])*int(number[9999])*int(number[99999])*int(number[999999])
progress_.progress()

if __name__ == '__main__':
    input()
