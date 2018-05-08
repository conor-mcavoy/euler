#useful stuff
from math import ceil, sqrt

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if not n % 2: return False
    for x in range(3, int(ceil(sqrt(n) + 1)), 2):
        if not n % x: return False
    return True

def sieve(n):
    A = [True for x in range(n)]
    for i in range(2, ceil(sqrt(n)) + 1):
        if A[i]:
            for j in range(i ** 2, n, i):
                A[j] = False
    p = []
    for pos, x in enumerate(A):
        if x: p.append(pos)
    return p[2:]

def divisors(n):
    d = []
    for x in range(1, int(sqrt(n))):
        if not n % x:
            d.append(x)
            d.append(n / x)
    if int(sqrt(n)) == sqrt(n): d.append(int(sqrt(n)))
    d.sort()
    return d
