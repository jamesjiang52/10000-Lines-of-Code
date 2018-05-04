if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 019: Counting Sundays", 0, answers_list[19])

thirty_months = [4, 6, 9, 11]
counter = 4*30 + 7*31 + 28
for year in range(1901, 2001):
    for month in range(1, 13):
        if month in thirty_months:
            counter += 30
        elif month != 2:
            counter += 31
        else:
            if year % 4 == 0:
                if year % 100 != 0:
                    counter += 29
                elif year % 400 == 0:
                    counter += 29
                else:
                    counter += 28
            else:
                counter += 28
        if counter % 7 == 6:
            progress_.count += 1
            progress_.progress()

if __name__ == '__main__':
    input()
