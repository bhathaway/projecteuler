def lower_factors(n):
    result = []
    d = 1
    r = n
    more_factors = True
    while more_factors:
        if r * d == n:
            result.append(d)
        d += 1
        r = n / d
        more_factors = r > d
    return result

def is_triangle(n):
    number = 2*n
    v = lower_factors(number)
    factor = v[-1]
    if (number/factor)-factor == 1:
        return True
    else:
        return False

def is_pentagonal(n):
    number = 2*n
    v = lower_factors(number)
    result = False
    v.reverse()
    for factor in v:
        if 3*factor - 1 == number/factor:
            result = True
            break
    return result

def is_hexagonal(n):
    v = lower_factors(n)
    result = False
    v.reverse()
    for factor in v:
        if 2*factor - 1 == n/factor:
            result = True
            break
    return result

# The above is fun, but terribly inefficient

def nextTriangular():
    n = 286
    while True:
        yield n * (n + 1) / 2
        n += 1

def nextPentagonal():
    n = 165
    while True:
        yield n * (3 * n - 1) / 2
        n += 1

def nextHexagonal():
    n = 143
    while True:
        yield n * (2 * n - 1)
        n += 1

# Hexagonal number are the dominating series.
p_iter = nextPentagonal()
t_iter = nextTriangular()
p = p_iter.next()
t = t_iter.next()
for n in nextHexagonal():
    while p < n:
        p = p_iter.next()
    while t < n:
        t = t_iter.next()

    if n == p and n == t:
        print(n)
        break

