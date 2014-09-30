reverseDigits = read . reverse . show

isPalindrone number = number == reverseDigits number

addToReverse number = number + reverseDigits number

isLychrelHelper iteration number
    | iteration > 55        = True
    | isPalindrone number && iteration > 0 = False
    | otherwise             = isLychrelHelper (iteration + 1) (addToReverse number)

isLychrel = isLychrelHelper 0

test = filter isLychrel [0..9999]

