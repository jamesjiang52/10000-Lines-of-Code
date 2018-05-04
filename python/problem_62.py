if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 062: Cubic permutations", 0, 600000000000)

dict_permutations = {}
dict_smallest = {}

n = 5
while True:
    digits_tuple = tuple(sorted([int(i) for i in str(n**3)]))
    if digits_tuple not in dict_permutations:
        dict_permutations[digits_tuple] = 1
        dict_smallest[digits_tuple] = n**3
        progress_.count = n**3
        progress_.progress()
    elif dict_permutations[digits_tuple] < 4:
        dict_permutations[digits_tuple] += 1
    else:
        #print(dict_smallest[digits_tuple])
        break
    n += 1

progress_.count = dict_smallest[digits_tuple]
progress_.total = answers_list[62]
progress_.progress()

if __name__ == '__main__':
    input()
