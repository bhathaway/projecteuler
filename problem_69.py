import sys
from prime import are_relatively_prime

# The naive implementation of totient is too slow,
# but a pattern emerged that helped me solve this problem by hand.
# The most "uncooperative" composites seem to be exactly the
# product of sequential primes. So, f(x) = n / phi(n) peaks at
# 2, 2*3, 2*3*5, 2*3*5*7, 2*3*5*7*11, etc.
# Having said that, it would be nice to actually prove that this
# is true, mathematically.

def totient(n):
    s = 0
    for i in xrange(1, n):
        if are_relatively_prime(i, n):
            s += 1
    return s

def solve():
    r = 1.0
    max_n = 1
    for n in xrange(2, 1000001):
        sys.stdout.write("n: {}\r".format(n))
        new_r = float(n) / totient(n)
        if new_r > r:
            r = new_r
            max_n = n
            print "Highest n so far: {}".format(max_n)

    print max_n

