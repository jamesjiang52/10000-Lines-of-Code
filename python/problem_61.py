if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))

all_functions = [is_triangle, is_square, is_pentagon, is_hexagon, is_heptagon, is_octagon]

all_triangles = []
all_squares = []
all_pentagons = []
all_hexagons = []
all_heptagons = []
all_octagons = []
all_nums = [all_triangles, all_squares, all_pentagons, all_hexagons, all_heptagons, all_octagons]

for i in range(1000, 10000):
    for j in range(6):
        if all_functions[j](i):
            all_nums[j].append(i)

progress_ = Progress("Problem 061: Cyclical figurate numbers", 0, len(all_triangles))

for triangle in all_triangles:
    progress_.count += 1
    progress_.progress()
    if find_cycle(all_nums[1:], triangle//100, triangle % 100, triangle):
        break

progress_.count = find_cycle(all_nums[1:], triangle//100, triangle % 100, triangle)
progress_.total = answers_list[61]
progress_.progress()

if __name__ == '__main__':
    input()
