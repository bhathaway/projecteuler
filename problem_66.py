import math
from fractions import *

# For the purposes of this problem, a continued fraction is
# assumed to repeat terms 
class SimpleContinuedFraction:
    def __init__(self, l):
        self.a0 = l[0]
        self.terms = l[1:]

    def getConvergent(self, n):
        if n == 0:
            return self.a0
        else:
            s = 0
            for i in xrange(n, 0, -1):
                s = Fraction(1, s + self.terms[(i-1) % len(self.terms)])

            return s + self.a0

    def __str__(self):
        result = "[{}; ".format(self.a0)
        for i in xrange(len(self.terms) - 1):
            result += "{},".format(self.terms[i])
        result += "{}]".format(self.terms[-1])
        return result

    def __repr__(self):
        return self.__str__()

# Integer root function, returns largest approximation not greater than
# the true root
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def continued_fraction_root(N):
    m0 = 0
    d0 = 1
    a0 = isqrt(N)
    m_next = d0*a0 - m0
    d_next = (N - m_next*m_next) // d0
    an = (a0 + m_next) // d_next
    
    result = [a0, an]
    
    while an != 2*a0:
        m_prev = m_next
        d_prev = d_next
        a_prev = an
        m_next = d_prev * a_prev - m_prev
        d_next = (N - m_next*m_next) // d_prev
        an = (a0 + m_next) // d_next
        result.append(an)

    return result

def isSquare(x):
    sq_rt = isqrt(x)
    return sq_rt * sq_rt == x


def solve():
    max_x = 0
    max_D = 0

    for D in range(2, 1001, 1):
        if isSquare(D):
            continue
        print "-------------- D: {} --------------".format(D)
        continued_frac = SimpleContinuedFraction(continued_fraction_root(D))
        r = len(continued_frac.terms) - 1

        if r % 2 != 0:
            # r is odd. Look at p sub r
            c = continued_frac.getConvergent(r)
            x = c.numerator
            y = c.denominator
        else:
            # r is even, look at p sub 2*r + 1
            c = continued_frac.getConvergent(2*r + 1)
            x = c.numerator
            y = c.denominator
        print("D = %i, smallest x is %i" % (D, x))

        assert(x*x == D*y*y + 1)

        if x > max_x:
            max_D = D
            max_x = x


    print("D = %i with x = %i" % (max_D, max_x))

solve()
