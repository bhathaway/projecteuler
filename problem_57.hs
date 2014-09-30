import Data.Ratio

nextIteration r = 1 + 1 / (1 + r)
numeratorMoreDigits r = (length $ show $ numerator r) > (length $ show $ denominator r)

test = filter numeratorMoreDigits $ take 1001 $ iterate nextIteration (1%1)
