from itertools import permutations
def f(n):
    s = 0
    for d in str(n): s += int(d) ** 2
    return s
t = 0
tandf = [False]
for x in range(2, 10000000):
    a = x
    while x > len(tandf) and x != 89:
        x = f(x)
    if x == 89 or tandf[x - 1]: tandf.append(True)
    else: tandf.append(False)
print(tandf.count(True))
