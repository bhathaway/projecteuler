def is_prime(n):
    if n < 2:
        return False

    d = 2
    q, r = divmod(n, d)
    while q >= d:
        if r == 0:
            return False
        else:
            d += 1
            q, r = divmod(n, d)

    return True

def is_composite(n):
    return not is_prime(n)

def prime_factors(n):
    factors = []
    d = 2
    while n != 1:
        if n % d != 0:
            d += 1
        else:
            factors.append(d)
            n //= d

    return factors

def are_relatively_prime(m, n):
    d = 2
    while n != 1:
        if m % d == 0 and n % d == 0:
            return False
        elif m % d != 0:
            m //= d
        elif n % d != 0:
            n //= d

    return True

