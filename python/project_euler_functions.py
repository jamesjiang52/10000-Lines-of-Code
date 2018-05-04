import math
import numpy as np
import collections
import copy
import decimal
decimal.getcontext().prec = 58

def is_prime(x):
    """
    Checks if x is prime
    """
    if x <= 1:
        return False
    for i in range(2, round(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    else:
        return True

def factors(x):
    """
    Returns list of distinct factors of x
    """
    factors_list = []
    if x % 2 == 1:
        step = 2
    else:
        step = 1
    for i in range(1, round(math.sqrt(x)) + 1, step):
        if x % i == 0:
            if i**2 == x:
                factors_list.append(i)
            else:
                factors_list.extend([i, x//i])
    return(factors_list)

def prime_factors(x):
    """
    Returns list of prime factors of x, not necessarily distinct
    """
    out_list = []
    while x != 1:
        n = 2
        out_list_temp = []
        for n in range(2, x + 1):
            if x % n == 0:
                for i in range(2, round(math.sqrt(n)) + 2):
                    if (n % i == 0) and (n != i):
                        break
                else:
                    out_list_temp.append(n)
        for i in out_list_temp:
            x = int(x/i)
        out_list.extend(out_list_temp)
    out_list.sort()
    return(out_list)

def num_factors(x):
    """
    Returns number of distinct factors of x
    """
    return(len(factors(x)))

def num_prime_factors(x):
    """
    Returns number of distinct prime factors of x
    """
    prime_factors_list = [1 for j in factors(x) if is_prime(j)]
    return(len(prime_factors_list))

def sum_factors(x):
    """
    Returns sum of distinct factors of x, not including x itself
    """
    return(sum(factors(x)) - x)

def is_abundant(x):
    """
    Checks if the sum of distinct factors of x, not including x itself,
    is larger than x
    """
    return(sum_factors(x) > x)


def is_pandigital(x):
    """
    Checks if x contains all digits between 1 and 9 (inclusive) exactly once
    """
    digits = [int(i) for i in str(x)]
    digits.sort()
    return(digits == list(range(1, 10)))

def is_palindrome(string):
    """
    Checks if string is a palindrome
    """
    return(string == string[::-1])

def collatz(x):
    """
    Generates the next term of the Collatz sequence, given the previous term x
    """
    if x % 2 == 0:
        return(x//2)
    else:
        return(3*x + 1)

def written(x):
    """
    For x >= 0 and x <= 1000, returns the number of letters required to
    write out x in words
    """
    total_letters = 0
    if x == 1000:
        return(11)
    elif x in range(10, 20):
        if x == 10:
            return(3)
        elif x in [11, 12]:
            return(6)
        elif x in [13, 14, 18, 19]:
            return(8)
        elif x in [15, 16]:
            return(7)
        elif x == 17:
            return(9)
    elif x in range(0, 10):
        if x in [1, 2, 6]:
            return(3)
        elif x in [4, 5, 9]:
            return(4)
        elif x in [3, 7, 8]:
            return(5)
        else:
            return(0)
    elif x in range(20, 100):
        if int(str(x)[0]) in [2, 3, 8, 9]:
            total_letters += 6
        elif int(str(x)[0]) in [4, 5, 6]:
            total_letters += 5
        else:
            total_letters += 7
        total_letters += written(int(str(x)[1]))
        return(total_letters)
    else:
        total_letters += 7
        total_letters += written(int(str(x)[0]))
        total_letters += written(int(str(x)[1:]))
        if str(x)[1:] != '00':
            total_letters += 3
        return(total_letters)

def score(letter):
    """
    Returns index of letter in alphabet e.g. A -> 1, B -> 2, ...
    """
    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return(string.index(letter) + 1)

def fib(x):
    """
    Returns the xth term of the Fibonacci sequence
    """
    a, b = 1, 1
    for i in range(1, x):
        a, b = b, a + b
        x += 1
    return(a)

def recurring_decimals_length(x):
    """
    Returns the cycle length of the reciprocal of x,
    if x is a prime number with more than one digit
    """
    k = 9
    while True:
        if k % x == 0:
            return(len(str(k)))
            break
        k = 10*k + 9

def coin_solutions(total, coin_index):
    """
    Returns the number of ways the total amount can be made,
    with the coin at coin_index being the largest available coin value
    """
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    if coin_index == 0:
        return(1)
    else:
        num_solutions = 0
        while total >= 0:
            num_solutions += coin_solutions(total, coin_index - 1)
            total -= coins[coin_index]
        return(num_solutions)

def arrangements(x):
    """
    Returns list of the circular arrangements of the digits of x
    """
    output_list = []
    circular = collections.deque(str(x))
    for i in range(len(circular)):
        output_list.append(int(''.join(list(circular))))
        circular.rotate(1)
    return(output_list)

def is_digits_divisible(x):
    """
    Checks if any digit of x is 0, 2, 4, 5, 6, or 8
    In other words, returns False when x only contains 1, 3, 7, and 9
    """
    if len(str(x)) == 1:
        return False
    allowable = [0, 2, 4, 5, 6, 8]
    for digit in str(x):
        if int(digit) in allowable:
            return True
    else:
        return False

def is_triangle(x):
    """
    Checks if x is a triangle number
    """
    n = (-1 + math.sqrt(8*x + 1))/2
    return(n == round(n))

def is_square(x):
    """
    Checks if x is a square number
    """
    n = math.sqrt(x)
    return(n == round(n))

def is_pentagon(x):
    """
    Checks if x is a pentagon number
    """
    n = (1 + math.sqrt(24*x + 1))/6
    return(n == round(n))

def is_hexagon(x):
    """
    Checks if x is a hexagon number
    """
    n = (1 + math.sqrt(8*x + 1))/4
    return(n == round(n))

def is_heptagon(x):
    """
    Checks if x is a heptagon number
    """
    n = (3 + math.sqrt(40*x + 9))/10
    return(n == round(n))

def is_octagon(x):
    """
    Checks if x is an octagon number
    """
    n = (1 + math.sqrt(3*x + 1))/3
    return(n == round(n))

def truncate(x):
    """
    Returns list of numbers produced by truncating consecutive digits of x
    """
    numbers = [x]
    for i in range(1, len(str(x))):
        numbers.extend([x % 10**i, x//10**i])
    return(numbers)

def analyze_hand(hand_values, hand_suits):
    """
    Returns rank of hand, according to standard poker rules
    """
    hand_values.sort()
    diffs = [hand_values[i + 1] - hand_values[i] for i in range(len(hand_values) - 1)]
    checker = hand_suits[0]
    if all(i == 1 for i in diffs) and all(i == checker for i in hand_suits) and (max(hand_values) == 14):
        return([24, 0]) #royal flush
    if all(i == 1 for i in diffs) and all(i == checker for i in hand_suits):
        return([23, 0]) #straight flush
    if diffs.count(0) == 3:
        if diffs[0] == diffs[-1]:
            return([21, 0]) #full house
        else:
            return([22, hand_values[diffs.index(0)]]) #four of a kind
    if all(i == checker for i in hand_suits):
        return([20, 0]) #flush
    if diffs.count(0) == 2:
        if diffs[diffs.index(0) + 1] == 0:
            return([18, hand_values[diffs.index(0)]]) #three of a kind
        else:
            return([17, 0]) #two pairs
    if diffs.count(0) == 1:
        return([16, hand_values[diffs.index(0)]]) #one pair
    if all(i == 1 for i in diffs):
        return([19, 0]) #straight
    return([max(hand_values), 0])

def fraction_expansion_sqrt_2(x):
    """
    Returns a list containing the lengths of the numerator and denominator
    of the x-th continued fraction expansion of sqrt(2)
    """
    numerator = 1
    denominator = 2
    for i in range(x - 1):
        numerator += 2*denominator
        numerator, denominator = denominator, numerator
    numerator += denominator
    return([math.floor(math.log(numerator, 10)) + 1, math.floor(math.log(denominator, 10)) + 1])

def sum_numerator_fraction_expansion_e(x):
    """
    Returns the digit sum of the numerator of the x-th continued fraction of e
    """
    numerator = 1
    if x % 3 == 2:
        denominator = 2*(x//3 + 1)
    else:
        denominator = 1
    while x > 1:
        if x % 3 == 0:
            numerator += 2*(x//3)*denominator
        else:
            numerator += denominator
        numerator, denominator = denominator, numerator
        x -= 1
    numerator += 2*denominator
    digits = [int(i) for i in str(numerator)]
    return(sum(digits))


def len_fraction_expansion_sqrt_period(x):
    """
    Returns the period length of the continued fraction expansion of sqrt(x)
    """
    a_0 = math.floor(math.sqrt(x))
    b = a_0
    c = x - a_0**2
    len_ = 1
    seen = [[b, c]]
    while True:
        a = math.floor((a_0 + b)/c)
        b = int(a*c - b)
        c = int((x - b**2)/c)
        if [b, c] in seen:
            return(len_)
        seen.append([b, c])
        len_ += 1

def fraction_expansion_sqrt(x, n):
    """
    Returns a list containing the numerator and denominator of the n-th
    continued fraction expansion of sqrt(x)
    """
    current = decimal.Decimal(x).sqrt()
    int_ = math.floor(current)
    remainders = []
    for i in range(len_fraction_expansion_sqrt_period(x)):
        current = 1/(current - int_)
        int_ = math.floor(current)
        remainders.append(int_)
    len_ = len(remainders)
    numerator = 1
    index_ = n % len_
    index_next = (index_ - 1) % len_
    denominator = remainders[index_]
    for i in range(n):
        numerator += remainders[index_next]*denominator
        numerator, denominator = denominator, numerator
        index_next = (index_next - 1) % len_
    numerator += denominator*math.floor(math.sqrt(x))
    return([numerator, denominator])

def minimal_solution(D):
    """
    Returns the minimum value of x that satisfies x**2 - D*y**2 = 1
    """
    n = 0
    while True:
        fraction = fraction_expansion_sqrt(D, n)
        if fraction[0]**2 - D*fraction[1]**2 == 1:
            return(fraction[0])
        n += 1

def increment(string):
    """
    Increments a string of letters e.g. aaa -> aab, aza -> baa, ...
    """
    letters = list('abcdefghijklmnopqrstuvwxyz')
    if string[-1] != 'z':
        chars = [char for char in string]
        chars[-1] = letters[letters.index(chars[-1]) + 1]
        return(''.join(chars))
    else:
        return(increment(string[:-1]) + 'a')

def is_prime_concatenatable(prime_list):
    """
    Checks if all pairs of primes in prime_list concatenated together
    in any order creates another prime, given that
    check_prime_concatenatable(prime_list[:-1]) == True
    """
    for i in range(len(prime_list) - 1):
        new_prime1 = int(str(prime_list[i]) + str(prime_list[-1]))
        new_prime2 = int(str(prime_list[-1]) + str(prime_list[i]))
        if not is_prime(new_prime1) or not is_prime(new_prime2):
            return False
    return True

def find_cycle(num_lists, first_pair, last_pair, total):
    """
    Checks if an element of a list in num_lists has the property that its
    first two digits match last_pair. If such an element exists, the list is
    removed from num_lists and the last two digits of that number becomes the
    next digits to check. The number is added to the total. The function is
    recursively called until the length of num_lists is one. If an element in
    that list has the property that its first two digits match last_pair and
    its last two digits match first_pair, the total is returned.
    """
    if (len(num_lists) == 1) and (100*last_pair + first_pair in num_lists[0]):
        for num in num_lists[0]:
            if (num//100 == last_pair) and (num % 100 == first_pair):
                return(total + num)
    for num_list in num_lists:
        for num in num_list:
            if num//100 == last_pair:
                num_lists_copy = copy.deepcopy(num_lists)
                num_lists_copy.remove(num_list)
                if find_cycle(num_lists_copy, first_pair, num % 100, total + num):
                    return(find_cycle(num_lists_copy, first_pair, num % 100, total + num))
    else:
        return None

def choose(n, r):
    """
    Returns the value of nCr
    """
    if r > n//2 + 1:
        r = n - r
    numerator = 1
    denominator = 1
    for i in range(n, n - r, -1):
        numerator *= i
        denominator *= (n - i + 1)
    return(numerator//denominator)

def reverse_and_add(x):
    """
    Returns the sum of x and y, where y is formed by reversing the digits of x
    """
    return(x + int(str(x)[::-1]))

def totient(x):
    """
    Returns the value of the Euler's Totient function of x
    """
    if is_prime(x):
        return(x - 1)
    p = 1
    for i in list(set(prime_factors(x))):
        p *= (i - 1)/i
    return(int(x*p))

def sum_factorial_digits(x):
    """
    Returns the sum of the factorials of the digits of x
    """
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    sum_factorial_digits_ = 0
    for i in str(x):
        sum_factorial_digits_ += factorials[int(i)]
    return(sum_factorial_digits_)

def count_triangles(p):
    """
    Returns the number of integer right triangles with perimeter p
    """
    count = 0
    for a in range(1, p//4 + 1):
        c = (a**2 + (p - a)**2)//(2*(p - a))
        remainder = (a**2 + (p - a)**2) % (2*(p - a))
        b = p - a - c
        if (remainder == 0) and (a <= b < c):
            count += 1
    return(count)

def angle_subtend(vector1, vector2):
    """
    Returns the angle subtended by the two points with position vectors vector1
    and vector2 with respect to the origin
    """
    cos_ = np.dot(vector1, vector2)/(np.linalg.norm(vector1)*np.linalg.norm(vector2))
    return(math.acos(cos_))
