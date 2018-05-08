#problem 12
#3/25/15
import math
def numOfDivisors(n):
    out = 0
    #divs = []
    for x in range(1, int(math.sqrt(n)) + 1):
        if n % x == 0: out += 2
    #if int(math.sqrt(n)) == math.sqrt(n): out -= 1
    return out


tNum = 1
while numOfDivisors(int((tNum**2 + tNum) / 2)) <= 500: tNum += 1
print(int((tNum**2 + tNum) / 2))
