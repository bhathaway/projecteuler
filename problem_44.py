N = 4000

def pentagonals_to_n(n):
    result = []
    for i in range(n):
        result.append(i*(3*i-1)/2)
    return result

p = pentagonals_to_n(N)
p_set = set(p)
solutions = []
for gap in range(1, N-1):
  for i in range(1, N-gap):
    high = i + gap
    diff = p[high] - p[i]
    sum = p[high] + p[i]
    if diff in p_set and sum in p_set:
        solutions.append((diff, i, high))

solutions.sort()

print(solutions)

