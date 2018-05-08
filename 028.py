def spiral(xbyx):
    n = int((xbyx + 1) / 2)
    s = 1
    for x in range(2, n + 1):
        s += 16 * x ** 2 - 28 * x + 16 #start * 4 + 6 * step
    return s

print(spiral(1001))
