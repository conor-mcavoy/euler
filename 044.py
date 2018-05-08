from math import sqrt

def pent_num(n):
    return int(n * (3 * n - 1) / 2)

def is_pent(n):
    x = (sqrt(24 * n + 1) + 1) / 6
    if x == int(x): return True
    return False

pents = [1]
termn = 1
a = True
while a:
    term = int(termn * (3 * termn - 1) / 2)
    for term2 in range(termn, 0, -1):
        t2 = int(term2 * (3 * term2 - 1) / 2)
        if is_pent(term + t2) and is_pent(term - t2):
            print(term - t2)
            a = False
    termn += 1
