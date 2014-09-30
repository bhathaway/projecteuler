# The complete generator for pythagorean triples is k*(m^2+n^2), 2*k*m*n, k*(m^2-n^2), where
# m > n. Distinct ordered triples (k, m, n) do not generate unique solutions. Interestingly,
# the sum of the three sides in this generalized form is quite factorable, to
# 2*k*m*(m+n). The first thing to note is that 2 must be a factor of any perimeters, so we may
# as well simply consider k*m*(m+n). Now, how can we restrict the values we consider for k, m, and
# n? Well, k is implicitly unrestricted, but we must choose m such that the remaining factors, say
# their product is 'r', are such than r-m < m. This can be simplified to r < 2m. But also, r > m,
# otherwise n is non-positive.

# It might be instructive to do an example by hand to show the process..
# Say p = 120. Then we consider p/2 = 60 and its factors. The prime factors of 60 are
# 2*2*3*5.

# Let's try k = 1. That leaves the full 60 to m and r. Suppose m=1, then r=60 fails. Suppose
# m=2, then r=30 fails. Suppose m=3, then r=20 fails. Suppose m=4, then r=15 fails. Suppose
# m=5, then r=12 fails. Suppose m=6, then r=10 is possible. This is, in fact, the last possibilty
# with k=1. (k, m, n) = (1, 6, 4) => [48, 20, 52]

# Let's choose k = 2. Then we have 2*3*5 to redistribute to m and r. If we choose m=2, then
# r = 15 which is greater than 2*m, so that's out. Next we try m=3, then r=10, still greater
# than 2*m. Moving on to m=5, then r=6, which works, with n=1. (2, 5, 1) => [20, 48, 52]. With
# n = 1, we can stop, knowing that further searches will result in smaller n. This example was
# rather illustrative, because (2, 5, 1) = (1, 6, 4). So it will be important to make the ordering
# of a and b irrelevant.

# Let's try out k = 3. Then we have 2*2*5 to play with. I'm beginnig to see it should be better to
# start the pairs as close to sqrt as possible and decrement m, actually. So let's choose m=4, r=5.
# This works, with n=1, So (3, 4, 1) => [24, 45, 51]. Cool. Decrement m to the next lowest factor.
# That's 2. m=2, r=20 violate r<2m, no go.

# Ok, on to k=4. 3*5 remains, with m=3, r=5 leads to (4, 3, 2) => [20, 48, 52]. Wow, another repeat!
# Well, does m=1 work, no. Moving on.

# k=5. 2*2*3 remains. Let's try m=3, r=4. That's (5, 3, 1) => [40, 30, 50]. Ok. That's new. What about
# m=2, r=6. Nope.

# k=6. m=2, r=5, Fail.

# k=10. m=2, r=3. Ok. (10, 2, 1) => [30, 40, 50]. Seen that one.

# k=12. Only 1 and 5 remain, no sol.

# k=15. 1 and 4 fails, 2 and 2 fails.

# k=20. 1 and 3 fails.

# k=30. 1 and 2 fails. That's a boundary case. Remember r must be strictly less than 2*m.

# k=60. Well, we could probably never check this case.

# So, going through manually, we saw 6 results, each a duplicate for 3 unique solutions.


# Now, considering this problem only needs to find the most solutions for p <= 1000, I don't need to make
# the lower factors algothim very sophisticated..

def full_factors(n):
    lower = []
    upper = []
    d = 1
    r = n
    more_factors = True
    while more_factors:
        if r * d == n:
            lower.append(d)
            if r != d:
                upper.insert(0, r)
        d += 1
        r = n / d
        more_factors = r >= d
    return lower + upper

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

def unique_triples_for_perimeter(p):
    result_set = set()
    if p % 2 != 0:
        return result_set

    for k in full_factors(p/2):
        remaining = (p/2)/k
        lower = lower_factors(remaining)
        lower.reverse()
        for m in lower:
            r = remaining / m
            n = r - m
            if n > 0 and n < m:
                # There should be a solution here.
                a = k * (m*m - n*n)
                b = k * 2 * m * n
                c = k * (m*m + n*n)
                if a < b:
                    result_set.add((a, b, c))
                else:
                    result_set.add((b, a, c))
            else:
                break

    return result_set

largest_count = 0
largest_count_i = 0
for i in range(1, 1001):
    s = unique_triples_for_perimeter(i)
    l = len(s)
    if l > largest_count:
        largest_count = l
        largest_count_i = i
        print(s)

print("The perimeter less than 1001 with the largest number of solutions is: %d" % largest_count_i)
