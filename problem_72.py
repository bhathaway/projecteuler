from prime import *
import sys

# This problem boils down to the sum of Euler's totient over the integers.

s = 0
LIMIT = 1000001

upgrade_primes(LIMIT)

for i in xrange(2, LIMIT):
    sys.stdout.write('i: {}\r'.format(i))
    s += totient(i)

print "Total: {}".format(s)

