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

def pandigitalPrimes(string, s):
    if len(s) == 0:
        number = int(string)
        if is_prime(number):
            return [number]
        else:
            return []
    else:
        result_list = []
        for e in s:
            test_string = str(string)
            test_string += e
            test_set = set(s)
            test_set.remove(e)
            result_list += pandigitalPrimes(test_string, test_set)
        return result_list

for i in range(2, 10):
    digit_bin = set()
    for k in range(1, i+1):
        digit_bin.add(str(k))
    print("pandigital primes (n = %d)" % i)
    print pandigitalPrimes("", digit_bin)

