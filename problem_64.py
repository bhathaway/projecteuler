from fractions import *
import math
# I've reduced this problem to a set of sequences that influence each other:
# Three sequences, call them a, b, and d.

def reduceTuple(tup):
    g = gcd(gcd(tup[0], tup[1]), tup[2])
    return (tup[0]/g, tup[1]/g, tup[2]/g)

# The tuple tup is (a, b, d), and represents (a\/x + b)/d
# x is the value we're trying to find the root of.
# f is the floor of root x, which should be easy to find.
def getNextSequenceValues(f, x, tup):
    a = tup[0]
    b = tup[1]
    d = tup[2]
    next_a = a * d
    next_b = -b * d
    next_d = a*a*x - b*b

    estimate = Fraction(next_a*f + next_b, next_d)
    # Integer division.
    n = estimate.numerator/estimate.denominator
    next_b -= n * next_d
    return ( n, reduceTuple((next_a, next_b, next_d)) )

def getContinuedFractionForRoot(x):
    cycle_list = []
    f = int(math.floor(math.sqrt(x)))
    if f * f != x:
        tuple_set = set()

        t = (1, -f, 1)
        n = f
        while not t in tuple_set:
            tuple_set.add(t)
            (n, t) = getNextSequenceValues(f, x, t)
            cycle_list.append(n)

    return (f, cycle_list)


odd_cycle_count = 0
for i in range(1, 10001, 1):
    if len(getContinuedFractionForRoot(i)[1]) % 2:
        odd_cycle_count += 1
print odd_cycle_count
