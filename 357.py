from math import ceil, sqrt

def divisors(n):
    if n in (2, 3): return [1]
    d = []
    for x in range(1, int(sqrt(n))):
        if not n % x:
            d.append(x)
    if int(sqrt(n)) == sqrt(n): d.append(int(sqrt(n)))
    d.sort()
    return d

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if not n % 2: return False
    for x in range(3, int(sqrt(n) + 2), 2):
        if not n % x: return False
    return True

def condition(n):
    for d in divisors(n):
        if is_prime(d + n / d): continue
        return False
    return True

t = 2
for x in range(2, 100000000, 2):
    if condition(x):
        t += x
print(t)
