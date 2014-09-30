import math

def is_prime(n):
    if n < 2:
        return False

    d = 2
    r = n / d
    while r >= d:
        if r * d == n:
            return False
        else:
            d += 1
            r = n / d

    return True

def is_composite(n):
    return not is_prime(n)

def is_twice_square_plus_prime(n):
    for i in range(2, n):
        if is_prime(i):
            diff = n - i
            if diff % 2 == 0:
                diff /= 2
                s = int(math.sqrt(diff))
                if s*s == diff:
                    return True
    return False

n = 2
while True:
    if n % 2 == 1 and is_composite(n) and not is_twice_square_plus_prime(n):
        print(n)
        break
    else:
        n += 1

