from prime import is_prime

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
    print("Generating for n = {}".format(i))
    primes = pandigitalPrimes("", digit_bin)
    if len(primes) != 0:
        print "Maximum: {}".format(max(primes))
