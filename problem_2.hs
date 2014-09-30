test = sum $ filter even $ takeWhile (<4000000) $ map fst (iterate (\(a,b)->(b,a+b)) (1,1))

