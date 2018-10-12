from prime import *
from fractions import *

LIMIT = 1000001
#LIMIT = 20
f = Fraction(3, 7)

max_f = 0

# Looking at the output, it looks like there is a regular pattern
# in the data, the ones digits of the numberators in increasing
# maxima follow the pattern 8 | 2 9 6 3 0 7 4 1 8 5 | 2 9 6 3 0 7 4 1 8 5 | 2 9 6 3 0 7 4 1 8 5 | 2 9
# Based on this pattern, I found the largest denominator of the form
# 7n + 5. It would be nice to prove all this, of course.
for c in xrange(999997, LIMIT):
    start = Fraction(3*c, 7)
    for n in xrange(int(start), 0, -1):
        if are_relatively_prime(n, c):
            candidate_f = Fraction(n, c)
            if candidate_f > max_f:
                max_f = candidate_f
                print "Largest f so far: {}".format(max_f)

print "Largest f less than 3/7: {}".format(max_f)

