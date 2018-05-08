import time
clock = time.time()

from math import ceil, sqrt

def is_prime(n):
    if n == 1: False
    if not n % 2 or not n % 3: return False
    for x in range(6, ceil(sqrt(n)) + 1, 6):
        if not n % (x - 1) or not n % (x + 1): return False
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

primes = sieve(1000000)
def phi(x):
    p = 1
    if is_prime(x):
        p *= 1 - 1 / x
    for prime in primes:
        if prime > ceil(sqrt(x)) + 1:
            break
        if not x % prime:
            p *= 1 - 1 / prime    
    return p


m = 0
for n in range(2, 1000000):
    r = 1 / phi(n)
    if r > m:
        m = r
        b = n

print(b)
print(time.time() - clock)
