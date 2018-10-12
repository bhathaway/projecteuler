from prime import *
import sys
import math

LIMIT = 12001

s = 0
for d in xrange(4, LIMIT):
    sys.stdout.write("d: {}\r".format(d))
    x1 = int(math.ceil(float(d) / 3.0))
    x2 = int(math.floor(float(d) / 2.0))
    for n in xrange(x1, x2+1):
        if are_relatively_prime(n, d):
            s += 1

print "Total: {}".format(s)

