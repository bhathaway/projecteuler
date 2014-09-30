#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#The product 7254 is unusual, as the identity, 39  186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

digit_bin = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '=='])

def magicPandigitals(string, s):
    if len(s) == 0:
        identity = False
        try:
            identity = eval(string)
        except:
            pass
        if identity:
            print(string)
    else:
        for e in s:
            test_string = str(string)
            test_string += e
            test_set = set(s)
            test_set.remove(e)
            magicPandigitals(test_string, test_set)

magicPandigitals("", digit_bin)

# Results so far:
# 5796, 4396, 7632, 6952, 7852, 5346, 7254

