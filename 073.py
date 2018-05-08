def coprime(a, b):
    if not a % 2 and not b % 2: return False
    while a != b:
        if not a % 2: a //= 2
        elif not b % 2: b //= 2
        elif a > b: a = (a - b) // 2
        else: b = (b - a) // 2
    if a == 1: return True
    return False

c = 0
for d in range(4, 12001):
    for n in range(1, d):
        if d > 3 * n: continue
        if 2 * n > d: break
        if coprime(n, d):
            c += 1
        
print(c)
