#problem 10
#3/20/15
import math
def prime(n):
    for x in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if not n % x: return False
    return True
s = 2
for a in range(3, 2000000, 2):
    if prime(a): s += a
print(s)
