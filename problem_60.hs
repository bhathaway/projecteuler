-- We're looking for prime pair sets of size five and grading them by the sum of all primes in the set.
-- Turns out this problem has a lot of substructure we can find a way to take advantage of. Specifically,
-- all subsets of prime pair sets are also prime pair sets. Seems pretty obvious, but the point is we
-- might be able to build up a structure by successively adding prime numbers, and generating rank 2 sets,
-- then rank 3 sets, etc. until a certain rank has no sets. Now, certainly if there are no rank n prime sets
-- over a set of primes, then there are also no n+1 prime sets, because the existence of a rank n+1 prime set
-- implies that n+1 rank n prime sets exist.

-- Whenever we add a new greatest prime to the frontier, any new minimal sum set we find will have to be
-- at least that prime. So, once we find a prime set of sum m for some maximal prime k < m, we set the new
-- maximum prime limit as m.

-- There are some additional results. 2 can never be part of a prime pair set, so all primes will be odd.
-- This might help when considering the maximal sum values. The sum of five odds will be odd, so we could
-- use that to cut the space in half.

primeHelper :: Integer -> Integer -> Bool
primeHelper number current_divisor
    | current_divisor * current_divisor <= number =
        if rem number current_divisor == 0 then False else primeHelper number (current_divisor + 1)
    | otherwise = True

prime :: Integer -> Bool
prime number
    | number < 2 = False
    | otherwise = primeHelper number 2

-- prime is expensive, so only pass in primes for this test
isConcatPrimePair :: Integer -> Integer -> Bool
isConcatPrimePair n1 n2 =
    let concatNum x y = (read $ concat [show x, show y]) in
        (prime $ concatNum n1 n2) && (prime $ concatNum n2 n1)
