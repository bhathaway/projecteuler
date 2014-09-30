def lower_factors(n):
    result = []
    d = 1
    r = n
    more_factors = True
    while more_factors:
        if r * d == n:
            result.append(d)
        d += 1
        r = n / d
        more_factors = r > d
    return result

def is_triangle(n):
    number = 2*n
    v = lower_factors(number)
    factor = v[-1]
    if (number/factor)-factor == 1:
        return True
    else:
        return False

triangle_words = []
for line in open("./words.txt"):
    word_sum = 0
    word = line.rstrip('\n')
    for c in word:
        word_sum += ord(c) - ord('A') + 1
    if is_triangle(word_sum):
        triangle_words.append(word)

print(triangle_words)
