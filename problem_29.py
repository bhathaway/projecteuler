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

x = set()

for a in range(2, 101):
    for b in range(2, 101):
        x.add(a ** b)

print len(x)
