# Finding all pythagorean triples such that the sum of the sides equals a
# specific integer can be done by using Euclid's general formula.
# Given a^2 + b^2 = c^2, a = k * (m^2 - n^2), b = k * (2 * m * n), c = k * (m^2 + n^2)

# Some basic algebra shows that letting s = a + b + c leads to
# s/2k = m * (m + n).
# So it becomes clear that finding integer solutions for m and n is really a
# factoring problem. As such, I choose p = m + n as a convenience. Since "a" must be
# positive, m > n. Since n = p - m, it is true that m > p - m by substitution;
# furthermore 2m > p. Also "b" must be positive, and therefore m + n > m, or
# p > m, by substitution. The whole point of this is now clarified by saving that
# we seek s/2k = m * p, where m and p are integers and 2m > p > m.

# So, supposing we're given an integer s for which we want all pythagorean
# triples whose values sum to s. Find an algorithm for exhaustively finding
# all possible triples. There may be some value in solving the slightly easier
# case of k = 1 frist. First, it's clear that s must at least be even, so reject it
# otherwise. If we focus on "m", we could use the integer square root function to
# choose an upper and lower bound on m. We can use the constraints to not be
# overly concerned with whether the bounds exactly capture the true range of candidates.
# As such, a lower bound for m is sqrt(s/4), and an upper bound is sqrt(s/2).
# With that range in mind, it's simply a matter of incrementing the values and
# checking for divisibility.

from prime import *
import sys

# Tested
def simpleTriplesWithSum(s):
    if s % 2 == 0:
        s_div_2 = s // 2
        lower = max(isqrt(s // 4), 1)
        upper = isqrt(s // 2)
        for m in xrange(lower, upper + 1):
            p = s_div_2 // m
            if p * m == s_div_2 and p > m and 2*m > p:
                n = p - m
                a = m*m - n*n
                b = 2*m*n
                c = m*m + n*n
                if a < b:
                    yield (a, b, c)
                else:
                    yield (b, a, c)

def allTriplesWithSum(s):
    triples = set()
    for d in xrange(1, (s // 2) + 1):
        if s % d == 0:
            for t in simpleTriplesWithSum(s // d):
                triple = (t[0]*d, t[1]*d, t[2]*d)
                if triple not in triples:
                    triples.add(triple)
    return triples

def solve(L):
    count = 0
    for i in xrange(12, L+1, 2):
        sys.stdout.write("Reviewing sum: {}\r".format(i))
        triples = allTriplesWithSum(i)
        if len(triples) == 1:
            count += 1
            #print "{} has exactly one triple: {}".format(i, triples.pop())
    print "\nTotal count: {}".format(count)

