factors number lowest_factor
    | lowest_factor <= 1    = []
    | number <= 1           = []
    | otherwise             =
        let quotient = quot number lowest_factor in
            if quotient * lowest_factor == number then
                lowest_factor : (factors quotient lowest_factor)
            else if quotient < lowest_factor then
                [number]
            else
                factors number (lowest_factor + 1)

test =
    maximum $ factors 600851475143 2

