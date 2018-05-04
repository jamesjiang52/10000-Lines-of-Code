if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 011: Largest product in a grid", 0, answers_list[11])

all_lines = [line.strip('\n') for line in open('C:\\Users\\James Jiang\\Documents\\Project Euler\\data\\problem_11_data.txt')]
all_rows = []
for line in all_lines:
    row = line.split(' ')
    all_rows.append([int(i) for i in row])

def product_horizontal(x, y):
    return(all_rows[y][x]*all_rows[y][x + 1]*all_rows[y][x + 2]*all_rows[y][x + 3])

def product_vertical(x, y):
    return(all_rows[y][x]*all_rows[y + 1][x]*all_rows[y + 2][x]*all_rows[y + 3][x])

def product_diagonal_forward(x, y):
    return(all_rows[y][x]*all_rows[y + 1][x + 1]*all_rows[y + 2][x + 2]*all_rows[y + 3][x + 3])

def product_diagonal_backward(x, y):
    return(all_rows[y][x]*all_rows[y + 1][x - 1]*all_rows[y + 2][x - 2]*all_rows[y + 3][x - 3])

for y_position in range(20):
    for x_position in range(20):
        if x_position < 17:
            progress_.count = max(progress_.count, product_horizontal(x_position, y_position))
            progress_.progress()
        if y_position < 17:
            progress_.count = max(progress_.count, product_vertical(x_position, y_position))
            progress_.progress()
        if (x_position < 17) and (y_position < 17):
            progress_.count = max(progress_.count, product_diagonal_forward(x_position, y_position))
            progress_.progress()
        if (x_position > 2) and (y_position < 17):
            progress_.count = max(progress_.count, product_diagonal_backward(x_position, y_position))
            progress_.progress()

if __name__ == '__main__':
    input()
