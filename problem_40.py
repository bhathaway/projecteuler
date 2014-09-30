n = 0
place = 1
desired_places = [1, 10, 100, 1000, 10000, 100000, 1000000]

while place <= max(desired_places):
    n += 1
    s = str(n)
    for m in range(len(s)):
        if place + m in desired_places:
            print(s[m])
            break
    place += len(s)

