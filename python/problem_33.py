import fractions

if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler')

from progress import Progress
answers_list = ['dummy']
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\answers.txt') as answers:
    for line in answers:
        answers_list.append(int(line))
progress_ = Progress("Problem 033: Digit cancelling fractions", 0, 1000)

product_numerator = 1
product_denominator = 1
for a in range(1, 10):
    for b in range(a, 10):
        for c in range(1, 10):
            progress_.count = a*b*c
            progress_.progress()
            num1_digits = [str(a), str(b)]
            num2_digits = [str(b), str(c)]
            num1 = ''.join(num1_digits)
            num2 = ''.join(num2_digits)
            if (int(num1)/int(num2) == a/c) and (a != b):
                product_numerator *= int(num1)
                product_denominator *= int(num2)

a = fractions.Fraction(product_numerator, product_denominator)

progress_.count = a.denominator
progress_.total = answers_list[33]
progress_.progress()

if __name__ == '__main__':
    input()
