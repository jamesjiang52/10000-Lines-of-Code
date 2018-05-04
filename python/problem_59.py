if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from functions import *

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 059: XOR decryption", 0, 26**3 - 1)

with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\data\\problem_59_data.txt') as f:
    string = f.readline()
    nums = string.split(',')
    nums_int = [int(i) for i in nums]

key = 'aaa'

with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\data\\problem_59_output.txt', 'w') as f:
    for i in range(26**3 - 1):
        progress_.count = i
        progress_.progress()
        key_nums = [ord(i) for i in key]
        new_nums = []
        for j in range(len(nums_int)):
            new_nums.append(key_nums[j % 3] ^ nums_int[j])
        new_chars = [chr(j) for j in new_nums]
        new_string = ''.join(new_chars)
        if new_string.count(' ') > 120:
            f.write(str(sum(new_nums)) + '   ' + new_string + '\n')
        key = increment(key)

progress_.count = answers_list[59]
progress_.total = answers_list[59]
progress_.progress()

if __name__ == '__main__':
    input()

"""
Answer: key == 'god', sum == 107359 (from text file)
"""
