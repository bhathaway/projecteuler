import math

# Assume v is in order
def nth_permutation(v, n):
    x = list(v)
    s = len(v)
    result = []
    for i in range(s):
        factor = math.factorial(s-i-1)
        index = n / factor
        result.append(x.pop(index))
        n = n - index*factor

    return result
