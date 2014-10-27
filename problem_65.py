from fractions import *

def rec(x):
    return Fraction(1, x)

def nth_e(n):
    if n % 3 == 0:
        return 2 * n / 3
    else:
        return 1

def e_expr(n):
    result = "2"
    for i in range(2, n, 1):
        result += '+rec(' + repr(nth_e(i))
    for i in range(2, n, 1):
        result += ')'
    return result

