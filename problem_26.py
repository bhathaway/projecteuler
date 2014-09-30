
def prime_factors(n):
    factors = []
    d = 2
    while n != 1:
        if n % d != 0:
            d = d + 1
        else:
            factors.append(d)
            n = n / d

    return factors

def cycle(i):
    factors = prime_factors(i)
    # Filter out all 2s and 5s

    i = 1
    for p in factors:
        if p != 2 and p != 5:
            i = i * p

    if i == 1:
        return 0

    digits = 1
    n = 9
    while n % i != 0:
        n = n * 10 + 9
        digits = digits + 1
    return digits

max_cycle = 0
max_d = 0
for d in range(1, 1001):
    c = cycle(d)
    if c > max_cycle:
        max_cycle = c
        max_d = d
    print("%i: %i" % (d, c))

print("Max cycle divisor: %i" % max_d)
