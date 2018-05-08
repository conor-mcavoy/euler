def chainLen(n):
    t = n
    c = 0
    while t != 4:
        c += 1
        if t % 2 == 1:
            t = 3 * t + 1
        else:
            t = int(t / 2)
    return c

best = 0
for x in range(13, 1000000):
    a = chainLen(x)
    if a > best:
        curr = x
        best = a
print(curr)
