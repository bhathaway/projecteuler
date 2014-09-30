def property(string):
    return int(string[1:4])%2 == 0 and\
           int(string[2:5])%3 == 0 and\
           int(string[3:6])%5 == 0 and\
           int(string[4:7])%7 == 0 and\
           int(string[5:8])%11 == 0 and\
           int(string[6:9])%13 == 0 and\
           int(string[7:10])%17 == 0

def pandigitalSpecial(string, s):
    if len(s) == 0:
        if property(string):
            return [int(string)]
        else:
            return []
    else:
        result_list = []
        for e in s:
            test_string=str(string)
            test_string+=e
            test_set=set(s)
            test_set.remove(e)
            result_list+=pandigitalSpecial(test_string, test_set)
        return result_list

digit_set = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
print(pandigitalSpecial('', digit_set))

