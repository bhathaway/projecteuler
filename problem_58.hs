primeHelper :: Integer -> Integer -> Bool
primeHelper number current_divisor
    | current_divisor * current_divisor <= number =
        if rem number current_divisor == 0 then False else primeHelper number (current_divisor + 1)
    | otherwise = True

prime :: Integer -> Bool
prime number
    | number < 2 = False
    | otherwise = primeHelper number 2

-- For ratios of about 11% and lower, the computation time is significant
solver ratio shell_number prime_count diagonal_count
    | shell_number > 1 && (fromIntegral prime_count / (fromIntegral diagonal_count)) < ratio = shell_number
    | otherwise =
        let n = shell_number + 2
            x = [n^2 - 3*(n-1), n^2 - 2*(n-1), n^2 - (n-1)]
            p = length (filter prime x) in
                solver ratio n (prime_count + p) (diagonal_count+4)

