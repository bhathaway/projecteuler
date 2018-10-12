import math
import sys

def sumOfDigitFactorials(n):
    literal = str(n)
    sum = 0
    for c in literal:
        sum += math.factorial(int(c))
    return sum

LIMIT=1000000

sixty_count = 0
for i in xrange(1, LIMIT):
    sys.stdout.write("i: {}\r".format(i))
    val = i
    cycle_set = set()
    while val not in cycle_set:
        cycle_set.add(val)
        val = sumOfDigitFactorials(val)

    if len(cycle_set) == 60:
        print "Wow, 60!"
        sixty_count += 1

print "Total: {}".format(sixty_count)
