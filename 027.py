from math import sqrt, ceil


def is_prime(n):
    if n < 2:
        return False
    if not n % 2:
        return False
    for x in range(3, ceil(sqrt(n)) + 1, 2):
        if not n % x:
            return False
    return True


m = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while is_prime(n ** 2 + a * n + b):
            n += 1
        if n > m:
            m = n
            amax = a
            bmax = b
print(amax * bmax)
            
