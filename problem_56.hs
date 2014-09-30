import Data.Char

digitSum number = foldr (+) 0 $ map digitToInt (show number)
test = maximum [digitSum (a^b) | a <- [1..99], b <- [1..99]]
