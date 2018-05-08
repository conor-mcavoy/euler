from math import ceil, sqrt

maxcpc = 0
for p in range(12, 1001):
    cpc = 0
    for a in range(1, ceil(p / 2)):
        b = (p ** 2 - 2 * p * a) / (2 * p - 2 * a)
        if int(b) == b:
            cpc += 1
    if cpc > maxcpc:
        maxcpc = cpc
        bestp = p
        
print(bestp)
