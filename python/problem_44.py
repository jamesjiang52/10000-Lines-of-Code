if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 044: Pentagon numbers", 1, 2200) #arbitrary number for display purposes

pentagon_list = [1]
while True:
    pentagon_list.append(progress_.count*(3*progress_.count - 1)//2)
    for i in range(len(pentagon_list) - 1):
        sum_ =  pentagon_list[progress_.count] + pentagon_list[i]
        diff_ = pentagon_list[progress_.count] - pentagon_list[i]
        if is_pentagon(sum_) and is_pentagon(diff_):
            break
    else:
        progress_.count += 1
        if progress_.count % 11 == 0: #arbitrary number for display purposes
            progress_.progress()
        continue
    break

progress_.count = diff_
progress_.total = answers_list[44]
progress_.progress()

if __name__ == '__main__':
    input()
