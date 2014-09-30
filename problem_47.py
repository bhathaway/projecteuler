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

distinct_primes = [1, 1, 1, 1]

n = 647

still_checking = True

while still_checking:
    distinct_primes[0] = distinct_primes[1]
    distinct_primes[1] = distinct_primes[2]
    distinct_primes[2] = distinct_primes[3]
    s = set(prime_factors(n))
    distinct_primes[3] = len(s)
    if distinct_primes[0] > 3 and distinct_primes[1] > 3 and distinct_primes[2] > 3 and distinct_primes[3] > 3:
        still_checking = False
        print(n)
    else:
        n += 1

