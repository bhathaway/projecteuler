# Modern English currency is now denominated as follows:
# 1 pence, 2 pence, 5 pence, 10 pence, 20 pence, 50 pence, 1 pound,
# where 100 pence = 1 pound. The question is, how many different ways
# are there to make 2 pounds using any number of coins.

# Order doesn't matter, which suggests representing the result as bins of
# denominations with a quantity in each bin.


denominations = [1, 2, 5, 10, 20, 50, 100, 200];

def getBinString(bin):
    result = ""
    result += "%3d *1p, " % bin[0]
    result += "%3d *2p, " % bin[1]
    result += "%3d *5p, " % bin[2]
    result += "%3d *10p, " % bin[3]
    result += "%3d *20p, " % bin[4]
    result += "%3d *50p, " % bin[5]
    result += "%3d *L1" %  bin[6]
    result += "%3d *L2" % bin[7]
    return result

def num_solutions_helper(amount, current_amount, index, bin):
    if index == len(denominations):
        if current_amount == 0:
            print(getBinString(bin))
            return 1
        else:
            return 0
    else:
        subsolutions = 0
        for i in range(amount / denominations[index] + 1):
            test_list = bin
            test_list[index] = i
            if current_amount - i*denominations[index] >= 0:
                subsolutions +=\
                  num_solutions_helper(amount, current_amount - i*denominations[index], index + 1, test_list)
        return subsolutions

def num_solutions(amount):
   return num_solutions_helper(amount, amount, 0, [0, 0, 0, 0, 0, 0, 0, 0])
