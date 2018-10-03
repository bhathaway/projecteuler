from prime import is_prime

# Find three numbers in arithmetic sequence that are 4 digits, prime, and permutations of each other.
# Start at 1000. Now, theoretically, there should only be up to 4! = 24 permutations of this, which seems
# much easier to process, actually. So, we could find all permutations that are prime, first. Obviously,
# the number of prime permutations must be at least 3. Greater than 3 complicates the situation. I'm thinking
# that merely printing them sorted would be a good start.

def perm_helper(string, l):
    if len(l) == 0:
        return [string]
    else:
        result_list = []
        for item in l:
            new_string = str(string)
            new_string += item
            new_list = list(l)
            new_list.remove(item)
            result_list += perm_helper(new_string, new_list)
        return result_list

def get_permutations(num_str):
    start_list = []
    for c in num_str:
        start_list.append(c)
    return perm_helper('', start_list)

def arithmetic_sequences(x):
    result = []
    x.sort()
    for i in range(len(x)):
        for k in range(i+1, len(x)):
            diff = x[k] - x[i]
            cand = x[k] + diff
            sub_result = [x[i], x[k]]
            while cand in x:
                sub_result.append(cand)
                cand += diff
            if len(sub_result) > 2:
                result.append(sub_result)
    return result

for number in range(1001, 10000):
    if is_prime(number):
        p = get_permutations(str(number))
        s = set(p) # removes duplicates.
        prime_perms = set()
        for i in s:
            if is_prime(int(i)):
                prime_perms.add(int(i))
        prime_list = list(prime_perms)
        if len(prime_list) >= 3:
            sequences = arithmetic_sequences(prime_list)
            if len(sequences) > 0:
                print(sequences)

# There are actually quite a few results. Here's a question. How do I find an arithmetic
# sequence in a set of numbers?

