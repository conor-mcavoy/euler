from math import sqrt

def is_pent(x):
    if x != int(x): return False
    n = (sqrt(24 * x + 1) + 1) / 6
    if n == int(n):
        return True
    return False

def is_hex(x):
    if x != int(x): return False
    n = (sqrt(8 * x + 1) + 1) / 4
    if n == int(n):
        return True
    return False

term = 286
while not is_pent(term * (term + 1) / 2) or not is_hex(term * (term + 1) / 2):
    term += 1
print(term * (term + 1) / 2)
