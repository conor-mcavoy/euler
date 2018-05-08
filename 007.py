#problem 7
#3/19/2015
import math
def prime(n):
    for x in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if not n % x: return False
    return True
c = 1
a = 1
while c < 10001:
    a += 2
    if prime(a): c += 1
print(a)
