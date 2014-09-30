def nextList(input_list):
    result_list = [1]
    for i in range(len(input_list) - 1):
        result_list.append(input_list[i] + input_list[i+1])
    result_list.append(1)
    return result_list

def numInListOver(input_list, n):
    count = 0
    for item in input_list:
        if item > n:
            count += 1
    return count

working_list = [1]
over_count = 0
N = 1000000
for i in range(1, 101):
    working_list = nextList(working_list)
    print(working_list)
    over_count += numInListOver(working_list, N)

print(over_count)
