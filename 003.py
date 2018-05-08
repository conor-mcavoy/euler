#problem 3
#3/19/15
import math
def pf(n):
    pf = []
    while not n % 2:
        pf.append(2)
        n /= 2
    x = 3
    while math.ceil(math.sqrt(n)) > x - 1:
        while not n % x:
            pf.append(x)
            n /= x
        x += 2
    return pf + [int(n)]
print(pf(600851475143))
