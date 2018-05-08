from math import ceil, sqrt

def is_prime(n):
    if not n % 2: return False
    for x in range(3, ceil(sqrt(n)) + 1, 2):
        if not n % x: return False
    return True

for x in range(7654321, 2, -1):
    if ''.join(sorted(str(x))) == "1234567"[:len(str(x))]:
        if is_prime(x):
            print(x)
            break
