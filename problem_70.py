from prime import *
import sys

def isPermutation(m, n):
    a = list(str(m))
    b = list(str(n))
    a.sort()
    b.sort()
    return a == b

LIMIT = 10**7+1
print "Creating prime table."
upgrade_primes(LIMIT)

# Even though I've improved the factoring algorthim by providing a list
# of primes, this function still takes a very long time to run. I think
# the lesson here is that some problems are just plain hard.
def solve():
    min_r = None
    min_n = None
    for n in xrange(2, LIMIT):
        sys.stdout.write("n: {}\r".format(n))
        t = totient(n)
        if isPermutation(n, t):
            r = float(n) / t
            if min_r != None:
                if r < min_r:
                    min_r = r
                    min_n = n
                    print("min n so far: {}".format(n))
            else:
                min_r = r
                min_n = n

    print min_n

solve()

