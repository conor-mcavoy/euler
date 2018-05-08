#def g(k):
#    return int(k * (3*k - 1)/2)
g = lambda n: int(n * (3*n - 1)/2)

def p(n):
    if n < 0: return 0
    if n <= 1: return 1

    k = 1
    t = 0
    while n >= g(k) and n >= g(-k):
        t += (-1)**(k-1) * p(n - g(k)) +\
             (-1)**abs(-k-1) * p(n - g(-k))
        k += 1
    return t

print(p(5))
