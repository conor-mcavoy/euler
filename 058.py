from math import sqrt, ceil

def is_prime(n):
    if not n % 2 or not n % 3: return False
    for x in range(6, ceil(sqrt(n)) + 1, 6):
        if not n % (x - 1) or not n % (x + 1): return False
    return True

p = 3
l = 5
n = 3
while True:
    if is_prime(4 * n ** 2 - 10 * n + 7):
        p += 1
    if is_prime(4 * n ** 2 - 8 * n + 5):
        p += 1
    if is_prime(4 * n ** 2 - 6 * n + 3):
        p += 1    
    l += 4
    if p / l < .1:
        break
    n += 1

print(2 * n - 1)
