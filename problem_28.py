# This should be pretty easy. Start with 1, add 2 4 times, then 4 4 times, then 6 4 times, etc, until the
# number equals or exceed the square of the length of the box. Done.

length = 1001

i = 1
sum = 0
inc_step = 2
j = 0
while i <= length * length:
    sum += i
    print("i: %d" % i)
    print("sum: %d" % sum)
    if (j == 4):
        inc_step += 2
        j = 0
    i += inc_step
    j += 1

print(sum)
