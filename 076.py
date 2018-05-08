import math


def pentagonal(x):
    return x * (3*x - 1) // 2

pentagonals = [pentagonal(x) for x in range(-9, 10)]
pentagonals.remove(0)


def p(n, pents):
    if n < 0:
        return 0
    if n == 0:
        return 1
    kmin = math.floor(-(math.sqrt(24*n + 1) + 1)/6)
    kmax = math.ceil((math.sqrt(24*n + 1) - 1)/6)
    ks = [k for k in range(kmin - 1, kmax + 1) if pentagonal(k) in pents]
    ms = list(map(pentagonal, ks))



p(5, pentagonals)
