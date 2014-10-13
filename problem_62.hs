import Data.List

isPermutationOf m n =
    let m_s = show m
        n_s = show n in

        length m_s == length n_s &&
        all (\x -> length (findN x m_s) == length (findN x n_s)) [ '0' .. '9' ]
        where
            findN digit list = findIndices (\x -> x == digit) list

-- Assume cube is the new cube to check..
findFivePermutation n permutations_list =
    let goal list = length list >= 5
        cube = n*n*n in
        if any goal permutations_list then
            filter goal permutations_list
        else
            findFivePermutation (n+1) (addPermutation cube permutations_list)

        where
            addPermutation i [] = [ [i] ]
            addPermutation i (head : tail) =
                if any (\x -> isPermutationOf x i) head then
                    (i : head) : tail
                else 
                    head : (addPermutation i tail)

