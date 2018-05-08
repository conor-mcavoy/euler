from math import sqrt, ceil

def is_prime(n):
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
        
def sum_finder(n):
    p = sieve(n)
    for prime in p:
        if sqrt((n - prime) / 2) == int(sqrt((n - prime) / 2)):
            return (prime, int(sqrt((n - prime) / 2)))
    return (0, 0)

t = 33
while sum_finder(t) != (0, 0):
    t += 2
    while is_prime(t):
        t += 2
print(t)
