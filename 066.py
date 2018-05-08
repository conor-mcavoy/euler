#never really solved this
#"pell equation"

from math import sqrt, floor

def is_square(n):
    n *= 1.0
    if sqrt(n) == int(sqrt(n)): return True
    return False

b = 0
for d in range(1001):
    if is_square(d): continue
    x = 2.0
    while not is_square((x ** 2 - 1) / d):
        x += 1
    print(x, d)
    if x > b:
        b = x
        v = d

print(b, v)
    
