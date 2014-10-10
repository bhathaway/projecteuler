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



import Data.List
import Data.Set

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

-- If I'm right, we won't actually even need this function.
isConcatPrimeSet :: [ Integer ] -> Bool
isConcatPrimeSet x =
    let isConcatPrimeOrderedPair (a, b) = isConcatPrimePair a b in
        all isConcatPrimeOrderedPair [(i, k) | i <- x, k <- x, i < k]

primePairsLteN :: Integer -> [ ( Integer, Integer)  ]
primePairsLteN x =
    [(i, k) | i <- [3,5 .. x], k <- [3,5 .. x], i < k, prime i, prime k, isConcatPrimePair i k]

-- Through experimentation, I've managed to conclude that this problem is equivalent to
-- the maxmimal clique problem, an NP-complete problem. I did, however, find a good formulation
-- of an algorithm to solve it, which I will translate here.

type Vertex = Integer

class Graph g where
    vertices    :: g -> [ Vertex ]
    connected   :: g -> Vertex -> Vertex -> Bool

data PrimePairGraph = PrimePairGraph { vertex_list :: [ Vertex ], edges :: Set (Vertex, Vertex) }

instance Graph PrimePairGraph where
    vertices g      = vertex_list g
    connected g a b = member (a, b) (edges g)

type Clique = [ Vertex ]
biggestCliques :: Graph g => g -> [ Clique ]
biggestCliques g = bk [] (vertices g) []  -- initial state
    where
        bk :: Clique -> [ Vertex ] -> [ Vertex ] -> [ Clique ]
        bk compsub cand excl =
            if Data.List.null cand && Data.List.null excl then [compsub]
                else loop cand excl
            where
                loop :: [ Vertex ] -> [ Vertex ] -> [ Clique ]
                loop [] _ = []
                loop (v : cand') excl =
                    bk (v:compsub) (cand' `res` v) (excl `res` v) ++ loop cand' (v : excl)
        res :: [ Vertex ] -> Vertex -> [ Vertex ]
        res vs v = Data.List.filter (connected g v ) vs

createPrimePairGraph :: Integer -> PrimePairGraph
createPrimePairGraph n = PrimePairGraph (toList v) (fromList e)
    where e = primePairsLteN n
          v = fromList (flatten e)
            where flatten :: [ ( Vertex, Vertex) ] -> [ Vertex ]
                  flatten [] = []
                  flatten ((i, j) : y) = [i, j] ++ (flatten y)

firstFourClique = find (\x -> prime x &&
  any (\clique -> length clique >= 4) (biggestCliques (createPrimePairGraph x))) [ 2 .. ]

firstFiveClique = find (\x -> prime x &&
  any (\clique -> length clique >= 5) (biggestCliques (createPrimePairGraph x))) [ 2 .. ]

