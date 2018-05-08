from math import ceil, sqrt

def four_factors(n):
    facs = []
    while not n % 2:
        facs.append(2)
        n = n // 2
    for x in range(3, ceil(sqrt(n)) + 1, 2):
        while not n % x:
            facs.append(x)
            n = n // x
    if n != 1: facs.append(n)
    facs = set(facs)
    if len(facs) == 4: return True
    return False

x = 647
while True:
    if four_factors(x) and four_factors(x + 1)\
       and four_factors(x + 2) and four_factors(x + 3):
        print(x)
        break
    x += 1
    
