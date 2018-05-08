from math import ceil, sqrt

def is_prime(n):
    if not n % 2: return False
    for x in range(3, ceil(sqrt(n)) + 1, 2):
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

primes = sieve(1000000)
end = False
mp = 0
for length in range(2, len(primes)):
    for start in range(len(primes)):
        s = sum(primes[start: start + length])
        if s > 1000000:
            if start == 0:
                end = True
            break
        if is_prime(s):
            mp = s
            break
    if end: break
print(mp)
