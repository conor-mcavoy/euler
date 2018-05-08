bestAbove = 4000000
bestBelow = 0
m = 0
n = 1

while m * n * (m + 1) * (n + 1) < 8000000:
    m += 1
    while m * n * (m + 1) * (n + 1) < 8000000:
        n += 1
    if m * n * (m + 1) * (n + 1) < 4 * bestAbove:
        bestAbove = m * n * (m + 1) * (n + 1) // 4
        bma = m
        bna = n
    if m * n * (m + 1) * (n - 1) > 4 * bestBelow:
        bestBelow = m * n * (m + 1) * (n - 1) // 4
        bmb = m
        bnb = n - 1
    n = 1

if bestAbove - 2000000 < 2000000 - bestBelow:
    print(bma * bna)
else:
    print(bmb * bnb)
