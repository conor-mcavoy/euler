from math import *
def d(n):
    divs = set()
    for x in range(1, ceil(sqrt(n)) + 1):
        if n % x == 0:
            divs.add(x)
            divs.add(n / x)
    t = 0
    divs.remove(n)
    for x in divs:
        t += x
    return t

def isAmicable(n, m):
    if d(n) == m and d(m) == n and n != m:
        return True

s = 0
for x in range(2, 10001):
    if isAmicable(x, d(x)) and d(x) < 10000:
        s += x
        print(x)
print(s)
