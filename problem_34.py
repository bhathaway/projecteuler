import math
import sys

base = math.log(10)

i = 1
#N = 10000
while i < int(sys.argv[1]):
    digits = []
    num_digits = int(math.floor(math.log(i)/base + 1))
    remainder = i
    for n in range(num_digits-1, -1, -1):
        digits.append(remainder / (10**n))
        remainder = remainder % (10**n)
    sum = 0
    for d in digits:
        sum += math.factorial(d)
    if sum == i:
        print i

    i += 1
