if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 055: Lychrel numbers", 0, answers_list[55])

for num in range(10, 10000):
    num_next = reverse_and_add(num)
    counter = 1
    while (counter < 50) and not is_palindrome(str(num_next)):
        num_next = reverse_and_add(num_next)
        counter += 1
    if counter == 50:
        progress_.count += 1
        progress_.progress()

if __name__ == '__main__':
    input()
