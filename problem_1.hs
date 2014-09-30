multipleOfThreeOrFive x = x `mod` 3 == 0 || x `mod` 5 == 0

test =
  foldl (+) 0 (filter multipleOfThreeOrFive [1..999])

main = do
  putStrLn ("The sum of integers less than 1000 and divisible by 3 or 5 is " ++ (show test))
