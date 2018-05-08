from math import factorial as fact

def combinations(n, r):
    return int(fact(n) / (fact(r) * fact(n - r)))

t = 0
for n in range(1, 101):
    for r in range(1, n):
        if combinations(n, r) > 1000000:
            t += 1
print(t)
