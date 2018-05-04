if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 008: Largest product in a series", 0, 	answers_list[8])

str_num = ''
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\data\\problem_8_data.txt') as f:
    for line in f:
        str_num += line.rstrip('\n')

for i in range(1, len(str_num) - 13):
    product_list = [int(str_num[i + j]) for j in range(13)]
    product = 1
    for j in product_list:
        product *= j
    progress_.count = max(progress_.count, product)
    progress_.progress()

if __name__ == '__main__':
    input()
